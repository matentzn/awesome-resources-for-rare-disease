#!/usr/bin/env python3
"""Apply a form-submitted change to README.md (conservative version).

The Google Form's Apps Script opens a GitHub issue whose body ends with a
marker comment and a ```json fenced block. This script reads that block from
the ISSUE_BODY environment variable, validates every field, edits README.md,
checks that the edit touched only what it should, and writes `result`,
`title` and `summary` (or `reason`) to $GITHUB_OUTPUT.

Everything in the issue is treated as untrusted. When anything is unusual the
script makes no change and returns result=skip with a reason, so a maintainer
looks at it instead.

Entry format enforced (from CONTRIBUTING.md):
    - [Resource Name](URL) - Brief description.
"""

import difflib
import json
import os
import re
import secrets
import unicodedata
from pathlib import Path

README = Path("README.md")
ENTRY_RE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)\s+-\s+(?P<desc>.*)$")
HEADING_RE = re.compile(r"^## (?P<title>.+?)\s*$")
RESERVED_SECTIONS = {"Contents", "Contributing", "License"}
NEW_CATEGORY_OPTION = "Propose a new category"

# Only the block directly after this marker, at the start of a line, is read.
BLOCK_RE = re.compile(r"^<!-- form-submission:v1 -->\n```json\n(.*?)\n```[ \t]*$", re.M | re.S)

# Must stay in step with the Apps Script.
URL_RE = re.compile(
    r"^https?://[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+(:[0-9]{1,5})?(/[^\s<>\"'`()\[\]{}|\\^]*)?$"
)
NAME_FORBIDDEN = re.compile(r"[\[\]()<>`|\\]")
DESC_FORBIDDEN = re.compile(r"[\[\]<>`|\\]|://|www\.", re.I)

LIMITS = {"name": 120, "url": 400, "description": 400, "reason": 1000, "submitter": 80}
MIN_DESC = 10
KNOWN_KEYS = {"action", "category", "name", "url", "description", "existing_url", "reason", "submitter"}

# Control, zero-width, soft-hyphen, bidi and BOM characters.
INVISIBLE = re.compile(
    "[" + "".join(f"{chr(a)}-{chr(b)}" for a, b in [
        (0x00, 0x1F), (0x7F, 0x9F), (0xAD, 0xAD), (0x200B, 0x200F),
        (0x2028, 0x202E), (0x2060, 0x2069), (0xFEFF, 0xFEFF),
    ]) + "]"
)
ZWSP = chr(0x200B)


# --------------------------------------------------------------------------- #
# Output helpers
# --------------------------------------------------------------------------- #
def set_output(key: str, value: str) -> None:
    """Write a value to $GITHUB_OUTPUT using a random heredoc delimiter, so
    user-influenced text cannot end the value early and set other outputs."""
    value = value.replace("\r", "")
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        print(f"[output] {key}={value}")
        return
    delim = f"EOF_{secrets.token_hex(16)}"
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"{key}<<{delim}\n{value}\n{delim}\n")


def skip(reason: str) -> None:
    print(f"SKIP: {reason}")
    set_output("result", "skip")
    set_output("reason", reason)
    raise SystemExit(0)


def md(text: str, limit: int = 200) -> str:
    """Make untrusted text inert in a single markdown line."""
    text = clean_text(text)
    if len(text) > limit:
        text = text[:limit] + "..."
    text = re.sub(r"([\\`*_{}\[\]()<>#+\-.!|~&:=])", r"\\\1", text)
    return text.replace("@", "@" + ZWSP)


# --------------------------------------------------------------------------- #
# Parsing and validation
# --------------------------------------------------------------------------- #
def clean_text(text) -> str:
    text = unicodedata.normalize("NFC", str(text or ""))
    text = INVISIBLE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_issue(body: str) -> dict:
    body = body.replace("\r\n", "\n")
    blocks = BLOCK_RE.findall(body)
    if not blocks:
        skip("Could not find the machine-readable block (marker line followed by a json code block).")
    if len(blocks) > 1:
        skip("The issue contains more than one machine-readable block.")
    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        skip(f"The json block in the issue is not valid JSON: {md(str(exc))}")
    if not isinstance(data, dict):
        skip("The json block must be a JSON object.")
    unknown = set(data) - KNOWN_KEYS
    if unknown:
        skip(f"The json block has unexpected fields: {md(', '.join(sorted(unknown)))}")
    for key, value in data.items():
        if value is not None and not isinstance(value, str):
            skip(f"Field '{key}' must be text.")
    return data


def field(data: dict, key: str) -> str:
    value = clean_text(data.get(key))
    if key in LIMITS and len(value) > LIMITS[key]:
        skip(f"Field '{key}' is longer than {LIMITS[key]} characters.")
    return value


def check_url(url: str, label: str) -> None:
    if not URL_RE.match(url):
        skip(f"The {label} does not look like a plain web address: {md(url)}")


def check_name(name: str) -> None:
    if len(name) < 2 or NAME_FORBIDDEN.search(name):
        skip(f"The resource name is too short or contains [ ] ( ) < > | or backticks: {md(name)}")


def check_desc(desc: str) -> None:
    if len(desc) < MIN_DESC:
        skip("The description is missing or too short.")
    if DESC_FORBIDDEN.search(desc):
        skip("The description contains links, brackets or markdown, which the automation does not accept. "
             "A maintainer can edit the json block and retry.")


def norm_url(url: str) -> str:
    """Normalise a URL for duplicate matching (scheme, www, trailing slash, case)."""
    url = (url or "").strip().lower()
    url = re.sub(r"^https?://", "", url)
    url = re.sub(r"^www\.", "", url)
    return url.rstrip("/")


def norm_name(name: str) -> str:
    return clean_text(name).casefold()


def make_entry(name: str, url: str, desc: str) -> str:
    desc = desc.lstrip("-" + chr(0x2013) + " ").strip()
    if desc and desc[-1] not in ".!?":
        desc += "."
    return f"- [{name}]({url}) - {desc}"


# --------------------------------------------------------------------------- #
# README navigation
# --------------------------------------------------------------------------- #
def sections(lines: list[str]) -> dict[str, tuple[int, int]]:
    """Map '## Heading' title -> (heading_index, end_index_exclusive)."""
    heads = [(i, m.group("title")) for i, line in enumerate(lines) if (m := HEADING_RE.match(line))]
    result = {}
    for n, (idx, title) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        result[title] = (idx, end)
    return result


def section_of(lines: list[str], line_idx: int) -> str | None:
    for title, (start, end) in sections(lines).items():
        if start < line_idx < end:
            return title
    return None


def entries(lines: list[str]) -> list[tuple[int, dict]]:
    """All list entries outside the reserved sections."""
    out = []
    for i, line in enumerate(lines):
        m = ENTRY_RE.match(line)
        if m and section_of(lines, i) not in RESERVED_SECTIONS:
            out.append((i, m.groupdict()))
    return out


def insert_into_section(lines: list[str], category: str, entry: str) -> None:
    start, end = sections(lines)[category]
    bullets = [i for i in range(start, end) if lines[i].startswith("- [")]
    if bullets:
        lines.insert(bullets[-1] + 1, entry)
        return
    last = end - 1
    while last > start and not lines[last].strip():
        last -= 1
    lines[last + 1:last + 1] = ["", entry]


def tidy_blank_lines(lines: list[str]) -> list[str]:
    out, prev_blank = [], False
    for line in lines:
        blank = not line.strip()
        if blank and prev_blank:
            continue
        out.append(line)
        prev_blank = blank
    return out


def check_change(before: list[str], after: list[str], max_changed: int) -> None:
    """Refuse the edit unless it only added/removed list entries (and blank
    lines), touched at most `max_changed` entry lines, and kept all headings."""
    if [l for l in before if HEADING_RE.match(l)] != [l for l in after if HEADING_RE.match(l)]:
        skip("Internal check failed: the change would alter README headings.")
    changed = [
        line[1:] for line in difflib.unified_diff(before, after, lineterm="", n=0)
        if line[:1] in "+-" and not line.startswith(("+++", "---"))
    ]
    non_blank = [l for l in changed if l.strip()]
    if len(non_blank) > max_changed or any(not ENTRY_RE.match(l) for l in non_blank):
        skip("Internal check failed: the change would touch more of the README than expected.")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    issue_no = os.environ.get("ISSUE_NUMBER", "")
    if not issue_no.isdigit():
        skip("Missing issue number.")
    data = parse_issue(os.environ.get("ISSUE_BODY", ""))

    action = field(data, "action").lower()
    category = field(data, "category")
    name = field(data, "name")
    url = field(data, "url")
    desc = field(data, "description")
    existing_url = field(data, "existing_url")
    reason = field(data, "reason")
    submitter = field(data, "submitter") or "anonymous"

    if action not in {"add", "edit", "remove"}:
        skip(f"Unrecognised type of change: {md(action)}. Expected Add, Edit or Remove.")
    if category.startswith(NEW_CATEGORY_OPTION):
        skip("The submitter proposed a new category. A maintainer needs to decide "
             "where this belongs (or add the heading) before it can be applied.")

    check_name(name)
    check_url(url, "URL")
    if existing_url:
        check_url(existing_url, "current URL")

    original = README.read_text(encoding="utf-8").split("\n")
    lines = list(original)
    secs = {t for t in sections(lines) if t not in RESERVED_SECTIONS}
    if category not in secs:
        skip(f"Section {md(category)} does not match any README heading.")
    all_entries = entries(lines)

    def by_url(u: str) -> list[tuple[int, dict]]:
        return [(i, e) for i, e in all_entries if norm_url(e["url"]) == norm_url(u)]

    def by_name(n: str) -> list[tuple[int, dict]]:
        return [(i, e) for i, e in all_entries if norm_name(e["name"]) == norm_name(n)]

    # ----------------------------- ADD --------------------------------- #
    if action == "add":
        if existing_url:
            skip("An Add request should not have a current URL. Was this meant to be an Edit?")
        check_desc(desc)
        if by_url(url):
            skip(f"This URL is already listed (section {md(section_of(lines, by_url(url)[0][0]) or '?')}). "
                 "If the submitter meant to update it, this should be an Edit.")
        if by_name(name):
            skip(f"An entry named {md(name)} already exists. A maintainer should check whether this is a duplicate.")
        entry = make_entry(name, url, desc)
        insert_into_section(lines, category, entry)
        check_change(original, lines, max_changed=1)
        title = f"Add {name} to {category}"
        change = f"Added to **{category}**:\n\n```markdown\n{entry}\n```"

    # ----------------------------- EDIT / REMOVE ------------------------ #
    else:
        lookup_url = existing_url or url
        matches = by_url(lookup_url)
        if len(matches) != 1:
            skip(f"Expected exactly one entry with URL {md(lookup_url)}, found {len(matches)}. "
                 "A maintainer should locate it manually.")
        idx, old = matches[0]
        if norm_name(old["name"]) != norm_name(name):
            skip(f"The entry at that URL is named {md(old['name'])}, but the submission says {md(name)}. "
                 "Both must match before the automation changes an existing entry.")
        old_line = lines[idx]
        current_section = section_of(lines, idx)

        if action == "remove":
            if existing_url and norm_url(existing_url) != norm_url(url):
                skip("A removal should give only the URL of the entry to remove.")
            del lines[idx]
            lines = tidy_blank_lines(lines)
            check_change(original, lines, max_changed=1)
            title = f"Remove {old['name']} from {current_section}"
            change = f"Removed from **{current_section}**:\n\n```markdown\n{old_line}\n```"
        else:
            new_url = url if existing_url else old["url"]
            if existing_url and norm_url(new_url) != norm_url(old["url"]) and by_url(new_url):
                skip(f"The new URL {md(new_url)} is already used by another entry.")
            if desc:
                check_desc(desc)
            entry = make_entry(old["name"], new_url, desc or old["desc"])
            target = category
            if entry == old_line and target == current_section:
                skip("The requested edit is identical to the existing entry.")
            if target == current_section:
                lines[idx] = entry
                moved = ""
            else:
                del lines[idx]
                insert_into_section(lines, target, entry)
                moved = f" and moved from **{current_section}** to **{target}**"
            check_change(original, lines, max_changed=2)
            title = f"Update {old['name']}" + (f" (moved to {target})" if moved else "")
            change = f"Edited{moved}:\n\n```diff\n- {old_line[2:]}\n+ {entry[2:]}\n```"

    README.write_text("\n".join(lines), encoding="utf-8")

    summary = "\n".join([
        f"Automated pull request from web-form submission #{issue_no}.",
        "",
        change,
        "",
        f"- **Reason / source given (submitter's words):** {md(reason, 1000) if reason else 'none provided'}",
        f"- **Submitted by:** {md(submitter, 80)}",
        "",
        "Please check the URL and description against the quality standards in CONTRIBUTING.md before merging.",
    ])
    set_output("result", "ok")
    set_output("title", clean_text(title)[:200])
    set_output("summary", summary)
    print(f"OK: {title}")


if __name__ == "__main__":
    main()

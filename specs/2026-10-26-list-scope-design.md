# List scope: research data resources, not family support

Issue: [#36](https://github.com/matentzn/awesome-resources-for-rare-disease/issues/36). Branch: `rescope-list`.

## Audience and inclusion test

The list is for researchers, bioinformaticians, data engineers and developers who work with rare disease data.

An entry must be something such a person can **query, download, run, adopt as a standard, or apply to for data or samples**. Organisations are listed only when they run research infrastructure. Otherwise, the registry, dataset or tool they run is listed on its own.

The existing quality standards still apply on top of this test: predominantly rare, recently maintained, freely accessible or an open coordination point, and reputable.

## Out of scope

- Patient and family support, advocacy and funding organisations.
- Events, podcasts, social media groups and other media.
- Individual patient-organisation registries on shared platforms. The platform (CoRDS, IAMRARE, RARE-X) is listed instead. This covers the 69 CoRDS-hosted registries in the second sheet of `background/rare_resources_reviewed.xlsx`.

## Positioning against overlapping resources

| Resource | Audience | What it covers | Relation to this list |
|---|---|---|---|
| [Librarey](https://www.librarey.com/) | Families, caregivers | Over 4,850 support resources, searchable by location, disease and demographics | Referred to in the intro for family support. Not listed as an entry. |
| [Resource Ecosystem](https://boycelab.github.io/rare-resources/) (BoyceLab) | Families, disability, patient organisations | 936 entries: 577 for individuals and families, and a comparison of 42 registry hosting options for patient organisations | About 75 of our entries appear there with rewritten descriptions. It is the broad directory and we are the research subset. Referred to in the intro. |
| Orphanet | Everyone | Diseases, expert centres, registries, biobanks, trials | Listed as a knowledge base. We don't replicate its resource listings. |
| ERDRI.dor (EU RD Platform) | Registry holders, researchers | Metadata on European registries | Linked from the EU RD Platform entry under Directories & Catalogues. It is the place for completeness on registries. |
| ERDERA Virtual Platform | Researchers | Federated discovery across FAIR resources | Listed under Directories & Catalogues. |
| IRDiRC Recognized Resources | Researchers | A small, labelled set of platforms, tools, standards and guidelines | Listed under Directories & Catalogues. We are broader and record access details. |

What this list adds over these:

- It is cross-cutting: knowledge bases, ontologies, standards, datasets, data-access points and tools sit in one place.
- Each entry states how to get at the resource: downloads, an API, or a data access committee.
- Its coverage is global, not EU-only.
- It is CC0 and open to contribution by PR or the web form.

## Section changes

| Before | After |
|---|---|
| Disease-Gene-Phenotype Data | Unchanged. Gains MedGen, RDAS and RARe-SOURCE. Monarch API merged into the Monarch entry. |
| APIs & Data Downloads | Removed. Every entry now carries its own download or API link. Orphadata was a duplicate. ERDERA VP moved to Directories. |
| Datasets & Benchmarks | Gains NF Data Portal, ALS Knowledge Portal and Rare Barometer. |
| Clinical & Diagnostic Resources | Renamed **Diagnosis & Patient Matching** and limited to undiagnosed disease programmes and matchmaking services. Duplicate Exomiser and LIRICAL entries dropped. Six software entries moved to Analysis Tools. ERICA PROMs moved to Data Standards. |
| Research Platforms & Initiatives | Renamed **Research Programmes & Communities**. NCATS and C-Path removed (their resources are listed). Data, tools and biobanks moved to their own sections. EU RD Platform moved to Directories. |
| Patient Registries | Renamed **Patient Registries & Biobanks**. Duplicate RD-Connect dropped. Gains Rare-X, RDCA-DAP, the Telethon biobank network and BioNER. CDA-AMC inventory moved to Directories. |
| Patient Advocacy & Support Organizations | Removed. Rare Barometer moved to Datasets. The other 13 entries are recorded in EXCLUDED.md. |
| (new) Directories & Catalogues | ERDERA VP, EU RD Platform (with ERDRI.dor), IRDiRC Recognized Resources (new), CDA-AMC inventory. |

Net change: 165 entries become 150. That is 16 removed, 4 duplicates dropped and 1 added (IRDiRC Recognized Resources). The Model Consent Clauses link was broken and now points to the GA4GH Consent Toolkit.

## Consequences

- The web form's category dropdown has to list the new section names. Until it does, the form bot maps the old names of renamed sections to the new headings (`LEGACY_SECTIONS` in `.github/scripts/apply_form_submission.py`). Submissions to removed sections go to `needs-manual-review`.
- Funders are out of scope, and the "disease-specific funders stay in Patient Advocacy until there are more than 10" policy is dropped. A data resource a funder runs can still be listed on its own.
- Out-of-scope form submissions are recorded in EXCLUDED.md and closed: #22, #24, #26, #28, #30, #33 and #35. #32 (GeoALS) needs a decision on its own.
- Triage of the 2,938-row spreadsheet is limited to the roughly 370 data-like rows.

## Not decided here

- Whether project-type entries without their own data or tools (SimPaThIC, Screen4Care, JARDIN, ERNs) stay. They were kept for now.
- GARD is patient-facing but has structured data. It was kept.

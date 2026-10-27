# Excluded Resources

Resources that were considered but excluded from the main list, mostly because they are not specific enough to rare diseases or fall outside the list's research and data scope, despite often being tremendously useful. This document helps maintainers track decisions and avoid re-evaluating the same resources.

## Patient Advocacy, Support & Funding Organisations

The list covers resources for people working with rare disease data (see [#36](https://github.com/matentzn/awesome-resources-for-rare-disease/issues/36)). Organisations whose main role is advocacy, family support or research funding are out of scope; any data, registry or tool they run is listed on its own. For family support see [Librarey](https://www.librarey.com/) and the [Resource Ecosystem](https://boycelab.github.io/rare-resources/).

| Resource | Reason for Exclusion |
|----------|---------------------|
| NORD | Patient advocacy alliance; its IAMRARE Registry Program is listed |
| EURORDIS | Patient advocacy alliance; its Rare Barometer survey is listed |
| Global Genes | Patient advocacy and support; its RARE-X data platform is listed |
| Rare Diseases International | Global advocacy alliance |
| Genetic Alliance | Advocacy network |
| EveryLife Foundation (now RARE Foundation) | Policy advocacy |
| Genetic Alliance UK / Rare Disease UK | Advocacy and campaigning |
| SWAN UK | Family support network |
| CORD | Canadian patient advocacy |
| Rare Diseases South Africa | Information and support hub |
| Children's Tumor Foundation (CTF) | Funder and advocacy; its NF Registry is listed |
| Gilbert Family Foundation (GFF) | Funder; NF Research Tools Central (with GFF) is listed under the NF Data Portal |
| NTAP | Research funder |
| NCATS | NIH funding and research centre; its rare disease resources (GARD, RaDaR, RDAS, RARe-SOURCE) are listed |
| C-Path | Drug development consortium organiser; its RDCA-DAP platform is listed |
| Penn Orphan Disease Center | Research funder and coordinator (#28) |
| Raregivers Global | Family support charity (#24) |
| Rare New England | Regional family support and events (#26) |
| Librarey | Directory of support resources for families; referenced in the README intro instead (#35) |
| Once Upon a Gene | Podcast (#33) |
| Rare Disease Patient Registry Coordinators (Facebook group) | Social media group (#30) |

## General-Purpose Tools & Infrastructure

These are valuable tools but not rare disease-specific:

| Resource | Reason for Exclusion |
|----------|---------------------|
| GitHub | General software development platform |
| BioPortal | General ontology repository |
| OBO Foundry | General ontology registry |
| LinkML | General data modeling language |
| SSSOM | General mapping standard |
| Biolink Model | General biomedical data model |
| KGX | General knowledge graph exchange format |
| ROBOT | General ontology tooling |
| Ontobio | General ontology library |
| OAK (Ontology Access Kit) | General-purpose ontology library; can work with HPO/Mondo but is not RD-specific software |
| KGExplorer | General R package for exploring biomedical knowledge graphs and ontologies; can work with Monarch/HPO but is not RD-specific (proposed in #10) |
| pronto | General OBO parser |
| fastobo | General OBO parser |
| InterMine | General data warehouse framework |
| PhenoTagger | General HPO concept recognition in biomedical text; not RD-specific |
| EUPID | General pseudonymisation and record-linkage service; used in RD and paediatric oncology but not RD-specific |
| CURE ID | FDA/NCATS drug repurposing case-report platform; not RD-specific |
| GA4GH | The umbrella genomics standards organization; not RD-specific (the GA4GH Rare Disease Community is included separately) |

## General European Health Data & Research Infrastructures

EU infrastructures that rare disease work builds on (many are named in the EURORDIS European Blueprint for Rare Diseases), but which serve all of health or research:

| Resource | Reason for Exclusion |
|----------|---------------------|
| European Health Data Space (EHDS) | General legal framework for primary and secondary use of health data; no RD-specific provisions |
| MyHealth@EU / eHDSI | General cross-border exchange of patient summaries and prescriptions; carries ORPHAcodes but is not RD-specific |
| EEHRxF | General European EHR exchange format; RD-relevant only via ORPHAcodes in the Patient Summary (the JARDIN RD dataset is included separately) |
| Xt-EHR | General Joint Action on EHR exchange and telemedicine |
| DARWIN EU | EMA's general real-world evidence network; covers all medicines |
| BBMRI-ERIC | General biobanking research infrastructure |
| ECRIN | General clinical trials research infrastructure |
| EATRIS | General translational medicine research infrastructure |

## General Genomics Resources

Useful for genomics broadly, but not rare disease-focused:

| Resource | Reason for Exclusion |
|----------|---------------------|
| Gene Ontology (GO) | Gene function annotations, not disease-specific |
| Ensembl REST API | General genomic annotations |
| VEP | General variant effect prediction |
| SnpEff | General variant annotation |
| dbSNP | General variant database |
| HGNC | Gene nomenclature (useful but not RD-specific) |
| UniProt | Protein database (has disease annotations but primarily protein-focused) |
| CIViC | Cancer-focused variant interpretation; rare cancer syndromes are insufficiently specific to RD |
| Gabriella Miller Kids First DRC | Paediatric cancer and structural birth defect cohorts; same reasoning as CIViC, and the birth defect half is not RD-specific |
| Cellosaurus | General cell line knowledge base; only a minority of lines are RD-derived |
| hPSCreg | General stem cell line registry |
| IMPC | General mouse functional genomics, not RD-specific |
| Phenolyzer | Phenotype-based gene prioritisation for common and rare disease; inactive, and Phen2Gene from the same lab is listed |
| Helix GenoSphere | Commercial, licensed population genomics platform without an RD focus or open data (proposed in #6) |
| Fabric GEM / Congenica | Commercial general clinical genome interpretation platforms; not RD-specific |

## General Ontologies & Classification Systems

Ontologies and terminologies that support rare disease work but are not themselves rare disease resources:

| Resource | Reason for Exclusion |
|----------|---------------------|
| Uberon | Cross-species anatomy ontology |
| OBI | Biomedical investigations ontology |
| RO | Relations ontology |
| GENO | Genotype ontology |
| SEPIO | Evidence and provenance ontology |
| MAXO | Medical actions (borderline - may reconsider) |
| SNOMED CT | General clinical terminology for all of healthcare; has Orphanet alignment but is not RD-specific |
| ICD-11 | General WHO disease classification; includes more RD codes than ICD-10 but remains a general-purpose classification |

## Variant Pathogenicity Predictors

These help interpret variants but are general-purpose tools:

| Resource | Reason for Exclusion |
|----------|---------------------|
| CADD | General deleteriousness scores |
| SpliceAI | Splicing predictions |
| REVEL | Missense pathogenicity |
| AlphaMissense | Missense predictions |

## General Data Standards

Standards that are useful for rare disease work but are general-purpose:

| Resource | Reason for Exclusion |
|----------|---------------------|
| FHIR Genomics | General HL7 FHIR resources for genomic data in clinical settings; not RD-specific |
| VRS | GA4GH Variation Representation Specification for computable variant identifiers; general genomics standard |
| HGVS Nomenclature | Standard for describing sequence variants; applies to all genomics, not RD-specific |
| FAIR Genomes | General Dutch NGS metadata schema |
| DUO / ICO | General data-use and informed-consent ontologies (the RD-specific IRDiRC/GA4GH model consent clauses are listed) |

## APIs & Data Services

General bioinformatics APIs:

| Resource | Reason for Exclusion |
|----------|---------------------|
| MyGene.info | General gene API |
| MyVariant.info | General variant API |
| PubTator Central | General literature annotation |
| NCBI E-utilities | General NCBI access |
| OLS4 | General ontology lookup service for all biomedical ontologies; not RD-specific |

## Other Exclusions

RD-relevant resources excluded for reasons other than scope:

| Resource | Reason for Exclusion |
|----------|---------------------|
| CureTopia | Token-funded BioDAO without public data or tools (proposed in #5) |
| PhenoTips | Commercial with no free tier; the open-source edition is archived |
| Healx | Proprietary drug repurposing platform; no public data or API |
| FDA Rare Disease Repurposing Database (RDRD) | Frozen around 2010, no live successor |

## Not Recently Maintained

RD-specific resources that are still online but show no update in roughly the last two years (see the [quality standards](CONTRIBUTING.md#quality-standards)). Any of them can come back once it is updated again:

| Resource | Reason for Exclusion |
|----------|---------------------|
| ClinPhen | Last release (1.28 on PyPI) in Aug 2019 |
| PhenoGenius | Last code change May 2024; the web app still runs on 2024 HPO data |
| RSDB (Rare Skin Disease Database) | Still built on the Dec 2020 HPO release; no data release since 2022 |
| OLIDA | Last data release (v4) in Mar 2024, covering literature up to Jan 2024 |
| FindZebra | No index or software update found since 2023 |
| PRO-ACT | Last dated data release in Aug 2022 |
| ModelMatcher | No visible update since its 2021 launch (site © 2021, only a 2021 preprint); unreachable since Oct 2026. Clinician-to-model-organism matching is covered by RDMM and the Matchmaker Exchange |

## Retired Resources

Resources that were on the list but are no longer operational:

| Resource | Reason for Exclusion |
|----------|---------------------|
| NIH GRDR | Global Rare Diseases Patient Registry Data Repository, retired in 2017; succeeded by RaDaR (listed) |

## Notes

- A resource being excluded doesn't mean it's not useful - it means this list focuses specifically on rare disease resources
- If you believe a resource should be reconsidered, please open an issue with rationale for its rare disease relevance

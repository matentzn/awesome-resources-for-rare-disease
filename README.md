# Awesome Resources for Rare Disease

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://oboacademy.github.io/obook/tutorial/pull-requests/)
![License](https://img.shields.io/github/license/matentzn/awesome-resources-for-rare-disease.svg?color=blue)

> A curated list of data resources, ontologies, and tools for rare disease research and data integration.

This list is for researchers, bioinformaticians, and developers working to integrate rare disease data to advance diagnosis and treatment. Resources that provide downloadable data or APIs are emphasized.

For resources that were considered but excluded (e.g., general-purpose tools like GitHub, general ontologies), see [EXCLUDED.md](EXCLUDED.md).

## Contents

- [Disease-Gene-Phenotype Data](#disease-gene-phenotype-data)
- [Ontologies & Terminologies](#ontologies--terminologies)
- [Data Standards & Exchange Formats](#data-standards--exchange-formats)
- [Variant & Genomic Data](#variant--genomic-data)
- [APIs & Data Downloads](#apis--data-downloads)
- [Clinical & Diagnostic Resources](#clinical--diagnostic-resources)
- [Analysis Tools & Software](#analysis-tools--software)
- [Research Platforms & Initiatives](#research-platforms--initiatives)
- [Patient Registries](#patient-registries)
- [Patient Advocacy & Support Organizations](#patient-advocacy--support-organizations)

## Disease-Gene-Phenotype Data

Core knowledge bases providing structured data on rare diseases, their genetic causes, and clinical presentations.

- [Orphanet](https://www.orpha.net/) - The European reference portal for rare diseases, providing expert-validated information on over 6,500 rare diseases including prevalence, inheritance, age of onset, and gene associations. The primary source of ORPHAcodes used in European health systems.
- [OMIM](https://omim.org/) - The authoritative compendium of human genes and Mendelian phenotypes, maintained since 1966. Contains detailed clinical synopses and molecular genetics for inherited disorders. [Downloads](https://omim.org/downloads) (requires registration).
- [Monarch Initiative](https://monarchinitiative.org/) - Integrates rare disease data across species, linking human diseases to model organism phenotypes to support variant interpretation and therapeutic target discovery. [Data downloads](https://monarchinitiative.org/downloads).
- [Orphadata](https://www.orphadata.com/) - The downloadable data arm of Orphanet, providing gene-disease associations, epidemiology, phenotype annotations, and disease classifications in machine-readable formats (XML, JSON).
- [HPO Annotations (HPOA)](https://hpo.jax.org/data/annotations) - Curated disease-to-phenotype associations linking rare diseases to HPO terms. Powers phenotype-driven diagnostic tools like Exomiser and LIRICAL. Freely downloadable.
- [DisGeNET](https://www.disgenet.org/) - Aggregates gene-disease associations from curated sources (OMIM, ClinVar, UniProt) and text mining. Useful for exploring genetic underpinnings of rare diseases. [Downloads available](https://www.disgenet.org/downloads).
- [GARD](https://rarediseases.info.nih.gov/) - NIH Genetic and Rare Diseases Information Center providing patient-accessible disease summaries, inheritance patterns, and links to clinical resources for over 7,000 rare diseases.
- [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/) - Expert-authored, peer-reviewed clinical descriptions of genetic conditions including diagnosis, management, and genetic counseling. The clinical reference standard for inherited disorders.
- [MalaCards](https://www.malacards.org/) - Integrates rare disease information from 74 sources into unified disease cards, useful for exploring disease relationships and annotations.
- [DECIPHER](https://www.deciphergenomics.org/) - Database of chromosomal imbalance and phenotype in humans. Contains over 60,000 patient records linking genomic variants to rare disease phenotypes, critical for CNV interpretation.
- [Open Targets Platform](https://platform.opentargets.org/) - Integrates genetics, genomics, and drug data to identify therapeutic targets. Includes rare disease associations from OMIM, Orphanet, and ClinVar. [Data downloads](https://platform.opentargets.org/downloads).
- [FDA Orphan Drug Designations](https://www.accessdata.fda.gov/scripts/opdlisting/oopd/) - Searchable database of 5,000+ orphan drug designations since 1983, tracking which rare diseases have drugs in development or approved.
- [EMA Orphan Designation](https://www.ema.europa.eu/en/medicines/ema_group_types/ema_orphan) - European Medicines Agency database of orphan medicinal product designations, providing information on drugs designated for rare diseases in the EU.

## Ontologies & Terminologies

Standardized vocabularies essential for rare disease data integration. These enable cross-resource queries and interoperability between databases, registries, and clinical systems.

- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/) - The unifying disease ontology that harmonizes OMIM, Orphanet, NCIT, and other disease sources. Provides stable identifiers and cross-references essential for integrating rare disease data across resources. [GitHub](https://github.com/monarch-initiative/mondo).
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) - The standard vocabulary for clinical phenotypes with over 18,000 terms. Used by ClinVar, OMIM, Orphanet, and diagnostic tools. Enables phenotype-driven rare disease diagnosis. [GitHub](https://github.com/obophenotype/human-phenotype-ontology).
- [Orphanet Rare Disease Ontology (ORDO)](https://www.orphadata.com/ordo/) - The ontological representation of the Orphanet nomenclature. ORPHAcodes are [mandated for rare disease coding in EU health systems](https://ojrd.biomedcentral.com/articles/10.1186/s13023-015-0251-8) and enable cross-border data sharing.

## Data Standards & Exchange Formats

Standards specifically designed for or widely adopted by the rare disease community for data exchange.

- [Phenopackets](https://phenopackets.org/) - GA4GH standard for sharing patient phenotype and disease information. Adopted by rare disease diagnostic pipelines and the [Matchmaker Exchange](https://www.matchmakerexchange.org/). [Schema](https://github.com/phenopackets/phenopacket-schema).
- [GA4GH Beacon](https://beacon-project.io/) - Protocol for querying genomic variant presence across federated datasets. Enables privacy-preserving rare variant discovery across institutions.
- [RD-CDM](https://rd-cdm.readthedocs.io/) - Rare Disease Common Data Model extending ERDRI-CDS for international registry harmonization, compatible with Phenopackets and FHIR.

## Variant & Genomic Data

Resources providing variant-level data essential for rare disease genetic diagnosis.

- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) - The primary public archive of variant-disease relationships with clinical interpretations. Contains over 2 million submissions, essential for rare disease variant classification. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/).
- [gnomAD](https://gnomad.broadinstitute.org/) - Population allele frequencies from 140,000+ exomes/genomes. Critical for filtering common variants in rare disease diagnosis - variants above population frequency thresholds are unlikely to cause rare Mendelian disorders. [Downloads](https://gnomad.broadinstitute.org/downloads).
- [ClinGen](https://clinicalgenome.org/) - NIH-funded resource providing expert-curated gene-disease validity, variant pathogenicity, and dosage sensitivity assessments. The authority for clinical actionability of genetic findings. [Data downloads](https://clinicalgenome.org/docs/downloads/).
- [LOVD](https://www.lovd.nl/) - Locus-specific variant databases maintained by gene experts. Many rare disease genes have dedicated LOVD instances with curated variant interpretations.
- [HGMD](http://www.hgmd.cf.ac.uk/) - Human Gene Mutation Database cataloging published disease-causing mutations. Commercial with limited public access; widely used in clinical genetics labs.

## APIs & Data Downloads

Programmatic access points for rare disease data integration.

- [Orphadata](https://www.orphadata.com/) - Bulk downloads of Orphanet data including disease classifications, gene associations, epidemiology, and phenotype annotations in XML and RDF formats.
- [Monarch API](https://api-v3.monarchinitiative.org/v3/docs) - REST API for querying integrated rare disease data: disease-gene associations, phenotype profiles, and cross-species mappings.
- [MedGen](https://www.ncbi.nlm.nih.gov/medgen/) - NCBI's portal aggregating disease concepts from OMIM, Orphanet, HPO, Mondo, and ClinVar into unified identifiers. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/medgen/).

## Clinical & Diagnostic Resources

Resources supporting rare disease diagnosis and patient matching.

- [Matchmaker Exchange](https://www.matchmakerexchange.org/) - Federated network connecting patient databases (PhenomeCentral, DECIPHER, GeneMatcher, etc.) to find phenotypically and genotypically similar patients. Critical for confirming novel gene-disease associations in ultra-rare disorders.
- [PhenomeCentral](https://www.phenomecentral.org/) - Secure repository for sharing rare disease patient phenotypes to facilitate diagnosis and research collaboration.
- [Exomiser](https://www.sanger.ac.uk/tool/exomiser/) - Phenotype-driven variant prioritization tool that ranks variants by matching patient HPO terms to known disease-gene phenotypes. Standard tool in rare disease diagnostic pipelines. [GitHub](https://github.com/exomiser/Exomiser).
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Likelihood ratio-based diagnostic tool that provides probabilistic rankings of candidate diagnoses based on phenotypes and genotypes.
- [Phen2Gene](https://phen2gene.wglab.org/) - Phenotype-to-gene prioritization using HPO terms to rank candidate genes before sequencing or for variant interpretation.
- [AMELIE](https://amelie.stanford.edu/) - Automatic literature-based variant interpretation that extracts gene-phenotype relationships from publications.
- [Face2Gene](https://www.face2gene.com/) - AI-powered facial analysis for recognizing dysmorphic features associated with genetic syndromes. Aids diagnosis of syndromic rare diseases.
- [Undiagnosed Diseases Network](https://undiagnosed.hms.harvard.edu/) - NIH-funded network of clinical sites bringing together experts to diagnose patients who have eluded diagnosis despite extensive workup.
- [Undiagnosed Diseases Program (UDP)](https://www.genome.gov/Current-NHGRI-Clinical-Studies/Undiagnosed-Diseases-Program-UDP) - The original NHGRI program at NIH Clinical Center that pioneered systematic approaches to solving undiagnosed rare diseases.
- [ACMG Guidelines](https://www.acmg.net/ACMG/Medical-Genetics-Practice-Resources/Practice-Guidelines.aspx) - Standards for variant interpretation (pathogenic, likely pathogenic, VUS, etc.) that define how rare disease variants are classified clinically.

## Analysis Tools & Software

Open-source tools developed for or widely used in rare disease analysis.

- [Exomiser](https://github.com/exomiser/Exomiser) - The standard phenotype-aware variant prioritization tool for rare disease exome/genome analysis.
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Probabilistic phenotype-driven diagnostic tool.
- [Seqr](https://github.com/broadinstitute/seqr) - Open-source web platform for rare disease family-based variant analysis, used by the Broad Institute's rare disease genomics programs.
- [PhenoTips](https://phenotips.com/) - Patient phenotyping software using HPO for structured data collection in rare disease clinics. [Open source](https://github.com/phenotips/phenotips).
- [MARRVEL](https://marrvel.org/) - IRDiRC-recognized tool integrating human variant databases with 7 model organism resources to prioritize rare variants for functional study.

## Research Platforms & Initiatives

Major programs and consortia advancing rare disease research through data sharing and collaboration.

- [NCATS](https://ncats.nih.gov/) - NIH National Center for Advancing Translational Sciences with dedicated rare disease programs including RDCRN, GARD, and drug repurposing initiatives.
- [IRDiRC](https://irdirc.org/) - International Rare Diseases Research Consortium coordinating global research efforts with goals to diagnose all rare diseases and develop 1000 new therapies.
- [Solve-RD](https://solve-rd.eu/) - European project applying multi-omics approaches to solve undiagnosed rare diseases through data sharing across European Reference Networks.
- [Genomics England](https://www.genomicsengland.co.uk/) - UK initiative that has sequenced over 100,000 genomes, with rare disease as a primary focus. Provides access to research datasets.
- [RD-Connect](https://rd-connect.eu/) - European platform linking rare disease registries, biobanks, and clinical bioinformatics to enable integrated research.
- [Rare-X](https://rare-x.org/) - Patient-powered platform enabling rare disease patients to collect and share their health data for research.
- [RDCA-DAP](https://ncats.nih.gov/research/research-activities/rdca-dap) - Rare Diseases Clinical Research Network Data Analysis Platform providing centralized data management for RDCRN consortia.
- [RDMM](https://rare-diseases-catalyst-network.ca/) - Canadian Rare Diseases Models and Mechanisms network connecting clinicians with basic scientists to validate rare disease gene discoveries.
- [GA4GH Rare Disease Community](https://www.ga4gh.org/community/rare-disease/) - Dedicated community bridging clinical and technical RD stakeholders, coordinating global data sharing and standards implementation.
- [OHDSI Rare Disease Working Group](https://www.ohdsi.org/ohdsi2025-workgroups/) - Develops methods for rare disease cohort identification and research using OMOP CDM across global real-world data networks.
- [EU RD Platform (ERDRI)](https://eu-rd-platform.jrc.ec.europa.eu/) - European Commission platform providing directory of registries, common data elements, and cross-registry search tools for RD patient data harmonization.
- [ELIXIR Rare Disease Community](https://elixir-europe.org/communities/rare-diseases) - European bioinformatics infrastructure community focused on rare disease data resources and standards.
- [ERDERA](https://erdera.org/) - European Rare Diseases Research Alliance (launched 2024) unifying research resources, clinical networks, and expertise across Europe. Successor to EJP RD.
- [European Reference Networks (ERNs)](https://health.ec.europa.eu/rare-diseases-and-european-reference-networks_en) - 24 cross-border networks of specialist centers for rare disease diagnosis and care, mandated by EU Cross-Border Healthcare Directive.
- [RDCRN](https://www.rarediseasesnetwork.org/) - NIH Rare Diseases Clinical Research Network with 21 consortia studying 200+ rare diseases, providing infrastructure for natural history studies and clinical trials.
- [IRUD](https://www.amed.go.jp/en/program/IRUD/) - Japan's Initiative on Rare and Undiagnosed Diseases with 418 participating hospitals, achieving diagnosis in 44% of 6,300+ registered pedigrees.
- [Every Cure](https://everycure.org/) - ARPA-H funded nonprofit using AI to identify drug repurposing opportunities across 4,000 approved drugs for rare disease treatment.

## Patient Registries

Registries collecting patient-level data essential for understanding rare disease natural history and enabling clinical trials.

- [NIH GRDR Program](https://grdr.hms.harvard.edu/) - Global Rare Diseases Patient Registry Data Repository providing standardized data elements for rare disease registries.
- [TREAT-NMD](https://www.treat-nmd.org/) - Global neuromuscular disease registry network that has enabled clinical trials for DMD, SMA, and other NMDs by providing trial-ready patient populations.
- [RD-Connect](https://rd-connect.eu/) - European platform linking over 100 rare disease registries and biobanks with genomic data for integrated research.
- [CoRDS](https://sanfordresearch.org/cords/) - Coordination of Rare Diseases at Sanford providing registry infrastructure for rare disease patient organizations.
- [IAMRARE Registry Program](https://ncats.nih.gov/iamrare) - NCATS program providing registry infrastructure and support for rare disease advocacy organizations.
- [RaDaR](https://registries.ncats.nih.gov/) - NCATS Rare Diseases Registry Program providing guidance, best practices, and resources for developing rare disease registries.

## Patient Advocacy & Support Organizations

Organizations representing patients, driving research priorities, and providing support to affected families.

- [NORD](https://rarediseases.org/) - National Organization for Rare Disorders (US), the leading rare disease patient advocacy organization providing disease information, patient assistance programs, and research support.
- [EURORDIS](https://www.eurordis.org/) - European alliance representing 1,000+ rare disease patient organizations, driving EU rare disease policy and research priorities.
- [Global Genes](https://globalgenes.org/) - Patient advocacy organization providing support programs and resources for rare disease families.
- [Rare Diseases International](https://www.rarediseasesinternational.org/) - Global alliance of national rare disease organizations advocating for rare disease recognition worldwide.
- [Genetic Alliance](https://geneticalliance.org/) - Network connecting disease-specific advocacy organizations with researchers and policymakers.
- [EveryLife Foundation](https://everylifefoundation.org/) - Policy advocacy organization focused on rare disease legislation and regulatory issues.
- [SWAN UK](https://www.undiagnosed.org.uk/) - Support network for families of children with Syndromes Without A Name (undiagnosed genetic conditions).
- [CORD](https://www.raredisorders.ca/) - Canadian Organization for Rare Disorders providing patient support and advocating for rare disease policy in Canada.
- [Rare Diseases South Africa](https://www.rarediseases.co.za/) - South African rare disease information and support hub.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.

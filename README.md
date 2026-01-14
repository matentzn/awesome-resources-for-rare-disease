# Awesome Rare Disease Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of data resources, ontologies, and tools for rare disease research and data integration.

This list is for researchers, bioinformaticians, and developers working to integrate rare disease data to advance diagnosis and treatment. Resources that provide downloadable data or APIs are emphasized.

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

- [Monarch Initiative](https://monarchinitiative.org/) - Integrated platform linking diseases, genes, phenotypes, and model organisms. [Data downloads](https://monarchinitiative.org/downloads).
- [OMIM](https://omim.org/) - Authoritative compendium of human genes and Mendelian disorders. [Downloads](https://omim.org/downloads) (requires registration).
- [Orphanet](https://www.orpha.net/) - European reference portal for rare diseases with expert-curated disease information.
- [Orphadata](https://www.orphadata.com/) - Downloadable Orphanet datasets including gene-disease associations, epidemiology, and classifications.
- [HPO Annotations (HPOA)](https://hpo.jax.org/data/annotations) - Disease-phenotype associations linking diseases to HPO terms. Freely downloadable.
- [DisGeNET](https://www.disgenet.org/) - Gene-disease associations aggregated from curated and text-mined sources. [Downloads available](https://www.disgenet.org/downloads).
- [GARD](https://rarediseases.info.nih.gov/) - NIH Genetic and Rare Diseases Information Center with disease summaries.
- [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/) - Expert-authored clinical descriptions of genetic conditions.
- [MalaCards](https://www.malacards.org/) - Integrated database consolidating disease information from 74 sources.
- [UniProt Disease Annotations](https://www.uniprot.org/) - Protein-disease associations with functional context. [Downloads](https://www.uniprot.org/downloads).
- [DECIPHER](https://www.deciphergenomics.org/) - Database of genomic variants and associated phenotypes from clinical cases.
- [Open Targets Platform](https://platform.opentargets.org/) - Target-disease associations integrating genetics, expression, and literature. [Data downloads](https://platform.opentargets.org/downloads).

## Ontologies & Terminologies

Standardized vocabularies essential for data integration and interoperability across rare disease resources.

- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/) - Unified disease ontology harmonizing OMIM, Orphanet, and other sources. Essential for cross-resource integration. [GitHub](https://github.com/monarch-initiative/mondo).
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) - Standard vocabulary for phenotypic abnormalities. Widely used in rare disease diagnosis. [GitHub](https://github.com/obophenotype/human-phenotype-ontology).
- [Orphanet Rare Disease Ontology (ORDO)](https://www.orphadata.com/ordo/) - Structured vocabulary for rare diseases derived from Orphanet classifications.
- [Gene Ontology (GO)](http://geneontology.org/) - Functional annotations for gene products. [Downloads](http://geneontology.org/docs/downloads/).
- [MAXO](https://github.com/monarch-initiative/MAxO) - Medical Action Ontology for treatments and interventions.
- [GENO](https://github.com/monarch-initiative/GENO-ontology) - Genotype Ontology for representing genetic variation.
- [SEPIO](https://github.com/monarch-initiative/SEPIO-ontology) - Scientific Evidence and Provenance Information Ontology.
- [Uberon](https://github.com/obophenotype/uberon) - Cross-species anatomy ontology.
- [OBI](https://github.com/obi-ontology/obi) - Ontology for Biomedical Investigations.
- [RO](https://github.com/oborel/obo-relations) - OBO Relations Ontology defining standard relationship types.
- [SNOMED CT](https://www.snomed.org/) - Comprehensive clinical terminology used in EHRs.
- [ICD-11](https://icd.who.int/) - WHO disease classification with rare disease codes.
- [OMIM Phenotypic Series](https://omim.org/phenotypicSeriesTitle/all) - Groups of phenotypically similar disorders with distinct genetic causes.

## Data Standards & Exchange Formats

Standards for representing and exchanging rare disease data to enable interoperability.

- [Phenopackets](https://phenopackets.org/) - GA4GH standard for sharing disease and phenotype information. [Schema](https://github.com/phenopackets/phenopacket-schema).
- [FHIR Genomics](https://www.hl7.org/fhir/genomics.html) - HL7 FHIR resources for genomic data in clinical settings.
- [SSSOM](https://github.com/mapping-commons/sssom) - Simple Standard for Sharing Ontology Mappings. Critical for terminology alignment.
- [Biolink Model](https://biolink.github.io/biolink-model/) - Data model for biological knowledge graphs used by Monarch and other projects.
- [LinkML](https://linkml.io/) - Linked Data Modeling Language for defining schemas and generating artifacts.
- [VRS](https://vrs.ga4gh.org/) - GA4GH Variation Representation Specification for genomic variants.
- [GA4GH Beacon](https://beacon-project.io/) - Protocol for querying genomic variant presence across datasets.
- [HGVS Nomenclature](https://hgvs-nomenclature.org/) - Standard for describing sequence variants.
- [KGX](https://github.com/biolink/kgx) - Knowledge Graph Exchange format for sharing graph data.

## Variant & Genomic Data

Resources providing variant-level data for rare disease genetics.

- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) - Public archive of variant-disease relationships. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/).
- [gnomAD](https://gnomad.broadinstitute.org/) - Population allele frequencies from 140,000+ exomes/genomes. [Downloads](https://gnomad.broadinstitute.org/downloads).
- [ClinGen](https://clinicalgenome.org/) - Gene and variant curation with actionability assessments. [Data downloads](https://clinicalgenome.org/docs/downloads/).
- [LOVD](https://www.lovd.nl/) - Locus-specific variant databases for individual genes.
- [HGMD](http://www.hgmd.cf.ac.uk/) - Human Gene Mutation Database (commercial, limited public access).
- [dbSNP](https://www.ncbi.nlm.nih.gov/snp/) - Database of short genetic variations.
- [CIViC](https://civicdb.org/) - Clinical Interpretation of Variants in Cancer with community curation.
- [CADD](https://cadd.gs.washington.edu/) - Variant deleteriousness scores. [Downloads available](https://cadd.gs.washington.edu/download).
- [SpliceAI](https://github.com/Illumina/SpliceAI) - Deep learning predictions for splicing variants.
- [REVEL](https://sites.google.com/site/revelgenomics/) - Ensemble pathogenicity scores for missense variants.
- [AlphaMissense](https://github.com/google-deepmind/alphamissense) - DeepMind's proteome-wide missense pathogenicity predictions.

## APIs & Data Downloads

Programmatic access points and bulk download resources for rare disease data.

- [Monarch API](https://api-v3.monarchinitiative.org/v3/docs) - REST API for diseases, genes, phenotypes, and their associations.
- [Orphadata](https://www.orphadata.com/) - Bulk downloads of Orphanet data in XML and other formats.
- [OLS4](https://www.ebi.ac.uk/ols4/) - Ontology Lookup Service API for accessing biomedical ontologies.
- [OBO Foundry](http://obofoundry.org/) - Central repository for OBO ontologies with standardized downloads.
- [BioPortal](https://bioportal.bioontology.org/) - Ontology repository with REST API access.
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25497/) - APIs for ClinVar, PubMed, Gene, and other NCBI databases.
- [Ensembl REST API](https://rest.ensembl.org/) - Programmatic access to genomic annotations.
- [MyGene.info](https://mygene.info/) - Gene annotation API aggregating multiple sources.
- [MyDisease.info](https://mydisease.info/) - Disease annotation API with rare disease coverage.
- [MyVariant.info](https://myvariant.info/) - Variant annotation API consolidating ClinVar, gnomAD, and more.
- [HGNC](https://www.genenames.org/) - Authoritative gene nomenclature with [downloads](https://www.genenames.org/download/).
- [PubTator Central](https://www.ncbi.nlm.nih.gov/research/pubtator/) - NLP-based annotations of biomedical literature.

## Clinical & Diagnostic Resources

Resources supporting rare disease diagnosis and clinical interpretation.

- [Matchmaker Exchange](https://www.matchmakerexchange.org/) - Federated network for matching patients with similar phenotypes and genotypes.
- [PhenomeCentral](https://www.phenomecentral.org/) - Secure repository for sharing patient phenotype data.
- [Exomiser](https://www.sanger.ac.uk/tool/exomiser/) - Variant prioritization using phenotype matching. [GitHub](https://github.com/exomiser/Exomiser).
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Likelihood ratio-based phenotype-driven diagnostics.
- [Phen2Gene](https://phen2gene.wglab.org/) - Phenotype to gene prioritization.
- [AMELIE](https://amelie.stanford.edu/) - Literature-based variant interpretation.
- [Face2Gene](https://www.face2gene.com/) - AI-powered facial phenotyping for syndrome recognition.
- [Undiagnosed Diseases Network](https://undiagnosed.hms.harvard.edu/) - NIH network for solving undiagnosed cases.
- [Undiagnosed Diseases Program (UDP)](https://www.genome.gov/Current-NHGRI-Clinical-Studies/Undiagnosed-Diseases-Program-UDP) - NHGRI flagship program for rare disease diagnosis.
- [ACMG Guidelines](https://www.acmg.net/ACMG/Medical-Genetics-Practice-Resources/Practice-Guidelines.aspx) - Variant interpretation standards.

## Analysis Tools & Software

Open-source tools for rare disease data analysis and integration.

- [Exomiser](https://github.com/exomiser/Exomiser) - Phenotype-aware variant prioritization for exome/genome analysis.
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Phenotype-driven diagnostic interpretation.
- [OAK (Ontology Access Kit)](https://github.com/INCATools/ontology-access-kit) - Python library for ontology operations and analysis.
- [Seqr](https://github.com/broadinstitute/seqr) - Web-based platform for rare disease variant analysis.
- [PhenoTips](https://phenotips.com/) - Patient phenotyping and pedigree collection. [Open source](https://github.com/phenotips/phenotips).
- [ROBOT](https://github.com/ontodev/robot) - Command-line tool for ontology development and processing.
- [Ontobio](https://github.com/biolink/ontobio) - Python library for ontology and association analysis.
- [pronto](https://github.com/althonos/pronto) - Fast Python ontology parser.
- [fastobo](https://github.com/fastobo/fastobo) - Rust library for OBO format parsing.
- [VEP](https://www.ensembl.org/vep) - Ensembl Variant Effect Predictor.
- [SnpEff](http://pcingola.github.io/SnpEff/) - Genetic variant annotation and effect prediction.
- [InterMine](http://intermine.org/) - Data warehouse framework used by many model organism databases.
- [KGHub](https://kghub.org/) - Infrastructure for building and sharing biomedical knowledge graphs.

## Research Platforms & Initiatives

Major programs and consortia advancing rare disease research through data sharing.

- [NCATS](https://ncats.nih.gov/) - NIH center supporting translational science including rare disease programs.
- [IRDiRC](https://irdirc.org/) - International consortium coordinating rare disease research globally.
- [Solve-RD](https://solve-rd.eu/) - European project for solving undiagnosed rare diseases.
- [Genomics England](https://www.genomicsengland.co.uk/) - UK genomic medicine initiative with major rare disease program.
- [RD-Connect](https://rd-connect.eu/) - European platform linking registries, biobanks, and clinical data.
- [Rare-X](https://rare-x.org/) - Patient-powered data sharing platform.
- [RDCA-DAP](https://ncats.nih.gov/research/research-activities/rdca-dap) - Rare Diseases Clinical Research Network data platform.
- [RDMM](https://rare-diseases-catalyst-network.ca/) - Canadian Rare Diseases Models and Mechanisms network.
- [All of Us](https://allofus.nih.gov/) - NIH precision medicine cohort with rare disease representation.
- [GA4GH](https://www.ga4gh.org/) - Global Alliance for Genomics and Health developing data sharing standards.
- [ELIXIR Rare Disease Community](https://elixir-europe.org/communities/rare-diseases) - European infrastructure for rare disease data.
- [ERDERA](https://erdera.org/) - European Rare Diseases Research Alliance unifying resources and expertise across Europe.
- [European Reference Networks (ERNs)](https://health.ec.europa.eu/rare-diseases-and-european-reference-networks_en) - Cross-border networks of specialist centers for rare disease care.
- [RDCRN](https://www.rarediseasesnetwork.org/) - Rare Diseases Clinical Research Network with 21 consortia studying 200+ diseases.

## Patient Registries

Registries collecting patient-level data for rare disease research.

- [NIH GRDR Program](https://grdr.hms.harvard.edu/) - Global Rare Diseases Patient Registry Data Repository.
- [TREAT-NMD](https://www.treat-nmd.org/) - Neuromuscular disease registry network.
- [RD-Connect](https://rd-connect.eu/) - European registry and biobank platform.
- [CoRDS](https://sanfordresearch.org/cords/) - Coordination of Rare Diseases at Sanford.
- [IAMRARE Registry Program](https://ncats.nih.gov/iamrare) - NCATS-supported patient registry infrastructure.
- [RaDaR](https://registries.ncats.nih.gov/) - NCATS guidance and resources for developing rare disease registries.

## Patient Advocacy & Support Organizations

Organizations providing patient support and driving rare disease awareness.

- [NORD](https://rarediseases.org/) - National Organization for Rare Disorders (US).
- [EURORDIS](https://www.eurordis.org/) - European alliance of rare disease patient organizations.
- [Global Genes](https://globalgenes.org/) - Rare disease patient advocacy and support.
- [Rare Diseases International](https://www.rarediseasesinternational.org/) - Global patient alliance.
- [Genetic Alliance](https://geneticalliance.org/) - Network of disease-specific advocacy organizations.
- [EveryLife Foundation](https://everylifefoundation.org/) - Rare disease policy advocacy.
- [SWAN UK](https://www.undiagnosed.org.uk/) - Support for undiagnosed genetic conditions.
- [CORD](https://www.raredisorders.ca/) - Canadian Organization for Rare Disorders.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.

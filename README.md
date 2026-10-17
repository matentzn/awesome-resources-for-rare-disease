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
- [Monarch Initiative](https://monarchinitiative.org/) - Integrates rare disease data across species, linking human diseases to model organism phenotypes to support variant interpretation and therapeutic target discovery. [Data downloads](https://monarchinitiative.org/kg/downloads).
- [Orphadata](https://www.orphadata.com/) - The downloadable data arm of Orphanet, providing gene-disease associations, epidemiology, phenotype annotations, and disease classifications in machine-readable formats (XML, JSON).
- [HPO Annotations (HPOA)](https://hpo.jax.org/data/annotations) - Curated disease-to-phenotype associations linking rare diseases to HPO terms. Powers phenotype-driven diagnostic tools like Exomiser and LIRICAL. Freely downloadable.
- [DisGeNET](https://www.disgenet.org/) - Aggregates gene-disease associations from curated sources (OMIM, ClinVar, UniProt) and text mining. Useful for exploring genetic underpinnings of rare diseases. [Downloads available](https://www.disgenet.org/downloads).
- [GARD](https://rarediseases.info.nih.gov/) - NIH Genetic and Rare Diseases Information Center providing patient-accessible disease summaries, inheritance patterns, and links to clinical resources for over 7,000 rare diseases.
- [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/) - Expert-authored, peer-reviewed clinical descriptions of genetic conditions including diagnosis, management, and genetic counseling. The clinical reference standard for inherited disorders.
- [MalaCards](https://www.malacards.org/) - Integrates rare disease information from 74 sources into unified disease cards, useful for exploring disease relationships and annotations.
- [GenCC](https://thegencc.org/) - The Gene Curation Coalition, a collaborative resource that standardises gene-disease validity classifications from multiple genetic testing organisations and research centres worldwide.
- [DECIPHER](https://www.deciphergenomics.org/) - Database of chromosomal imbalance and phenotype in humans. Contains over 60,000 patient records linking genomic variants to rare disease phenotypes, critical for CNV interpretation.
- [Open Targets Platform](https://platform.opentargets.org/) - Integrates genetics, genomics, and drug data to identify therapeutic targets. Includes rare disease associations from OMIM, Orphanet, and ClinVar. [Data downloads](https://platform.opentargets.org/downloads).
- [FDA Orphan Drug Designations](https://www.accessdata.fda.gov/scripts/opdlisting/oopd/) - Searchable database of 5,000+ orphan drug designations since 1983, tracking which rare diseases have drugs in development or approved.
- [EMA Orphan Designation](https://www.ema.europa.eu/en/human-regulatory-overview/orphan-designation-overview) - European Medicines Agency database of orphan medicinal product designations, providing information on drugs designated for rare diseases in the EU.
- [Gene2Phenotype (G2P)](https://www.ebi.ac.uk/gene2phenotype/) - Expert-curated gene-disease models for monogenic disorders, maintained at EMBL-EBI. Each record holds allelic requirement, variant consequence, molecular mechanism, phenotypes and a confidence level, organised into panels (developmental disorders, eye, skin, skeletal, cardiac, ear, cancer). [Downloads](https://www.ebi.ac.uk/gene2phenotype/download), open REST API.
- [PanelApp](https://panelapp.genomicsengland.co.uk/) - Genomics England knowledge base of crowdsourced, expert-reviewed virtual gene panels for rare disease and cancer. Genes, STRs and CNVs are rated by evidence level, and the panels set the analysis scope for the NHS Genomic Medicine Service. [API](https://panelapp.genomicsengland.co.uk/api/docs/), panel downloads.
- [PanelApp Australia](https://panelapp-aus.org/) - Australian instance of PanelApp holding rare disease and cancer gene panels curated and used by Australian diagnostic laboratories. [API](https://panelapp-aus.org/api/docs/), panel downloads.
- [SysNDD](https://sysndd.dbmr.unibe.ch/) - Manually curated database of gene-inheritance-disease units for neurodevelopmental disorders, each with a confidence class and HPO-linked phenotypes. Successor to SysID, hosted at the University of Bern and updated every 3 to 4 months. REST API; [GitHub](https://github.com/berntpopp/sysndd).
- [IEMbase](https://www.iembase.org/) - Knowledge base and diagnosis-support tool for inborn errors of metabolism, covering clinical and biochemical features, genes and treatments. Maintained by teams at the University of British Columbia and the University of Zurich with the Society for Inherited Metabolic Diseases. Free web access.
- [NanbyoData](https://nanbyodata.jp/) - Japanese knowledge base on designated intractable (nanbyo) diseases from the Database Center for Life Science (DBCLS), built on the NANDO ontology, with disease-gene and HPO-coded disease-phenotype associations. Downloads (RDF, Excel, CSV, JSON) and an API under CC BY 4.0.
- [DDrare](https://ddrare.nibn.go.jp/index_e.html) - Database of Drug Development for Rare Diseases from Japan's National Institutes of Biomedical Innovation, Health and Nutrition. Links Japanese designated intractable diseases to drugs in US, EU, Chinese and Japanese clinical trial registries and to their target genes and pathways. [Data on figshare](https://doi.org/10.6084/m9.figshare.25904107).
- [KDCA Rare Disease List](https://www.data.go.kr/data/3074262/fileData.do) - South Korea's official list of nationally designated rare diseases from the Korea Disease Control and Prevention Agency, with Korean and English names, KCD codes, insurance codes and registration criteria. Free XLSX download.
- [CTGA](https://cags.org.ae/en/ctga-overview) - Catalogue for Transmission Genetics in Arabs from the Centre for Arab Genomic Studies (Dubai). Links inherited disorders reported in Arab populations to genes, variants, inheritance patterns, countries of origin and publications. Free web search.
- [RSDB (Rare Skin Disease Database)](https://rsdb.cmdm.tw/) - Network database linking rare skin diseases to genes, phenotypes and chemical compounds, including candidate drug-repurposing relationships. Maintained by the CMDM lab, National Taiwan University. [Downloads](https://figshare.com/articles/dataset/Rare_Skin_Disease_Database/17704502).

## Ontologies & Terminologies

Standardized vocabularies essential for rare disease data integration. These enable cross-resource queries and interoperability between databases, registries, and clinical systems.

- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/) - The unifying disease ontology that harmonizes OMIM, Orphanet, NCIT, and other disease sources. Provides stable identifiers and cross-references essential for integrating rare disease data across resources. [GitHub](https://github.com/monarch-initiative/mondo).
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) - The standard vocabulary for clinical phenotypes with over 18,000 terms. Used by ClinVar, OMIM, Orphanet, and diagnostic tools. Enables phenotype-driven rare disease diagnosis. [GitHub](https://github.com/obophenotype/human-phenotype-ontology).
- [Orphanet Rare Disease Ontology (ORDO)](https://sciences.orphadata.com/ordo/) - The ontological representation of the Orphanet nomenclature. ORPHAcodes are [mandated for rare disease coding in EU health systems](https://ojrd.biomedcentral.com/articles/10.1186/s13023-015-0251-8) and enable cross-border data sharing.
- [ORPHAcodes Nomenclature Pack](https://www.orphacode.org/pack-nomenclature/) - Annual Orphanet package for coding rare diseases in health information systems: nomenclature, specialty classifications, linearisation, ICD-10 and ICD-11 mappings, a master file for EU-level data sharing and a change file. Released each July in 9 languages under CC BY 4.0, with a SNOMED CT mapping file and an API.
- [Alpha-ID-SE](https://www.bfarm.de/EN/Code-systems/Terminologies/Alpha-ID-SE/_node.html) - German coding system maintained by BfArM that links diagnostic terms and ICD-10-GM codes to ORPHAcodes, so rare diseases can be coded uniquely in hospital data. Updated annually. [Downloads](https://www.bfarm.de/EN/Code-systems/Services/Downloads/_node.html).
- [NANDO (Nanbyo Disease Ontology)](https://nanbyodata.jp/about_nando) - Ontology of Japan's designated intractable diseases and specified chronic diseases of children, maintained by DBCLS, with English labels and mappings to Mondo, Orphanet and MedGen. CC BY 4.0; used by NanbyoData.
- [Online IMD (ICIMD)](https://oimd.org/) - Online catalogue for the International Classification of Inherited Metabolic Disorders, with an entry per disorder in a hierarchy of disease groups covering genes, pathways, phenotypes and diagnostic features. Developed by MetabERN and the Medical University of Innsbruck. Classification paper: [doi:10.1002/jimd.12348](https://doi.org/10.1002/jimd.12348).
- [Nosology of Genetic Skeletal Disorders](https://internationalsds.org/nosology/) - Expert classification of genetic skeletal disorders by the International Skeletal Dysplasia Society, with disorder groups, inheritance, causal genes and OMIM links. The 2023 revision is a searchable online table plus a paper ([doi:10.1002/ajmg.a.63132](https://doi.org/10.1002/ajmg.a.63132)).

## Data Standards & Exchange Formats

Standards specifically designed for or widely adopted by the rare disease community for data exchange.

- [Phenopackets](http://phenopackets.org/) - GA4GH standard for sharing patient phenotype and disease information. Adopted by rare disease diagnostic pipelines and the [Matchmaker Exchange](https://www.matchmakerexchange.org/). [Schema](https://github.com/phenopackets/phenopacket-schema).
- [GA4GH Beacon](https://beacon-project.io/) - Protocol for querying genomic variant presence across federated datasets. Enables privacy-preserving rare variant discovery across institutions.
- [RD-CDM](https://rd-cdm.readthedocs.io/) - Rare Disease Common Data Model extending ERDRI-CDS for international registry harmonization, compatible with Phenopackets and FHIR.
- [Clinical And Registry Entries Semantic Model (CARE-SM)](https://care-sm.readthedocs.io/en/latest/) - Semantic data model for representing a set of common data elements for rare diseases registration. [GitHub](https://github.com/CARE-SM/CARE-Semantic-Model).
- [EJP RD Resource Metadata Model](https://github.com/ejp-rd-vp/resource-metadata-schema) - DCAT-based metadata model for describing rare disease registries, biobanks and catalogues with Orphanet codes, developed for the EJP RD (now ERDERA) Virtual Platform and FAIR Data Points. RDF examples and SHACL/ShEx shapes under CC0.
- [MII Core Data Set Module Rare Diseases](https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Seltene_Erkrankungen_2026/MIIIGModulSeltene.html) - HL7 FHIR R4 Implementation Guide from the German Medical Informatics Initiative for rare disease care data: HPO-based phenotyping, diagnoses, measurements, family history, therapy recommendations and trial participation.
- [CDISC Rare Diseases Therapeutic Area User Guide](https://www.cdisc.org/standards/therapeutic-areas/rare-diseases/rare-diseases-therapeutic-area-user-guide) - CDISC guide for structuring rare disease clinical trial data in CDASH, SDTM and ADaM, with sample annotated CRFs and example datasets. Developed with NORD (v1.0, 2023); files require a CDISC sign-in.
- [Model Consent Clauses for Rare Disease Research](https://www.ga4gh.org/document/model-consent-clauses-for-rare-disease-research/) - Template consent language from a joint IRDiRC and GA4GH task force covering familial participation, imaging, data sharing, recontact for matching, data linkage and return of results to relatives. Part of the GA4GH Consent Toolkit ([doi:10.1186/s12910-019-0390-x](https://doi.org/10.1186/s12910-019-0390-x)).

## Variant & Genomic Data

Resources providing variant-level data essential for rare disease genetic diagnosis.

- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) - The primary public archive of variant-disease relationships with clinical interpretations. Contains over 2 million submissions, essential for rare disease variant classification. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/).
- [gnomAD](https://gnomad.broadinstitute.org/) - Population allele frequencies from 140,000+ exomes/genomes. Critical for filtering common variants in rare disease diagnosis - variants above population frequency thresholds are unlikely to cause rare Mendelian disorders. [Downloads](https://gnomad.broadinstitute.org/downloads).
- [ClinGen](https://clinicalgenome.org/) - NIH-funded resource providing expert-curated gene-disease validity, variant pathogenicity, and dosage sensitivity assessments. The authority for clinical actionability of genetic findings.
- [LOVD](https://www.lovd.nl/) - Locus-specific variant databases maintained by gene experts. Many rare disease genes have dedicated LOVD instances with curated variant interpretations.
- [HGMD](http://www.hgmd.cf.ac.uk/) - Human Gene Mutation Database cataloging published disease-causing mutations. Commercial with limited public access; widely used in clinical genetics labs.
- [GREGoR](https://gregorconsortium.org/data) - NHGRI Genomics Research to Elucidate the Genetics of Rare Diseases consortium dataset: family structure, phenotypes, genetic findings, short- and long-read genomes and RNA-seq from thousands of rare disease families. Controlled access via dbGaP (phs003047) on AnVIL; public [variant browser](https://variants.gregorconsortium.org/).
- [Genomics4RD](https://www.genomics4rd.ca/) - National rare disease data platform of the Care4Rare Canada Consortium with structured phenotypes, family history and multi-omic data from Canadian families. Aggregate phenotypes and candidate genes are open; individual-level and raw data are available through registered and controlled access.
- [Australian Genomics Data](https://www.australiangenomics.org.au/tools-and-resources/accessing-australian-genomics-data/) - Genomic and clinical data from Australian Genomics flagship studies, most of them rare disease cohorts (e.g. mitochondrial disease, leukodystrophy, neuromuscular disease, intellectual disability). Access via the Australian Genomics Data Access Committee.
- [Gabriella Miller Kids First Data Resource Center](https://kidsfirstdrc.org/) - NIH Common Fund portal for harmonised genomic and clinical data from pediatric cancer and structural birth defect cohorts. Free to use; controlled genomic data require dbGaP approval.
- [OLIDA](https://olida.ibsquare.be/) - Curated database of oligogenic diseases and the published gene and variant combinations reported to cause them, with evidence and confidence information. Maintained by the Interuniversity Institute of Bioinformatics in Brussels; successor to DIDA. TSV and Excel export, [API](https://olida.ibsquare.be/api/swagger/).
- [CFTR2](https://cftr2.org/) - Cystic fibrosis variant database from the Cystic Fibrosis Foundation, Johns Hopkins University and SickKids, stating for each CFTR variant whether it causes CF, with aggregate clinical data (sweat chloride, lung function, pancreatic status).
- [CFTR-France](https://cftr.chu-montpellier.fr/) - French national CFTR variant database focused on rare variants and clinical phenotypes, run by 10 French laboratories with the Filière Muco-CFTR. Browse online; variant list downloadable.

## APIs & Data Downloads

Programmatic access points for rare disease data integration.

- [Orphadata](https://www.orphadata.com/) - Bulk downloads of Orphanet data including disease classifications, gene associations, epidemiology, and phenotype annotations in XML and RDF formats.
- [Monarch API](https://api-v3.monarchinitiative.org/v3/docs) - REST API for querying integrated rare disease data: disease-gene associations, phenotype profiles, and cross-species mappings.
- [MedGen](https://www.ncbi.nlm.nih.gov/medgen/) - NCBI's portal aggregating disease concepts from OMIM, Orphanet, HPO, Mondo, and ClinVar into unified identifiers. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/medgen/).
- [ERDERA Virtual Platform](https://vp.erdera.org/) - Federated network of FAIR rare disease resources (registries, biobanks, genomic-phenomic repositories, catalogues, knowledge bases) with a discovery portal that queries all participating resources in real time while data stays with its holder. Originally built under EJP RD; part of the [ERDERA Data Hub](https://erdera.org/data-hub/).
- [Phenopacket Store](https://monarch-initiative.github.io/phenopacket-store/) - Curated collection of GA4GH Phenopackets for published individuals with Mendelian diseases, organised by gene, for benchmarking diagnostic software and genotype-phenotype research. Maintained by the Monarch Initiative. [Releases](https://github.com/monarch-initiative/phenopacket-store/releases).
- [RareBench](https://github.com/chenxz1111/RareBench) - Benchmark and patient-case dataset for evaluating large language models on rare disease differential diagnosis, built from five sources (RAMEDIS, MME, HMS, LIRICAL, PUMCH). Apache-2.0, data on [Hugging Face](https://huggingface.co/datasets/chenxz/RareBench).
- [PRO-ACT](https://ncri1.partners.org/ProACT/) - Pooled Resource Open-Access ALS Clinical Trials database from Massachusetts General Hospital, with anonymised records from Phase II/III ALS trials (demographics, labs, history, outcomes). Free download after registration.
- [Taiwan Rare Disease Case Statistics](https://data.gov.tw/dataset/128772) - Open dataset from Taiwan's Health Promotion Administration with counts of confirmed cases per government-designated rare disease. CSV download under the Taiwan Government Open Data License.

## Clinical & Diagnostic Resources

Resources supporting rare disease diagnosis and patient matching.

- [Matchmaker Exchange](https://www.matchmakerexchange.org/) - Federated network connecting patient databases (PhenomeCentral, DECIPHER, GeneMatcher, etc.) to find phenotypically and genotypically similar patients. Critical for confirming novel gene-disease associations in ultra-rare disorders.
- [PhenomeCentral](https://www.phenomecentral.org/) - Secure repository for sharing rare disease patient phenotypes to facilitate diagnosis and research collaboration.
- [Exomiser](https://monarchinitiative.org/tools/exomiser) - Phenotype-driven variant prioritization tool that ranks variants by matching patient HPO terms to known disease-gene phenotypes. Standard tool in rare disease diagnostic pipelines. [GitHub](https://github.com/exomiser/Exomiser).
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Likelihood ratio-based diagnostic tool that provides probabilistic rankings of candidate diagnoses based on phenotypes and genotypes.
- [Phen2Gene](https://phen2gene.wglab.org/) - Phenotype-to-gene prioritization using HPO terms to rank candidate genes before sequencing or for variant interpretation.
- [AMELIE](https://amelie.stanford.edu/) - Automatic literature-based variant interpretation that extracts gene-phenotype relationships from publications.
- [Face2Gene](https://www.face2gene.com/) - AI-powered facial analysis for recognizing dysmorphic features associated with genetic syndromes. Aids diagnosis of syndromic rare diseases.
- [Undiagnosed Diseases Network](https://undiagnosed.hms.harvard.edu/) - NIH-funded network of clinical sites bringing together experts to diagnose patients who have eluded diagnosis despite extensive workup.
- [ERICA PROMs Repository](https://erica-rd.eu/work-packages/patient-centred-research/proms-repository/) - Central repository of patient-reported outcome measures (PROMs) and other clinical outcome assessments relevant to rare diseases, built by Orphanet, Mapi Research Trust, and ERN EuroBloodNet with input from the ERNs. Links through to PROQOLID for detailed instrument information; being scaled up under ERDERA.
- [Undiagnosed Diseases Program (UDP)](https://www.genome.gov/Current-NHGRI-Clinical-Studies/NIH-Undiagnosed-Diseases-Program) - The original NHGRI program at NIH Clinical Center that pioneered systematic approaches to solving undiagnosed rare diseases.

## Analysis Tools & Software

Open-source tools developed for or widely used in rare disease analysis.

- [Exomiser](https://monarchinitiative.org/tools/exomiser) - The standard phenotype-aware variant prioritization tool for rare disease exome/genome analysis.
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Probabilistic phenotype-driven diagnostic tool.
- [Seqr](https://github.com/broadinstitute/seqr) - Open-source web platform for rare disease family-based variant analysis, used by the Broad Institute's rare disease genomics programs.
- [MARRVEL](https://marrvel.org/) - IRDiRC-recognized tool integrating human variant databases with 7 model organism resources to prioritize rare variants for functional study.
- [monarchR](https://monarch-initiative.github.io/monarchr/articles/monarchr) - R package providing programmatic access to Monarch Initiative biomedical knowledge graphs for querying genes, diseases, and phenotype relationships. [GitHub](https://github.com/monarch-initiative/monarchr).
- [HPOExplorer](https://github.com/neurogenomics/HPOExplorer) - R package for importing, annotating, filtering, and visualising the Human Phenotype Ontology (HPO) at multiple biological levels including diseases, phenotypes, and genes.
- [MSTExplorer](https://github.com/neurogenomics/MSTExplorer) - R package that identifies, prioritises, and visualises cell-type-specific gene therapy targets across the phenome by analysing associations between diseases, phenotypes, cell types, and genes.
- [Rare Disease Celltyping Portal](https://neurogenomics-ukdri.dsi.ic.ac.uk/) - Interactive portal for exploring cell-type associations across rare diseases, linking phenotypes to cell types using single-cell transcriptomic data.
- [DeepRare](https://github.com/MAGIC-AI4Med/DeepRare) - AI-powered agentic diagnostic system that processes symptoms, genetic data, and medical history to generate ranked rare disease diagnoses with transparent reasoning chains, integrating 40+ specialized tools and outperforming traditional methods on benchmarks.

## Research Platforms & Initiatives

Major programs and consortia advancing rare disease research through data sharing and collaboration.

- [NCATS](https://ncats.nih.gov/) - NIH National Center for Advancing Translational Sciences with dedicated rare disease programs including RDCRN, GARD, and drug repurposing initiatives.
- [IRDiRC](https://irdirc.org/) - International Rare Diseases Research Consortium coordinating global research efforts with goals to diagnose all rare diseases and develop 1000 new therapies.
- [Solve-RD](https://solve-rd.eu/) - European project applying multi-omics approaches to solve undiagnosed rare diseases through data sharing across European Reference Networks.
- [Genomics England](https://www.genomicsengland.co.uk/) - UK initiative that has sequenced over 100,000 genomes, with rare disease as a primary focus. Provides access to research datasets.
- [RD-Connect](https://rd-connect.eu/) - European platform linking rare disease registries, biobanks, and clinical bioinformatics to enable integrated research.
- [Rare-X](https://rare-x.org/) - Patient-powered platform enabling rare disease patients to collect and share their health data for research.
- [RDMM](https://rare-diseases-catalyst-network.ca/) - Canadian Rare Diseases Models and Mechanisms network connecting clinicians with basic scientists to validate rare disease gene discoveries.
- [GA4GH Rare Disease Community](https://www.ga4gh.org/community/rare-disease/) - Dedicated community bridging clinical and technical RD stakeholders, coordinating global data sharing and standards implementation.
- [OHDSI Rare Disease Working Group](https://www.ohdsi.org/ohdsi2025-workgroups/) - Develops methods for rare disease cohort identification and research using OMOP CDM across global real-world data networks.
- [EU RD Platform](https://eu-rd-platform.jrc.ec.europa.eu/) - European Commission platform providing directory of registries, common data elements, and cross-registry search tools for RD patient data harmonization.
- [ELIXIR Rare Disease Community](https://elixir-europe.org/communities/rare-diseases) - European bioinformatics infrastructure community focused on rare disease data resources and standards.
- [ERDERA](https://erdera.org/) - European Rare Diseases Research Alliance (launched 2024) unifying research resources, clinical networks, and expertise across Europe. Successor to EJP RD.
- [European Reference Networks (ERNs)](https://health.ec.europa.eu/rare-diseases-and-european-reference-networks_en) - 24 cross-border networks of specialist centers for rare disease diagnosis and care, mandated by EU Cross-Border Healthcare Directive.
- [RDCRN](https://www.rarediseasesnetwork.org/) - NIH Rare Diseases Clinical Research Network with 21 consortia studying 200+ rare diseases, providing infrastructure for natural history studies and clinical trials.
- [IRUD](https://www.amed.go.jp/en/program/IRUD/) - Japan's Initiative on Rare and Undiagnosed Diseases with 418 participating hospitals, achieving diagnosis in 44% of 6,300+ registered pedigrees.
- [Every Cure](https://everycure.org/) - ARPA-H funded nonprofit using AI to identify drug repurposing opportunities across 4,000 approved drugs for rare disease treatment.
- [SimPaThIC](https://simpathic.eu/) - EU Horizon-funded consortium of 22 partners repurposing existing drugs for rare neurological, neurometabolic, and neuromuscular disorders using patient-derived cell models.
- [Screen4Care](https://www.screen4care.eu/) - IMI2/IHI-funded public-private-patient consortium (2021-2026) shortening the rare disease diagnostic journey through genetic newborn screening of ~25,000 infants and AI-based diagnostic tools. Produced the TREAT gene panel for selecting treatable rare diseases for genomic newborn screening.
- [JARDIN](https://jardin-ern.eu/) - EU Joint Action (2024-2027) integrating the European Reference Networks into national health systems. Its data management work package addresses ERN registry interoperability and is defining a rare disease dataset for EHRs, aligned with the European EHR exchange format (EEHRxF) and ORPHAcodes.
- [RDAS](https://rdas.ncats.nih.gov/) - NCATS Rare Disease Alert System integrating PubMed articles, clinical trials, and NIH grant data into a searchable knowledge graph. Users can browse and subscribe to alerts for rare diseases of interest.
- [RARe-SOURCE](https://raresource.nih.gov/) - NCATS bioinformatics platform providing annotated data on rare diseases, associated genes, variants, and proteins, with AI-enhanced literature search and protein structure visualization to support drug discovery.
- [C-Path](https://c-path.org/) - Critical Path Institute, a nonprofit that brings together regulators, industry, and academia to accelerate drug development for diseases with unmet needs, including dedicated rare disease programmes such as Duchenne muscular dystrophy and polycystic kidney disease.

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
- [Rare Barometer](https://www.eurordis.org/rare-barometer/) - EURORDIS survey programme collecting the experience of people living with a rare disease and their carers (diagnostic odyssey, access to care, social participation, mental health) in up to 26 languages. Results are published as reports and fact sheets and are widely cited in EU rare disease policy.
- [Global Genes](https://globalgenes.org/) - Patient advocacy organization providing support programs and resources for rare disease families.
- [Rare Diseases International](https://www.rarediseasesinternational.org/) - Global alliance of national rare disease organizations advocating for rare disease recognition worldwide.
- [Genetic Alliance](https://geneticalliance.org/) - Network connecting disease-specific advocacy organizations with researchers and policymakers.
- [EveryLife Foundation](https://everylifefoundation.org/) - Policy advocacy organization focused on rare disease legislation and regulatory issues.
- [SWAN UK](https://geneticalliance.org.uk/support-and-information/swan-uk-syndromes-without-a-name/) - Support network for families of children with Syndromes Without A Name (undiagnosed genetic conditions).
- [CORD](https://www.raredisorders.ca/) - Canadian Organization for Rare Disorders providing patient support and advocating for rare disease policy in Canada.
- [Rare Diseases South Africa](https://www.rarediseases.co.za/) - South African rare disease information and support hub.
- [Rare Disease UK](http://www.raredisease.org.uk/) - National campaign by Genetic Alliance UK representing and uniting the rare disease community across the United Kingdom.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.

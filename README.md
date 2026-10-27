# Awesome Resources for Rare Disease

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://oboacademy.github.io/obook/tutorial/pull-requests/)
![License](https://img.shields.io/github/license/matentzn/awesome-resources-for-rare-disease.svg?color=blue)

> A curated list of data resources, ontologies, standards and tools for rare disease research and data integration.

This list is for researchers, bioinformaticians, data engineers and developers who work with rare disease data. Every entry is something you can query, download, run, adopt as a standard, or apply to for data access. Where a resource offers bulk downloads or an API, the entry links to them.

**Not in scope:** patient and family support, advocacy and funding organisations, events and media. Families looking for support are better served by [Librarey](https://www.librarey.com/), and the [Resource Ecosystem](https://boycelab.github.io/rare-resources/) covers rare disease, disability and family support resources more broadly. Resources that were considered but excluded (for example general-purpose tools such as GitHub, or general ontologies) are listed in [EXCLUDED.md](EXCLUDED.md).

## Contents

- [Disease-Gene-Phenotype Data](#disease-gene-phenotype-data)
- [Ontologies & Terminologies](#ontologies--terminologies)
- [Data Standards & Exchange Formats](#data-standards--exchange-formats)
- [Variant & Genomic Data](#variant--genomic-data)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Patient Registries & Biobanks](#patient-registries--biobanks)
- [Diagnosis & Patient Matching](#diagnosis--patient-matching)
- [Analysis Tools & Software](#analysis-tools--software)
- [Research Programmes & Communities](#research-programmes--communities)
- [Directories & Catalogues](#directories--catalogues)

## Disease-Gene-Phenotype Data

Core knowledge bases providing structured data on rare diseases, their genetic causes, and clinical presentations.

- [Orphanet](https://www.orpha.net/) - The European reference portal for rare diseases, providing expert-validated information on over 6,500 rare diseases including prevalence, inheritance, age of onset, and gene associations. The primary source of ORPHAcodes used in European health systems.
- [OMIM](https://omim.org/) - The authoritative compendium of human genes and Mendelian phenotypes, maintained since 1966. Contains detailed clinical synopses and molecular genetics for inherited disorders. [Downloads](https://omim.org/downloads) (requires registration).
- [Monarch Initiative](https://monarchinitiative.org/) - Integrates rare disease data across species, linking human diseases to model organism phenotypes to support variant interpretation and therapeutic target discovery. [Data downloads](https://monarchinitiative.org/kg/downloads), [REST API](https://api-v3.monarchinitiative.org/v3/docs).
- [Orphadata](https://www.orphadata.com/) - The downloadable data arm of Orphanet, providing gene-disease associations, epidemiology, phenotype annotations, and disease classifications in machine-readable formats (XML, JSON).
- [HPO Annotations (HPOA)](https://obophenotype.github.io/human-phenotype-ontology/annotations/introduction/) - Curated disease-to-phenotype associations linking rare diseases to HPO terms. Powers phenotype-driven diagnostic tools like Exomiser and LIRICAL. Freely downloadable.
- [DisGeNET](https://www.disgenet.org/) - Aggregates gene-disease associations from curated sources (OMIM, ClinVar, UniProt) and text mining. Useful for exploring genetic underpinnings of rare diseases. [Downloads available](https://www.disgenet.org/downloads).
- [GARD](https://rarediseases.info.nih.gov/) - NIH Genetic and Rare Diseases Information Center providing patient-accessible disease summaries, inheritance patterns, and links to clinical resources for over 7,000 rare diseases.
- [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/) - Expert-authored, peer-reviewed clinical descriptions of genetic conditions including diagnosis, management, and genetic counseling. The clinical reference standard for inherited disorders.
- [MalaCards](https://www.malacards.org/) - Integrates rare disease information from 74 sources into unified disease cards, useful for exploring disease relationships and annotations.
- [GenCC](https://thegencc.org/) - The Gene Curation Coalition, a collaborative resource that standardises gene-disease validity classifications from multiple genetic testing organisations and research centres worldwide.
- [Gene2Phenotype (G2P)](https://www.ebi.ac.uk/gene2phenotype/) - Expert-curated gene-disease models for monogenic disorders, maintained at EMBL-EBI. Each record holds allelic requirement, variant consequence, molecular mechanism, phenotypes and a confidence level, organised into panels (developmental disorders, eye, skin, skeletal, cardiac, ear, cancer). [Downloads](https://www.ebi.ac.uk/gene2phenotype/download), open REST API.
- [PanelApp](https://panelapp.genomicsengland.co.uk/) - Genomics England knowledge base of crowdsourced, expert-reviewed virtual gene panels for rare disease and cancer. Genes, STRs and CNVs are rated by evidence level, and the panels set the analysis scope for the NHS Genomic Medicine Service. [API](https://panelapp.genomicsengland.co.uk/api/docs/), panel downloads.
- [PanelApp Australia](https://panelapp-aus.org/) - Australian instance of PanelApp holding rare disease and cancer gene panels curated and used by Australian diagnostic laboratories. [API](https://panelapp-aus.org/api/docs/), panel downloads.
- [SysNDD](https://sysndd.dbmr.unibe.ch/) - Manually curated database of gene-inheritance-disease units for neurodevelopmental disorders, each with a confidence class and HPO-linked phenotypes. Successor to SysID, hosted at the University of Bern. REST API; [GitHub](https://github.com/berntpopp/sysndd).
- [DECIPHER](https://www.deciphergenomics.org/) - Database of chromosomal imbalance and phenotype in humans. Contains over 60,000 patient records linking genomic variants to rare disease phenotypes, critical for CNV interpretation.
- [Open Targets Platform](https://platform.opentargets.org/) - Integrates genetics, genomics, and drug data to identify therapeutic targets. Includes rare disease associations from OMIM, Orphanet, and ClinVar. [Data downloads](https://platform.opentargets.org/downloads).
- [FDA Orphan Drug Designations](https://www.accessdata.fda.gov/scripts/opdlisting/oopd/) - Searchable database of 5,000+ orphan drug designations since 1983, tracking which rare diseases have drugs in development or approved.
- [EMA Orphan Designation](https://www.ema.europa.eu/en/human-regulatory-overview/orphan-designation-overview) - European Medicines Agency database of orphan medicinal product designations, providing information on drugs designated for rare diseases in the EU.
- [IEMbase](https://www.iembase.org/) - Knowledge base and diagnosis-support tool for inborn errors of metabolism, covering clinical and biochemical features, genes and treatments. Maintained by teams at the University of British Columbia and the University of Zurich with the Society for Inherited Metabolic Diseases. Free web access.
- [Online IMD (OIMD)](https://oimd.org/) - Free clinical knowledge base on inherited metabolic disorders from MetabERN and the Institute of Human Genetics at the Medical University of Innsbruck. It has an entry for every disorder in the International Classification of Inherited Metabolic Disorders (ICIMD), covering biochemistry, clinical presentation, differential diagnosis, genetics and treatment. Classification paper: [doi:10.1002/jimd.12348](https://doi.org/10.1002/jimd.12348).
- [NanbyoData](https://nanbyodata.jp/) - Japanese knowledge base on designated intractable (nanbyo) diseases from the Database Center for Life Science (DBCLS), built on the NANDO ontology, with disease-gene and HPO-coded disease-phenotype associations. Downloads (RDF, Excel, CSV, JSON) and an API under CC BY 4.0.
- [DDrare](https://ddrare.nibn.go.jp/index_e.html) - Database of Drug Development for Rare Diseases from Japan's National Institutes of Biomedical Innovation, Health and Nutrition. Links Japanese designated intractable diseases to drugs in US, EU, Chinese and Japanese clinical trial registries and to their target genes and pathways. Web search only.
- [CTGA](https://cags.org.ae/en/ctga-overview) - Catalogue for Transmission Genetics in Arabs from the Centre for Arab Genomic Studies (Dubai). Links inherited disorders reported in Arab populations to genes, variants, inheritance patterns, countries of origin and publications. Free web search.
- [MedGen](https://www.ncbi.nlm.nih.gov/medgen/) - NCBI's portal aggregating disease concepts from OMIM, Orphanet, HPO, Mondo, and ClinVar into unified identifiers. [FTP downloads](https://ftp.ncbi.nlm.nih.gov/pub/medgen/).
- [RDAS](https://rdas.ncats.nih.gov/) - NCATS Rare Disease Alert System integrating PubMed articles, clinical trials, and NIH grant data into a searchable knowledge graph. Users can browse and subscribe to alerts for rare diseases of interest.
- [RARe-SOURCE](https://raresource.nih.gov/) - NCATS bioinformatics platform providing annotated data on rare diseases, associated genes, variants, and proteins, with AI-enhanced literature search and protein structure visualization to support drug discovery.

## Ontologies & Terminologies

Standardized vocabularies essential for rare disease data integration. These enable cross-resource queries and interoperability between databases, registries, and clinical systems.

- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/) - The unifying disease ontology that harmonizes OMIM, Orphanet, NCIT, and other disease sources. Provides stable identifiers and cross-references essential for integrating rare disease data across resources. [GitHub](https://github.com/monarch-initiative/mondo).
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) - The standard vocabulary for clinical phenotypes with over 18,000 terms. Used by ClinVar, OMIM, Orphanet, and diagnostic tools. Enables phenotype-driven rare disease diagnosis. [GitHub](https://github.com/obophenotype/human-phenotype-ontology).
- [Orphanet Rare Disease Ontology (ORDO)](https://sciences.orphadata.com/ordo/) - The ontological representation of the Orphanet nomenclature. ORPHAcodes are [mandated for rare disease coding in EU health systems](https://ojrd.biomedcentral.com/articles/10.1186/s13023-015-0251-8) and enable cross-border data sharing.
- [ORPHAcodes Nomenclature Pack](https://www.orphacode.org/pack-nomenclature/) - Annual Orphanet package for coding rare diseases in health information systems: nomenclature, specialty classifications, linearisation, ICD-10 and ICD-11 mappings, a master file for EU statistical reporting and a change file. Released annually in several languages under CC BY 4.0, with a SNOMED CT mapping file and an API.
- [Alpha-ID-SE](https://www.bfarm.de/EN/Code-systems/Terminologies/Alpha-ID-SE/_node.html) - German coding system maintained by BfArM that links diagnostic terms and ICD-10-GM codes to ORPHAcodes, so rare diseases can be coded uniquely in hospital data. Updated annually. [Downloads](https://www.bfarm.de/EN/Code-systems/Services/Downloads/_node.html).
- [KDCA Rare Disease List](https://www.data.go.kr/data/3074262/fileData.do) - South Korea's official list of nationally designated rare diseases from the Korea Disease Control and Prevention Agency, with Korean and English names, KCD codes, insurance codes and registration criteria. Free XLSX download.
- [NANDO (Nanbyo Disease Ontology)](https://nanbyodata.jp/about_nando) - Ontology of Japan's designated intractable diseases and specified chronic diseases of children, maintained by DBCLS, with English labels and mappings to Mondo, Orphanet and MedGen. CC BY 4.0; used by NanbyoData.
- [Nosology of Genetic Skeletal Disorders](https://internationalsds.org/nosology/) - Expert classification of genetic skeletal disorders by the International Skeletal Dysplasia Society, with disorder groups, inheritance, causal genes and OMIM links. The 2023 revision is a searchable online table plus a paper ([doi:10.1002/ajmg.a.63132](https://doi.org/10.1002/ajmg.a.63132)).

## Data Standards & Exchange Formats

Standards specifically designed for or widely adopted by the rare disease community for data exchange.

- [Phenopackets](http://phenopackets.org/) - GA4GH standard for sharing patient phenotype and disease information. Adopted by rare disease diagnostic pipelines and the [Matchmaker Exchange](https://www.matchmakerexchange.org/). [Schema](https://github.com/phenopackets/phenopacket-schema).
- [GA4GH Beacon](https://beacon-project.io/) - Protocol for querying genomic variant presence across federated datasets. Enables privacy-preserving rare variant discovery across institutions.
- [RD-CDM](https://rd-cdm.readthedocs.io/) - Rare Disease Common Data Model extending ERDRI-CDS for international registry harmonization, compatible with Phenopackets and FHIR.
- [RareLink](https://github.com/BIH-CEI/rarelink) - Open-source framework from the Berlin Institute of Health that implements the RD-CDM in REDCap, with ready-made forms, a CLI and export to HL7 FHIR and GA4GH Phenopackets. [Documentation](https://rarelink.readthedocs.io/en/latest/).
- [Clinical And Registry Entries Semantic Model (CARE-SM)](https://care-sm.readthedocs.io/en/latest/) - Semantic data model for representing a set of common data elements for rare diseases registration. [GitHub](https://github.com/CARE-SM/CARE-Semantic-Model).
- [EJP RD Resource Metadata Model](https://github.com/ejp-rd-vp/resource-metadata-schema) - DCAT-based metadata model for describing rare disease registries, biobanks and catalogues with Orphanet codes, developed for the EJP RD (now ERDERA) Virtual Platform and FAIR Data Points. RDF examples and SHACL/ShEx shapes under CC0.
- [MII Core Data Set Module Rare Diseases](https://www.medizininformatik-initiative.de/en/modules-mii-core-data-set) - HL7 FHIR R4 Implementation Guide from the German Medical Informatics Initiative for rare disease care data: HPO-based phenotyping, diagnoses, measurements, family history, therapy recommendations and trial participation. The current release is linked from the modules page.
- [CDISC Rare Diseases Therapeutic Area User Guide](https://www.cdisc.org/standards/therapeutic-areas/rare-diseases/rare-diseases-therapeutic-area-user-guide) - CDISC guide for structuring rare disease clinical trial data in CDASH, SDTM and ADaM, with sample annotated CRFs and example datasets. Developed with NORD (v1.0, 2023); files require a CDISC sign-in.
- [Model Consent Clauses for Rare Disease Research](https://www.ga4gh.org/product/consent-toolkit/) - Template consent language from a joint IRDiRC and GA4GH task force covering familial participation, imaging, data sharing, recontact for matching, data linkage and return of results to relatives. Part of the GA4GH Consent Toolkit ([doi:10.1186/s12910-019-0390-x](https://doi.org/10.1186/s12910-019-0390-x)).
- [ERICA PROMs Repository](https://erica-rd.eu/work-packages/patient-centred-research/proms-repository/) - Central repository of patient-reported outcome measures (PROMs) and other clinical outcome assessments relevant to rare diseases, built by Orphanet, Mapi Research Trust, and ERN EuroBloodNet with input from the ERNs. Links through to PROQOLID for detailed instrument information; being scaled up under ERDERA.

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
- [CFTR2](https://cftr2.org/) - Cystic fibrosis variant database from the Cystic Fibrosis Foundation, Johns Hopkins University and SickKids, stating for each CFTR variant whether it causes CF, with aggregate clinical data (sweat chloride, lung function, pancreatic status).
- [CFTR-France](https://cftr.chu-montpellier.fr/) - French national CFTR variant database focused on rare variants and clinical phenotypes, run by 10 French laboratories with the Filière Muco-CFTR. Browse online; variant list downloadable.

## Datasets & Benchmarks

Curated case collections, benchmark corpora and open datasets for rare disease research and method evaluation.

- [Phenopacket Store](https://monarch-initiative.github.io/phenopacket-store/) - Curated collection of GA4GH Phenopackets for published individuals with Mendelian diseases, organised by gene, for benchmarking diagnostic software and genotype-phenotype research. Maintained by the Monarch Initiative. [Releases](https://github.com/monarch-initiative/phenopacket-store/releases).
- [RareBench](https://github.com/chenxz1111/RareBench) - Benchmark and patient-case dataset for evaluating large language models on rare disease differential diagnosis, built from five sources (RAMEDIS, MME, HMS, LIRICAL, PUMCH_ADM). Apache-2.0, data on [Hugging Face](https://huggingface.co/datasets/chenxz/RareBench).
- [Taiwan Rare Disease Case Statistics](https://data.gov.tw/dataset/128772) - Open dataset from Taiwan's Health Promotion Administration with counts of confirmed cases per government-designated rare disease. CSV download under the Taiwan Government Open Data License.
- [NF Data Portal](https://nf.synapse.org/) - Data repository focused on neurofibromatosis (NF) diseases hosted by Sage Bionetworks with community support through the NF Open Science Initiative; includes [NF Research Tools Central](https://nf.synapse.org/Research%20Tools%20Central/Browse%20Tools/), a repository of research tools for neurofibromatosis (NF) diseases hosted by Sage Bionetworks and developed in collaboration with the Gilbert Family Foundation.
- [ALS Knowledge Portal](https://ampals.synapse.org/) - Data repository focused on Amyotrophic Lateral Sclerosis (ALS) hosted by Sage Bionetworks with community support through the AMP ALS initiative.
- [Rare Barometer](https://www.eurordis.org/rare-barometer/) - EURORDIS survey programme collecting the experience of people living with a rare disease and their carers (diagnostic odyssey, access to care, social participation, mental health) in up to 26 languages. Results are published as reports and fact sheets and are widely cited in EU rare disease policy.

## Patient Registries & Biobanks

Registries, biobanks and pooled data platforms that hold patient-level data or samples and give researchers a route to apply for access, plus programmes that host or guide registries. Patient-organisation registries hosted on CoRDS or IAMRARE are not listed one by one. Find them through those programmes or the [directories](#directories--catalogues).

- [TREAT-NMD](https://www.treat-nmd.org/) - Global neuromuscular disease registry network that has enabled clinical trials for DMD, SMA, and other NMDs by providing trial-ready patient populations.
- [CoRDS](https://research.sanfordhealth.org/rare-disease-registry) - Coordination of Rare Diseases at Sanford providing registry infrastructure for rare disease patient organizations.
- [IAMRARE Registry Program](https://iamrare.org/) - NORD program providing registry infrastructure and support for rare disease advocacy organizations.
- [RaDaR](https://registries.ncats.nih.gov/) - NCATS Rare Diseases Registry Program providing guidance, best practices, and resources for developing rare disease registries.
- [BNDMR](https://www.bndmr.fr/) - French National Rare Disease Data Bank, holding the national rare disease minimum data set collected by expert centres through the BaMaRa application (AP-HP). Researchers apply for pseudonymised data through a formal procedure. [Minimum data set](https://www.bndmr.fr/les-donnees-collectees/le-set-de-donnees-minimal/) (French page, with an English PDF).
- [NARSE](https://www.narse.de/) - Germany's National Registry for Rare Diseases, operated by the Berlin Institute of Health at Charité. Dataset documentation, protocol and usage rules on the [downloads page](https://www.narse.de/downloads).
- [NCARDRS](https://digital.nhs.uk/ndrs/about/ncardrs) - NHS England's National Congenital Anomaly and Rare Disease Registration Service, a population-based register across England. Data requests via NHS England's Data Access Request Service (DARS).
- [RePER](https://registroraras.isciii.es/Comun/Inicio.aspx) - Spanish Rare Disease Patient Registry run by ISCIII-IIER. Researchers and clinicians can work with registry data on their disease of interest under controlled access.
- [Norwegian Registry for Rare Diagnoses](https://www.oslo-universitetssykehus.no/avdelinger/barne-og-ungdomsklinikken/nasjonalt-senter-for-sjeldne-diagnoser/norsk-register-for-sjeldne-diagnoser/) - National registry at Oslo University Hospital recording ORPHA-coded diagnoses, with extra modules for selected disease groups. De-identified data available for ethics-approved research.
- [Swiss Rare Disease Registry (SRDR)](https://www.raredisease.ch/) - National cross-disease registry at the University of Bern collecting epidemiological and clinical information on people with any rare disease in Switzerland.
- [NRDRS](https://www.nrdrs.org.cn/) - National Rare Diseases Registry System of China, led by Peking Union Medical College Hospital with hospitals nationwide ([Orphanet J Rare Dis 2021](https://doi.org/10.1186/s13023-021-02130-7)). Data available from the NRDRS administrative group on request.
- [RADDAR-J](https://www.raddarj.org/en/) - Rare Disease Data Registry of Japan, an AMED-supported platform that hosts and integrates clinical and genomic registries for intractable diseases, with standard protocols and consent templates.
- [NRROID](https://rdrdb.icmr.org.in/registry/) - ICMR National Registry for Rare and Other Inherited Disorders (India), collecting demographics, phenotype, natural history and outcomes for several rare disease groups from contributing centres.
- [Pūnaha Io](https://www.mda.org.nz/registry-biobank) - New Zealand Neuro-Genetic Registry and BioBank for neuromuscular and neurogenetic conditions. Researchers with approved proposals can request de-identified data, samples or recruitment support.
- [ERKReg](https://www.erknet.org/patients-registry) - European Rare Kidney Disease Registry run by the ERKNet European Reference Network, with disease-specific subregistries. Data requests under a published data access policy.
- [EuRREB](https://eurreb.eu/) - European Registries for Rare Endocrine and Bone Conditions, a core registry with condition-specific modules run with Endo-ERN and ERN BOND. Data requests reviewed by a Data Access Committee.
- [ERN-RND Registry](https://www.ern-rnd.eu/ern-rnd-registry/) - Registry of the European Reference Network for Rare Neurological Diseases covering ataxias, HSPs, dystonia, leukodystrophies and other groups. Aggregated data are public; patient-level data via a Data Access Committee.
- [U-IMD](https://u-imd.org/) - Unified European Registry for Inherited Metabolic Disorders, the MetabERN registry, implementing the EU RD Platform common data elements.
- [ESID Registry](https://esid.org/working-parties/registry-working-party/esid-registry/) - European Society for Immunodeficiencies' longitudinal registry of patients with inborn errors of immunity. Research proposals using registry data are reviewed by the steering committee.
- [SDMregistries](https://sdmregistries.org/) - International registry platform for rare conditions affecting sex development and maturation (I-DSD, I-CAH, I-TS, I-HH). Data access via a Data Access Committee; fees apply.
- [GenIDA](https://genida.eu/) - International participatory registry where families report clinical features and natural history for genetic forms of intellectual disability, autism and epilepsy. Professionals can request data access.
- [Simons Searchlight](https://www.simonssearchlight.org/) - Simons Foundation natural history study, registry and biorepository for rare genetic neurodevelopmental disorders. Researchers request phenotype, genetic data and biospecimens through SFARI Base.
- [My Retina Tracker Registry](https://www.fightingblindness.org/my-retina-tracker-registry) - Foundation Fighting Blindness' patient-initiated registry for around 20 inherited retinal diseases. Approved researchers get de-identified diagnosis, gene and variant data through a researcher portal, and the registry supports trial recruitment. People with a clinical IRD diagnosis can get [no-cost genetic testing](https://www.fightingblindness.org/no-cost-genetic-testing) and counselling through it.
- [INPDR](https://inpdr.org/) - International Niemann-Pick Disease Registry, collecting longitudinal patient and clinical data. Data access requests are reviewed by a Scientific Advisory Committee; academic and commercial access carry fees.
- [Enroll-HD](https://www.enroll-hd.org/) - Global observational study and clinical research platform for Huntington's disease families, run by the CHDI Foundation. Periodic clinical datasets are free to researchers at recognised institutions; biosamples on approval with cost-recovery fees.
- [ECFS Patient Registry](https://pr.ecfs.eu/) - European Cystic Fibrosis Society registry with longitudinal data from people with cystic fibrosis across Europe. Annual reports are public; researchers apply for data access.
- [CF Foundation Patient Registry](https://www.cff.org/medical-professionals/patient-registry) - US Cystic Fibrosis Foundation registry of health and treatment data from accredited CF care centres. Annual reports are public; data requests need a proposal and IRB approval.
- [NF Registry](https://www.ctf.org/nf-registry/) - Patient-driven registry for neurofibromatosis (NF) to advance research and improve care funded by the Children's Tumor Foundation.
- [Rare-X](https://rare-x.org/) - Patient-powered platform enabling rare disease patients to collect and share their health data for research.
- [RDCA-DAP](https://portal.rdca.c-path.org/) - Rare Disease Cures Accelerator Data and Analytics Platform, run by C-Path with NORD and FDA funding, pooling patient-level natural history, registry and trial data for many rare diseases in CDISC format. Access requires approval by a Data Use Committee and a Data Use Agreement.
- [Telethon Network of Genetic Biobanks](https://biobanknetwork.telethon.it/) - Fondazione Telethon network of Italian biobanks holding samples for rare genetic diseases, searchable in an online catalogue; samples released for non-commercial research after approval and an MTA.
- [BioNER](https://iier.isciii.es/bioner-inicio) - Spain's National Rare Diseases Biobank, run by ISCIII-IIER, holding samples from people with rare diseases, relatives and controls, linked to the Spanish rare disease registry. Samples available after scientific and ethical review.

## Diagnosis & Patient Matching

Undiagnosed disease programmes and matchmaking services that connect clinicians and researchers around unsolved cases. Diagnostic software is under [Analysis Tools & Software](#analysis-tools--software).

- [Matchmaker Exchange](https://www.matchmakerexchange.org/) - Federated network connecting patient databases (PhenomeCentral, DECIPHER, GeneMatcher, etc.) to find phenotypically and genotypically similar patients. Critical for confirming novel gene-disease associations in ultra-rare disorders.
- [PhenomeCentral](https://www.phenomecentral.org/) - Secure repository for sharing rare disease patient phenotypes to facilitate diagnosis and research collaboration.
- [Undiagnosed Diseases Network](https://undiagnosed.hms.harvard.edu/) - NIH-funded network of clinical sites bringing together experts to diagnose patients who have eluded diagnosis despite extensive workup.
- [Undiagnosed Diseases Program (UDP)](https://www.genome.gov/Current-NHGRI-Clinical-Studies/NIH-Undiagnosed-Diseases-Program) - The original NHGRI program at NIH Clinical Center that pioneered systematic approaches to solving undiagnosed rare diseases.
- [K-UDP](https://raredisease.snuh.org/en/main-projects/k-udp/) - Korean Undiagnosed Diseases Program run by the Seoul National University Hospital Center for Rare Diseases, offering trio genetic testing, multidisciplinary interpretation and functional studies, and sharing data on unsolved cases with international research groups.
- [IRUD](https://www.amed.go.jp/en/program/IRUD/) - Japan's Initiative on Rare and Undiagnosed Diseases with 418 participating hospitals, achieving diagnosis in 44% of 6,300+ registered pedigrees.
- [UDNI](https://www.udninternational.org/) - Undiagnosed Diseases Network International, coordinated from the Istituto Superiore di Sanità, connecting national undiagnosed disease programmes that share HPO-coded phenotype and genetic data under a common agreement.
- [PRaGeD](https://praged.cdfd.org.in/) - Indian Mission Programme on Pediatric Rare Genetic Disorders led by the Centre for DNA Fingerprinting and Diagnostics, applying exome and genome sequencing and functional validation to children with undiagnosed genetic disorders.
- [GeneMatcher](https://genematcher.org/) - Matchmaker Exchange node from Johns Hopkins University that connects clinicians and researchers who submit the same candidate gene, supporting discovery of new Mendelian gene-disease associations. Free; registration required.
- [MyGene2](https://mygene2.org/) - Public portal from the University of Washington Center for Mendelian Genomics where families, clinicians and researchers share phenotype and candidate-gene information, matched through the Matchmaker Exchange.
- [GestaltMatcher Database](https://db.gestaltmatcher.org/) - Curated database of medical photographs and case reports of genetic syndromes for facial-phenotype analysis and patient matching. Maintained at the University of Bonn; access by invitation or request. [Model code](https://github.com/igsb/GestaltMatcher-Arc).

## Analysis Tools & Software

Software and analysis platforms developed for or widely used in rare disease analysis and diagnosis.

- [Exomiser](https://monarchinitiative.org/tools/exomiser) - Phenotype-driven variant prioritization tool that ranks variants by matching patient HPO terms to known disease-gene phenotypes. Standard tool in rare disease diagnostic pipelines. [GitHub](https://github.com/exomiser/Exomiser).
- [LIRICAL](https://github.com/TheJacksonLaboratory/LIRICAL) - Likelihood ratio-based diagnostic tool that provides probabilistic rankings of candidate diagnoses based on phenotypes and genotypes.
- [Seqr](https://github.com/broadinstitute/seqr) - Open-source web platform for rare disease family-based variant analysis, used by the Broad Institute's rare disease genomics programs.
- [MARRVEL](https://marrvel.org/) - IRDiRC-recognized tool integrating human variant databases with 7 model organism resources to prioritize rare variants for functional study.
- [monarchR](https://monarch-initiative.github.io/monarchr/articles/monarchr) - R package providing programmatic access to Monarch Initiative biomedical knowledge graphs for querying genes, diseases, and phenotype relationships. [GitHub](https://github.com/monarch-initiative/monarchr).
- [HPOExplorer](https://github.com/neurogenomics/HPOExplorer) - R package for importing, annotating, filtering, and visualising the Human Phenotype Ontology (HPO) at multiple biological levels including diseases, phenotypes, and genes.
- [MSTExplorer](https://github.com/neurogenomics/MSTExplorer) - R package that identifies, prioritises, and visualises cell-type-specific gene therapy targets across the phenome by analysing associations between diseases, phenotypes, cell types, and genes.
- [Rare Disease Celltyping Portal](https://neurogenomics-ukdri.dsi.ic.ac.uk/) - Interactive portal for exploring cell-type associations across rare diseases, linking phenotypes to cell types using single-cell transcriptomic data.
- [DeepRare](https://github.com/MAGIC-AI4Med/DeepRare) - AI-powered agentic diagnostic system that processes symptoms, genetic data, and medical history to generate ranked rare disease diagnoses with transparent reasoning chains, integrating 40+ specialized tools and outperforming traditional methods on benchmarks.
- [PhEval](https://monarch-initiative.github.io/pheval/) - Framework for benchmarking phenotype-driven gene, variant and disease prioritisation tools on GA4GH Phenopacket corpora, with plug-in runners per tool. Maintained by the Monarch Initiative. [GitHub](https://github.com/monarch-initiative/pheval).
- [Phenomiser](https://github.com/TheJacksonLaboratory/Phenomiser) - Command-line tool that ranks rare diseases by HPO semantic similarity to a patient profile, with batch analysis of phenopackets. Maintained at The Jackson Laboratory.
- [SHEPHERD](https://github.com/mims-harvard/SHEPHERD) - Deep learning model that uses a knowledge graph and simulated patients to prioritise causal genes, find similar patients and characterise novel rare genetic diseases. From the Zitnik Lab, Harvard Medical School.
- [SvAnna](https://monarch-initiative.github.io/SvAnna/stable) - Prioritises coding and regulatory structural variants from short- and long-read VCFs using patient HPO terms. Maintained by the Monarch Initiative. [GitHub](https://github.com/monarch-initiative/SvAnna).
- [ORVAL](https://orval.ibsquare.be/) - Web platform for predicting and exploring candidate disease-causing oligogenic variant combinations from a patient's variant list. Maintained by the Interuniversity Institute of Bioinformatics in Brussels.
- [VarFish](https://www.varfish.de/) - Open-source, self-hosted web platform for filtering, prioritising and interpreting exome and genome variants for rare disease diagnosis. Developed at Charité and the Berlin Institute of Health. [GitHub](https://github.com/varfish-org/varfish-server).
- [Scout](https://clinical-genomics.github.io/scout/) - Open-source web interface for analysing and classifying variants from rare disease VCFs and sharing cases between institutes. Maintained by Clinical Genomics, SciLifeLab Stockholm. [GitHub](https://github.com/Clinical-Genomics/scout).
- [nf-core/raredisease](https://nf-co.re/raredisease/) - Nextflow pipeline that calls, annotates and ranks SNVs, SVs, CNVs, repeat expansions, mobile elements and mitochondrial variants from rare disease WGS/WES. [GitHub](https://github.com/nf-core/raredisease).
- [Talos](https://github.com/populationgenomics/talos) - Nextflow workflow for automated cohort-scale reanalysis of rare disease genomes, flagging variants that become reportable as ClinVar and PanelApp evidence changes. Maintained by the Centre for Population Genomics.
- [DROP](https://gagneurlab-drop.readthedocs.io/) - Pipeline that detects aberrant expression, aberrant splicing and mono-allelic expression in RNA-seq data to support molecular diagnosis of rare disorders. From the Gagneur Lab, Technical University of Munich. [GitHub](https://github.com/gagneurlab/drop).
- [Phen2Gene](https://phen2gene.wglab.org/) - Phenotype-to-gene prioritization using HPO terms to rank candidate genes before sequencing or for variant interpretation.
- [AMELIE](https://amelie.stanford.edu/) - Automatic literature-based variant interpretation that extracts gene-phenotype relationships from publications.
- [Face2Gene](https://www.face2gene.com/) - AI-powered facial analysis for recognizing dysmorphic features associated with genetic syndromes. Aids diagnosis of syndromic rare diseases.
- [Genomics England Rare Disease Genome Analysis Guide](https://pipeline-rd-help.genomicsengland.co.uk/) - Documentation of the Genomics England bioinformatics pipeline for annotating and tiering variants likely to be disease-causing, supporting NHS clinical diagnosis of rare genetic disorders.
- [PatientMatcher](https://clinical-genomics.github.io/patientMatcher/) - Open-source Matchmaker Exchange server for running a local phenotype and genotype patient-matching node. Maintained by Clinical Genomics, SciLifeLab Stockholm. [GitHub](https://github.com/Clinical-Genomics/patientMatcher).
- [PubCaseFinder](https://pubcasefinder.dbcls.jp/) - Ranks rare genetic diseases, genes and published case reports from a patient's HPO terms, with case sharing and gene-panel search. Maintained by DBCLS (Japan), CC BY 4.0. [REST API](https://pubcasefinder.dbcls.jp/api).
- [CaRDinal](https://populationgenomics.org.au/cardinal/) - Australian national cloud platform for collaborative rare disease genomic analysis from the Centre for Population Genomics, with automated variant calling, seqr-based interpretation, monthly reanalysis and cross-cohort gene matching.

## Research Programmes & Communities

Research programmes, networks and communities that produce rare disease data or agree on how it is shared. Organisations are listed here only when they run research infrastructure; their data and tools are listed in the sections above.

- [IRDiRC](https://irdirc.org/) - International Rare Diseases Research Consortium coordinating global research efforts with goals to diagnose all rare diseases and develop 1000 new therapies.
- [Solve-RD](https://solve-rd.eu/) - European project applying multi-omics approaches to solve undiagnosed rare diseases through data sharing across European Reference Networks.
- [Genomics England](https://www.genomicsengland.co.uk/) - UK initiative that has sequenced over 100,000 genomes, with rare disease as a primary focus. Provides access to research datasets.
- [RD-Connect](https://rd-connect.eu/) - European platform linking over 100 rare disease registries and biobanks with genomic data and clinical bioinformatics to enable integrated research.
- [RDMM](https://rare-diseases-catalyst-network.ca/) - Canadian Rare Diseases Models and Mechanisms network connecting clinicians with basic scientists to validate rare disease gene discoveries.
- [GA4GH Rare Disease Community](https://www.ga4gh.org/community/rare-disease/) - Dedicated community bridging clinical and technical RD stakeholders, coordinating global data sharing and standards implementation.
- [OHDSI Rare Disease Working Group](https://www.ohdsi.org/ohdsi2025-workgroups/) - Develops methods for rare disease cohort identification and research using OMOP CDM across global real-world data networks.
- [ELIXIR Rare Disease Community](https://elixir-europe.org/communities/rare-diseases) - European bioinformatics infrastructure community focused on rare disease data resources and standards.
- [ERDERA](https://erdera.org/) - European Rare Diseases Research Alliance (launched 2024) unifying research resources, clinical networks, and expertise across Europe. Successor to EJP RD.
- [European Reference Networks (ERNs)](https://health.ec.europa.eu/rare-diseases-and-european-reference-networks_en) - 24 cross-border networks of specialist centers for rare disease diagnosis and care, mandated by EU Cross-Border Healthcare Directive.
- [RDCRN](https://www.rarediseasesnetwork.org/) - NIH Rare Diseases Clinical Research Network with 21 consortia studying 200+ rare diseases, providing infrastructure for natural history studies and clinical trials.
- [Every Cure](https://everycure.org/) - ARPA-H funded nonprofit using AI to identify drug repurposing opportunities across 4,000 approved drugs for rare disease treatment.
- [SimPaThIC](https://simpathic.eu/) - EU Horizon-funded consortium of 22 partners repurposing existing drugs for rare neurological, neurometabolic, and neuromuscular disorders using patient-derived cell models.
- [Screen4Care](https://www.screen4care.eu/) - IMI2/IHI-funded public-private-patient consortium (2021-2026) shortening the rare disease diagnostic journey through genetic newborn screening of ~25,000 infants and AI-based diagnostic tools. Produced the TREAT gene panel for selecting treatable rare diseases for genomic newborn screening.
- [JARDIN](https://jardin-ern.eu/) - EU Joint Action (2024-2027) integrating the European Reference Networks into national health systems. Its data management work package addresses ERN registry interoperability and is defining a rare disease dataset for EHRs, aligned with the European EHR exchange format (EEHRxF) and ORPHAcodes.
- [RARAS](https://raras.org.br/) - Brazilian Rare Diseases Network linking university hospitals and reference services that collect standardised rare disease patient data. Its [observatory](https://observatorio.raras.org.br/) publishes dashboards on epidemiology, diagnosis, treatment and costs (in Portuguese).
- [N=1 Collaborative](https://n1collaborative.org/) - Organisation for individualised genetic therapies (e.g. ASOs for ultra-rare variants), offering the VARIANT eligibility tool, a Gene Registry of individualised therapy programmes, and protocol and regulatory resources.
- [GeoALS](https://www.geoals.org/) - Nonprofit that applies geographic information systems to ALS, mapping cases, clinics, and environmental exposures to support research, resource planning, and advocacy for the ALS community.

## Directories & Catalogues

Catalogues and directories that list more resources of a given type than this list does. Use them to find, for example, every registry for a disease.

- [ERDERA Virtual Platform](https://vp.erdera.org/) - Federated network of FAIR rare disease resources (registries, biobanks, genomic-phenomic repositories, catalogues, knowledge bases) with a discovery portal that queries all participating resources in real time while data stays with its holder. Originally built under EJP RD; part of the [ERDERA Data Hub](https://erdera.org/data-hub/).
- [EU RD Platform](https://eu-rd-platform.jrc.ec.europa.eu/) - European Commission platform providing directory of registries, common data elements, and cross-registry search tools for RD patient data harmonization. Its [European Directory of Registries (ERDRI.dor)](https://eu-rd-platform.jrc.ec.europa.eu/erdridor/) is the place to look for rare disease registries in Europe.
- [IRDiRC Recognized Resources](https://irdirc.org/resources-2/irdirc-recognized-resources/) - Platforms, tools, standards and guidelines that IRDiRC has labelled as being of fundamental importance to international rare disease research, judged against published criteria on quality, sustainability and use.
- [CDA-AMC Rare Disease Registries Inventory](https://www.cda-amc.ca/drugs-rare-diseases-rare-disease-based-registries) - Searchable inventory from Canada's Drug Agency of rare disease registries in Canada and international registries with Canadian participants, filterable by disease area, data type and coverage. Registry metadata only.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.

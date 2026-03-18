# Idara Health (IDARA) — Deep Research Report

**Prepared:** March 2026
**Scope:** Organization overview, publications, institutional structure, evidence verification
**Primary Sources:** Official websites, PubMed, arXiv, institutional databases, web search

---

## 1. Organization Overview

### 1.1 What Idara Health Is

**IDARA** stands for **Intelligent Digestive and AI Research Alliance**. It is a multidisciplinary clinical research group embedded within the Digestive Diseases Service (*Servicio de Aparato Digestivo*) of the Complexo Hospitalario Universitario de Pontevedra (CHUP), Galicia, Spain. IDARA was established in **2012** and is formally affiliated with the **Instituto de Investigación Sanitaria Galicia Sur (IIS Galicia Sur / IISGS)**.

**Official website:** [https://www.idara.health/](https://www.idara.health/)
**Project portal:** [https://gift.idara.health/](https://gift.idara.health/)

IDARA defines itself as a research group that combines clinical care, clinical trial participation, and biomedical research, with a particular focus on developing **artificial intelligence-based tools** for gastroenterology and hepatology.

### 1.2 Mission and Focus Areas

IDARA's mission centers on three pillars: investigation, innovation, and commitment to public health service. Its core focus areas are:

- **AI-assisted clinical decision support** for primary care–specialist coordination in gastroenterology and endocrinology
- **AI-enabled disease elimination** — specifically hepatitis C virus (HCV) patient retrieval and linkage to care
- **Domain-specific large language models (LLMs)** for hepatology and liver imaging
- **Synthetic patient data generation** for research on rare or uncommon clinical conditions
- **AI-assisted endoscopy** — detection and classification of colorectal polyps during colonoscopies
- **Science outreach** — including "Gastrosapiens," a program introducing primary school students to scientific research

### 1.3 Key People

| Name | Role | Affiliation |
|------|------|-------------|
| **Dr. Juan Turnes Vázquez** | Director of IDARA; Head of Gastroenterology & Hepatology Service, Hospital Montecelo | CHUP / IIS Galicia Sur |
| **Pablo Parada Vázquez** | Researcher; first author on HCV retrieval study | CHUP / IIS Galicia Sur |
| **Belén Castiñeira Domínguez** | Researcher | CHUP / IIS Galicia Sur |
| **José Manuel Mera Calviño** | Researcher | CHUP / IIS Galicia Sur |
| **Raquel Souto-Rodríguez** | Researcher | CHUP / IIS Galicia Sur |
| **Yolanda Falagán Cachafeiro** | Researcher | CHUP / IIS Galicia Sur |
| **Indhira Pérez-Medrano** | Researcher | CHUP / IIS Galicia Sur |
| **Santiago Pérez-Cachafeiro** | Collaborator (preventive medicine) | University of Santiago de Compostela |

**Note:** Dr. Turnes also holds an associate professorship at the **Universidad de Santiago de Compostela** and previously worked at Hospital Clínic de Barcelona (2002–2006). He is actively involved in national hepatology networks (CIBERehd, AEEH — Spanish Association for the Study of the Liver). The IDARA group comprises approximately **11+ professionals** combining clinical, research, and technological roles.

### 1.4 Partners and Affiliations

| Partner | Nature of Relationship | Evidence Level |
|---------|----------------------|----------------|
| **IIS Galicia Sur (IISGS)** | Formal research institute affiliation | Confirmed (PubMed affiliations, institutional records) |
| **SERGAS (Servizo Galego de Saúde)** | Parent health service; owns CHUP | Confirmed |
| **Universidad de Santiago de Compostela** | Academic affiliation (Turnes associate professorship) | Confirmed |
| **Gilead Sciences** | FOCUS programme funding for HCV retrieval | Confirmed (publication co-authorship, PMID 38950646) |
| **AbbVie** | Research funding for COMTA protocol | Confirmed (workspace AICOMTA documentation) |
| **Novo Nordisk** | Research funding for COMTA protocol | Confirmed (workspace AICOMTA documentation) |
| **AstraZeneca** | AICOMTA validation funding | Confirmed (workspace AICOMTA documentation) |
| **BCLC Group, Hospital Clínic Barcelona** | LiverAI / LI-RADS collaboration | Confirmed (joint publication, PMID 39576290) |
| **Spanish Association for the Study of the Liver (AEEH)** | LiverAI platform support (Javier Pazó, IT) | Confirmed (publication co-authorship) |
| **Ministry for Digital Transformation (Spain)** | GIFT/Aidatamed selected for European data space | Confirmed (web sources, Next Generation EU) |

### 1.5 Major Projects

**AICOMTA (Artificial Intelligence Sharing Talent / AI COMunication TAlent)**
- RAG-based clinical decision support system built on **Google Gemini 2.0 Flash**
- Designed for primary care physicians to query specialist-validated gastroenterology and endocrinology knowledge
- 328 clinical conversations validated; expert panel quality score 4.2/5; 87.5% physician adoption intent
- Winner of **E-nnova Health 2024** award for best AI project in health
- Knowledge base uses Spanish clinical guidelines (AEG, AEEH), local SERGAS protocols
- Technical stack: multilingual-e5-large embeddings, Qdrant vector database, HNSW algorithm

**GIFT (Gastroenterology Interface with Fair Treatment)**
- AI conversational assistant for querying updated clinical information in gastroenterology
- Selected by Spain's Ministry for Digital Transformation for European data space initiative
- Funded through Next Generation EU community funds

**Aidatamed**
- Generative AI system for creating **synthetic patient databases** that mimic real data without identifying individuals
- Focuses on rare or uncommon digestive pathologies where real-world datasets are limited
- Winner of **RIES 25 Forum Award** (2025) for innovative use of AI in health
- Also funded through Next Generation EU

**LiverAI**
- Domain-specific LLM (GPT-4-based) for LI-RADS v2018 categorization of hepatic observations from free-text MRI reports
- Developed in collaboration with BCLC Group (Hospital Clínic Barcelona)
- Achieved 0.96 specificity for LR-5 identification when used as triage tool
- Reduced radiologist workload by up to 60% in data curation workflow

**HCV Patient Retrieval**
- AI-powered retrospective screening of electronic health records (HEXIN/IANUS databases) to identify HCV patients lost to follow-up
- Retrieved 64.6% (64/99) of identified lost patients; 87.1% achieved sustained virological response
- Aligned with WHO 2030 HCV elimination targets

**Colorectal Polyp Detection AI**
- Real-time AI assistance during colonoscopies for detection and classification of colorectal polyps
- Status: in development (limited public documentation)

---

## 2. Publications and Scientific Output

### 2.1 Peer-Reviewed Scientific Publications (AI-Related, with Turnes at CHUP/IDARA)

Based on articles retrieved from PubMed and arXiv:

#### Publication 1
- **Title:** Artificial intelligence-assisted identification and retrieval of chronic hepatitis C patients lost to follow-up in the health area of Pontevedra and O Salnés (Spain)
- **Authors:** Parada Vázquez P, Pérez-Cachafeiro S, Castiñeira Domínguez B, González-Pérez JM, Mera Calviño JM, Souto-Rodríguez R, Falagán Cachafeiro Y, Pérez-Medrano I, Vázquez-Temprano N, Trigo M, Carrodeguas A, González-Sánchez JL, Durán-Parrondo C, **Turnes J** (corresponding author)
- **Year:** 2024
- **Journal:** *Gastroenterología y Hepatología*, 48(1):502226
- **DOI:** [10.1016/j.gastrohep.2024.502226](https://doi.org/10.1016/j.gastrohep.2024.502226)
- **Summary:** Used AI-assisted screening (HEXIN application) of the Galician Health Service electronic health database to identify 99 chronic HCV patients lost to follow-up. Retrieved 64 (64.6%); 62 initiated DAA treatment; 54 achieved SVR (87.1%). Mean time since diagnosis was >10 years. Main reasons for loss to follow-up: fear of treatment adverse effects (30%) and mobility impediments (21%).
- **Relevance:** Core IDARA publication demonstrating AI-enabled HCV elimination strategy — a flagship project.

#### Publication 2
- **Title:** Utilizing a domain-specific large language model for LI-RADS v2018 categorization of free-text MRI reports: a feasibility study
- **Authors:** Matute-González M, Darnell A, Comas-Cufí M, Pazó J, Soler A, Saborido B, Mauro E, **Turnes J**, Forner A, Reig M, Rimola J
- **Year:** 2024
- **Journal:** *Insights into Imaging*, 15:280
- **DOI:** [10.1186/s13244-024-01850-1](https://doi.org/10.1186/s13244-024-01850-1)
- **Summary:** Developed LiverAI, a GPT-4-based domain-specific LLM for automated LI-RADS v2018 categorization from free-text MRI reports. Tested on 291 liver observations. Moderate standalone agreement (κ=0.54); but when used as triage tool, achieved κ=0.86–0.87 with radiologists and sensitivity 0.76/specificity 0.96 for LR-5. Reduced workload by up to 60%.
- **Relevance:** Demonstrates IDARA's collaborative work on domain-specific LLMs for liver health — directly tied to LiverAI project.

#### Publication 3
- **Title:** Advancing radiology reporting with large language models: Is GPT-4 the LI-RADS game changer or just a wild card?
- **Authors:** Díaz-González Á, Forner A, **Turnes J**
- **Year:** 2024
- **Journal:** *Liver International*, 44(7):1575-1577
- **DOI:** [10.1111/liv.15952](https://doi.org/10.1111/liv.15952)
- **Summary:** Editorial commentary on the application of GPT-4 and LLMs to liver radiology reporting, with focus on LI-RADS categorization challenges and opportunities.
- **Relevance:** Positions IDARA leadership (Turnes) as thought leaders on AI in hepatology radiology.

#### Publication 4
- **Title:** LiverAI: New tool in the landscape for liver health
- **Authors:** Marti-Aguado D, Pazó J, Diaz-Gonzalez A, de Las Heras Páez de la Cadena B, Conthe A, Gallego Duran R, Rodríguez-Gandía MA, **Turnes J**, Romero-Gomez M
- **Year:** 2024
- **Journal:** *Gastroenterología y Hepatología*, 47(6):646-648
- **DOI:** [10.1016/j.gastrohep.2024.04.001](https://doi.org/10.1016/j.gastrohep.2024.04.001)
- **Summary:** Editorial introducing the LiverAI platform and its potential applications in liver health, including automated LI-RADS classification from unstructured clinical text.
- **Relevance:** Companion editorial to the LiverAI feasibility study; shows IDARA's role within the Spanish hepatology AI ecosystem.

#### Publication 5 (Pre-print)
- **Title:** Artificial Intelligence in Spanish Gastroenterology: high expectations, limited integration. A national survey
- **Authors:** Includes **Turnes J** and multiple co-authors (SEPD network)
- **Year:** 2025
- **Venue:** arXiv pre-print (2601.17011)
- **Link:** [https://arxiv.org/abs/2601.17011](https://arxiv.org/abs/2601.17011)
- **Summary:** Cross-sectional observational study via structured online survey distributed by the Spanish Society of Digestive Pathology (SEPD). Among 283 respondents, 87.5% acknowledged AI as transformative, but only 60.2% reported using it — mostly outside institutional frameworks. Independent predictors of frequent use included prior training, university hospital employment, and younger age. Main barriers: lack of training (61%), absence of institutional strategies (46%), ethical concerns (50%).
- **Relevance:** National-level survey establishing the adoption landscape for AI tools like AICOMTA/GIFT within Spanish gastroenterology.

#### Publication 6 (Pre-print)
- **Title:** The Integration of Artificial Intelligence in Undergraduate Medical Education in Spain: Descriptive Analysis and International Perspectives
- **Authors:** Enériz Janeiro A, Pitombeira Pereira K, Mayol J, Crespo J, Carballo F, Cabello JB, Ramos-Casals M, **Turnes J** and others
- **Year:** 2025
- **Venue:** arXiv pre-print (2510.17938)
- **Link:** [https://arxiv.org/abs/2510.17938](https://arxiv.org/abs/2510.17938)
- **Summary:** First systematic evaluation of AI integration in Spanish medical curricula. Of 52 universities analyzed, only 10 (19.2%) offer specific AI courses; 36 (69.2%) include no AI-related content. Most courses are elective (3–6 ECTS, ~1.17% of total degree).
- **Relevance:** Demonstrates IDARA team's engagement with AI education policy, complementing their clinical tool development.

### 2.2 Selected Clinical Hepatology Publications (Recent, 2023–2025)

These publications demonstrate Dr. Turnes's and IDARA's broader clinical research activity in hepatology, providing context for the AI work. Based on articles retrieved from PubMed:

| Title | Year | Journal | DOI | Turnes Role |
|-------|------|---------|-----|-------------|
| Safety and efficacy of elafibranor in PSC: ELMWOOD phase II RCT | 2025 | *J Hepatol* | [10.1016/j.jhep.2025.04.025](https://doi.org/10.1016/j.jhep.2025.04.025) | Co-investigator |
| Noninvasive criteria for drug therapy in MASLD | 2025 | *Clin Gastroenterol Hepatol* | [10.1016/j.cgh.2025.08.023](https://doi.org/10.1016/j.cgh.2025.08.023) | Co-author |
| Impact of multiple DDIs in HCV patients treated with DAAs in Spain | 2024 | *Rev Esp Sanid Penit* | [10.18176/resp.00095](https://doi.org/10.18176/resp.00095) | First author |
| Real-life effectiveness of SOF/VEL/VOX in HCV retreatment | 2024 | *Aliment Pharmacol Ther* | [10.1111/apt.18020](https://doi.org/10.1111/apt.18020) | Co-author |
| Biochemical pattern defines MASLD phenotypes | 2024 | *J Gastroenterol* | [10.1007/s00535-024-02098-8](https://doi.org/10.1007/s00535-024-02098-8) | Co-author |
| Advanced fibrosis associated with NASH in Spain: Delphi study | 2023 | *Gastroenterol Hepatol* | [10.1016/j.gastrohep.2023.06.005](https://doi.org/10.1016/j.gastrohep.2023.06.005) | Co-author |
| Thrombocytopenia management in liver cirrhosis: consensus | 2023 | *Gastroenterol Hepatol* | [10.1016/j.gastrohep.2023.03.008](https://doi.org/10.1016/j.gastrohep.2023.03.008) | Co-author |
| TDF reduces COVID-19 severity in chronic hepatitis B | 2023 | *Dig Dis Sci* | [10.1007/s10620-022-07817-w](https://doi.org/10.1007/s10620-022-07817-w) | Co-author |

**Note:** Dr. Turnes has **56+ PubMed-indexed publications** with "Pontevedra" affiliation (2023–2026 alone: 15 publications), and **35+ publications** specifically on hepatitis C. His total PubMed-indexed output is substantially larger when including earlier work at Hospital Clínic Barcelona and other collaborations.

### 2.3 Other Scientific Output (Non–Peer-Reviewed)

| Type | Item | Details |
|------|------|---------|
| **Award application** | AICOMTA — Zendal Prize application | Project description, team biosketches, Latin American expansion plan (workspace document) |
| **Award application** | AICOMTA — E-nnova Health 2024 | Best AI project in health (confirmed via web sources) |
| **Award** | Aidatamed — RIES 25 Forum Award (2025) | Innovation in synthetic data generation for healthcare |
| **Ethics protocol** | COMTA Protocol (CEIC-approved) | Full clinical protocol for AICOMTA evaluation (workspace document, 2023) |
| **Draft manuscript** | AICOMTA validation study (Borrador paper v1.0) | Prospective observational mixed-methods study; 328 conversations; near publication-ready (workspace document) |
| **Press coverage** | Diario de Pontevedra (Aug 2025) | Coverage of IDARA's AI projects: "Médicos virtuales y pacientes sintéticos" |
| **Outreach** | Gastrosapiens program | Science literacy initiative for primary school students |
| **Institutional presentations** | Centro de Supercomputación de Galicia | Presentations on AI in gastroenterology (confirmed via web) |

### 2.4 Unpublished but Documented Work (from Workspace Analysis)

The AICOMTA-documentation workspace folder contains a near-final manuscript (**Borrador paper_v1.0**) describing a 6-month prospective observational study of AICOMTA (Nov 2024–Apr 2025) with 16 physicians, 328 clinical conversations, expert panel evaluation (13 blinded evaluators), and CHART compliance. This manuscript has not yet appeared in PubMed or pre-print servers as of this report date, suggesting it is in final preparation or peer review.

---

## 3. Institutional and Administrative Structure

### 3.1 Governance Hierarchy

```
XUNTA DE GALICIA (Regional Government of Galicia)
    │
    ▼
CONSELLERÍA DE SANIDADE (Health Ministry)
    │
    ▼
SERGAS — Servizo Galego de Saúde (Galician Health Service)
    │   • Autonomous administrative body
    │   • 7 territorial health areas
    │   • Governed by Board of Directors (chaired by Health Minister)
    │
    ▼
ÁREA SANITARIA DE PONTEVEDRA E O SALNÉS
    │   • Manager (Gerente): José Flores
    │   • Assistant Director: Yolanda Sanduende
    │   • Manages: Hospital Montecelo, Hospital Provincial,
    │     Hospital do Salnés, Centro de Especialidades Mollabao
    │
    ▼
COMPLEXO HOSPITALARIO UNIVERSITARIO DE PONTEVEDRA (CHUP)
    │   • Public hospital complex (Decree 229/1998)
    │   • University hospital status since 2012
    │   • Teaching hospital for Universidad de Santiago de Compostela
    │   • >14,000 endoscopic procedures/year
    │   • >20,000 outpatient consultations/year
    │
    ▼
SERVICIO DE APARATO DIGESTIVO (Digestive Diseases Service)
    │   • Head: Dr. Juan Turnes Vázquez
    │   • Hospital Montecelo (4th floor hospitalization,
    │     ground floor consultations & endoscopy)
    │
    ▼
IDARA — Intelligent Digestive and AI Research Alliance
        • Established: 2012
        • ~11+ professionals
        • ~30 active clinical trials
        • Affiliated with IIS Galicia Sur
```

### 3.2 Research Infrastructure: IIS Galicia Sur

IDARA's formal research affiliation is through the **Instituto de Investigación Sanitaria Galicia Sur (IISGS)**, a multidisciplinary research institute:

| Attribute | Detail |
|-----------|--------|
| **Created** | 2008 |
| **Accreditation** | Instituto de Salud Carlos III (ISCIII) |
| **Scientific Director** | Eva Poveda López |
| **Vice President & Foundation Director** | Beatriz Gil de Araujo de Simón |
| **Managing Entity** | Fundación Biomédica Galicia Sur |
| **Academic Partner** | Universidad de Vigo |
| **Health Areas** | Vigo, Ourense, and Pontevedra |
| **Headquarters** | Hospital Álvaro Cunqueiro (Vigo) |
| **Research Areas** | 8 (6 thematic + 2 transversal) |

**IDARA's likely placement within IIS Galicia Sur:** Area 7 (Transversal: Clinical Decision Support Systems) or Area 6 (Efficiency and Quality in Health Services), based on its AI/clinical decision support focus. *Note: The exact area assignment is not publicly confirmed.*

**Governance bodies of IIS Galicia Sur:**
- Consejo Rector (Governing Board)
- Dirección Científica (Scientific Direction)
- External Scientific Committee
- Internal thematic commissions (Scientific, Quality, Training & Communication)

### 3.3 How IDARA Fits Within the Structure

IDARA operates as a **clinical research group** within the Digestive Diseases Service of CHUP. It is not a standalone legal entity. Its institutional identity flows through two parallel channels:

1. **Clinical channel:** CHUP → Área Sanitaria Pontevedra → SERGAS → Consellería de Sanidade → Xunta de Galicia. This is the service delivery and patient care pathway.

2. **Research channel:** IIS Galicia Sur → Fundación Biomédica Galicia Sur → co-governed by SERGAS health areas and Universidad de Vigo. This is the formal research affiliation that appears in publication bylines and enables competitive grant applications.

Dr. Turnes holds dual authority as both Head of the clinical Digestive Service and Director of the IDARA research group, allowing tight integration between clinical activity and research innovation.

---

## 4. Evidence and Verification

### 4.1 Confirmed Facts

| Claim | Source(s) | Confidence |
|-------|----------|------------|
| IDARA stands for "Intelligent Digestive and AI Research Alliance" | idara.health, gift.idara.health | **Confirmed** |
| Established 2012 at CHUP Pontevedra | Official website, web sources | **Confirmed** |
| Dr. Juan Turnes Vázquez is director | Official website, PubMed affiliations, institutional records | **Confirmed** |
| Affiliated with IIS Galicia Sur | PubMed author affiliations across multiple publications | **Confirmed** |
| CHUP is part of Área Sanitaria Pontevedra e O Salnés under SERGAS | SERGAS official portal, institutional records | **Confirmed** |
| IIS Galicia Sur scientific director is Eva Poveda López | IISGS official website | **Confirmed** |
| IIS Galicia Sur accredited by ISCIII | IISGS official website | **Confirmed** |
| Fundación Biomédica Galicia Sur is the managing entity of IISGS | IISGS official website, Fundación website | **Confirmed** |
| GIFT and Aidatamed funded by Next Generation EU | Web sources, GIFT project page | **Confirmed** |
| AICOMTA won E-nnova Health 2024 award | Web sources | **Confirmed** |
| Aidatamed won RIES 25 Forum Award (2025) | Twitter/X (@pontegastro), web sources | **Confirmed** |
| Gilead Sciences co-authored HCV retrieval study | PubMed (PMID 38950646) | **Confirmed** |
| AbbVie, Novo Nordisk funded COMTA protocol | Workspace documents (Protocolo CEIC COMTA.pdf) | **Confirmed** (internal documents) |
| LiverAI developed with BCLC Group, Hospital Clínic Barcelona | PubMed (PMID 39576290) | **Confirmed** |
| Dr. Turnes has 56+ recent publications indexed in PubMed | PubMed search results | **Confirmed** |

### 4.2 Reasonable Inferences

| Claim | Basis | Confidence |
|-------|-------|------------|
| IDARA likely falls under IIS Galicia Sur's Area 7 (Clinical Decision Support Systems) or Area 6 | AI/decision support focus matches these areas; not explicitly stated | **Inferred** |
| ~11 professionals comprise the IDARA team | Referenced in workspace documents; exact current headcount not independently verified | **Inferred** |
| ~30 active clinical trials at CHUP Digestive Service | Referenced in web sources; not independently verified against clinical trial registries | **Inferred** |
| AICOMTA manuscript (Borrador paper v1.0) is in peer review | Near-final draft quality; not yet visible in PubMed/pre-print servers | **Inferred** |
| Latin American expansion of AICOMTA is planned | Workspace Zendal Prize application references Colombia and partnerships | **Inferred** (internal documents) |

### 4.3 Unknown / Not Publicly Available

| Item | Status |
|------|--------|
| IDARA formal legal status (research group vs. department vs. unit) | Not publicly specified |
| IDARA annual research budget | Not publicly available |
| Specific reporting lines between Turnes and CHUP/Área Sanitaria management | Not documented in public sources |
| Full team roster with individual roles | Partially available from publications; no complete public directory |
| Detailed AICOMTA technical roadmap beyond current validation | Not public |
| Latin American partner institutions and timelines | Referenced in internal documents only |
| Whether IDARA has applied for or received EVAH (Wellcome/Gates/Novo Nordisk) funding | Not confirmed; workspace analysis suggests alignment but no submitted application was found |

### 4.4 Sources Used

| Source Category | Specific Sources |
|----------------|-----------------|
| **Official websites** | idara.health, gift.idara.health, iisgaliciasur.es, pontevedrasalnes.sergas.gal, sergas.gal, fundacionbiomedica.es |
| **PubMed** | 15+ publications retrieved and verified with full metadata |
| **arXiv** | 2 pre-prints identified (2601.17011, 2510.17938) |
| **Publisher sites** | Elsevier (Gastroenterol Hepatol), Wiley (Liver Int, Aliment Pharmacol Ther), Springer (Insights Imaging, J Gastroenterol, Dig Dis Sci) |
| **Institutional sources** | SERGAS portal, IIS Galicia Sur structure pages, Fundación Biomédica Galicia Sur |
| **Press / media** | Diario de Pontevedra, PontevedraViva, Twitter/X (@pontegastro) |
| **Workspace documents** | AICOMTA-documentation folder analysis (cross-referenced) |

---

## 5. Summary Assessment

IDARA is a **genuine, well-documented, and scientifically productive** clinical research group operating within Spain's public health system. Its AI work is distinctive for three reasons: (1) it operates under a **clinical governance model** where specialist panels validate all AI knowledge base content before deployment; (2) it has produced **measurable clinical impact** through HCV patient retrieval with published outcomes; and (3) it spans the full AI lifecycle from tool development (AICOMTA, GIFT, LiverAI, Aidatamed) through national-level adoption research (SEPD survey) and educational policy analysis.

The group's publication track record, institutional affiliation through IIS Galicia Sur, and recognition via competitive awards (E-nnova Health 2024, RIES 25) all corroborate its credibility. Its primary limitation is geographic concentration in a single health area (Pontevedra) with relatively small sample sizes in AI validation studies — a gap the group appears to be actively addressing through multi-center collaborations and planned international expansion.

---

*Report compiled March 2026 using PubMed, arXiv, official institutional websites, and workspace cross-referencing. All publications cited with DOIs. No affiliations or publications were invented.*

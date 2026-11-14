# Agent 07: Hardware acquisition cost in Colombia, Ecuador and Venezuela vs. the US/EU used market

**Question tested:** Does the second-hand market in Colombia, Ecuador or Venezuela sell old servers and GPUs below global used-market prices?
**Research date:** 2026-11-14. All "today" prices are as observed on that date unless stated otherwise.
**FX used:** COP/USD **3,316.70** (Colombian TRM in force 2026-11-14, datos.gov.co). VES/USD **911.62 official (BCV)** and **1,069.20 parallel** (ve.dolarapi.com, 2026-11-13/14). Ecuador uses the USD, so no conversion is needed. EUR/USD **1.104** (open.er-api.com, 2026-11-14).
**Labels:** **CONFIRMED** means a primary or live source with a date. **ESTIMATE** means search-snippet data with no date, or a derived figure. **INFERENCE** means my reasoning.

---

## 1) Executive summary

- **The hypothesis is not supported.** I found no item, in any of the three countries, that is reliably cheaper locally than on the US used market. Where like-for-like data exists, LATAM asks are **at parity or higher**:
  - **DDR4 ECC RDIMM:** 1.0–1.4x the US price (CONFIRMED, live Bogotá shop vs. US eBay medians).
  - **Complete used servers:** about 1.1–3x (ESTIMATE).
  - **Old 11G/12G servers (R610/R710/R720):** about 3–10x. These sell for USD 400–1,650 in Ecuador and Venezuela and are close to scrap in the US.
- **Datacenter GPUs are almost absent locally.** I found no P40, T4, A100 or RTX A-series listings in CO, EC or VE. The only Colombian V100 16GB listings ask COP 44.9–55.2M (**USD 13.5k–16.6k**), against **USD 350–440** in the US. These are non-market asks, not a supply source.
- **The only "discount" is an artefact of stale listings.** MercadoLibre listings for RTX 3090/4090 look 10–35% cheaper than today's US prices, for example 3090s at COP 3.5–4.5M (USD 1,055–1,357) vs. USD 1,540–1,660 in the US. But these listings are undated, and one Venezuelan 3090 listing dates to about 2024 by its bolívar equivalent (implied 36.1 Bs/USD). Against the US prices of their era (USD 700–900), they were **1.1–1.6x the US**. A live check is still needed. If a real gap exists, it is an **export** play (sell to the US/EU), not a rental play.
- **US used prices more than doubled in 2026 (CONFIRMED, trackers dated 2026-11-13/14):**

  | Card | US used price, Nov 2026 |
  |---|---|
  | RTX 3090 | USD 1,500 lowest offer; USD 1,540–1,660 fair-ask range; up from about USD 700–850 in early 2026 |
  | RTX 4090 | USD 2,999 lowest / USD 3,814 median ask |
  | RTX 5090 | USD 5,500 used / USD 6,250 new; MSRP was USD 1,999 |
  | A100 80GB | USD 10,999 |
  | V100 32GB | USD 1,039 |
  | P40 | USD 384 |
  | DDR4 32GB RDIMM | about USD 200 |
  | DDR4 64GB RDIMM | about USD 500 |

- **Landed cost of shipping US used gear in:**
  - **Colombia:** about **1.20x** for GPUs and RAM, and **1.40x** for a 2U server, with 0% tariff and 19% VAT. A VAT-registered exporter of services that can recover import VAT pays about 1.01–1.18x.
  - **Ecuador:** **1.18–1.57x**, or 1.23–1.57x including the 5% currency-exit tax (ISD).
  - **Venezuela:** **1.07–1.39x** if "all-in" casillero rates hold, or about 1.37–1.56x if duties and VAT apply.
- **Regulatory friction is material:**
  - **Colombia:** used goods require a **licencia previa** (Decreto 925/2013 art. 14). The courier channel caps each shipment at USD 2,000 and 50 kg.
  - **Ecuador:** the 4x4 courier regime is capped at USD 400 / 4 kg per package, costs a flat USD 20, allows USD 1,600 per year, and is for individuals only.
  - **Venezuela:** a Miami–Venezuela carrier lists **crypto-mining equipment as prohibited**, which is a seizure risk for multi-GPU rigs.
- **The memory shock changes the economics.** Conventional DRAM contract prices rose about **+90–95% QoQ in Q1 2026** (TrendForce, via DatacenterDisk). An old server's RAM is now often worth more than the whole server's asking price: the parts-out value of a 256GB R730 is about USD 1,500–1,700, against whole-unit asks of USD 900–1,600. Selling into the 2026 US/EU parts market competes strongly with renting.
- **The FX trend works against the idea.** The COP strengthened from 4,409/USD (Jan 2025) to 3,317 (Nov 2026), so COP-priced hardware became about 33% dearer in USD.
- **Volume is thin.** I found dozens of relevant server listings per country, not lots, and no evidence of datacenter-decommissioning GPU lots. Government and bank asset auctions (CISA in Colombia, public-asset "bajas" in Ecuador) exist but could not be verified this session.

---

## 2) Detailed findings

### 2.1 Method and data-access limits (read first)

| Source | Result |
|---|---|
| MercadoLibre listing pages (CO/VE/EC) | Redirected to an anti-bot "account-verification" wall (HTTP 302→verification; WebFetch 403). |
| MercadoLibre public API `api.mercadolibre.com/sites/{MCO,MLV,MEC}/search` | **HTTP 403 "forbidden"** without authentication (2026-11-14). |
| eBay search and sold listings | HTTP 403 (bot block). |
| Reddit r/homelabsales JSON | HTTP 403. |
| What I used instead | Search-engine snippets of ML listings (**undated, so ESTIMATE**). A live Bogotá server-parts shop (pcyservidores.co, **CONFIRMED live**). Live US/EU vendors (Core 4 Solutions, PC Server & Parts, newserverlife, serverando.de). eBay-derived price trackers (GPUDojo, ResalePrices, VRAMGlass, CresvaMent), all dated 2026-11-13/14. |
| Web-search budget | The search budget, shared across agents, ran out partway through. Some sub-items were not researched (see §4). |

**Important caveat on tracker data:** GPUDojo's "lowest offer" and "median ask", VRAMGlass's and CresvaMent's medians, and ResalePrices' "fair asking range" are **eBay asking prices**, not completed sales. Real sold prices are typically 5–15% lower (INFERENCE).

### 2.2 Exchange rates and FX history (CONFIRMED)

| Date | COP per USD (TRM) | Note |
|---|---|---|
| 2023-06-01 | 4,434.09 | |
| 2024-06-04 | 3,860.92 | |
| 2025-01-02 | 4,409.15 | |
| 2025-06-03 | 4,148.72 | |
| 2026-01-02 | 3,757.08 | |
| 2026-06-02 | 3,560.24 | |
| 2026-09-01 | 3,213.97 | |
| **2026-11-14** | **3,316.70** | Rate used in this report |
| VES official (BCV), 2026-11-13 | 911.62 Bs/USD | |
| VES parallel, 2026-11-14 | 1,069.20 Bs/USD | Gap about 17% |

Implication: an undated COP listing converted at today's TRM shows a USD price up to **25–33% higher** than the USD price at the time it was posted, if it was posted in 2024–25. In the tables below, COP prices are converted at today's TRM, with era-TRM conversions noted where relevant.

### 2.3 Local listings

#### Colombia

| Item | Local price (COP) | USD at 3,316.70 | Source / status |
|---|---|---|---|
| Dell R730, used (typical configs) | 4.8M – 5.9M | 1,447 – 1,779 | ML CO search snippets, undated (ESTIMATE) |
| Dell R730, 24 cores / 128GB / 60TB | 12.5M | 3,769 | ML CO snippet (ESTIMATE) |
| Dell R730xd (small config) | 5.2M | 1,568 | ML CO snippet (ESTIMATE) |
| Dell R730xd, 256GB / 72TB HDD | 30.9M | 9,321 | ML CO snippet (ESTIMATE); storage-heavy |
| Dell R730 motherboard only | 1.1M | 332 | ML CO snippet (ESTIMATE) |
| Dell R740, used | 10.0M | 3,015 | ML CO snippet (ESTIMATE) |
| RTX 3090, used: range | 3.2M – 9.0M | 965 – 2,714 | ML CO snippets (ESTIMATE); at least one page about 4 years old |
| RTX 3090, used: examples | Gigabyte Vision OC 3.8M; Founders Edition 4.5M; EVGA FTW3 Ultra 7.3M | 1,146; 1,357; 2,201 | ML CO snippets (ESTIMATE) |
| RTX 4090, used (MSI Gaming Trio) | 10.0M | 3,015 | ML CO snippet (ESTIMATE) |
| RTX 4090, new (likely old listings) | 8.8M – 9.5M | 2,653 – 2,864 | ML CO snippet (ESTIMATE) |
| Tesla V100 16GB | 44.9M – 55.2M | 13,537 – 16,648 | ML CO snippets (ESTIMATE); non-market asks |
| DDR4 32GB ECC RDIMM (ML) | 187k – 960k | 56 – 289 | ML CO snippets (ESTIMATE); mixed new and used |
| **DDR4 32GB RDIMM PC4-2666V** | **670,000** | **202** | **pcyservidores.co, Bogotá, live 2026-11-14 (CONFIRMED)** |
| **DDR4 32GB RDIMM PC4-2133P** | **590,000** | **178** | pcyservidores.co (CONFIRMED) |
| **DDR4 16GB RDIMM PC4-2400T (HPE)** | **340,000** | **103** | pcyservidores.co (CONFIRMED) |
| **DDR4 16GB RDIMM PC4-2133** | **320,000** | **96** | pcyservidores.co (CONFIRMED) |
| **Intel Xeon E5-2680 v4** | **260,000** | **78** | pcyservidores.co (CONFIRMED) |

Not found in Colombia: P40, T4, A100, RTX A4000/A5000/A6000, HPE DL380 Gen9/Gen10 with prices, Supermicro 4028GR/4029GP, and any 4- or 8-GPU server. Snippets showed that Bogotá concentrates most of the V100 sellers, but the price levels make clear these are not a liquid market.

#### Ecuador (USD; MercadoLibre Ecuador; OLX Ecuador did not resolve)

| Item | Price (USD) | Source / status |
|---|---|---|
| Used rack servers: R330 / R610 / R710 / R720 | 400 – 1,650 | ML EC snippets, undated (ESTIMATE) |
| Dell R710, used | 999 | ML EC snippet (ESTIMATE) |
| Dell R610, used | 1,300 | ML EC snippet (ESTIMATE) |
| New towers: T40 / T150 | 1,100 – 1,519 / 1,550 – 2,299 | ML EC snippets (ESTIMATE); new, entry-level |
| RTX 3090, used | from ~700 | ML EC snippets (ESTIMATE) |
| RTX 3090 ASUS ROG Strix, "seminueva" | 1,900 | ML EC snippet (ESTIMATE) |
| RTX 3090 Gigabyte Gaming OC, new | 3,897 | ML EC snippet (ESTIMATE) |
| RTX 4090 ASUS ROG Strix | 2,889 | ML EC snippet, listing about 1,393 days old, i.e. about 2023 (ESTIMATE) |
| Tesla / datacenter GPUs | none found | — |

#### Venezuela (USD-denominated listings on MercadoLibre Venezuela)

| Item | Price (USD) | Source / status |
|---|---|---|
| Dell R710 / R720 / R730 (light configs) | 900 – 1,800 | ML VE snippets (ESTIMATE) |
| Dell R720 | 1,336 | ML VE snippet (ESTIMATE) |
| Dell R730, 24 cores / 128GB / 4.8TB SAS | 3,500 | ML VE snippet (ESTIMATE) |
| Dell R730, 256GB | 7,800 | ML VE snippet (ESTIMATE) |
| Dell T110 / T310 (16GB) | 489 / 699 | ML VE snippet (ESTIMATE) |
| Dell T150 (new, 36-month warranty, plus VAT if a fiscal invoice is requested) | 1,720 | ML VE snippet (ESTIMATE) |
| RTX 3090, used | 650 – 1,400; typical 700 – 1,200 | ML VE snippets (ESTIMATE) |
| RTX 3090 MSI Ventus, used | 1,099 (= Bs 39,668.95) | ML VE snippet. The implied **36.1 Bs/USD** dates the listing to about **2024**, against 911.6 today. |
| Tesla M40 12GB / C2075 6GB, used | 225 / 45 | ML VE snippets (ESTIMATE) |
| V100 water blocks (no V100 cards found) | 469 – 676 | ML VE snippets (ESTIMATE) |
| V100 / P40 / A100 / A-series cards | none found | — |

### 2.4 US/EU benchmarks (2026-11-13/14)

#### GPUs (eBay US asking prices, via trackers; CONFIRMED as dated asks)

| GPU | Lowest used offer | Median ask (middle 50%) [sample] | Recent trend | Source |
|---|---|---|---|---|
| RTX 3060 12GB | $349 | $445 ($400–450) [78] | $279–340 in Sep–Oct 2026 | GPUDojo |
| RTX 3090 24GB | $1,500 | $2,030 ($1,899–2,200) [53] | Fair ask $1,540–1,660 (ResalePrices, n=314: 30-day +6.9%, 90-day +28.8%). Lowest offers: $1,000 (May 2026), $1,389 (Sep), $1,500 (Nov). | GPUDojo, ResalePrices |
| RTX 4090 24GB | $2,999 | $3,814 ($3,400–4,453) [35] | $2,799 (Sep 18) → $3,300 (Nov 6) | GPUDojo |
| RTX 5090 32GB | $5,500 (new from $6,250) | $7,249 ($6,800–8,225) [83] | Asks fell about $1,000 between mid-Oct and Nov 11 | GPUDojo |
| RTX A4000 16GB | $850 | $1,130 ($1,000–1,299) [37] | Flat since Aug | GPUDojo |
| RTX A5000 24GB | $2,199 | n/a | $2,050–2,500 since Aug | GPUDojo |
| RTX A6000 48GB | $4,250 | $4,999 ($4,510–5,196) [17] | $3,999 (Aug) → $4,250 | GPUDojo |
| Tesla V100 16GB | $350 | $440 ($400–484) [9] | $240 (Sep/Oct) → $350 | GPUDojo |
| Tesla V100 32GB | $1,039 | $1,121 ($1,065–1,471) [8] | $625–650 (Aug–Sep) → $1,039 (+60%) | GPUDojo |
| Tesla P40 24GB | $384 | $398–442 IQR [7] | $225–239 (Aug) → $384 (+60–70%) | GPUDojo |
| Tesla T4 16GB | $470 | $675 ($623–959) [35] | $399 (Aug) → $470 | GPUDojo |
| A100 40GB | $5,850 | n/a | $3,500–4,495 (Sep–Oct) → $5,850 | GPUDojo |
| A100 80GB | $10,999 | n/a | $12,500 (Sep–Oct) → $10,999 | GPUDojo |
| H100 PCIe 80GB (reference) | $52,000 | n/a | $28,000 (Sep) | GPUDojo |

EU cross-check: BestValueGPU (EU) shows a used RTX 3090 at **€1,426** (about USD 1,574), "54% above its 12-month average of €927", in November 2026 (search-result snippet, ESTIMATE). EU used prices track US prices.

#### DDR4 ECC RDIMM (eBay US medians; CONFIRMED as dated asks)

| Module | US median | 30- / 90-day trend | Source |
|---|---|---|---|
| 16GB 2133 | $70 | −12.5% (30d) | VRAMGlass, 2026-11-14 |
| 16GB 2666 | $92 | −24.0% (30d) | VRAMGlass |
| 16GB 3200 | $129 | 0% (30d) | VRAMGlass |
| 32GB 2133 | $154 | −21.8% (30d) | VRAMGlass |
| 32GB 2666 | $199 | −7.9% (30d) | VRAMGlass; CresvaMent median $200 (n=103, −23.1% over 90 days) |
| 32GB 3200 | $300 | −7.7% (30d) | VRAMGlass |
| 64GB (2933/3200) | $500 (IQR $400–580) | −9.1% (90d) | CresvaMent, n=32 |

#### Servers and chassis (US/EU vendors, live)

| Item | Price | Source / status |
|---|---|---|
| Dell R730 barebones (8SFF / 16SFF / 8LFF) | $190 / $220 / $749 | newserverlife.com, live (CONFIRMED) |
| 13G/14G chassis (R630/R730/R640/R740) | $79.95 – $461.84 | PC Server & Parts, survey of 3 other stores, 2026-10-01 (CONFIRMED) |
| Configured 64GB 13G/14G builds | $811 – $1,127 | PCSP, 2026-10-01 (CONFIRMED) |
| Cheapest complete R640 with drives | $1,050.38 | PCSP shelf, 2026-10-01 (CONFIRMED) |
| Cheapest complete R740 with drives; R730xd | $1,874; $1,186.69 | PCSP, via search snippet (ESTIMATE) |
| Used R730 128GB (eBay asks) | $900 – $1,600; 2x E5-2620v4/32GB at $405 | eBay via search snippets (ESTIMATE) |
| 15G (R650 etc.) chassis; configured R650 | $3,000 – $4,937; $7,877 | PCSP, 2026-10-01 (CONFIRMED) |
| HPE DL380 Gen9, 2x E5-26xx v3/v4, 32GB | €520 – €700 incl. VAT (about $480 – $650 ex-VAT) | serverando.de, live (CONFIRMED) |
| HPE DL380 Gen10, 2x Gold 61xx, 32GB | €900 – €1,900 incl. VAT | serverando.de (CONFIRMED) |
| Dell R640, 32GB / R740xd, 32GB | €835 – €990 / €975 incl. VAT | serverando.de (CONFIRMED) |
| Dell R740, 2x Gold 6254 + 2x Tesla M10 | €1,620 incl. VAT | serverando.de (CONFIRMED) |
| **Supermicro 4028GR-TRT, 8-GPU barebone, refurbished** | **$1,495** (16 units in stock) | Core 4 Solutions, live (CONFIRMED); eBay asks $999–1,295 (ESTIMATE) |
| **Supermicro 4029GP-TRT, 8-GPU barebone, refurbished** | **$1,999** (13 units in stock) | Core 4 Solutions, live (CONFIRMED) |

### 2.5 Comparison: item | CO | EC | VE | US | ratio LATAM/US

| Item | CO (USD) | EC (USD) | VE (USD) | US used benchmark (USD, Nov 2026) | LATAM/US ratio |
|---|---|---|---|---|---|
| Dell R730 used, about 128GB | 1,447 – 1,779 (E) | n/f | 900 – 1,800 band (E); 128GB config 3,500 | 900 – 1,600 (eBay asks); barebones 105 – 190 | **CO about 1.1–1.6x** (about 0.9–1.3x at listing-era TRM); **VE 128GB config 2.2–3.9x** |
| Dell R740 used, configured | 3,015 (E) | n/f | n/f | 1,050 – 1,874; EU €1,620 with 2 GPUs | **CO about 1.6–2.9x** |
| Dell R610 / R710 (11G) | n/f | 999 – 1,300 (E) | within 900 – 1,800 (E) | about 100 – 300 (INFERENCE; 12G already sold out at PCSP) | **EC/VE about 3–10x** |
| HPE DL380 Gen9 / Gen10 | n/f | n/f | n/f | about 480 – 650 / about 750 – 1,600 ex-VAT (EU) | — |
| Supermicro 4028GR / 4029GP | n/f | n/f | n/f | 1,495 / 1,999 | — (no LATAM supply) |
| RTX 3060 12GB | n/f | n/f | n/f | 349 – 445 | — |
| **RTX 3090** | 1,055 – 1,357 typical (E, undated) | ~700 used; 1,900 semi-new (E) | 650 – 1,400 (E, about 2024) | 1,500 – 1,660 | **Apparent 0.45–0.9x, but stale.** Against the era's US price of 700–900, about 1.1–1.6x. |
| RTX 4090 | about 3,015 (E) | 2,889 new (about 2023) | n/f | 2,999 – 3,814 | Apparent 0.8–1.0x, stale |
| RTX A4000 / A5000 / A6000 | n/f | n/f | n/f | 850 / 2,199 / 4,250 | — |
| Tesla V100 16GB | 13,537 – 16,648 (E) | n/f | n/f | 350 – 440 | **about 30–45x** (non-market) |
| Tesla V100 32GB / P40 / T4 | n/f | n/f | n/f (M40 at 225) | 1,039 / 384 / 470 | — |
| A100 40GB / 80GB | n/f | n/f | n/f | 5,850 / 10,999 | — |
| **DDR4 32GB RDIMM 2666** | **202 (C)** | n/f | n/f | 199 – 200 | **1.0x** |
| **DDR4 32GB RDIMM 2133** | **178 (C)** | n/f | n/f | 154 | **1.16x** |
| **DDR4 16GB RDIMM 2400/2666** | **103 (C)** | n/f | n/f | 92 | **1.12x** |
| **DDR4 16GB RDIMM 2133** | **96 (C)** | n/f | n/f | 70 | **1.37x** |
| DDR4 64GB RDIMM | n/f | n/f | n/f | 500 | — |
| Xeon E5-2680 v4 | 78 (C) | n/f | n/f | about 20 – 40 (E, not verified this session) | about 2–4x |

C = CONFIRMED live price; E = ESTIMATE from an undated snippet; n/f = not found.

### 2.6 Import regimes and landed-cost multipliers vs. the US price

#### Rules found

| | Colombia | Ecuador | Venezuela |
|---|---|---|---|
| Tariff on HS 8471.41/49/50/80, 8473.30 (parts and GPUs), 8517.62 (switches), 8504.40 (PSUs/UPS) | **0%** (CONFIRMED: Arancel de Aduanas, Decreto 1881/2021, DIAN compilation) | Not verified this session. A thesis reports 8471.30 cut from 10% to 0% (COMEX 024-2019). I modelled 0% with 10% as a sensitivity (ESTIMATE). | Not verified (ESTIMATE). |
| VAT | 19% on customs value plus tariff (CONFIRMED). Exclusion up to 50 UVT (COP 2,618,700, about USD 790; UVT 2026 = COP 52,374) applies to *personal computers* only, not servers or GPUs. | 15% (Category C) plus FODINFA 0.5% of CIF (CONFIRMED, importacionesecuador.com.ec, updated 2025-11-30). Also ISD 5% on payments abroad (ESTIMATE, not verified). | 16% (ESTIMATE). Casilleros sell "door-to-door, taxes handled" rates, but quote separately for goods over USD 500 and for electronics or commercial cargo. |
| Courier channel | Tráfico postal / envíos urgentes: max **USD 2,000 and 50 kg** per shipment. USD 200 FOB de-minimis restored after **Sentencia C-079/2026** struck down Decreto Legislativo 1474/2025 (which had cut it to USD 50); the decree stopped applying on 2026-01-29. Generic courier tariff 10%, or the specific subheading. Shipment splitting is policed. (CONFIRMED: contagracia.com 2026-07-28; Corte Constitucional comunicado 15, 2026-04-15) | **Category B (4x4):** at most 4 kg and USD 400 FOB per package; **flat USD 20 tariff** since June 2025 (COMEX 006-2025) plus FODINFA, no VAT; **USD 1,600 per year per person**; individuals only, non-commercial. **Category C:** at most 100 kg and USD 5,000, product tariff plus 15% VAT plus FODINFA. (CONFIRMED: Andersen 2026-08-19; LogisticBox 2026-04-12.) Andersen lists a Category F for "libros y equipos de computación" with no limit, but another source says F covers books only. **This conflict is unresolved.** | Miami casilleros: air **USD 5.40/lb** to Caracas (USD 6.50 interior), sea **USD 35/ft³**, insurance 5% (Next Day Cargo, updated 2026-10-25). Globus Cargo: USD 5.70/lb, 10 lb minimum, 3% mandatory insurance. (CONFIRMED) |
| **Used goods** | **Licencia previa required** for used, refurbished or reconstructed goods (Decreto 925/2013 art. 14; MinCIT FAQ). Approval is by the Comité de Importaciones and they cannot be imported under an annual license (VUCE manual). (CONFIRMED) | No explicit prohibition for HS 8471 found. COMEX 009-2022 Annex II, as described, lists used tires and used clothing/footwear. 4x4 is for personal goods only, and phones must be new. (ESTIMATE: verify with SENAE or a customs agent.) | **Next Day Cargo lists crypto-mining equipment and parts as prohibited** (2026-10-25). Multi-GPU rigs risk being treated as mining gear (INFERENCE). |

#### Landed-cost multipliers (computed; assumptions stated)

Assumptions: the US price includes delivery to a Miami forwarding address and **excludes US sales tax** (add about 7% if bought to a Florida address). Colombia casillero USD 3.00/lb (USD 2.80/lb at 56 lb and over; PrimeBox, 2026-06-19). Ecuador about USD 4.99/lb (LogisticBox). Venezuela USD 5.40/lb air or USD 35/ft³ sea, with 5% insurance. Shipping weights: GPU 6 lb; 8 RDIMMs 1.5 lb; 2U server 70 lb / 5.5 ft³; 4U 8-GPU barebone 120 lb / 10 ft³.

| Item (US price) | Colombia, 0% tariff + 19% VAT | Colombia, 10% courier tariff | Colombia, VAT recovered* | Ecuador, 0% tariff (+ISD 5%) | Venezuela, all-in casillero | Venezuela, with 10% duty + 16% VAT (stress case) |
|---|---|---|---|---|---|---|
| Used RTX 3090 ($1,600) | 1.20x | 1.32x | 1.01x | 1.18x (1.23x) | 1.07x | 1.37x |
| 8x DDR4 32GB RDIMM ($1,600) | 1.20x | 1.32x | 1.01x | 1.16x (1.21x) | 1.06x | 1.36x |
| 2U server, R740-class ($1,100) | 1.40x | 1.54x | 1.18x | 1.52x (1.57x) | 1.39x air / 1.23x sea | 1.56x |
| 4U 8-GPU barebone, 4029GP-TRT ($1,999) | 1.39x** | 1.53x** | 1.17x** | 1.50x (1.55x) | 1.37x air / 1.23x sea | 1.56x |

\* A Colombian VAT-responsible company exporting services (rental to foreign marketplaces is plausibly an exempt service export) can in principle credit or refund import VAT. This is slow and requirement-heavy (INFERENCE; verify with a Colombian tax advisor).
\*\* Over the USD 2,000 courier cap, so this needs a formal import with a customs broker (add about USD 150–300, ESTIMATE). As used goods it also needs a **licencia previa**.

**Rule of thumb:** dense, high-value parts (GPUs, RAM) land at **about 1.05–1.35x** the US price. Whole servers land at **about 1.25–1.6x**, because freight on 30–55 kg chassis is a large share of a USD 1,000–2,000 item. **Ship parts, not chassis.**

### 2.7 DRAM/GPU price context 2025–2026

| Indicator | Figure | Date / source |
|---|---|---|
| Conventional DRAM contract prices | TrendForce forecast of +55–60% QoQ for Q1 2026, **revised to +90–95%** on 2026-02-02 | DatacenterDisk, 2026-10-11 |
| HBM share of DRAM wafer input (top 3) | About 18% (end-2025), 22% (end-2026F), 30% (end-2027F) | TrendForce 2026-06-02, via DatacenterDisk |
| DDR4 ECC RDIMM (new) | +60–80% from early 2025 to Q1 2026; DDR5 RDIMM +100–116% | DatacenterDisk |
| DDR4 8Gb spot | Record about $42.50 (Aug 2026), $47.04 (Oct 2026) | Search snippet (ESTIMATE) |
| 32GB DDR4-3200 desktop kit | About $70 (mid-2025) → **$250** (Oct 2026), about 3.5x | PCSP, re-checked 2026-10-10 |
| Used 32GB DDR4 RDIMM | About $200 median now; easing −8% to −23% over 30–90 days from a Sep 2026 peak (CresvaMent median $259.99 in mid-Sep) | VRAMGlass / CresvaMent, 2026-11-14 |
| Used RTX 3090 | $500–650 (PCSP "June" guide, likely 2025); $700–850 (early 2026); about $1,070 (Jun 2026); $1,343 avg (Sep 4); **$1,540–1,660** (Nov 14) | runaihome 2026-06-13; PCSP 2026-09-09; ResalePrices |
| Used RTX 4090 | About $2,268 (Aug 2026) → $2,999 lowest / $3,814 median (Nov) | runaihome; GPUDojo |
| RTX 5090 new | $2,250 (Sep 2025) → $4,999 (Sep 2026) → $6,250 lowest (Nov 2026); MSRP $1,999 | PCSP (citing Tom's Hardware); GPUDojo |
| Stated drivers | GDDR7 shortage; reported 30–40% cut in gaming-GPU production in 2026; fabs shifting to HBM/server DRAM | runaihome, 2026-06-13 (analyst claims) |

**Are old servers' parts worth more as resale than as rental assets? Often yes in 2026 (INFERENCE from the figures above).**

- **Dell R730, 2x E5-2680 v4, 256GB (8x32GB DDR4-2400):**
  - Parts-out: RAM 8 x about $170 = about **$1,360**, CPUs 2 x about $20–40, chassis $105–190, so **about $1,500–1,650**.
  - Whole-unit US asks for a 128GB R730 are $900–1,600, and configured 64GB 13G/14G builds sell for $811–1,127.
  - **The RAM alone can be worth more than a typical configured unit.**
- **8-GPU node (4028GR-TRT barebone $1,495 + 8x P40 at $384–420 + CPUs/RAM about $1,400):** about **$6,000–6,300** at today's US asks. The P40s alone rose about 60–70% since August.
- **Opportunity-cost test (illustrative placeholders only; use the rental and power figures from the other agents):**
  - A used 3090 now resells at about $1,550.
  - At a hypothetical $0.20/h list price, 60% utilisation and 25% platform fees, gross is about $790/yr.
  - Power at 0.35 kW x 60% x 8,760 h x $0.15/kWh costs about $276/yr.
  - Net is about **$510/yr**, so it takes **about 3 years just to earn back the cash you could get by selling today**, before depreciation risk. The 2026 price doubling roughly doubled this hurdle.

### 2.8 Volume and supply channels

- **MercadoLibre volume:** at most dozens of relevant server listings per country, mostly 11G–13G Dell and storage-heavy configs. No P40, T4, A100 or A-series in CO, EC or VE. V100s appear only at non-market prices (CO). Venezuela shows hobbyist leftovers such as M40, C2075 and water blocks (ESTIMATE from snippets).
- **Live Bogotá parts shop** (pcyservidores.co): stocks DDR3/DDR4 RDIMMs, a single CPU SKU and caddies/fans. That is a parts-trade scale, not lots.
- **Institutional channels** (not verified this session; background knowledge, INFERENCE):
  - **Colombia:** Central de Inversiones (CISA) sells public entities' movable assets. The site was reachable but JS-rendered, so I could not inspect the listings. Martillo del Banco Popular's site showed "en construcción". SAE, Ecopetrol, banks and telcos run "bajas de activos". Enterprise servers are often leased through OEM financial services and go back to OEM or ITAD channels, which frequently export them.
  - **Ecuador:** public-sector "bajas", "remates" and "chatarrización" under the Contraloría asset regulation. INMOBILIAR's site did not resolve.
  - **Venezuela:** few formal channels. Seized-goods auctions exist, and a 2024 mining crackdown led to confiscations (background, unverified).
- **Bottom line on volume:** no evidence of recurring datacenter-decommissioning lots with GPUs in any of the three countries. Any such deal would be one-off and relationship-driven. Its price would anchor to eBay, because sellers can see the US price (VE listings are already in USD; EC is dollarized).

---

## 3) Implications for the LATAM used-hardware rental business

1. **Sourcing in LATAM does not create the margin.** Local asks for comparable hardware are at or above US used prices. Datacenter-class GPUs, the cards that rent best on Vast.ai, RunPod and similar platforms, are essentially unavailable locally. The base case should be **buying in the US/EU (or Asia) and importing parts**, budgeting a **1.05–1.35x** landed multiplier for GPUs and RAM and **1.25–1.6x** for chassis.
2. **Colombia is the cleanest import jurisdiction for IT gear:**
   - 0% tariff on 8471/8473/8517 (confirmed).
   - VAT can be recoverable through a formal company that exports services.
   - The binding constraints are the **licencia previa for used goods** and the USD 2,000 / 50 kg courier cap.
   - A workable pattern is chassis bought new or locally, with used GPUs and RAM brought in by courier in batches under USD 2,000. Tax and legal advice is needed on whether repeated batches count as commercial splitting.
3. **Ecuador:** the 4x4 regime only fits single cards under USD 400 (for example an RTX 3060 12GB) and USD 1,600 per year per person. Anything serious goes through Category C or a formal import, with 15% VAT plus 5% ISD and an unverified tariff.
4. **Venezuela has the cheapest courier pricing but the highest seizure and legal risk.** Carriers prohibit crypto-mining equipment, multi-GPU rigs look like mining rigs, and the USD/VES gap and payment frictions add risk. Do not plan on importing GPU clusters into Venezuela without counsel.
5. **The 2026 memory and GPU shock argues for an "inventory monetisation" lens.** If the entrepreneur can source old servers at genuinely distressed prices (auctions or bank bajas), the best risk-adjusted move may be to **part them out and sell RAM, CPUs and GPUs into the US/EU market** rather than rent them. Old 13G/14G platforms are poor rental hosts anyway: PCIe 3.0, limited GPU slots and power. Reverse arbitrage carries its own costs: eBay/marketplace fees of about 13% (ESTIMATE), export logistics, and the risk that the 2026 spike reverses as the shortage eases. Used RDIMM and RTX 5090 asks already fell 8–23% in the last 30–90 days.
6. **FX headwind:** the strong COP (3,317 vs. 4,409 in Jan 2025) makes COP-priced local hardware about 33% dearer in USD than 22 months ago. It does, however, make USD-earned rental income worth less in COP terms for local costs.
7. **Decision rule:** pursue local sourcing only if a specific auction or decommissioning lot is quoted **below 0.7x US eBay asks** (to cover testing, failure rate and resale fees). Otherwise, model hardware CAPEX at US price x landed multiplier.

---

## 4) Confidence and gaps

| Topic | Confidence | Why |
|---|---|---|
| US used GPU and RDIMM prices (Nov 2026) | **High** for direction and level (±10–15%) | Multiple trackers agree (GPUDojo, ResalePrices, VRAMGlass, CresvaMent). They are asking prices, not sold prices. |
| US/EU server chassis prices | Medium–High | Live vendor pages (Core4, PCSP, newserverlife, serverando). eBay figures come from snippets. |
| Colombia DDR4 and CPU prices | Medium–High | One live shop only, so the sample is small. |
| CO/EC/VE MercadoLibre server and GPU prices | **Low–Medium** | Bot wall and 403 API. Prices come from search-engine snippets with no posting dates; some are clearly years old. |
| Colombia tariff (0%) and used-goods licencia previa | High | Official DIAN tariff text and the MinCIT FAQ. |
| Colombia courier thresholds post-C-079/2026 | Medium–High | Court communiqué plus professional commentary (Jul 2026). |
| Ecuador courier rules | Medium | Andersen and courier blogs (2026). **Tariff on 8471/8473 not verified; Category F conflict unresolved; ISD rate not verified.** |
| Venezuela duties | **Low** | Only casillero tariff pages. SENIAT duty rates for 8471/8473 not verified. |
| Auctions / decommissioning volume | **Low** | Not verifiable this session. Sites were JS-only or unreachable, and the search budget ran out. |

**Not researched or not found (gaps):**
- Wallapop / eBay.es prices.
- US eBay *sold* (completed) data.
- LATAM prices for HPE DL380 Gen9/Gen10, R620/R750, and the Supermicro GPU servers.
- Colombian and Ecuadorian listings for A-series, P40, T4 and A100.
- Current RTX 3090/4090 asks on ML CO, which are decisive for the "stale-listing" question. A human should run a live check of `listado.mercadolibre.com.co/rtx-3090` sorted by most recent.
- Official SENAE tariff schedule.
- SENIAT courier rules.
- Concrete CISA and INMOBILIAR auction lots of IT equipment.

**Suggested next steps:**
1. A person in Colombia should spend 30 minutes on MercadoLibre and Facebook Marketplace, logging 20 current 3090/4090/server listings with dates.
2. Request a quote from a Colombian customs broker for a used 4U GPU server (licencia previa timing and cost).
3. Ask CISA and two Bogotá ITAD firms for upcoming IT-equipment lots.

---

## 5) Sources (all accessed 2026-11-14)

**FX**
- Colombian TRM (Superfinanciera via datos.gov.co): https://www.datos.gov.co/resource/32sa-8pi3.json
- VES official and parallel: https://ve.dolarapi.com/v1/dolares
- Cross rates (COP, VES, EUR): https://open.er-api.com/v6/latest/USD

**LATAM listings and shops**
- MercadoLibre Colombia listing pages (search-snippet data only; pages blocked):
  - https://listado.mercadolibre.com.co/servidor-dell-poweredge-r730
  - https://listado.mercadolibre.com.co/servidores-dell-usados
  - https://listado.mercadolibre.com.co/3090-usada
  - https://listado.mercadolibre.com.co/rtx-3090
  - https://listado.mercadolibre.com.co/4090-rtx
  - https://listado.mercadolibre.com.co/nvidia-tesla-v100
  - https://listado.mercadolibre.com.co/memoria-ram-ddr4-32-gb-servidor
- MercadoLibre Venezuela:
  - https://listado.mercadolibre.com.ve/servidores-dell-poweredge
  - https://listado.mercadolibre.com.ve/poweredge-r630
  - https://listado.mercadolibre.com.ve/computacion/3090
  - https://articulo.mercadolibre.com.ve/MLV-749732523-msi-ventus-geforce-rtx-3090-24gb-gddr6x-tarjeta-video-usada-_JM
  - https://listado.mercadolibre.com.ve/nvidia-tesla-a100
- MercadoLibre Ecuador:
  - https://listado.mercadolibre.com.ec/computacion/servidor-dell-poweredge
  - https://computacion.mercadolibre.com.ec/componentes-tarjetas-video/rtx-3090
- MercadoLibre API (403 without auth): https://api.mercadolibre.com/sites/MCO/search?q=dell%20r730
- pcyservidores.co (Bogotá), live prices:
  - https://www.pcyservidores.co/memoria-ram-servidor
  - https://www.pcyservidores.co/servidores-1
  - https://www.pcyservidores.co/procesadores-servidor

**US/EU benchmarks**
- GPUDojo (eBay US lowest offers and asking-price distributions, updated 2026-11-13):
  - https://gpudojo.com/rtx-3090 ; https://gpudojo.com/rtx-4090 ; https://gpudojo.com/rtx-5090 ; https://gpudojo.com/rtx-3060-12gb
  - https://gpudojo.com/a4000 ; https://gpudojo.com/a5000 ; https://gpudojo.com/a6000
  - https://gpudojo.com/tesla-v100 ; https://gpudojo.com/tesla-v100-16gb ; https://gpudojo.com/tesla-p40 ; https://gpudojo.com/t4
  - https://gpudojo.com/a100-40gb ; https://gpudojo.com/a100-80gb ; https://gpudojo.com/h100-pcie
  - https://gpudojo.com/market-notes
- ResalePrices RTX 3090 (updated 2026-11-14): https://resaleprices.com/gpu/nvidia-rtx-3090
- BestValueGPU EU, RTX 3090 (search snippet; site returned 429): https://bestvaluegpu.com/en-eu/history/new-and-used-rtx-3090-price-history-and-specs/
- DDR4 RDIMM medians:
  - VRAMGlass (updated 2026-11-14): https://vramglass.com/ddr4
  - CresvaMent 32GB: https://cresvament.com/deals/memory/ddr4-32gb-ecc-rdimm
  - CresvaMent 64GB: https://cresvament.com/deals/memory/ddr4-64gb-ecc-rdimm
- Servers:
  - Core 4 Solutions 4028GR-TRT: https://www.core4solutions.com/supermicro-4028gr-trt.html
  - Core 4 Solutions 4029GP-TRT: https://www.core4solutions.com/products/4u-24x2-5-2x-xeon-gen-1-2-8x-gpu-server
  - PC Server & Parts, Dell generations (shelf priced 2026-10-01): https://pcserverandparts.com/news/dell-poweredge-generations-explained-2026/
  - newserverlife R730: https://newserverlife.com/server-models/dell-poweredge-r730/
  - serverando.de (EU, VAT incl.): https://serverando.de/es/servidores/rack-server/hpe/ ; https://serverando.de/es/servidores/rack-server/dell/

**Market context**
- DatacenterDisk, memory shortage analysis (2026-10-11): https://datacenterdisk.com/news/memory-chip-shortage-2026-server-ram-prices
- PCSP, DDR4 vs DDR5 2026 (re-checked 2026-10-10): https://pcserverandparts.com/blog/ddr4-vs-ddr5-memory-pricing-trends-2025/
- PCSP, used GPU buying guide 2026 (modified 2026-11-03): https://pcserverandparts.com/news/used-graphics-card-buying-guide-2026/
- runaihome, NVIDIA/GDDR7 shortage guide (2026-06-13): https://www.runaihome.com/blog/nvidia-no-new-consumer-gpus-2026-home-lab-buying-guide/

**Import rules: Colombia**
- Arancel de Aduanas, Decreto 1881/2021 (DIAN compilation): https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1881_2021.htm
- MinCIT FAQ on licencia previa: https://www.mincit.gov.co/servicio-ciudadano/preguntas-frecuentes/direccion-de-comercio-exterior
- VUCE licencia previa manual: https://www.vuce.gov.co/getattachment/ayuda/importaciones/manual-regimen-de-licencia-previa/manual-regimen-de-licencia-previa-9oct2024.pdf.aspx
- Corte Constitucional, comunicado 15, C-079/26 (2026-04-15): https://www.corteconstitucional.gov.co/comunicados/Comunicado-15-Abril-15-de-2026.pdf
- Courier regime after C-079/2026 (2026-07-28): https://contagracia.com/blog/envios-exterior-umbral-200-dolares-iva-2026
- Alegra, import taxation (updated 2026-07-21): https://blog.alegra.com/colombia/tributacion-de-importaciones-en-colombia/
- PrimeBox casillero rates, UVT 2026, 50 UVT (2026-06-19): https://primebox.com.co/guias/cuanto-cuesta-traer-macbook-usa-colombia

**Import rules: Ecuador**
- Andersen, courier categories (2026-08-19): https://ec.andersen.com/courier-mayor-control-sobre-el-valor-declarado-y-nueva-asignacion-de-responsabilidades/
- LogisticBox, Category B 2026 (2026-04-12): https://logistic-box.com/blog/categoria-b-4x4-ecuador-2026.html
- Importaciones Ecuador, courier categories (updated 2025-11-30): https://www.importacionesecuador.com.ec/despacho-aduanero/importaciones-por-courier
- GLOBI, used machinery in Ecuador and COMEX 009-2022 (2026-08-14): https://www.globigroup.com/blog-importar-maquinaria-usada-ecuador.html

**Import rules: Venezuela**
- Next Day Cargo rates and prohibited items (updated 2026-10-25): https://www.nextdaycargo.com/en/envios-a-venezuela/
- Globus Cargo, Venezuela rates: https://globuscargo.com/envios-a/venezuela

**Auction channels (unverified)**
- CISA (JS-rendered, not inspectable): https://www.cisa.gov.co/

# 06: GPU Rental Price Benchmark, Price Indices and Trends (November 2026)

**Agent 06 of 10. Topic: what the "industry standard" GPU rental price is, how it has moved since 2023, and what to assume for 2027–2028.**
Research date: 2026-11-14. All prices are USD per GPU-hour unless stated otherwise.
Labels: **[C]** means CONFIRMED (primary source or a live API pull, dated). **[S]** means a secondary source (an aggregator or a vendor blog). **[E]** means my ESTIMATE or inference.

---

## 1. Executive summary

- **The market is in a shortage regime, and prices are rising, not falling.** Every index and tracker shows GPU rental prices *up* year-on-year in November 2026. Over 12 months to the week of 9 Nov 2026, the GetDeploying on-demand provider median rose by these amounts [C, CC-BY dataset]:
  - H100: +32% ($2.99 → $3.96)
  - H200: +44%
  - B200: +48%
  - A100: +14% ($1.70 → $1.93)
  - L40S: +27%

  Neoclouds are still raising list prices this month:
  - **Lambda**, effective 16 Nov 2026: H100 $3.99 → $4.59, A100 80GB $2.79 → $3.19, B200 $6.69 → $7.69 [C]. In June 2026 these were $2.99, $1.79 and $4.99 [S].
  - **Crusoe**, effective 1 Dec 2026: H100 $3.90 → $4.50, H200 $4.29 → $5.40 [C].
- **Today's benchmark levels (13–14 Nov 2026):**

  | GPU | Ornn OCPI | Silicon Data index | Vast.ai marketplace median (my API pull, ~2,470 machines) |
  |---|---|---|---|
  | H100 SXM | $3.29 | $3.10 (SDH100RT) | $2.30–2.37 |
  | A100 | $1.04 | $1.64 (SDA100RT) | $0.73 (PCIe) – $0.95 (SXM) |
  | B200 | $9.72 | $6.87 (SDB200RT) | — |
  | H200 | $6.73 | $3.60 | — |
  | RTX PRO 6000 | $1.57 | — | — |
  | RTX 5090 | $0.68 | — | $0.71 |

  Vast.ai medians for the GPUs a LATAM used-hardware buyer can realistically source [C]:

  | GPU | Vast median |
  |---|---|
  | RTX 4090 | $0.53 |
  | RTX A6000 | $0.44 |
  | A40 | $0.60 |
  | RTX 3090 | $0.23 |
  | RTX A5000 | $0.23 |
  | RTX A4000 | $0.10 |
  | V100 | $0.09 |
  | T4 | $0.14 |
  | P40 / P100 | ~$0.09–0.11 |
- **There are three price tiers, and they are far apart.** For an H100 per GPU-hour:
  - Hyperscalers on-demand: $6.88 (AWS), $11.07 (GCP), $12.29 (Azure).
  - Neoclouds: $3.90–6.16.
  - Marketplaces: $1.73–2.69.
  - **For old GPUs the gap is absurd.** AWS still charges **$3.06/hr for a V100** (the 2017 price), which is 33 times the Vast.ai median of $0.093. Hyperscaler prices are not a usable benchmark for used hardware. The marketplace tier is.
- **The H100 price path:**
  - Hyperscaler: ~$7.8 (2H 2023) → $9.3 (2H 2024) → $6.3 (2H 2025) → ~$6.9–7.5 (2026).
  - Marketplace: $2.58 (2H 2024) → $1.95 (2H 2025), which is **−24% in a year** → ~$2.3–3.1 (Nov 2026), which is **+20% to +60%** [C, Silicon Data].
  - The one-year contract rate rose ~40% between Oct 2025 ($1.70) and Mar 2026 ($2.35) [C, SemiAnalysis].
- **Older consumer GPUs have been flat to slightly up in 2026.**
  - RTX 3090: ~$0.21–0.23, flat.
  - RTX 4090: medians between $0.46 and $0.53, while the cheapest listing **nearly doubled** ($0.18 → $0.33).
  - V100: still sinking to ~$0.09, which is near the cost of power.
- **Normal-regime decay (2023–2025, before the shortage):** roughly −20 to −30% a year for A100 and RTX 4090, −10 to −15% a year for RTX 3090, and −30% a year for V100 [E]. In cross-section, each older consumer generation rents for about 35–75% of its successor (5090 $0.71 → 4090 $0.53 → 3090 $0.23 → 2080 Ti $0.08).
- **The forecast is split.** SemiAnalysis says rental prices are "more likely to continue rising than falling." The Silicon Data H100 forward curve implies $2.83 in 6 months against $3.10 spot (−9%). Its B200 12-month forward (as of Sep) was −12% below spot. Packaging (CoWoS) and memory (HBM/DRAM) supply is constrained into mid-2027. NVIDIA is raising server prices by more than 15% in early 2027. **Assumptions to use in a 3-year payback model** (annual change in $/GPU-hr from today's level):
  - **Bull ≈ −5%/yr**
  - **Base ≈ −17%/yr**
  - **Bear ≈ −30%/yr**

  For GPUs that already sit near the power-cost floor (V100, P40, 3080-class), model a fall in *occupancy*, not only a fall in price.
- **Geography: buyers are global, so marketplace prices converge.** LATAM hosts are **~1.3% of Vast.ai supply** (32 of ~2,470 machines; none in Colombia or Venezuela, one in Ecuador). They list at a **~25–35% discount** to North America and Europe (RTX 3090 $0.14 vs $0.21 NA and $0.26 EU, n=13), and they have weaker upload bandwidth and reliability. Hyperscalers, by contrast, charge **+60–70% more in São Paulo** than in us-east-1.

---

## 2. Detailed findings

### 2.1 Cross-provider price table, November 2026 ($/GPU-hr)

#### 2.1a Hyperscalers (US East, Linux; per GPU = instance price ÷ GPU count)

Sources:
- AWS and Azure: the Vantage instances.vantage.sh datasets, pulled 2026-11-14 [C, derived from the providers' price APIs].
- GCP: GetDeploying's Google Cloud page, 2026-11-14 [S]. GCP's own page is rendered in JavaScript and would not extract.

| GPU | AWS on-demand | AWS spot (avg) | GCP on-demand | GCP spot | Azure on-demand | Azure spot |
|---|---|---|---|---|---|---|
| B300 | 17.80 (p6-b300) | 8.04 | – | – | – | – |
| B200 | 14.24 (p6-b200) | 8.59 | 1-yr reserved 11.22 | 3.98 | – | – |
| H200 | 7.91 (p5en) | 4.97 | – (3-yr 4.66) | 5.72 | 10.60 (ND H200 v5) | – |
| H100 SXM | 6.88 (p5 / p5.4xlarge) | 3.88 | 11.07 (a3-high) | 4.98 | 12.29 (ND H100 v5) | 2.27 |
| H100 NVL/PCIe | – | – | – | – | 6.98 (NC40ads H100) | 1.42 |
| A100 80GB | 3.43 (p4de) | 2.61 | – | – | 4.10 (ND A100 v4) / 3.67 (NC24ads) | 1.06 / 0.68 |
| A100 40GB | 2.74 (p4d) | 2.12 | 3.72 (a2) | 2.23 | 3.40 (ND96asr) | 0.75 |
| L40S | 1.86 (g6e.xlarge) | 1.65 | – | – | – | – |
| RTX PRO 6000 Blackwell | 3.36 (g7e.2xl) | 1.91 | 4.50 (g4) | 1.81 | 5.50–6.38 (NC RTX6k v6) | 1.02 |
| V100 | 3.06 (p3.2xl) | 0.43 | 2.53 | 1.44 | 3.06 (NC6s v3) | 0.57 |
| T4 | 0.53 (g4dn.xl) | 0.23 | 0.42 | 0.24 | 0.53 (NC4as T4) | 0.16 |
| P100 | – | – | 1.51 | 0.55 | – | – |
| L4 / A10G (reference) | 0.80 / 1.01 | 0.57 / 0.64 | 0.70 (L4) | 0.39 | – | – |

Not offered by hyperscalers: RTX 6000 Ada, A6000, A40, RTX 5090, RTX 4090, RTX 3090, A5000, A4000, P40.

#### 2.1b Neoclouds (on-demand list prices)

| GPU | CoreWeave [C] | Lambda, eff. 16 Nov 2026 [C] | Nebius [C] | Crusoe, now → 1 Dec [C] | Together [C] | Voltage Park [C] |
|---|---|---|---|---|---|---|
| GB200 | 10.50 | – | contact | contact | contact | – |
| B300 | contact | – | 9.50 | 8.96 → 9.90 | 11.49 | – |
| B200 | 8.60 | 7.69–7.99 | 8.50 | contact → 8.50 | 9.29 | – |
| H200 | 6.31 | – | 5.40 | 4.29 → 5.40 | 5.99 | – |
| H100 SXM | 6.16 | 4.59–4.89 | 4.50 | 3.90 → 4.50 | 3.99 | "from 1.99" (undated) |
| H100 PCIe | – | 3.79 | – | – | – | – |
| A100 80GB | 2.70 | 3.19 | – | 2.30 (SXM) / 2.00 (PCIe) | – | – |
| A100 40GB | – | 1.99 | – | – | – | – |
| L40S | 2.25 | – | 1.55–1.82 | 1.50 | – | – |
| RTX PRO 6000 | 2.50 | – | 1.80 | – | – | – |
| A6000 | – | 1.09 | – | – | – | – |
| V100 | – | 0.79 | – | – | – | – |

Preemptible and discounted prices:
- **Nebius preemptible:** "from" $0.79 for H100/H200, $0.99 for B200/B300, and $0.74–0.90 for L40S.
- **Together preemptible:** H100 $1.99, H200 $2.99, B200 $4.65.
- **Together 31–90-day reservation:** H100 $3.45, B200 $7.99.
- **Lambda 1-Click Clusters:** H100 $5.54–6.16, B200 $8.87–9.86.

#### 2.1c Marketplaces and P2P platforms

| GPU | RunPod Secure / Community (12 Nov) [C] | Vast.ai median, all listings (occupied-only median) [C, my API pull 14 Nov] | Vast.ai p25–p75 | TensorDock "from" [C] | Hyperbolic "from" [C] | SaladCloud batch → high priority [C] |
|---|---|---|---|---|---|---|
| B200 | 7.99 / 5.98 | 9.99 (8.75), n=40 | 7.50–10.63 | – | 5.99 | – |
| H200 | 5.29 / 3.59 | 4.61 (4.61), n=33 | 3.68–5.26 | – | 3.99 | – |
| H100 SXM | 4.39 / 2.69 | 2.37 (2.30), n=36 | 2.16–3.33 | 2.25 | 3.19 | – |
| H100 PCIe | 2.89 / 1.99 | 2.67, n=9 | 2.53–2.85 | – | – | – |
| A100 80GB SXM | 2.19 / 1.39 | 0.95 (1.05), n=93 | 0.55–1.15 | 1.80 | – | – |
| A100 PCIe | 2.09 / 1.19 | 0.73 (0.75), n=55 | 0.60–0.87 | – | – | – |
| L40S | 1.09 / 0.79 | 0.60, n=55 | 0.47–0.80 | – | – | – |
| RTX PRO 6000 Blackwell (WS / Server / Max-Q) | 2.69 / 1.69 | 1.47 / 1.68 / 1.35, n≈376 | 1.08–1.80 | – | – | – |
| RTX 6000 Ada | 1.09 / 0.74 | 0.67, n=34 | 0.60–0.79 | – | – | – |
| RTX A6000 | 0.69 / 0.33 | 0.44, n=46 | 0.40–0.48 | – | – | – |
| A40 | 0.59 / 0.35 | 0.60, n=25 | 0.56–0.68 | – | – | – |
| RTX 5090 | 1.39 / 0.69 | 0.71 (0.69), n=664 | 0.57–0.93 | – | – | 0.25 → 0.60 |
| RTX 4090 | 0.89 / 0.34 | 0.53 (0.52), n=207 | 0.47–0.67 | 0.35 | – | 0.16 → 0.44 |
| RTX 3090 | 0.50 / 0.22 | 0.23 (0.23), n=374 | 0.19–0.33 | – | – | 0.09 → 0.20 |
| RTX A5000 | 0.27 / 0.16 | 0.23, n=38 | 0.20–0.23 | – | – | – |
| RTX A4000 | – | 0.096, n=84 | 0.089–0.12 | – | – | – |
| V100 | – | 0.093, n=104 | 0.067–0.147 | – | – | – |
| T4 | – | 0.137, n=11 | 0.093–0.148 | – | – | – |
| P40 / P100 | – | 0.107 (n=5) / 0.093 (n=12) | – | – | – | – |

Notes on the Vast.ai pull:
- The pull covers 38 GPU models. "n" is unique machines; "occupied" means listings flagged `rentable=false`.
- The price is the host's asking price (`dph_base`) per GPU, so it **excludes storage and bandwidth** charges. The host receives less than this after Vast's fee (other agents cover fees).
- SF Compute does not publish public prices; its order book is behind a login [S, computeprices.com, reviewed 28 Sep 2026].

Aggregator cross-checks (on-demand, all tiers mixed):

| GPU | GetDeploying median, week of 9 Nov 2026 [C] | computeprices.com median, 13–14 Nov 2026 [S] |
|---|---|---|
| H100 | $3.96 (44 providers) | $3.39 (H100 SXM, 57 providers) |
| H200 | $5.05 | $4.47 |
| B200 | $8.12 | $7.94 |
| A100 | $1.93 | $1.60 (A100 SXM 80GB) |
| RTX PRO 6000 | $2.41 | $2.03 |
| L40S | $1.64 | $1.18 |
| RTX 5090 | $0.72 | – |
| RTX 4090 | $0.46 | – |
| RTX 3090 | $0.22 | – |
| A6000 | $0.65 | $0.55 |

Spot prices run at **52–60% of on-demand** across GPU types (GetDeploying) [C].

### 2.2 Price indices: current levels and history

| Index (publisher) | What it measures | Latest (date) | Recent history |
|---|---|---|---|
| **SDH100RT** (Silicon Data, on Bloomberg; CME/NYMEX futures listed from 5 Oct 2026, pending CFTC) | Neocloud and marketplace H100 listings, standardized for specs, term and geography | **$3.10** (13 Nov 2026) | 2.53 (~Apr 2026) → 2.57 (4 May) → 2.73 (31 May) → 2.79 (5 Jun high) → 2.75 (27 Jul) → 2.63 (7 Sep) → 2.81 (15 Oct) → 3.10 (13 Nov) |
| SD H100 Hyperscaler | Hyperscaler on-demand H100 | $7.40–7.52 band (1 Mar–20 Apr 2026) | Flat in 2026; hyperscaler H100 fell 26–54% by region between Q1 2025 and Q3 2026 |
| **SDA100RT** (Silicon Data) | A100, neocloud | **$1.64** (13 Nov 2026) | 1.52 (15 Oct) → 1.64; +7.9% in 30 days |
| **SDB200RT** (Silicon Data) | B200 | **$6.87** (13 Nov 2026) | ~4.40 (1 Jan, implied) → 5.42 (Jun) → 5.62 (1 Sep, +27.6% YTD) → 6.01 (15 Oct) → 6.87, i.e. **~+56% YTD** |
| SD H200 | H200 | **$3.60** (13 Nov 2026) | 2.70 (4 May) → 3.10 (18 Jul) → 3.29 (7 Sep) → 3.37 (15 Oct) → 3.60 |
| SD H100 forward curve | No-arbitrage term structure | Spot 3.10; 6-month term rate 3.00; **6-month implied forward 2.83** (13 Nov) | The curve is downward-sloping, so the market expects H100 prices to ease |
| **Ornn OCPI** (on Bloomberg as ORNNH100) | *Transacted* neocloud deals, volume-weighted and winsorized, settled daily | H100 **$3.29**; H200 **$6.73**; B200 **$9.72**; A100 SXM4 **$1.04**; RTX PRO 6000 WS **$1.57**; RTX 5090 **$0.68** (13 Nov 2026) | H100 3-month range $2.46–3.53; last 30 days $2.80–3.53, swinging ±5–10% day to day. 30-day changes: B200 +23%, H200 +7%, A100 +8%, RTX PRO 6000 +7% |
| **SemiAnalysis** H100 index | Monthly survey of 100+ market participants, checked against transactions | Composite $2.82; 1-year contract $2.10–2.70 (Apr 2026); B200 $3.68 (Apr 2026) | Composite $3.60 (1Q25) → $3.34 (2Q25) → $2.79 (Jul 25) → $2.80–2.84 (Aug 25–Mar 26). 1-year contract **$1.70 (Oct 2025) → $2.35 (Mar 2026), +38–40%** |
| GetDeploying index (CC-BY dataset) | Median of providers' on-demand listings, weekly | H100 $3.96 | H100 $2.99 (Nov 25) → 2.92 (Mar 26) → 3.07 (Jun) → 3.35 (Jul) → 3.38 (Sep) → 3.83 (Oct) → 3.96 (Nov). Across 22 models, +13% year-on-year (17 rose, 5 fell) |
| SF Compute | Order book for H100/H200 clusters | Not public (login) | – |
| S&P Global Platts | Announced US GPU compute price assessments launching 23 Nov 2026 (subscriber note 110526; page returned 403) | – | – |

**The index levels disagree by method.** Ornn (transacted neocloud deals) puts the H200 at $6.73 and the B200 at $9.72. Silicon Data (standardized observations that include marketplaces) puts them at $3.60 and $6.87. For the H100 they roughly agree ($3.29 vs $3.10). For the A100, Ornn is *lower* ($1.04 vs $1.64). Implicator.ai documented up to an ~8x spread between H100 "trackers" because they measure different things (marketplace spot vs hyperscaler on-demand). **For a P2P host, the relevant benchmark is the Vast/RunPod-Community tier, which sits about 25–40% below SDH100RT and Ornn for H100s.**

### 2.3 Trends, 2023 → November 2026

#### 2.3a H100 (best-documented series)

| Period | Hyperscaler | Neocloud | Marketplace / short-term | Source |
|---|---|---|---|---|
| Mid-2023 | ~$7.8 (Aug–Dec 2023 median $7.76) | – | ~$8 at peak scarcity (short-term) | [C] Silicon Data; [S] Latent Space, coloprice |
| Jan–May 2024 | $7.92 | – | $3–5, falling | [C] SD; [S] coloprice |
| Jun–Dec 2024 | $9.34 | $2.99 | **$2.58** | [C] SD |
| Jan–May 2025 | $8.96 | $3.50 | $2.29 | [C] SD |
| Jul–Dec 2025 | $6.26 (AWS cut P5 by ~44% in June 2025) | $3.33 | **$1.95**; 1-year contract low **$1.70** (Oct 2025) | [C] SD, SemiAnalysis |
| Mar 2026 | $7.40–7.52 (SD hyperscaler index) | – | 1-year contract $2.35 | [C] SD, SemiAnalysis |
| Nov 2026 | AWS $6.88; GCP $11.07; Azure $12.29 | RunPod Secure $4.39; Lambda $4.59; Nebius $4.50 | SDH100RT $3.10; Ornn $3.29; Vast median $2.30–2.37; RunPod Community $2.69 | [C] |

Year-on-year change in the marketplace H100 price:
- **2H 2024 → 2H 2025: −24%.**
- **Nov 2025 → Nov 2026:** +32% on the GetDeploying median, +40% on the SemiAnalysis 1-year contract (Oct–Mar), and about +20% on Vast ($1.95 → $2.37, different methods).
- From the 2023 scarcity peak to the 2025 trough, the short-term price fell ~75%, about −45% a year. That was a post-launch normalization, not a steady-state decay rate.

#### 2.3b Older classes (approximate; marketplace tier unless noted)

| GPU (launch year) | 2023 | 2024 | 2025 | Nov 2026 | Approx. annual change, 2023→2025 | Nov 2025 → Nov 2026 |
|---|---|---|---|---|---|---|
| **A100 80GB** (2020) | Marketplace ~$1.0–1.5 [E]; neocloud ~$1.3–1.9 [E] | ~$0.9–1.3 [E] | ~$0.6–0.9 [E]; floor $0.34 (Nov 2025, GetDeploying) [C]; Lambda $1.79 [S] | Vast $0.73–0.95 (occupied SXM $1.05); Ornn $1.04; SDA100RT $1.64; RunPod Community $1.19–1.39; Lambda $3.19 [C] | **−20 to −30%/yr** [E] | GetDeploying median **+14%** ($1.70 → $1.93) [C]; floor $0.34 → $0.77; Lambda **+78%** |
| **RTX 4090** (Oct 2022) | ~$0.50–0.75 [E] | ~$0.35–0.45 [E] | ~$0.30–0.45 [E]; provider median $0.52, floor $0.18 (Nov 2025) [C] | Vast median **$0.53** [C]; Mar 2026 Vast average $0.35 [S, DeployBase]; RunPod Community $0.34; provider median $0.46 [C] | **−20 to −25%/yr** [E] | Provider median **−12%**; **floor +83%** ($0.18 → $0.33); Vast vs March 2026 about +50% (different methods) |
| **RTX 3090** (2020) | ~$0.25–0.35 [E] | ~$0.20–0.25 [E] | ~$0.18–0.22; provider median $0.21 (Nov 2025) [C] | Vast **$0.23**; RunPod Community $0.22; Salad $0.09–0.20 [C] | **−10 to −15%/yr** [E] | **+4%** (flat) [C] |
| **V100** (2017) | Marketplace ~$0.20–0.30 [E]; AWS $3.06 [C] | ~$0.15–0.25 [E] | ~$0.10–0.15 [E]; floor $0.14 [C] | Vast **$0.093** (p25 $0.067); Lambda $0.79 (was ~$0.50–0.55 [E]); AWS still $3.06 [C] | **≈ −30%/yr** marketplace [E] | Marketplace flat at the floor; the hyperscaler price has not moved since 2017 |
| H100 (2022/23), for reference | ~$8 peak | $2.6–3.0 | $1.95–3.3 | $2.3–3.3 | −45%/yr from the scarcity peak | **+20 to +40%** |

Why the 2023–2024 consumer figures are only estimates: the Wayback Machine was blocked from this sandbox, and the shared web-search budget ran out mid-task, so I could not pull dated archive snapshots. Treat every [E] cell as ±30%.

#### 2.3c How fast older GPUs decay after a new generation ships

- **Timeline:**
  - Blackwell B200 reached volume in 1H 2025.
  - Blackwell Ultra (B300/GB300) ramped from 2H 2025 through 2026. It is now listed at RunPod ($6.94–8.99), Nebius ($9.50), Crusoe ($8.96 → $9.90) and Together ($11.49).
  - Vera Rubin appears on Crusoe's price list as "contact sales" and in GetDeploying's dataset (slug `nvidia-vera-rubin`), but it is "not shipping in volume." NVIDIA told customers that Grace Blackwell and Vera Rubin servers shipping in early 2027 will cost >15% more (Bloomberg, 22 Aug 2026, via Akash) [S].
- **What happened to the H100 when Blackwell volume arrived (2025):** hyperscaler H100 on-demand prices reset by 26–54% by region (Q1 2025 → Q3 2026), and marketplace H100s fell from $2.29 to $1.95 (−15%) within about two quarters [C, Silicon Data].
- **Then the 2026 shortage reversed this for every generation at once.** Drivers named by sources:
  - Agentic and inference demand.
  - TSMC CoWoS packaging booked to mid-2027.
  - DRAM and HBM prices up multiples (TrendForce: server DRAM +13–18% quarter-on-quarter in Q3 2026).
  - NVIDIA shifting wafers away from the H100.

  SemiAnalysis: "higher rental rates extend the economic useful life of existing GPUs," and H100s are being renewed "at the exact same rate they were signed at 2–3 years ago."
- **Cross-sectional vintage decay** (Vast medians, Nov 2026) [C, derived]:

  | Series | Ratio between neighbours |
  |---|---|
  | RTX 5090 (2025) $0.71 → 4090 (2022) $0.53 → 3090 (2020) $0.23 → 2080 Ti (2018) $0.08 | 0.75, 0.43, 0.35 per ~2-year generation |
  | B200 ~$8.75–10 → H100 $2.30–3.30 → A100 $0.73–1.05 → V100 $0.09 | The step down to Volta is a cliff (0.1x) |

  Volta and Pascal have 16 GB of memory, no BF16, and were dropped by CUDA 13 (August 2025, from background knowledge; not re-verified today).
- **Rule of thumb for modelling [E]:**
  - In a normal (non-shortage) market, a GPU's rental price drops ~25–40% in the 12–18 months after its successor reaches volume.
  - It then declines ~15–25% a year toward a floor of power + hosting + host margin.
  - Once software support ends, demand falls away regardless of price.
  - In a shortage market, as in 2026, all generations reprice upward together. Older and VRAM-poor cards move least.

### 2.4 Forecast, 2027–2028

| Source | View | Credibility |
|---|---|---|
| SemiAnalysis (Mar 2026 newsletter) | "GPU rental pricing is more likely to continue rising than falling"; on-demand sold out across types; Blackwell lead times into mid-2026 | High (survey- and transaction-based), but dated March 2026 |
| Silicon Data forward curve (13 Nov 2026) | H100 6-month implied forward $2.83 vs $3.10 spot (**−9% in 6 months ≈ −17% annualized**). B200 12-month forward $5.03 vs $5.69 spot (7 Sep), −12% | High (market-implied), but short horizon |
| NVIDIA via Bloomberg (22 Aug 2026) | GB/VR server prices up >15% for early-2027 shipments; The Information reported ~17% | High. Higher replacement cost props up the value and rental rates of the installed base |
| TrendForce (via Akash) | Server DRAM up 13–18% quarter-on-quarter in Q3 2026; HBM contract prices up substantially in 2027 | High (on the input-cost side) |
| Computestacker / Spheron / GPUnex [S] | HBM and CoWoS shortage lasts at least through 1H 2027; relief late 2027–2028 | Medium (vendor blogs) |
| Coloprice [S] | Base case: H100 holds $2–3 through 2026, then grinds toward "power-plus-margin" $1.00–1.50 in 2027–28 as each B200 displaces ~2.5–3 H100s of demand and expiring 2023–24 reservations release capacity | Medium |
| Akash [S] | Newer-hardware rents ~+10–20% in 2027 (its own modelling) | Low–medium (vendor) |

**Assumptions to use in a 3-year payback model** (annual change in renter $/GPU-hr from Nov 2026 levels; apply to the specific GPU model bought):

| Scenario | 2027 | 2028 | 2029 | ≈ Average/yr | Cumulative after 3 years | Narrative |
|---|---|---|---|---|---|---|
| **Bull** | 0% | −5% | −10% | ≈ −5% | ≈ −15% | The shortage persists through 2027 and Rubin is supply-limited. Older cards are re-rated like the H100 in 2026 |
| **Base** | −10% | −20% | −20% | ≈ −17% | ≈ −42% | The forward curve plays out. Supply relief from late 2027 brings a return to normal vintage decay |
| **Bear** | −30% | −30% | −30% | ≈ −30% | ≈ −66% | A replay of 2024–25 (−24% in a year for marketplace H100s, $8 → $2 for short-term H100s). Rubin volume plus expiring contracts flood the secondary market, and older consumer cards lose demand |

Two adjustments. For cards already near the power floor (V100, P40/P100, RTX 3080, A4000), cap the price decline at about −10%/yr but cut occupancy by 10–20 points a year. For RTX 4090 and 5090, add a bear-case risk that 2025-generation 32 GB consumer cards cannibalize demand.

### 2.5 Price per unit of capability (Vast.ai median, 14 Nov 2026)

Spec values are from NVIDIA datasheets, entered from background knowledge. "Dense FP16 tensor" is the rate without sparsity; for GeForce cards it is the FP16-accumulate rate, and FP32-accumulate is half of that.

| GPU | VRAM (GB) | Dense FP16 TFLOPS | Memory bandwidth (TB/s) | Vast median $/hr | RunPod Community $/hr | ¢ per GB-VRAM-hr | $ per 100 TFLOP-hr | $ per TB/s-hr | Vast occupied share* |
|---|---|---|---|---|---|---|---|---|---|
| B200 | 180 | 2,250 | 8.0 | 9.99 | 5.98 | 5.55 | 0.44 | 1.25 | 65% |
| H200 | 141 | 989 | 4.8 | 4.61 | 3.59 | 3.27 | 0.47 | 0.96 | 64% |
| H100 SXM | 80 | 989 | 3.35 | 2.37 | 2.69 | 2.96 | **0.24** | 0.71 | 83% |
| H100 PCIe | 80 | 756 | 2.0 | 2.67 | 1.99 | 3.34 | 0.35 | 1.34 | 78% |
| A100 80GB SXM | 80 | 312 | 2.04 | 0.95 | 1.39 | **1.19** | 0.30 | **0.47** | 70% |
| A100 80GB PCIe | 80 | 312 | 1.94 | 0.73 | 1.19 | **0.91** | 0.23 | **0.38** | 69% |
| L40S | 48 | 362 | 0.86 | 0.60 | 0.79 | 1.25 | **0.17** | 0.69 | 71% |
| RTX PRO 6000 (WS) | 96 | ~504 | 1.79 | 1.47 | 1.69 | 1.53 | 0.29 | 0.82 | 71% |
| RTX 6000 Ada | 48 | 364 | 0.96 | 0.67 | 0.74 | 1.40 | 0.18 | 0.70 | 82% |
| RTX A6000 | 48 | 155 | 0.77 | 0.44 | 0.33 | **0.92** | 0.28 | 0.57 | **83%** |
| A40 | 48 | 150 | 0.70 | 0.60 | 0.35 | 1.25 | 0.40 | 0.86 | 68% |
| RTX 5090 | 32 | 419 | 1.79 | 0.71 | 0.69 | 2.22 | 0.17 | **0.40** | 60% |
| RTX 4090 | 24 | 330 | 1.01 | 0.53 | 0.34 | 2.21 | **0.16** | 0.52 | 73% |
| RTX 3090 | 24 | 142 | 0.94 | 0.23 | 0.22 | **0.96** | **0.16** | **0.25** | 68% |
| RTX A5000 | 24 | 111 | 0.77 | 0.23 | 0.16 | 0.96 | 0.21 | 0.30 | 61% |
| RTX A4000 | 16 | 77 | 0.45 | 0.10 | – | 0.60 | 0.12 | 0.21 | 57% |
| V100 16GB | 16 | 125 | 0.90 | 0.09 | – | 0.58 | 0.07 | 0.10 | 65% |
| T4 | 16 | 65 | 0.32 | 0.14 | – | 0.86 | 0.21 | 0.43 | 55% |
| P100 | 16 | 19 (no tensor cores) | 0.73 | 0.09 | – | 0.58 | 0.49 | 0.13 | 42% |
| P40 | 24 | 0.18 (FP16 crippled) | 0.35 | 0.11 | – | 0.45 | n/m | 0.31 | n=5 |

\*Occupied share = the fraction of the model's listed machines flagged not rentable (rented) in the 14 Nov snapshot. It is a point-in-time listing share, not time-weighted utilization, and it is approximate. Reference points: RTX 3080 54%, 2080 Ti 47%, RTX 5080 62%.

Reading the table:
- **Renters pay for VRAM first, then bandwidth, then FLOPs.** The cards with the highest occupancy are VRAM-rich and cheap per GB: A6000 (48 GB at $0.44, 83% occupied), RTX 6000 Ada (82%), H100 SXM (83%), RTX 4090 (73%), and the A100 80GB (~70%, under 1.2¢ per GB-hr).
- **Cards with 16 GB or less are the weakest group** (A4000 57%, T4 55%, RTX 3080 54%, P100 42%), even though they look "cheap" per FLOP.
- **The RTX 3090 is the value standout among cards that can be bought used:** 24 GB at $0.23/hr is under 1¢ per GB-hr and $0.25 per TB/s-hr, the best bandwidth-per-dollar after the V100. It stays rented for LLM inference and fine-tuning at 68% occupancy, with 374 machines listed.
- **The V100 looks cheapest on every metric but is a stranded asset.** It has 16 GB, no BF16, has lost CUDA 13 support, and at ~300 W its power alone costs $0.03–0.05/hr, which is a third to a half of the $0.09 rent.

### 2.6 Geography: do marketplace prices differ by region?

**Vast.ai, 14 Nov 2026** [C, my pull; available and occupied listings combined; n = machines]:

| GPU | North America | Europe | Asia | LATAM |
|---|---|---|---|---|
| RTX 3090 | 0.213 (138) | 0.259 (155) | 0.200 (55) | **0.140 (13)** |
| RTX 4090 | 0.582 (96) | 0.533 (61) | 0.467 (47) | 0.467 (1) |
| RTX 5090 | 0.720 (257) | 0.800 (245) | 0.560 (149) | **0.520 (4)** |
| RTX A6000 | 0.420 (20) | 0.467 (20) | 0.427 (5) | 0.400 (1) |
| A100 SXM4 | 0.800 (49) | 1.067 (34) | 1.147 (6) | – |
| H100 SXM | 2.333 (7) | 2.867 (15) | 1.840 (13) | – |
| RTX A4000 | 0.107 (25) | 0.107 (32) | 0.093 (24) | 0.089 (1) |
| V100 | 0.093 (84) | 0.156 (14) | 0.093 (3) | – |

Host profile by region:

| Region | Machines (of ~2,470 unique) | Median upload (Mbps) | Median reliability score |
|---|---|---|---|
| North America | 1,059 | 911 | 0.994 |
| Europe | 812 | 914 | 0.993 |
| Asia | 490 | 615 | 0.994 |
| LATAM | **32 (1.3%)** | **522** | **0.985** |

LATAM hosts in the sample were in Argentina (8), Brazil (15), Mexico (6), Chile (1) and **Ecuador (1 RTX 3090 host at $0.199, rented)**. None were in Colombia or Venezuela. Almost all LATAM listings are RTX 3080/3090/4090/5090 plus one Brazilian 8×H200 at $7.24.

**Other regional evidence:**
- **Hyperscalers price regionally** [C, Vantage]. AWS São Paulo (sa-east-1) against us-east-1:
  - H100 p5 $11.56 vs $6.88 (+68%).
  - A100 p4d $4.44 vs $2.74 (+62%).
  - A10G +70%, T4 +69%.
  - Frankfurt is about +25%; Tokyo +25–45%.
  - Azure Brazil South: A100 80GB $8.19 vs $4.10/GPU (2.0x).
- **Silicon Data (Q3 2026):** non-hyperscaler H100 ranged only **$2.00–3.30** across seven regions, against $4.80–6.10 for hyperscalers. The hyperscaler premium fell from ~250% (early 2025) to ~120%. LATAM is not covered.
- **Silicon Data (Jan 2026, 2025 data):** buyers in São Paulo or Riyadh "may pay 3–4x" a Chicago peer for local capacity (an H100 in São Paulo at ~$9/hr vs Texas $2.50). That describes *local buyer-side* cloud prices, not P2P host prices.

**Why prices differ:**
1. P2P marketplace demand is global and price-sorted, so asking prices converge across regions. Hosts outside the US and EU discount by 10–35% to make up for latency to US and EU users, thinner bandwidth, lower reliability scores, and data-residency or compliance preferences (some renters filter for US/EU or "datacenter" hosts).
2. Cheap power in parts of Asia and LATAM lets hosts accept lower asks.
3. Hyperscaler and local-cloud regional premiums reflect import duties, power and facility costs, thinner competition and less liquid markets. A LATAM host selling into a global marketplace cannot capture these premiums. Selling locally, for example to Brazilian or Colombian enterprises, is a different business with different pricing.

---

## 3. Implications for the LATAM used-hardware rental business

1. **Benchmark against the marketplace tier.** A used 3090, 4090, A6000 or A100 in Colombia or Ecuador listed on Vast, RunPod Community or Salad will earn roughly the Vast median *minus a LATAM discount*. Hyperscaler or neocloud prices are not the benchmark. Realistic renter-side prices today:

   | GPU | Renter price/hr |
   |---|---|
   | RTX 3090 | $0.14–0.23 |
   | RTX 4090 | $0.34–0.53 |
   | RTX A6000 | $0.33–0.44 |
   | A100 80GB | $0.73–1.05 |
   | V100 | $0.07–0.09 |

   As a ceiling, gross renter revenue per GPU-year at 60% occupancy, before platform fees, power and bandwidth, is about:

   | GPU | Gross revenue per GPU-year |
   |---|---|
   | RTX 3090 | $1,200 |
   | RTX 4090 | $2,800 |
   | RTX A6000 | $2,300 |
   | A100 80GB | $5,000 |
   | V100 | $490 |

   [E, derived as price × 8,760 hours × 0.6.]
2. **Do not model today's prices as flat.** November 2026 is a cyclical high, driven by a shortage. Use the base case (≈ −17%/yr, ≈ −42% over 3 years) for the central payback and require the project to survive the bear case (≈ −30%/yr). A hardware purchase that only pays back at flat prices is a bet on the shortage lasting.
3. **The same shortage inflates the purchase side.** Memory-driven price rises (the RTX 5090 aftermarket roughly doubled, per Computestacker [S]) mean used GPUs in LATAM may *not* be cheap relative to rental yields right now. The business case depends on the local price gap. Other agents cover that; check their findings against these yields.
4. **Buy VRAM, not FLOPs.** Prefer 24 GB+ Ampere or newer cards (3090, A5000/A6000, A40, A100, 4090). Avoid cards with 16 GB or less (A4000, T4, 3080) and Volta/Pascal (V100, P40, P100). Those older cards are at or near the power-cost floor, have lost CUDA 13 support, and show the lowest occupancy.
5. **Host quality matters as much as price.** LATAM hosts already price 25–35% below North America and Europe, partly because of lower upload bandwidth (522 vs ~910 Mbps median) and reliability (0.985 vs 0.993–0.994). Symmetric fiber of at least 1 Gbps, high uptime and a datacenter-verified listing are what close the gap. Expect a structural 10–25% discount even so [E].
6. **Daily price volatility is high** (Ornn H100 ±5–10% day to day; the cheapest 4090 listing moved $0.18 → $0.33 within a year). Ask prices are host-set, so a LATAM host can undercut to win occupancy. The trade-off between price and occupancy is a model variable.

---

## 4. Confidence and gaps

| Item | Confidence | Note |
|---|---|---|
| Current list prices (RunPod, Lambda, CoreWeave, Nebius, Crusoe, Together, Salad, AWS, Azure) | High | Primary pages or provider price APIs via Vantage, 12–14 Nov 2026 |
| Vast.ai medians and regional splits | Medium–high | Live API, ~2,470 machines. A one-day snapshot of *asking* prices, not transacted prices. Small n for H100 SXM (36), LATAM (32) and P40 (5). The API caps results at 64 per query; I paginated by price |
| Vast "occupied share" | Medium–low | Point-in-time listing flag, not utilization; `rentable=false` may include unlisted or maintenance machines |
| Index levels (Ornn, Silicon Data) | High as published | They disagree with each other by method (H200 $6.73 vs $3.60). Silicon Data's pages also show stale FAQ values ($2.53, $1.29, $5.45) that conflict with their own charts; I used the dated chart values |
| GCP prices | Medium | From GetDeploying (secondary); GCP's page is rendered in JavaScript |
| 12-month trend (GetDeploying dataset) | Medium | Same method over time, but provider mix changes (A5000 +234% and V100 swings are composition artefacts). The dataset only starts Nov 2025 for most models |
| 2023–2025 consumer-GPU and A100 marketplace history | **Low** | Estimates from background knowledge. The Wayback Machine was blocked and the shared web-search budget (200 calls) ran out mid-task. Treat as ±30% |
| SemiAnalysis index | Medium | Public dashboard only showed values through Mar/Apr 2026 |
| SF Compute, TensorDock, Hyperbolic | Low | SF Compute is login-gated; TensorDock and Hyperbolic show only "from" prices |
| 2027–28 forecast | Low–medium | Only the Silicon Data forward curve (6 months) and SemiAnalysis are rigorous; the rest are vendor blogs. The base/bear/bull figures are my synthesis |
| GPU specs | Medium–high | From NVIDIA datasheets via background knowledge (RTX PRO 6000 FP16 derived as ~504 TFLOPS dense) |
| CUDA 13 dropping Maxwell/Pascal/Volta | Medium | Background knowledge (Aug 2025 release); not re-verified today |

Next steps if more budget is allowed: pull the GetDeploying `/api/gpu-price-history` series back to mid-2024 (paid API); take repeated Vast snapshots over 2–4 weeks to measure real occupancy and price dispersion; check Clore.ai, io.net and Akash host-side prices for consumer GPUs.

---

## 5. Sources (all accessed 2026-11-14 unless noted)

**Live data and APIs (primary):**
- Vast.ai public offer search API: https://console.vast.ai/api/v0/bundles/ (paginated pull of 38 GPU models, available and occupied listings, ~12:00 UTC 14 Nov 2026). Scratch outputs: `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent06/data/vast_combined_2026-11-14.txt`
- Ornn OCPI: https://data.ornn.com/markets ; https://data.ornn.com/markets/h100 ; https://data.ornn.com/api/public-index/daily-index/all (settled 13 Nov 2026)
- GetDeploying GPU price dataset (CC BY 4.0, weekly, updated 14 Nov 2026): https://getdeploying.com/dataset/gpu-prices/weekly.csv ; https://getdeploying.com/dataset/gpu-prices ; https://getdeploying.com/gpu-price-trends ; https://getdeploying.com/gpu-price-index ; https://getdeploying.com/gpus ; https://getdeploying.com/gpus/nvidia-h100 ; https://getdeploying.com/google-cloud
- Vantage EC2 and Azure instance datasets: https://instances.vantage.sh/instances.json ; https://instances.vantage.sh/azure/instances.json

**Provider pricing pages (primary):**
- RunPod: https://www.runpod.io/pricing (JSON-LD dateModified 2026-11-12)
- Lambda: https://lambda.com/pricing (prices effective 16 Nov 2026); change log: https://pricingsaas.com/companies/lambdalabs and https://pricingsaas.com/companies/lambdalabs/diffs/2026W46
- CoreWeave: https://www.coreweave.com/pricing
- Nebius: https://nebius.com/prices
- Crusoe: https://www.crusoe.ai/cloud/pricing (current and 1 Dec 2026 prices)
- Together AI: https://www.together.ai/pricing
- Voltage Park: https://www.voltagepark.com/pricing
- Hyperbolic: https://www.hyperbolic.ai/marketplace
- TensorDock: https://tensordock.com/
- SaladCloud: https://salad.com/pricing

**Indices and analysts:**
- Silicon Data:
  - Index pages: https://www.silicondata.com/products/silicon-index/h100 ; .../a100 ; .../b200 ; .../h200 ; https://www.silicondata.com/products/forward-curve ; https://www.silicondata.com/llms.txt
  - Blog: https://www.silicondata.com/blog/h100-rental-price-over-time ; https://www.silicondata.com/blog/h100-rental-prices-by-region-q3-2026 ; https://www.silicondata.com/blog/h200-vs-h100-rental-prices-may-july-2026 ; https://www.silicondata.com/blog/b200-rental-price-august-2026-update ; https://www.silicondata.com/blog/geography-of-gpu-pricing-a100-vs-h100 ; https://www.silicondata.com/blog/gpu-market-dynamics-a100-h100
- SemiAnalysis: https://gpu-index.semianalysis.com/ ; https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
- computeprices.com: https://computeprices.com/ ; https://computeprices.com/providers/runpod/gpus/rtx3090 ; https://computeprices.com/providers/sf-compute
- Implicator.ai (tracker disagreement, CME futures): https://www.implicator.ai/gpu-price-trackers-disagree-8x-cme-compute-futures/
- S&P Global Platts subscriber note (returned 403; title only): https://www.spglobal.com/energy/en/pricing-benchmarks/our-methodology/subscriber-notes/110526-platts-to-launch-us-gpu-compute-prices-nov-23

**Secondary / vendor blogs (used for context and forecasts):**
- Thunder Compute: https://www.thundercompute.com/blog/ai-gpu-rental-market-trends
- Akash: https://akash.network/the-bid/h100-rental-price-2026-cost-per-hour/ ; https://akash.network/the-bid/blackwell-vera-rubin-gpu-prices-2027/ (cites Fortune/Bloomberg 22 Aug 2026 and TrendForce)
- Coloprice: https://coloprice.com/guides/h100-rental-prices/
- Computestacker: https://computestacker.com/insights/gpu-capacity-crunch-rental-prices/
- Latent Space, "$2 H100s: How the GPU Rental Bubble Burst" (Oct 2024; via search excerpts only): https://latent.space/p/gpu-bubble
- DeployBase, Vast.ai prices as of 22 Mar 2026: https://deploybase.ai/articles/vast-ai-gpu-cloud-pricing-complete-guide-vs-hr-for-every-gpu
- Vast.ai live pricing guide (competitor prices checked 20 Jul 2026): https://vast.ai/article/how-much-does-it-cost-to-rent-a-gpu-in-the-cloud-live-pricing-guide

**Scratch work:** `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent06/` (scripts/ and data/)

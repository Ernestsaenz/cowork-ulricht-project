# 03 — Consumer GPU-sharing apps that pay individuals, plus the mining baseline

**Agent 03 · Research date: 2026-11-14 · Scope:** SaladCloud/Salad "chopping", other consumer node apps (Nosana, Golem, Theta EdgeCloud, Gaimin, Livepeer, Hivenet, Kryptex, 2025–26 newcomers), the GPU-mining opportunity cost, and net monthly income per consumer GPU.

**How the data was gathered:** Most numbers come from public machine-readable endpoints, pulled live on 2026-11-14:
- Salad's own weekly earnings dataset (`cdn.salad.com/site-data/earning-rates.json`, window 2026-11-07 to 2026-11-13) and its demand-monitor API.
- Nosana's market API.
- Golem's stats API.
- The Livepeer explorer's embedded data.
- Kryptex per-GPU daily revenue series.
- NiceHash and WhatToMine APIs.
- CoinGecko prices.

Labels used throughout:
- **CONFIRMED**: taken from a dated primary source.
- **INFERENCE**: my own calculation or interpretation.
- **ESTIMATE**: an assumption, such as power draw.

*Limitation:* the shared web-search budget ran out partway through. Some secondary checks could not be done: country-by-country PayPal lists, Nosana's geographic rules, and Theta's reward rates. They are listed as gaps in §4.

---

## 1) Executive summary

- **Salad pays individuals real money only for modern RTX cards.** Average chef earnings for the week of 7–13 Nov 2026 (CONFIRMED, Salad dataset) are below. The figures include idle hours.

  | GPU | $/hour | $/day | $/month gross |
  |---|---|---|---|
  | RTX 5090 | 0.376 | 9.01 | ~270 |
  | RTX 4090 | 0.272 | 6.53 | ~196 |
  | RTX 5080 | 0.169 | 4.06 | ~122 |
  | RTX 4080 | 0.130 | 3.11 | ~93 |
  | RTX 3090 | 0.115 | 2.75 | ~82 |
  | RTX 4070 | 0.065 | 1.56 | ~47 |
  | RTX 3080 | 0.058 | 1.40 | ~42 |
  | RTX 3070 | 0.039 | 0.93 | ~28 |
  | RTX 3060 Ti | 0.036 | 0.87 | ~26 |
  | RTX 3060 | 0.031 | 0.73 | ~22 |
  | RTX 4060 | 0.028 | 0.68 | ~20 |

  Utilization is high right now: 81–97% of chopping hours had a container job running.
- **Salad's chef rate is exactly 80% of the SaladCloud list price at every priority tier** (INFERENCE: the demand monitor's minimum and maximum earning rates equal 0.8 × the batch and high prices on salad.com/pricing for every class checked). For the RTX 4090, customers pay $0.16–0.44/h and chefs earn $0.128–0.352/h.
- **Net income after electricity on Salad** (ESTIMATE, running 24/7 at assumed wall power):

  | GPU | Net $/month @ $0.05/kWh | @ $0.10/kWh | @ $0.20/kWh |
  |---|---|---|---|
  | RTX 4090 | ~181 | ~166 | ~135 |
  | RTX 3090 | ~70 | ~58 | ~33 |
  | RTX 3080 | ~31 | ~19 | ~−3 |
  | RTX 3060 | ~15 | ~8 | ~−6 |

  Cards at or below the RTX 3080 break even at about $0.16–0.19/kWh.
- **Salad's structure is a poor fit for a server farm.** Salad uses **one GPU per machine** and needs Windows with WSL2, 16 GB RAM (32 GB recommended) and 70 GB free on C:. Its terms ban VMs and machines you don't own or control. Many machines on one account are allowed, but each person has a **$1,000/day withdrawal cap** (CONFIRMED, Salad support and Chef ToS of 2026-09-28). Nosana is likewise "1 GPU per PC", on native Linux. **Old data-center GPUs (Tesla K80/P40/V100 and similar) earn nothing on either app.** Pascal-era GeForce cards earn $9–18 a month on Salad.
- **These markets are small.** The approximate payout pools are below. A 100 × RTX 4090 farm would earn about $20k a month on Salad, roughly 11% of Salad's entire chef payout pool. That share invites dilution.

  | Network | Payout pool | Status |
  |---|---|---|
  | Salad | ~$176k/month to all chefs | ESTIMATE, from RNP-023's illustrative figures |
  | Nosana | ~$50k–160k/month to hosts | INFERENCE, from live running jobs |
  | Livepeer | ~$23.6k/month in fees across 100 orchestrators | CONFIRMED, explorer |
  | Golem | ~$1.9k/month across the whole network, with about 3 GPU providers online | CONFIRMED, stats API |

- **Nosana pays hosts in NOS, priced in USD.** Host rates per hour (CONFIRMED, API): 4090 $0.364, 5090 $0.455, 3090 $0.174, 4080 $0.145, 3080/4070 $0.087, 3060 $0.044. The network fee is 10%. Utilization is unverified: 973 jobs show as "running", but 685 of them started more than 30 days ago and are probably stale. At an assumed 50% job time, a 4090 grosses about $131 a month.
- **The mining floor depends on a single coin, Pearl (PRL).** Pearl is a matrix-multiplication "AI-compute" PoW coin; mainnet launched on 27 Apr 2026. Kryptex's 7-day average gross per day: RTX 4090 $6.00, 5090 $6.98, 4080 $3.72, 3090 $2.57, 3080 $2.31, 3070 $1.51, 3060 $0.97 (CONFIRMED). Those figures are down about 28% from the 30-day average and still falling. **Without Pearl**, NiceHash pays $0.08–0.36 a day per card, so mining loses money even at $0.05/kWh. Before Pearl (Nov 2025–May 2026), a 4090 grossed $0.42–0.71 a day on Kryptex.
- **Salad and mining are roughly at parity today.** For a 4090, Salad pays $196 a month gross against $180 from mining Pearl. Older cards (3060/3070/4060) earn more mining Pearl than on Salad: $29–45 against $20–28 gross a month.
- **The other apps are not viable income sources for this business.** Theta's edge nodes pay TFUEL, now $0.0071, at unpublished rates. Gaimin's GMRX ($7.7e-6) rewards gaming activity, not GPU compute. On Livepeer, the median active orchestrator earned about 0.004 ETH (≈$8) in fees over 30 days, and most rewards follow LPT stake, not GPUs. Hivenet runs its own GPUs. Kryptex's GPU rental is a closed beta drawing on mining farms. Gonka needs at least 320 GB of VRAM per node. Inference.net (formerly Kuzco) is now an API seller only.
- **Vast.ai reference point** (a ballpark snapshot; another agent covers Vast in depth): median listed renter prices are about $0.07/h for a 3060, $0.20 for a 3090, $0.49 for a 4090 and $0.54 for a 5090. These are list prices before Vast's fee and idle time. At about 50% rented hours, Vast hosts land roughly where Salad's all-hours average sits.

---

## 2) Detailed findings

### 2.1 SaladCloud / Salad app ("chopping")

#### 2.1.1 What customers pay: SaladCloud list prices, USD per GPU-hour
Source: salad.com/pricing, fetched 2026-11-14. The page shows no effective date and is © 2026.

| GPU (VRAM) | High | Medium | Low | Batch (lowest) |
|---|---|---|---|---|
| RTX 5090 (32 GB) | 0.600 | 0.483 | 0.367 | 0.250 |
| RTX 4090 (24 GB) | 0.440 | 0.347 | 0.253 | 0.160 |
| RTX 5080 (16 GB) | 0.320 | 0.263 | 0.207 | 0.150 |
| RTX 4080 (16 GB) | 0.270 | 0.217 | 0.163 | 0.110 |
| RTX 5070 Ti (16 GB) | 0.270 | 0.213 | 0.157 | 0.100 |
| RTX 4070 Ti Super (16 GB) | 0.240 | 0.190 | 0.140 | 0.090 |
| RTX 3090 Ti (24 GB) | 0.220 | 0.180 | 0.140 | 0.100 |
| RTX 3090 (24 GB) | 0.200 | 0.163 | 0.127 | 0.090 |
| RTX 3080 Ti (12 GB) | 0.195 | 0.157 | 0.118 | 0.080 |
| RTX 4070 (12 GB) | 0.165 | 0.133 | 0.102 | 0.070 |
| RTX 3080 (10 GB) | 0.155 | 0.123 | 0.092 | 0.060 |
| RTX 4060 Ti (16 GB) | 0.140 | 0.120 | 0.100 | 0.080 |
| RTX 3060 / 3070 / 3070 Ti | not tiered on page | | | "from $0.015" |

**Chef's share (INFERENCE, exact match):** the demand-monitor API (`app-api.salad.com/api/v2/demand-monitor/gpu`, 2026-11-14 12:02 UTC) shows each class's minimum and maximum chef earning rate. These equal exactly 0.8 × the Batch and High prices:

| GPU | Batch × 0.8 | Chef minimum | High × 0.8 | Chef maximum |
|---|---|---|---|---|
| RTX 4090 | 0.128 | 0.128 | 0.352 | 0.352 |
| RTX 5090 | 0.200 | 0.200 | 0.480 | 0.480 |
| RTX 3090 | 0.072 | 0.072 | 0.160 | 0.160 |
| RTX 3080 | 0.048 | 0.048 | 0.124 | 0.124 |

So the GPU-hour pass-through is **80%**.

Render proposal RNP-023 (dated 2026-03-26, approved) states it differently: chef rewards equal about **56% of SaladCloud container (SCE) revenue** and about 31% of gateway (SGS, bandwidth) revenue. After RENDER integration, Salad keeps 35%, 60% of SCE revenue is burned, and the Render Foundation gets 5%. CONFIRMED in RNP-023. The gap between 80% and 56% is probably revenue that isn't GPU-time, such as CPU/RAM, storage and discounts; this is not verified.

#### 2.1.2 What chefs actually earn by GPU
Source: Salad's own measured weekly dataset, `cdn.salad.com/site-data/earning-rates.json`, which feeds salad.com/earning-rates. Updated 2026-11-14T08:08Z; window 2026-11-07 to 2026-11-13, 7 days of data. CONFIRMED.

Salad's method, as stated on the page:
- The figure is everything machines earned (container jobs + bandwidth sharing + mining), divided by **every chopping hour, including hours with no job**.
- Only single-GPU machines that chopped at least 4 hours a day are included.
- p25–p75 is the "middle half of machines"; the page tells new chefs to "expect to start here".
- p99 is the "top chefs" (best 1%).
- "Work" is the share of chopping hours with a container job running.

| GPU | Mean $/h | p25 $/h | p75 $/h | p99 $/h | Job-hours | Mean $/day | Mean $/month (720 h) | p25 $/month |
|---|---|---|---|---|---|---|---|---|
| RTX 5090 | 0.376 | 0.336 | 0.407 | 0.615 | 97% | 9.01 | 270 | 242 |
| RTX 4090 | 0.272 | 0.245 | 0.294 | 0.360 | 97% | 6.53 | 196 | 176 |
| RTX 5080 | 0.169 | 0.163 | 0.181 | 0.304 | 97% | 4.06 | 122 | 117 |
| RTX 4080 SUPER | 0.139 | 0.130 | 0.146 | 0.232 | 97% | 3.33 | 100 | 94 |
| RTX 5070 Ti | 0.131 | 0.122 | 0.139 | 0.238 | 97% | 3.15 | 95 | 88 |
| RTX 4080 | 0.130 | 0.124 | 0.143 | 0.201 | 96% | 3.11 | 93 | 89 |
| RTX 3090 | 0.115 | 0.097 | 0.131 | 0.168 | 94% | 2.75 | 82 | 70 |
| RTX 4070 Ti SUPER | 0.111 | 0.105 | 0.117 | 0.179 | 97% | 2.65 | 80 | 75 |
| RTX 3090 Ti | 0.098 | 0.078 | 0.108 | 0.175 | 92% | 2.34 | 70 | 56 |
| RTX 3080 Ti | 0.072 | 0.058 | 0.083 | 0.184 | 91% | 1.74 | 52 | 42 |
| RTX 5070 | 0.065 | 0.056 | 0.074 | 0.153 | 93% | 1.57 | 47 | 40 |
| RTX 4070 | 0.065 | 0.057 | 0.071 | 0.099 | 95% | 1.56 | 47 | 41 |
| RTX 3080 | 0.058 | 0.049 | 0.066 | 0.097 | 92% | 1.40 | 42 | 36 |
| RTX 4060 Ti | 0.053 | 0.036 | 0.064 | 0.113 | 85% | 1.28 | 38 | 26 |
| RTX 3070 Ti | 0.045 | 0.035 | 0.050 | 0.101 | 88% | 1.07 | 32 | 25 |
| RTX 3070 | 0.039 | 0.030 | 0.045 | 0.096 | 83% | 0.93 | 28 | 22 |
| RTX 3060 Ti | 0.036 | 0.028 | 0.043 | 0.083 | 87% | 0.87 | 26 | 20 |
| RTX 3060 | 0.031 | 0.017 | 0.039 | 0.086 | 82% | 0.73 | 22 | 12 |
| RTX 4060 | 0.028 | 0.017 | 0.035 | 0.060 | 81% | 0.68 | 20 | 12 |
| RTX 2080 Ti | 0.047 | 0.040 | 0.054 | 0.084 | 91% | 1.12 | 34 | 29 |
| GTX 1080 Ti | 0.023 | 0.016 | 0.024 | n/a | 87% | 0.54 | 16 | 12 |
| GTX 1070 | 0.025 | 0.011 | 0.026 | n/a | 77% | 0.60 | 18 | 8 |
| GTX 1060 6 GB | 0.013 | 0.005 | 0.017 | n/a | 72% | 0.30 | 9 | 4 |
| AMD RX 9070 XT | 0.051 | 0.045 | 0.061 | n/a | 96% | 1.23 | 37 | 32 |

Notes:
- The live demand monitor (2026-11-14 12:02 UTC) rates demand **"High" for almost every RTX class**. RTX 4060 Ti, 5060 and RX 7900 XTX are "Moderate"; RTX A5000 is "Low", with a $0 average. CONFIRMED.
- Customer-side availability at High priority (`cdn.salad.com/site-data/availability.json`, 2026-11-14 11:06Z) shows how small the supply of top cards is: about 490 × 4090, 470 × 5090, 442 × 3090 and 526 × 5080. The headline is 5,829 NVIDIA GPUs with 8 GB or more. CONFIRMED.
- Salad's network-size claims vary:
  - "60,000 daily heartbeating GPUs" (RNP-023, Mar 2026; Salad blog, 7 Apr 2026).
  - 11k–16k+ daily active GPUs (salad.com marketing).
  - US and Canada hold 50–60% of nodes (Salad docs).

#### 2.1.3 How often a node gets work
- This week's job-hour share is **81–97%** for RTX 30/40/50 cards and **72–87% for 60-class and Pascal cards** (CONFIRMED, as above). This is unusually high; Salad's own text warns that at Low demand "you'll likely wait longer between jobs".
- High-priority jobs aren't preempted. Lower tiers can be preempted by higher-paying work, and nodes are reallocated when a container exits (Salad docs, priority pricing).
- Salad's 2025 test of 100 instances: 25% ran 7 days without interruption, and the average uptime per run was 60 hours (docs.salad.com, service-performance).
- **Survivorship bias:** the dataset only counts machines chopping at least 4 hours a day. Machines that quit because they earned nothing are excluded.

#### 2.1.4 Does it depend on country or region?
- **Container job rates do not vary by country.** The rate is set by the customer's priority tier (80% of list price) (INFERENCE from the API and pricing). Salad's earning-rates page and Chef ToS do not mention any country-based rate.
- **Customers can restrict a job to certain countries.** The SaladCloud API field `country_codes` reads: "Remove this field to permit nodes from any country." The allowed list includes co, ec and ve (CONFIRMED, API reference). Jobs pinned to US/EU nodes are invisible to a LATAM node. What share of demand is pinned is unknown. With 50–60% of nodes in the US and Canada, a LATAM node probably sees somewhat less work (INFERENCE).
- **Bandwidth-sharing income (Salad Gateway Service) does depend on country.** A server is provisioned in the requested country and nodes there are signalled to connect (Salad docs, SGS FAQ). Salad says bandwidth "carries a big share of the total on older and entry-level cards" (earning-rates page). For a LATAM residential IP, this part could be much higher or lower than the averages above; there is no data.
- **Requirements that matter in LATAM:**
  - Download speed of at least 20 Mbps (support page on container jobs).
  - Consumer upload is often only tens of Mbps (Salad docs).

#### 2.1.5 Supported countries (Colombia, Ecuador, Venezuela?)
- The Chef ToS (last updated 2026-09-28) excludes only users in "a country or territory subject to comprehensive United States sanctions" or on US restricted-party lists. Salad and its reward providers screen against sanctions lists (CONFIRMED). No eligible-country list is published. Salad says it has nodes in "180+/190+ countries".
- **Colombia and Ecuador** are not under comprehensive US sanctions, so they are eligible (INFERENCE).
- **Venezuela** is, to my knowledge, under a list-based OFAC program, not a comprehensive embargo. So it is probably eligible under the ToS wording (INFERENCE, **verify**: the US sanctions picture for Venezuela changed in 2026, and payout rails there are the practical problem).

#### 2.1.6 Payout methods
- **PayPal transfer, prepaid Visa/Mastercard and gift cards** (Steam, Discord, etc.) are in the Chef ToS §3, CONFIRMED. PayPal and prepaid-card country lists are on separate pages I could not retrieve; Venmo is US territories only.
- **RENDER tokens to a self-custody Solana wallet** (CONFIRMED, Salad support withdrawal-limit page: "No other direct crypto conversion is supported"). This is the result of the Salad × Render deal (RNP-023, approved; Salad blog, 2026-04-07). For Venezuela, the RENDER-to-stablecoin route is likely the only practical one (INFERENCE).
- **Coinbase-email payouts** are in progress: the Salad web app's code has "Add Coinbase Email" screens with the text "Coinbase email settings are not available yet" (INFERENCE, rollout status unknown).
- **Limits and conditions** (CONFIRMED):
  - Withdrawals are capped at **$1,000 per person per day** (the page writes "$1.000").
  - Points "have no cash value", appear within 5 business days, and expire after 12 months with no earnings.
  - ID and tax-ID checks are possible.
  - Salad sets rates "from time to time" and can terminate accounts without cause.

#### 2.1.7 Are farms allowed?
- **Many machines are allowed:** "Can I run Salad on multiple devices at once? Yes!… earnings will be combined" (Salad support).
- **Only one account per person:** multiple accounts are a ToS breach and can lead to a ban.
- **Neither ToS nor support mentions data centers, server farms or a machine cap.** Still, the ToS prohibits running on "a virtual machine or emulator, or on any computer you do not own or control, without the Company's written permission". It also prohibits misrepresenting hardware or location.
- **Technical limits:**
  - Salad uses **only one GPU per machine** (support: getting container jobs). Multi-GPU machines are counted separately in the stats.
  - The chef app is Windows + WSL2 (Salad Enterprise Linux inside WSL2).
  - A machine needs 16 GB RAM (32 GB recommended), 70 GB free on C:, and virtualization enabled.
- **Bottom line:** a "farm" on Salad means **many single-GPU Windows PCs**, not multi-GPU servers.

### 2.2 Other consumer node apps

| App | Who can supply | Host payout per GPU (CONFIRMED where stated) | Utilization / demand evidence | Payout currency | Geo / other constraints | Verdict for this business |
|---|---|---|---|---|---|---|
| **Nosana** (Solana) | RTX 30/40/50, A-series, A100/H100. Native Linux only; WSL2 being deprecated. "1 private key per GPU, 1 GPU per PC". At least 12 GB RAM and 256 GB NVMe. **At least 100 Mbps down and 50 Mbps up** (500/250 recommended) | Premium market $/h (API, 2026-11-14): 5090 0.455, 4090 0.364, 3090 0.174, 5080 0.182, 4080 0.145, 5070 0.136, 3080 0.087, 4070 0.087, 3070 0.073, 4060 0.058, 3060 0.044. Community markets are about 25% lower (3090 0.131, 3060 0.033). Host gets 1/1.1 of the job price (10% fee); 4090 job price is $0.40/h. Some markets add an "uptime reward" of up to $1.76/day (4090) or $2.18/day (5090); this reading comes from the API field name `max_usd_uptime_reward_per_day` (INFERENCE). Utilization target is 0.6–0.8 | 973 jobs show as "running" across all markets. Of these, 685 started more than 30 days ago despite 45–60 min timeouts (probably stale). 148 started within 24 hours, paying $72/h in total. Of all 973, 167 were in the 3090 Community market and 97 in the 4090 Premium market. Lifetime: 4.27 M jobs and **$2.55 M paid to hosts** (`/api/jobs/stats`). Run-rate is about $50k–160k a month network-wide (INFERENCE) | **NOS** (priced in USD, paid in token). NOS = $0.358; ATH $7.83 (Mar 2024) | No geographic rules found (gap). A secondary source (Solana Compass, via search) says Nosana opened a 2-month 4090/5090 provider campaign on 17 Sep 2026 ending around late Nov 2026 (LOW confidence) | The only alternative with meaningful demand. Same one-GPU-per-PC limit. At about 50% job time, a 4090 grosses about $131/month and a 3090 about $63/month |
| **Golem Network** | Any provider; GPU runtime "vm-nvidia" | No market rate. Whole-network provider earnings (GLM, `api2.stats.golem.network`): **230 GLM in 24 h (≈$22)** and **19,842 GLM in 30 days (≈$1,890)**, at GLM = $0.095 | **1,342 providers online, about 16k CPU cores, 0 GPUs** in the main runtime. **vm-nvidia (GPU) providers: 3 online** (7 and 30 days) | GLM | none | **Dead for GPU income.** Golem's GPU effort now runs through Salad: RNP-023 says "Golem tests began early 2026" |
| **Theta EdgeCloud (Edge Node)** | Anyone. Windows/macOS app or Linux Docker. 4 cores, 16 GB RAM, 5 Mbps; GPU optional | Rates not published. Payouts arrive monthly in the first week. Theta's *customer* prices for reference: 3090 $0.14/h, 4090 $0.26/h, 5090 $0.49/h | No public utilization data found | Token (TFUEL/THETA ecosystem). **TFUEL = $0.0071**, −99% from ATH | none stated | Unquantifiable and token-heavy. Not a business basis |
| **Gaimin** | Gamers via the Gaimin launcher | No GPU-compute payout visible. GMRX rewards are for "play, watch streams or step away from the keyboard" | n/a | **GMRX = $0.0000077**; market cap about $480k; 24 h volume about $2.4k | Swiss company | **Not viable** (token illiquid, no compute pay) |
| **Livepeer** (orchestrators) | Linux + NVIDIA (CUDA 12+). Must be in the **top-100 active set by LPT stake** | Network **24 h service payouts $805.8 against $30.4K in protocol rewards** (livepeer.org/compute). **30-day fees across all 100 active orchestrators: 12.35 ETH ≈ $23.6k.** Top orchestrator 4.78 ETH; **median 0.004 ETH (≈$8)** (explorer) | Fees are concentrated in a few AI/video operators. 66 of 100 had any fees in 30 days | ETH (fees) + LPT (inflation, goes to stake) | Entry stake for the 100th slot ≈ 1,676 LPT (≈ $1.9k at $1.15). Arbitrum gas needed | Income follows **stake and business development**, not GPU count. Not a passive GPU-rental channel |
| **Hivenet Compute** | Hivenet itself ("operated by Hivenet end-to-end"). RTX 5090 / RTX 6000 in France, UAE and US | No program paying individuals for GPUs found | n/a | n/a | n/a | **Not a supply channel** |
| **Kryptex** | Mining app/pool. "Rent our GPUs" is a **closed beta** that "utilizes the capacity of thousands of mining farms" | No published host payout for rental | n/a | Mining payouts in BTC, USDT, USDC (Solana) and others | n/a | Worth watching as a channel for mining-farm GPUs, but there are no numbers yet |
| **Pearl (PRL)**, 2026 newcomer | Any GPU with tensor cores, RTX 20 series and newer (Kryptex). "AI-compute" matrix-multiplication PoW; mainnet 2026-04-27 | See §2.3: 4090 ≈ $6.0/day gross, falling | Hashrate rush: Tom's Hardware reported the 5090 dropping from about $33.80 to $17.19 a day after launch; Kryptex now shows $6.37 | PRL, $1.53, mcap $579 M, 24 h volume $18 M | none | It sets today's floor, but its decay is steep |
| **Gonka** (Product Science) | Data-center class only: **at least 320 GB total VRAM per MLNode**. Listed GPUs: B300, B200, RTX PRO 6000, H200, H100, A100-80G | GNK token | n/a | GNK | n/a | **Excludes consumer GPUs** |
| **Inference.net** (formerly Kuzco) | — | The site now sells only an inference API (per-million-token pricing); no consumer-GPU contributor program is visible | — | — | — | **No longer a channel** |
| **Salad × Render (RENDER payouts)** | Same as Salad | Same as Salad | — | RENDER, $1.49 | — | Adds a crypto exit, useful for Venezuela |

(io.net, Akash, Clore.ai, TensorDock, RunPod and Vast are covered by other agents. One note in passing: CoinGecko shows Clore's CLORE token at $0.0015 on 2026-11-14. That is a reminder of the token-denomination risk on DePIN host income.)

### 2.3 Mining baseline (opportunity cost), November 2026

**A. Kryptex, most profitable coin per day.** Kryptex per-GPU daily revenue series (`kryptex.com/en/hardware/<gpu>`, "Last updated 13 Nov 2026"; latest data point 2026-11-14). Every target card's best coin over the last 30 days was **Pearl (PRL)**, sometimes Iron Fish. The revenue figures are gross USD; Kryptex's "profit" uses a very low implied power price, so I recomputed net myself.

| GPU | Kryptex W (tuned) | Today $/day | 7-day avg $/day | 30-day avg $/day | Pre-Pearl monthly range, Nov 2025–May 2026 ($/day) |
|---|---|---|---|---|---|
| RTX 3060 | 135 | 0.86 | 0.97 | 1.31 | 0.13–0.22 |
| RTX 3060 Ti | 125 | 1.11 | 1.25 | 1.70 | — |
| RTX 3070 | 125 | 1.35 | 1.51 | 2.06 | — |
| RTX 3080 | 250 | 2.07 | 2.31 | 3.16 | — |
| RTX 3090 | 320 | 2.25 | 2.57 | 3.43 | 0.31–0.54 |
| RTX 4060 | 115 | 1.03 | 1.13 | 1.57 | — |
| RTX 4060 Ti | 200 | 1.50 | 1.65 | 2.28 | — |
| RTX 4070 | 200 | 2.01 | 2.20 | 3.05 | — |
| RTX 4080 | 180 | 3.39 | 3.72 | 5.15 | — |
| RTX 4090 | 300 | 5.47 | 6.00 | 8.30 | 0.42–0.71 |
| RTX 5070 Ti | 300 | 3.21 | 3.52 | 4.87 | — |
| RTX 5080 | 360 | 3.86 | 4.23 | 5.86 | — |
| RTX 5090 | 575 | 6.37 | 6.98 | 9.67 | 0.72–1.24 |
| RX 7900 XTX | 290 | 2.59 | 1.76 | 1.80 | — |

Monthly 4090 history on Kryptex (INFERENCE, averaged from the series): Nov 2025 $0.71/day, Mar 2026 $0.42, May $0.54, **Jun $7.85 (Pearl arrives)**, Jul $4.15, Aug $3.41, Sep $7.71, Oct $9.74, Nov to date $6.24. The PRL price peaked at $2.46 on 2026-10-21 and is now $1.53.

**Independent check (INFERENCE):**
- WhatToMine's Pearl data (2026-11-14): network hashrate 8.86e19 H/s, 188 s blocks, 2,169.7 PRL block reward.
- Kryptex's 4090 hashrate is 343.4 TH/s, and PRL is $1.53.
- With a 1% pool fee, that works out to 3.83 PRL/day, or **$5.86/day**, which matches Kryptex's figure.

**B. NiceHash, which has no Pearl** (classic algorithms such as KawPow, Octopus and kHeavyHash). Source: `api2.nicehash.com` profitability calculator; BTC = $67,198 (CoinGecko, 2026-11-14). All figures are $/day.

| GPU | Gross | Net @ $0.05/kWh | @ $0.10 | @ $0.20 |
|---|---|---|---|---|
| RTX 3060 | 0.10 | −0.04 | −0.18 | −0.46 |
| RTX 3070 | 0.13 | −0.10 | −0.33 | −0.78 |
| RTX 3080 | 0.20 | −0.13 | −0.46 | −1.12 |
| RTX 3090 | 0.22 | −0.19 | −0.61 | −1.43 |
| RTX 4060 | 0.08 | −0.05 | −0.18 | −0.45 |
| RTX 4070 | 0.13 | −0.05 | −0.23 | −0.59 |
| RTX 4080 | 0.20 | −0.10 | −0.40 | −1.00 |
| RTX 4090 | 0.28 | −0.12 | −0.51 | −1.29 |
| RTX 5080 | 0.27 | 0.00 | −0.28 | −0.83 |
| RTX 5090 | 0.36 | −0.07 | −0.51 | −1.37 |

**Conclusion:** "Classic" GPU mining is under water at any LATAM tariff. The only positive mining floor today is Pearl, plus smaller new coins such as Quantus (QTC) and EPIC. That floor fell about 28% between the 30-day and 7-day averages and is set by one 7-month-old coin.

### 2.4 Net monthly income per consumer GPU at three electricity prices

**Assumptions (ESTIMATE):**
- 720 h/month and 24/7 operation.
- **Salad/Nosana wall power** = 0.8 × GPU TGP + 60 W for the dedicated host PC, since these apps need one PC per GPU.
- **Mining power** = Kryptex tuned watts + 25 W of rig overhead per GPU (multi-GPU rig).
- Electricity only: no internet, hardware depreciation, Windows licences or payout fees.
- Nosana uses a 50% job-time assumption; idle draw is taken as 25% of load.

| GPU | Salad W | Salad gross $/mo (mean) | **Salad net @$0.05** | **@$0.10** | **@$0.20** | Salad net @$0.10 at p25 ("new chef") | Mining (Pearl, 7-day) gross $/mo | **Mining net @$0.05** | **@$0.10** | **@$0.20** | Nosana net @50% job time & $0.10 | Vast listed renter $/h (ballpark†) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX 3060 | 195 | 22 | 15 | 8 | −6 | −2 | 29 | 23 | 17 | 6 | 7 | ~0.07 |
| RTX 3060 Ti | 220 | 26 | 18 | 10 | −5 | 4 | 37 | 32 | 27 | 16 | n/a | — |
| RTX 3070 | 235 | 28 | 20 | 11 | −6 | 5 | 45 | 40 | 34 | 24 | 16 | ~0.10 |
| RTX 3080 | 315 | 42 | 31 | 19 | −3 | 13 | 69 | 59 | 49 | 30 | 17 | ~0.14 |
| RTX 3090 | 340 | 82 | 70 | 58 | 33 | 45 | 77 | 65 | 52 | 27 | 48 | ~0.20 |
| RTX 4060 | 150 | 20 | 15 | 10 | −1 | 1 | 34 | 29 | 24 | 14 | 14 | — |
| RTX 4060 Ti | 190 | 38 | 31 | 25 | 11 | 12 | 49 | 41 | 33 | 17 | n/a | ~0.15 |
| RTX 4070 | 220 | 47 | 39 | 31 | 15 | 25 | 66 | 58 | 50 | 34 | 22 | ~0.17 |
| RTX 4080 | 315 | 93 | 82 | 71 | 48 | 66 | 112 | 104 | 97 | 82 | 38 | ~0.25 |
| RTX 4090 | 420 | 196 | 181 | 166 | 135 | 146 | 180 | 168 | 156 | 133 | 112 | ~0.49 |
| RTX 5070 Ti | 300 | 95 | 84 | 73 | 51 | 66 | 106 | 94 | 82 | 59 | n/a | — |
| RTX 5080 | 350 | 122 | 109 | 97 | 71 | 92 | 127 | 113 | 99 | 71 | 50 | ~0.26 |
| RTX 5090 | 520 | 270 | 252 | 233 | 196 | 204 | 209 | 188 | 166 | 123 | 140 | ~0.54 |

†Vast column: median of the first 64 on-demand offers per model returned by Vast's public search (`console.vast.ai/api/v0/bundles/`, 2026-11-14, default ordering). These are renter list prices per GPU-hour, before Vast's fee and idle time, not a full-market median. See the Vast agent's report for depth. The same snapshot shows LATAM hosts already listing on Vast: a 3090 in Ecuador at $0.20/h, and 3080/3090 cards in Argentina and Chile at $0.10–0.22/h.

**Break-even electricity price on Salad** (gross ÷ kWh, INFERENCE): RTX 3060 ≈ $0.16/kWh; 3070 ≈ $0.17; 3080 ≈ $0.19; 4060 ≈ $0.19; 4070 ≈ $0.30; 3090 ≈ $0.33; 4080 ≈ $0.41; 4090 ≈ $0.65; 5090 ≈ $0.72.

**Compared with Vast (ballpark):** a 4090 on Salad earns $0.272 per *chopping* hour, idle included. That is about 55% of a typical Vast 4090 list price ($0.49/h). A Vast host renting about 60–70% of hours, before Vast's cut, lands in the same place. Salad's edge is that it needs no marketing, reliability scores or Linux hosting skills. Vast's edge is multi-GPU servers, higher prices for well-reviewed hosts, and no $1k/day cap.

---

## 3) Implications for the LATAM used-hardware rental business

1. **Old data-center GPUs have no market on consumer apps.**
   - Salad and Nosana pay only for modern consumer RTX cards. Nosana also takes A4000/A5000/A6000/A40/A100/H100 cards.
   - Salad pays nothing for Tesla K80/M40/P40/P100/V100-class server cards. Its A5000 class sits at a $0 average with "Low" demand.
   - Pascal GeForce cards (GTX 1060/1070/1080 Ti) average only **$9–18 a month gross** on Salad, which is below power cost at $0.10–0.20/kWh.
   - **If the business case is "cheap old servers", these apps don't support it.** The opportunity is limited to RTX 3090 and newer.
2. **The app architecture punishes multi-GPU servers.**
   - Salad allows one GPU per Windows/WSL2 machine; Nosana one GPU per Linux PC.
   - An 8-GPU server earns from only one card unless it is split into separate physical hosts. Salad's ToS bans VMs without written permission.
   - Each GPU therefore needs its own cheap host: motherboard, CPU, 16–32 GB RAM, SSD and a Windows licence for Salad. That adds capex and about 60 W of overhead per GPU (already in the tables above).
   - Multi-GPU servers belong on Vast, RunPod, TensorDock or Clore (other agents).
3. **Only 24 GB+ and 40/50-series cards clear the bar at LATAM-typical tariffs.**
   - At $0.10/kWh, a 4090 nets about $166 a month and a 5090 about $233 on Salad. A 3090 nets about $58; a 3080 about $19; a 3060 or 4060 about $8–10.
   - At $0.20/kWh, everything at or below the 3080 loses money on Salad.
   - Payback, as an ESTIMATE using hardware prices that other agents should confirm:
     - Used 3090 at ~$600–800 + ~$300 host PC: 15–19 months at $0.10/kWh.
     - Used 4090 at ~$1,600–2,000 + host: about 11–14 months.
     - Both assume today's unusually high Salad utilization (94–97% job-hours) holds.
4. **Market depth is the binding constraint, not only price.**
   - Salad's entire chef payout pool is on the order of **$176k a month** (RNP-023's illustrative Year-1 revenue of ≈$4.3 M × 56%/31% splits). Salad has only about 490 RTX 4090s available at High priority.
   - One farm of 100 × 4090 would add about 20% to 4090 supply and take about 11% of all chef payouts. Job-hours and average rates would probably drop.
   - Nosana is smaller still: a run-rate of perhaps $50k–160k a month, $2.55 M paid lifetime. Livepeer's fees are $24k a month; Golem's are $2k a month.
   - **Plan for a few dozen GPUs per app, not hundreds.**
5. **The mining floor is real today but fragile.**
   - Pearl keeps RTX cards at $1–7 a day gross. Without it, mining has been negative after power since at least late 2025 (Kryptex pre-June 2026 series; NiceHash today).
   - Treat mining as a short-term fallback for idle cards, not a floor in the business case. Pearl's 7-day average is already 28% below its 30-day average.
   - For low-end cards (3060/3070/4060), mining Pearl currently beats Salad by $7–17 a month gross.
6. **Location effects are mostly unknown, possibly negative.**
   - Container job rates don't depend on country, but SaladCloud customers can pin jobs to countries, and US/Canada nodes are 50–60% of supply. LATAM nodes may see fewer region-pinned jobs, though this is unverified.
   - Nosana requires 50 Mbps up and recommends ping under 100 ms. That is achievable on fibre in Bogotá, Medellín, Quito or Guayaquil, harder elsewhere. Venezuelan connectivity and grid stability are the bigger risk.
   - Salad's bandwidth-sharing earnings depend on country, with no LATAM data.
7. **Payout rails and compliance:**
   - Colombia and Ecuador: PayPal, prepaid cards or RENDER should work (country lists not verified).
   - Venezuela: RENDER (Solana) → stablecoin is the realistic exit; Nosana's NOS works similarly.
   - Salad's **$1,000/day-per-person cap**, one-account-per-person rule and possible tax-ID or sanctions screening make a large single-operator farm on Salad legally and operationally awkward. Consider a formal written arrangement with Salad, since the ToS allows "written permission" for non-standard setups.
   - Token-denominated apps (Nosana, Theta, Golem, Gaimin, Livepeer) add FX and token risk: NOS is −95% from its all-time high, TFUEL −99%.
8. **Recommended positioning (INFERENCE):** treat consumer apps such as Salad and Nosana as a **filler channel** for single RTX 3090/4090/5090 boxes in their idle hours. Do not make them the core revenue line of a used-server business. The economics only work with high-VRAM, recent cards and electricity at or below about $0.10–0.12/kWh.

---

## 4) Confidence & gaps

| Item | Confidence | Why / gap |
|---|---|---|
| Salad chef earnings by GPU (§2.1.2) | **High** for the week measured | Salad's own measured dataset (7 days, all hours counted). One week only: no history pulled, and utilization (81–97%) may be seasonally or temporarily high. Survivorship bias (machines with at least 4 h/day only). Includes bandwidth and mining income |
| Salad 80% pass-through | **High** (exact arithmetic match) / Medium on interpretation | The 56%-of-revenue figure (RNP-023) shows Salad's overall margin is larger |
| Salad country effects, PayPal country list | **Low** | Not published in what I could retrieve. Search budget ran out before I could look for the PayPal/Mastercard country pages |
| Salad farm policy | Medium | No explicit farm ban, but there are VM, ownership, single-account and withdrawal-cap rules. Salad can change rates and terminate at will |
| Nosana rates | **High** (API) | Rates are USD-priced but paid in NOS |
| Nosana utilization | **Low** | The jobs API shows 973 "running", but most look stale. No per-market idle-node count found (that endpoint requires auth) |
| Golem, Livepeer figures | High (public APIs) | — |
| Theta, Gaimin, Hivenet, Kryptex rental | Low–Medium | Rates not published; conclusions rest on what the sites say and don't say |
| Mining (Kryptex/Pearl) | High for today; **Low for persistence** | Two independent calculations agree (Kryptex and WhatToMine). Pearl's difficulty and price are moving fast |
| Power assumptions | ESTIMATE | Real draw depends on workload (LLM inference often draws less than TGP; diffusion draws near TGP). Kryptex's tuned watts (e.g., 4080 at 180 W) may be optimistic for PearlHash |
| Vast comparison | Low (ballpark) | Only 64 offers per model, default ordering; host fee and utilization not applied. See the Vast agent |
| Venezuela sanctions status | **Low** | Changed in 2026. Verify OFAC status and the PayPal or crypto-exchange rails before planning anything there |

Not done (out of scope or blocked): a multi-week Salad history (could be built by polling `earning-rates.json` weekly), Salad SGS bandwidth earnings by country, Nosana geographic rules, and Theta edge-node actual payouts.

---

## 5) Sources (all accessed 2026-11-14 unless noted)

**Salad / SaladCloud**
- SaladCloud pricing (customer GPU-hour prices): https://salad.com/pricing
- Salad chef earning-rates page: https://salad.com/earning-rates. Underlying data: https://cdn.salad.com/site-data/earning-rates.json (updatedAt 2026-11-14T08:08:18Z, window 2026-11-07 to 2026-11-13)
- Salad customer availability data: https://cdn.salad.com/site-data/availability.json (generated 2026-11-14T11:06:16Z)
- Salad demand monitor UI: https://salad.com/earn/demand. API: https://app-api.salad.com/api/v2/demand-monitor/gpu (pulled 2026-11-14 12:02 UTC)
- Network Monitor explainer: https://support.salad.com/article/613-network-monitor
- Chef Terms of Service (Last Updated 2026-09-28): https://salad.com/terms/chefs/ · terms index: https://salad.com/terms
- Container-job requirements: https://support.salad.com/guides/getting-jobs/getting-container-jobs
- Multiple accounts / multiple devices: https://support.salad.com/article/46-can-i-create-multiple-accounts
- Withdrawal limit / RENDER redemption: https://support.salad.com/faq/your-account/is-there-a-withdrawal-limit
- Rewards outside the US: https://support.salad.com/rewards/rewards-faq/i-live-outside-the-us-can-i-still-redeem-rewards-with-salad
- SaladCloud API, create container group (`country_codes`): https://docs.salad.com/reference/saladcloud-api/container-groups/create-container-group.md
- Priority pricing / preemption: https://docs.salad.com/container-engine/explanation/billing-pricing/priority-pricing.md
- Service performance (node geography, uptime test): https://docs.salad.com/container-engine/explanation/core-concepts/service-performance.md
- Salad joins Render Network (2026-04-07): https://blog.salad.com/salad-joins-render-network/
- Render RNP-023 (dated 2026-03-26, revenue splits and chef reward share): https://raw.githubusercontent.com/rendernetwork/RNPs/main/RNP-023.md
- Salad web app bundle (Coinbase/Solana payout strings), inspected without executing: https://salad.com/app/static/js/main.3a49af1f.js

**Nosana**
- Markets API: https://dashboard.k8s.prd.nos.ci/api/markets/ (also served at https://api.nosana.com/markets)
- Job stats: https://dashboard.k8s.prd.nos.ci/api/jobs/stats · running jobs: https://dashboard.k8s.prd.nos.ci/api/jobs?limit=50&state=RUNNING&offset=N · token stats: https://dashboard.k8s.prd.nos.ci/api/stats
- Host requirements: https://learn.nosana.com/hosts/grid.html
- Secondary (search snippet only, not opened): Solana Compass Nosana page https://solanacompass.com/projects/Nosana (HTTP 403 on fetch)

**Golem**
- Online stats: https://api2.stats.golem.network/v2/network/online/stats · earnings: https://api2.stats.golem.network/v1/network/earnings/overviewnew · history by runtime: https://api2.stats.golem.network/v2/network/historical/stats/combined

**Livepeer**
- https://livepeer.org/compute (24 h service payouts vs protocol rewards)
- https://explorer.livepeer.org/ (embedded data: 100 active orchestrators, 30-day fee volumes, stakes)

**Theta / Gaimin / Hivenet / Kryptex / Gonka / Inference.net**
- https://www.thetaedgecloud.com/ (customer GPU prices) · https://docs.thetatoken.org/docs/setup-theta-edge-node · https://docs.thetatoken.org/docs/theta-edgecloud-overview (last updated 2026-08-05)
- https://www.gaimin.io/
- https://www.hivenet.com/compute
- https://www.kryptex.com/en/rent-cloud-gpus
- https://gonka.ai/ · https://gonka.ai/docs/host/hardware-specifications/
- https://inference.net/

**Mining baseline**
- Kryptex per-GPU pages with embedded daily revenue series, e.g. https://www.kryptex.com/en/hardware/nvidia-rtx-4090 (also -3060, -3060-ti, -3070, -3080, -3090, -4060, -4060-ti, -4070, -4080, -5070, -5070-ti, -5080, -5090, amd-rx-7900-xtx, amd-rx-6800-xt). Pages say "Last updated: 13 Nov 2026"; latest series point is 2026-11-14
- WhatToMine coins JSON: https://whattomine.com/coins.json · Pearl: https://whattomine.com/coins/469.json
- NiceHash profitability calculator devices: https://api2.nicehash.com/main/api/v2/public/profcalc/devices · algorithm pay rates: https://api2.nicehash.com/main/api/v2/public/simplemultialgo/info · algorithm metadata: https://api2.nicehash.com/main/api/v2/mining/algorithms
- Tom's Hardware on the Pearl mining rush (headline only retrieved; article date not visible): https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding
- Kryptex Pearl pool news (2026-06-05, via search snippet): https://www.kryptex.com/news/pearl-mining-en

**Prices and reference**
- CoinGecko simple price and markets API (BTC $67,198; ETH $1,908; PRL $1.53; NOS $0.358; GLM $0.095; LPT $1.15; RENDER $1.49; TFUEL $0.00707; GMRX $0.0000077; CLORE $0.0015): https://api.coingecko.com/api/v3/simple/price · https://api.coingecko.com/api/v3/coins/markets
- Vast.ai public offer search (ballpark only): https://console.vast.ai/api/v0/bundles/ (POST, per-model `gpu_name` filter)

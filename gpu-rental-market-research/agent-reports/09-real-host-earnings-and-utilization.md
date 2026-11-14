# 09 — What GPU hosts actually earn: first-hand reports, utilization, ROI, competition, location

**Agent:** 09 of 10 · **Date of research:** 2026-11-14 · **Scope:** realised host earnings, utilization by GPU class, ROI trend, location effects (with LATAM focus), and operational pain points on peer-to-peer and decentralized GPU marketplaces.

**Labels used throughout**
- **CONFIRMED:** primary, dated data. This means either my own capture of a platform's public API, or a platform's own published rate table or documentation.
- **ANECDOTE:** a first-hand host report (self-reported, not audited).
- **ESTIMATE:** modelled numbers, mine or third-party.
- **LOW-CRED:** a third-party "review" or SEO page whose numbers are unsourced or internally inconsistent.

> **Method note (important for weighting the evidence)**
> - Reddit was not reachable from this environment. Both the WebFetch and WebSearch tools refuse reddit.com, and direct JSON requests to reddit.com and old.reddit.com were blocked (403 or empty). So **no r/vastai, r/LocalLLaMA or r/homelab threads could be read.** I did not use third-party Reddit archives.
> - The shared WebSearch budget (200 calls for all 10 agents) ran out partway through this task. Topics I could not search afterwards are listed in §4.
> - To compensate, I collected **primary market data**:
>   - **Two complete snapshots of the Vast.ai marketplace** from the public offer-search API (no account needed).
>     - S1: 2026-11-14, 12:22–12:29 UTC, a Saturday. 11,554 offers, **6,202 machines, 19,086 GPUs, 1,920 hosts.**
>     - S2: 12:29–12:36 UTC, used for stability.
>     - The API returns at most 64 results per query, so I split each query by machine-ID range until no query was truncated (0 truncated queries). An earlier attempt that split by price was incomplete and has been discarded.
>   - Akash's public console API.
>   - Salad's published host rate table.
>   - Hashrate.no's Vast occupancy tracker.
>   - Vast's host documentation.
> - Many "how much can you earn" pages ranking in search are affiliate or SEO content with unsourced or inconsistent figures. They are flagged LOW-CRED and are not used for the conclusions.

---

## 1) Executive summary

- **Vast.ai is busy (CONFIRMED, my snapshot, 2026-11-14).**
  - **75.7% of the 19,086 listed GPUs were occupied** (75.3% seven minutes later). Hashrate.no independently shows **74.2%**.
  - Occupancy is stable at the aggregate level, but **12.7% of machines changed state within 7 minutes**. Many rentals are short and churn is high.
- **The occupancy goes to verified, reliable, well-connected hosts (CONFIRMED snapshot).**
  - **Verified GPUs: 81% occupied. Unverified: 53%. Deverified: 50%.**
  - Reliability ≥0.99: **80%**. Reliability 0.95–0.98: **60%**. Reliability 0.90–0.95: **44%**.
  - Upload ≥1 Gbps: **79%**. Upload <100 Mbps: **65%**.
  - **Price matters less than you might expect:** listings below 0.8× the same-GPU median are 82% occupied; listings above 1.5× the median are 72% occupied.
- **Realised first-hand earnings in 2026 are modest (ANECDOTE).**
  - Verified RTX 4090: about **$6/day, ~$180/month gross** (RedPandaMining, May 2026).
  - Verified RTX 5090: about **$9/day, ~$270/month gross** (same source).
  - **The same 4090 unverified, at the same price, earned about $0.05/day.**
  - A new host with **5× RTX 5090 earned about $230 in 23 days in total**, roughly **$60 per GPU-month**, while unverified because upload was below 100 Mbps (bytwork.com, Oct 2026).
  - An RTX 3060 earned **$11.56 in its first week**, at 46% of hours rented (dev.to, Jun 2026).
  - Salad: RTX 5090 at about $7/day (India, Oct 2026).
- **Utilization and price by GPU class (CONFIRMED, verified machines, median renter list price per GPU-hour):**

  | GPU | Occupancy (verified) | Median renter price |
  |---|---|---|
  | RTX 3090 | 87% | $0.22 |
  | RTX 4090 | 84% | $0.47 |
  | RTX 5090 | 81% | $0.67 |
  | A100 SXM4 | 90% | $1.05 |
  | H100 SXM | 95% | $2.40 |
  | V100 | 83% | $0.14 |
  | RTX 3060 | 83% | $0.08 |
  | RTX 2080 Ti | 63% | $0.09 |
  | P100 | 33% | $0.09 |

  - **Unverified** occupancy is much lower: 4090 54%, 5090 64%, **A100 SXM4 29%**.
  - Old cards do get rented, but at **$0.07–0.14 per GPU-hour** they gross only **about $10–60 per GPU per month.**
- **What the host keeps.** On Vast, the renter price runs about **25% above host earnings**, so the host keeps about **80%** (Vast article, 2026-05-18). Hashrate.no lists a "25% hosting fee". At the Nov 2026 medians, **100% rented** grosses about:

  | GPU | Gross per month at 100% rented |
  |---|---|
  | RTX 3090 | $123 |
  | RTX 4090 | $273 |
  | RTX 5090 | $375 |
  | A100 SXM | $500 |
  | H100 SXM | $1,364 |
  | V100 | $62 |
  | RTX 3060 | $44 |

- **Realistic monthly net per GPU** (my model in §2.7, after power at $0.10/kWh, before hardware, internet and labour), conservative / typical / optimistic:

  | GPU | Conservative | Typical | Optimistic |
  |---|---|---|---|
  | RTX 3090 | $12 | $41 | $73 |
  | RTX 4090 | $36 | $110 | $189 |
  | RTX 5090 | $51 | $152 | $261 |
  | V100 / P40 | $2–4 | $16–19 | $30–35 |
  | A100 PCIe | $64 | $190 | $324 |
  | H100 SXM | $214 | $613 | $1,040 |

  These bands match the first-hand reports: bytwork sits at the conservative end, RedPandaMining at the optimistic end.
- **Location: weak price penalty and similar occupancy, but LATAM supply is tiny and less often verified (CONFIRMED snapshot).**
  - Latin America has **156 of 19,086 GPUs (0.8%)**: Brazil 70, Argentina 28, Mexico 21, Chile 19, Puerto Rico 13, **Ecuador 2 (both unverified RTX 3090s)**, Peru, Paraguay and Panama 1 each. **Colombia and Venezuela have zero.**
  - LATAM occupancy is **75%**, the same as North America (76%) and Europe (77%).
  - The mix-adjusted price index is **0.96** vs North America 1.00. Same-model medians are 4090 $0.423 vs $0.468 global, 3090 $0.201 vs $0.210, 5090 $0.589 vs $0.642: **about 4–10% lower.**
  - But only **63% of LATAM GPUs are verified**, against 81–83% in North America and Europe, and median upload is **625 Mbps vs about 880–900**.
  - Verification needs **500/500 Mbps wired, a public IPv4 address and >90% reliability** (Vast docs, Nov 2026).
- **ROI has compressed for older cards and moved toward 24–32 GB consumer cards, RTX PRO 6000 and datacenter GPUs.**
  - In September 2026, Salad **raised** 4090 and 5090 host rates ("demand exceeded supply for months") but **cut RTX 3090 by 32%** at the top tier ($0.150→$0.102/h) and cut 15 GPU classes (CONFIRMED).
  - A 2023 Hacker News comment priced a Vast 3090 at about **$0.20/h**. The Nov 2026 median is **$0.21/h**, so prices are flat in nominal terms while supply grew.
  - The bytwork host estimates payback for AI rental only at **~3 years for a new 5090** and **~2 years for a used 4090** (Oct 2026).
- **Pain points that matter more than price:**
  - Verification takes **2–4 weeks** (Woven AI) to **months** (Habr host, 2024).
  - Machines are auto-deverified on errors.
  - Reliability penalties apply for restarts and offline time, and breaking a rental contract early "carries a serious penalty".
  - Payouts go only via **Wise, PayPal or Stripe**, weekly, with a **$20 minimum**; hosts must be able to receive B2B payments. Venezuela is a likely problem here and must be checked.
  - Rentals are lumpy: one 2×5090 rig was rented 7–8 consecutive days, then nothing.

---

## 2) Detailed findings

### 2.1 First-hand host reports (2024–2026)

No Reddit access (see method note). These are the first-hand or near-first-hand reports I could read. "Gross" means before electricity.

| # | Date of report | Platform | GPU(s) | Host location | Reported earnings | Utilization / notes | Electricity | Label | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Oct 2026 (updated 2026-10-21) | Vast.ai | 5× RTX 5090 across 4 rigs (EPYC 7B12, 7950X, 2× 7945HX mini-PCs) | Not stated (Russian-language author) | **~$230 total in 23 days**, ≈ $2.0/GPU-day, ≈ $60/GPU-month gross | Unverified, because upload was below 100 Mbps, despite 99.29% reliability; priced "near the very top of the listings" and still often idle | n/r | ANECDOTE (screenshots) | bytwork.com/en/articles/ai-income |
| 2 | same | Vast.ai | 2× RTX 5090 (EPYC rig) | same | ~$138 in 23 days | "Rented for about seven or eight consecutive days… since then, it has earned practically nothing" | n/r | ANECDOTE | same |
| 3 | same | Vast.ai | 1× RTX 5090 (7950X) | same | ~$59 in 23 days | Rented fairly consistently in the last week | n/r | ANECDOTE | same |
| 4 | same | Vast.ai | 2× RTX 5090 in laptop-CPU (7945HX) mini-PCs | same | ~$15 and ~$11 in 23 days | Rarely or never rented | n/r | ANECDOTE | same |
| 5 | same | Vast.ai | RTX 4060 Ti (×3 rigs) | same | ~$0.35–0.50/day at first, then ~0 | "The cards were idle almost all the time"; "unverified machines receive practically no orders" | n/r | ANECDOTE | same |
| 6 | same | Vast.ai storage | SSD rental | same | ~$14/month | More than 10% of the extra income. Bandwidth income was negligible. | — | ANECDOTE | same |
| 7 | same | Salad vs Vast | 1× RTX 5090 | same | Earned more on Salad than on Vast "at the time" | Pearl mining would have earned ~$1,380 over the same 23 days (≈ 6× the rental income) | — | ANECDOTE | same |
| 8 | May 2026 (YouTube video) | Vast.ai | RTX 5090, verified | US (channel) | **~$9/day ≈ $270/month gross** | Live dashboard shown on camera | n/r | ANECDOTE (second-hand summary of a video) | RedPandaMining, via endlessmining.com/renting-your-gpu-for-ai-2026/ |
| 9 | May 2026 | Vast.ai | RTX 4090, verified (several) | US | **~$6/day each ≈ $180/month gross** | — | n/r | ANECDOTE (second-hand) | same |
| 10 | May 2026 | Vast.ai | RTX 4090, **unverified**, same asking price | US | **~$0.05/day** | Verification is the decisive variable | n/r | ANECDOTE (second-hand) | same |
| 11 | Jun 2026 (edited Oct) | Vast.ai | RTX 3060 12GB at $0.15/h | Probably Turkey ("Turkish electricity rates") | **$11.56 in week 1**; author projects $50–130/month for mid-tier GPUs | 77 of 168 hours rented (46%); daily range 0–22 h | Est. $8–15/month | ANECDOTE | dev.to/samhartley_dev/… |
| 12 | 2026-10-19 | Salad | RTX 5090 workstation | India | **$105 in 15 days ≈ $7/day** | — | n/r | ANECDOTE (review) | trustpilot.com/review/salad.com |
| 13 | 2026-11-12 | Salad | RTX 5060 Ti mini-PC | US | n/r | Must reboot twice a day; goes down overnight. Uptime problems kill earnings. | — | ANECDOTE (review) | same |
| 14 | 2026-11-10 | Salad | n/r | US | Cash-out fee ~$2 on a $10 balance | Removed machines | — | ANECDOTE (review) | same |
| 15 | 2026-11-02 | Salad | n/r | US | "Very slow income" | — | — | ANECDOTE (review) | same |
| 16 | Jun 2024 | Vast.ai | 2× RTX 3090 (dual Xeon E5-2697v2) plus a second machine | Russian-speaking (inferred) | n/r | Both machines rented **about ⅔ of the time** | n/r | ANECDOTE | habr.com/en/articles/821203/comments (user riv9231) |
| 17 | Jun 2024 | Vast.ai | 6× RTX 4090 | same | n/r | First rental a week after listing (2 GPUs). Remaining GPUs **idle about 3 weeks**. Verification "often takes months"; some unverified hosts waited more than 3 months. | — | ANECDOTE | same |
| 18 | Jun 2024 | Clore.ai | Ryzen 7950X server | same | n/r | "Only miners rented"; the CLORE token then fell about 4× | — | ANECDOTE | same |
| 19 | Sep 2026 | Vast.ai | n/r | NL, PL | "Great returns"; "payments and invoicing processed promptly" | No figures given | — | ANECDOTE (review) | trustpilot.com/review/vast.ai |
| 20 | 2026-06-09 | Own cloud (AMD MI300X, datacenter) | — | US | "Renting my GPUs out for more money now due to supply being so tight" | Datacenter operator, not a hobby host | — | ANECDOTE | news.ycombinator.com/item?id=48455436 |
| 21 | Dec 2025 (as told) | Vast.ai | RTX 4090, verified | Chiang Mai, Thailand | "$340/month at ~42% utilization" | **Internally inconsistent**: implies ≈ $1.12/h host income, about 3× the market price | n/r | **LOW-CRED** (second-hand) | passiveyieldlab.com/blog/cloud-gpu-rental-passive-income-2026/ |

**Reading the table.**
- The two most credible 2026 sources bracket reality.
  - A **verified** 4090 or 5090 in a good setup grosses **$180–270 per GPU per month**, which implies roughly 65–75% paid utilization at Nov 2026 prices.
  - A **new, unverified, bandwidth-limited** host grosses **about $60 per 5090 per month**, roughly 15–20% utilization, or near zero on mid-range cards.
- About ⅔ rented time was already reported in 2024.

### 2.2 Platform-level utilization and prices (CONFIRMED primary data)

**A. Vast.ai full-market snapshot S1 (public `bundles` API, on-demand, `external=false`, 2026-11-14 12:22–12:29 UTC).**
- **"Occupied"** = a machine's GPUs are not available for on-demand rental:
  - total GPUs = largest bundle the machine offers;
  - free GPUs = largest bundle still rentable.
- Totals: **6,202 machines · 19,086 GPUs · 1,920 hosts · 75.7% occupied.**
- Cross-check: Hashrate.no shows **74.16%**, with 7,802 GPUs available, 22,393 rented and a 25% fee (hashrate.no/platforms/vast, accessed 2026-11-14).

| GPU (≥140 listed GPUs, plus old cards) | GPUs listed | Occupied | Median renter list $/GPU-h | Host gross at 100% rented (≈ 0.8 × list × 730 h) |
|---|---|---|---|---|
| RTX 5090 | 4,305 | 76.2% | 0.642 | ~$375/mo |
| RTX 4090 | 2,623 | 78.0% | 0.468 | ~$273/mo |
| RTX 3090 | 1,582 | 83.2% | 0.210 | ~$123/mo |
| RTX 3060 | 824 | 78.6% | 0.075 | ~$44/mo |
| RTX 5060 Ti | 746 | 70.5% | 0.134 | ~$78/mo |
| RTX 5080 | 647 | 74.7% | 0.254 | ~$148/mo |
| Tesla V100 | 544 | 74.8% | 0.107 | ~$62/mo |
| RTX PRO 6000 (S / WS / Max-Q) | 1,369 | 82–86% | 1.34–1.60 | ~$780–935/mo |
| A100 SXM4 | 389 | 83.8% | 0.857 | ~$500/mo |
| A100 PCIe | 202 | 76.2% | 0.736 | ~$430/mo |
| H100 SXM | 141 | 84.4% | 2.336 | ~$1,364/mo |
| H200 / H200 NVL | 423 | 75–76% | 4.0–5.0 | ~$2,340–2,900/mo |
| RTX A6000 / RTX 6000 Ada | 154 / 128 | 93% / 95% | 0.44 / 0.67 | ~$256 / $389/mo |
| RTX A4000 | 294 | 66.3% | 0.104 | ~$61/mo |
| RTX 3080 | 208 | 63.9% | 0.136 | ~$79/mo |
| RTX 2080 Ti | 123 | 52.8% | 0.094 | ~$55/mo |
| Tesla P100 | 22 | 32% | 0.094 | ~$55/mo |
| Tesla P40 | 9 | 78% | n=9; too few to price | — |

Prices are renter list prices, which include Vast's fee and a little storage. The "Host gross" column is my approximation.

**B. Verified vs unverified for the key GPUs (CONFIRMED, S1).**

| GPU | Verified: GPUs / occupied / median $ | Unverified: GPUs / occupied / median $ | Deverified: GPUs / occupied |
|---|---|---|---|
| RTX 3090 | 1,316 / **87%** / 0.216 | 183 / 67% / 0.186 | 83 / 58% |
| RTX 4090 | 2,171 / **84%** / 0.472 | 185 / **54%** / 0.401 | 267 / 43% |
| RTX 5090 | 3,508 / **81%** / 0.667 | 337 / 64% / 0.536 | 460 / 51% |
| RTX 3060 | 674 / 83% / 0.077 | 71 / 59% / 0.069 | 79 / 61% |
| Tesla V100 | 269 / 83% / 0.142 | 118 / 65% / **0.067** | 157 / 68% |
| A100 SXM4 | 342 / **90%** / 1.054 | 24 / **29%** / 0.561 | 23 / 43% |
| H100 SXM | 94 / **95%** / 2.401 | 47 / 64% / 1.921 | — |
| RTX 2080 Ti | 89 / 63% / 0.094 | 26 / 27% / 0.094 | 8 / 25% |

- Unverified hosts already price lower, **typically 15–20% below verified** and up to about 50% below for V100 and A100, and are still rented much less.
- Unverified listings are only shown to renters who tick a "somewhat hidden" checkbox (bytwork, Oct 2026).
- Snapshot occupancy of unverified machines (~50–65%) is **survivor-biased**. It is far above what the new unverified hosts in the first-hand reports experienced (≈ 0–20%).

**C. Other platforms (CONFIRMED unless noted).**

| Platform | Data point | Date | Source |
|---|---|---|---|
| **Salad** (fixed host rates, no price-setting) | High / Med / Low / Lowest $/h: RTX 5090 0.300 / 0.271 / 0.233 / 0.175; RTX 4090 0.198 / 0.178 / 0.152 / 0.112; **RTX 3090 0.102 / 0.093 / 0.082 / 0.063 (was 0.150 at High)**; RTX 3080 0.084 / 0.074 / 0.061 / 0.042. At 100% uptime, a 4090 is $82–145/mo and a 3090 $46–74/mo. Salad: 5090/4090 "demand exceeded supply for months"; "does not guarantee 100% uptime". | Effective 2026-09-12 | blog.salad.com/earning-rate-changes-september-2026 |
| **Akash** | Whole network: 458 GPUs, 299 allocated (65%). H100 79% (56 GPUs, 3 providers, $2.56/h median); A100-80G 61% (200 GPUs, 4 providers, $1.49/h); **V100 SXM2 22%** (40 GPUs, 1 provider, $0.31/h); consumer cards in single or low double digits (3090: 11 GPUs, 100% used, $0.16/h). A tiny market concentrated in a few providers. | 2026-11-14 | console-api.akash.network/v1/gpu and /v1/gpu-prices |
| **Clore.ai** | "Rented servers": 133 with RTX 3090, 112 with 4090, 112 with 5090. "Earn up to" $330 / $620 / $700 per card per month, but only on bare-metal contracts of 2+ to 8+ GPUs on 14–30-day terms (vendor ceiling, not realised). | Accessed 2026-11-14 | clore.ai/host-3090.html |
| **RunPod** | The docs index has no host or provider onboarding pages, and runpod.io/host returns 404. The community-host route appears closed or invite-only for small operators (INFERENCE). | 2026-11-14 | docs.runpod.io/llms.txt |

### 2.3 What drives utilization (CONFIRMED snapshot S1 cross-tabs, plus Vast docs)

| Driver | Bucket | GPUs | Occupied |
|---|---|---|---|
| **Verification** | verified | 15,483 | **81.2%** |
| | unverified | 2,102 | 53.4% |
| | deverified | 1,501 | 50.2% |
| **Reliability score** | ≥0.99 | 12,635 | **80.3%** |
| | 0.98–0.99 | 3,295 | 75.0% |
| | 0.95–0.98 | 2,160 | 60.0% |
| | 0.90–0.95 | 550 | 44.2% |
| **Upload bandwidth** | ≥1,000 Mbps | 6,663 | **78.9%** |
| | 500–1,000 | 8,091 | 75.6% |
| | 100–500 | 3,417 | 73.0% |
| | <100 | 915 | 64.5% |
| **Price vs same-GPU median** | <0.8× | 3,046 | 82.1% |
| | 0.95–1.05× | 3,437 | 79.2% |
| | 1.05–1.25× | 3,310 | 72.3% |
| | >1.5× | 2,310 | 71.6% |
| **Machine size** | 1 / 2 / 4 / 8 GPUs | 2,531 / 2,756 / 4,224 / 7,768 | 76% / 73% / 76% / 77% |
| **Datacenter flag** | community / datacenter | 17,586 / 1,492 | 75.7% / 76.3%; datacenter median list $0.84 vs $0.37 (partly GPU mix) |

How to read this:
- **Verification and reliability matter most**, at 25–35 points of occupancy.
- **Price elasticity is modest:** going from <0.8× to >1.5× the median costs about 10 points.
- Vast says verification is algorithmic and weighs:
  - GPU tier (B200 > H200 >> 5090 > 4070);
  - GPU count per machine ("8×5090 >> 2×5090 > 1×5090");
  - VM support and symmetric bandwidth;
  - "supply & demand" (docs.vast.ai/host/understanding-verification).

**Minimum requirements for verification** (docs.vast.ai/host/verification-stages, accessed 2026-11-14):
- **500 Mbps down and 500 Mbps up**, wired.
- A **public IPv4** address.
- Reliability >90%.
- SSD with ≥200 GB dedicated to Docker.
- System RAM ≥95% of total VRAM.
- ≥2 CPU cores per GPU.
- PCIe >2.85 GiB/s per GPU.
- CUDA ≥11.8, VRAM >7 GB, and identical GPUs within a machine.

**Market concentration (S1).**
- The top 100 hosts hold **43.5%** of listed GPUs, the top 50 hold 30.7% and the top 10 hold 10.4%.
- **836 of the 1,920 hosts list only 1–2 GPUs.**
- A newcomer competes with professional fleets, but no single host dominates.

**Stability and churn (S1 vs S2, 7 minutes apart).**
- Aggregate occupancy moved 75.7% → 75.3%, and per-GPU occupancy within ±1 point (3090 83.2→83.4; 4090 78.0→78.0; 5090 76.2→75.3).
- At machine level, **12.7% of the machines present in both snapshots changed occupancy.** 734 GPUs became occupied and 706 were freed, out of 17,608.
- About 11% of machines appeared in or disappeared from listings between the two snapshots.
- A rough Little's-law reading (≈ 14.4k occupied GPUs, ≈ 100 starts/min) suggests an **average occupancy spell of only a few hours**. **Low confidence:** listing flapping and host self-tests inflate the churn. Either way, it is consistent with Vast's own segments: "hours to days" for inference and "days to weeks" for fine-tuning.

### 2.4 ROI and payback: how it changed from 2023/24 to 2026

| Evidence | 2023–2024 | 2026 | Label / source |
|---|---|---|---|
| Vast RTX 3090 renter price | "literally $0.2 per hour" (HN, May 2023) | Median **$0.210/h** list; verified $0.216 (Nov 2026) | ANECDOTE (news.ycombinator.com/item?id=36026101) vs CONFIRMED snapshot |
| Time rented, small hobby host | ~⅔ for 2×3090 (Habr, Jun 2024) | 46% for a 3060 in week 1 (dev.to, Jun 2026); near 0 for unverified 4060 Ti or 5090 (bytwork, Oct 2026) | ANECDOTE |
| Salad host rates | — | 3090 High $0.150 → **$0.102/h** (−32%) from 2026-09-12; 4090 $0.180 → $0.198 (+10%); 5090 $0.270 → $0.300 (+11%); 15 classes cut | CONFIRMED (Salad blog) |
| Vast price volatility in 2026, on-demand medians across regions (third-party scrape of the public API) | — | RTX 4090: May $0.67 → Aug $0.47 → Oct $0.57. RTX 5090: May $1.00 → Aug $0.40 → Oct $0.71. H100 SXM: May $3.72 → Jul $2.27 → Oct $3.06. A100 SXM 80G: steady $1.00–1.13. | CONFIRMED-ish (github.com/woodsonl/gpu-pricing-tracker, data/observations.csv) |
| Host-estimated payback, AI rental only | — | New RTX 5090: **~3 years** (~2 years with mining in idle time). RTX 5080: "a little over 2 years". Used RTX 4090: **~2 years**. | ANECDOTE / ESTIMATE (bytwork, Oct 2026) |
| Mining as idle filler | Clore's renters were mostly miners; the CLORE token fell ~4× (2024) | Pearl mining would have earned ~6× the AI income over 23 days for 5× 5090 (Oct 2026). Vast lets hosts run "default jobs" in idle time. | ANECDOTE; docs.vast.ai/host/using-your-own-machine |

**Synthesis on ROI.**
- **Consumer 24 GB cards:** nominal prices are flat since 2023 for the 3090. The 4090 lists at about $0.47–0.57.
- **Supply has grown,** so a new entrant's paid utilization depends on verification and reliability, not on simply being listed.
- **Prices became more volatile in 2026.** The tracker shows 5090 swinging 2.5× between May and August.
- **Old cards keep being devalued.** Salad cut 15 classes in September 2026; P100 and 2080 Ti are 32–53% occupied at about $0.09/h.
- **The upside:** 2026 is supply-tight for high-VRAM cards. Salad raised 4090/5090 rates, a datacenter operator reports tight supply, RTX PRO 6000 listings are 82–86% occupied, and RTX A6000 and RTX 6000 Ada listings are 93–95% occupied.

### 2.5 Location effects

**A. Where Vast supply sits (CONFIRMED S1).** The price index is each machine's price divided by the global median for the same GPU, GPU-weighted.

| Region | GPUs (share) | Occupied | Verified share | Median upload (Mbps) | Mix-adjusted price index |
|---|---|---|---|---|---|
| North America | 8,276 (43.4%) | 76.2% | 81% | 902 | 1.00 |
| Europe | 5,798 (30.4%) | 76.9% | 83% | 864 | 1.10 |
| Asia / Middle East (excl. China) | 2,561 | 76.2% | 84% | 622 | 0.96 |
| China / HK / TW | 2,047 | 71.4% | 76% | 602 | 0.93 |
| Oceania | 183 | 66.1% | 72% | 508 | 0.95 |
| **Latin America** | **156 (0.8%)** | **75.0%** | **63%** | **625** | **0.96** |
| Russia / CIS | 29 | **24.1%** | **3%** | 612 | 0.73 |
| Africa | 26 | 88.5% | 88% | 258 | 1.47 (n tiny) |

**Like-for-like small hosts (machines with ≤2 GPUs).**

| Region | Price index | Occupied |
|---|---|---|
| North America | 1.02 | 75% |
| Europe | 1.01 | 77% |
| **LATAM** | **0.96** | **75%** |
| Asia (other) | 0.92 | 78% |
| China/HK/TW | 1.01 | 57% |
| Oceania | 0.99 | 60% |

**LATAM detail (S1).**

| Country | GPUs | Occupied | Median $/GPU-h |
|---|---|---|---|
| Brazil | 70 | 71% | 0.230 |
| Argentina | 28 | 75% | 0.189 |
| Mexico | 21 | 81% | 0.469 |
| Chile | 19 | 84% | 0.228 |
| Puerto Rico | 13 | 85% | 0.481 |
| **Ecuador** | **2 (2× single RTX 3090, unverified)** | **1 of 2 rented** | 0.201 |
| Peru, Paraguay, Panama | 1 each | — | — |
| **Colombia** | **0** | — | — |
| **Venezuela** | **0** | — | — |

- LATAM GPU mix: RTX 3090 29, 5090 15, 4090 14, 3080 8, 5060 Ti 6, …
- Large LATAM boxes all fill up:
  - Brazil 8× H200: 8/8 rented at $7.24/GPU-h.
  - Brazil 8× 5090: 6/8 rented at $0.67.
  - Chile 2× 4×3090: 4/4 each at $0.20–0.21.
  - Puerto Rico 4× 5080: 3/4.

**B. Same-GPU pricing by region (CONFIRMED S1, median renter list $/GPU-h, occupancy in brackets).**

| GPU (global median) | North America | Europe | China/HK/TW | Asia (other) | LATAM |
|---|---|---|---|---|---|
| RTX 3090 ($0.210) | 0.209 (82%) | 0.227 (85%) | 0.181 (78%) | 0.215 (89%) | **0.201 (87%, 45 GPUs)** |
| RTX 4090 ($0.468) | 0.469 (80%) | 0.478 (77%) | 0.478 (69%) | 0.427 (86%) | **0.423 (94%, 18 GPUs)** |
| RTX 5090 ($0.642) | 0.668 (77%) | 0.668 (74%) | 0.561 (75%) | 0.564 (81%) | **0.589 (79%, 24 GPUs)** |
| A100 SXM4 ($0.857) | 0.667 (78%) | 1.067 (94%) | 1.067 (100%, 8 GPUs) | 1.081 (79%) | — |
| H100 SXM ($2.336) | 2.336 (92%) | 2.667 (80%) | 2.400 (100%) | 1.840 (84%) | — |
| Tesla V100 ($0.107) | 0.094 (74%) | 0.144 (76%) | 0.094 (50%) | 0.147 (100%) | — |

**Interpretation.**
- **Customers rent outside the US and EU at similar rates.** LATAM, Asia and Europe occupancy is roughly the same as North America.
- **The price penalty for location is small:** about **0–10%** for LATAM consumer cards. It is larger in Asia for 5090 and H100 (−15 to −20%), and very large for Russia/CIS (index 0.73, 24% occupied, 3% verified), consistent with sanctions and payment friction (INFERENCE).
- New Zealand shows a thin, remote market: 69 GPUs, 30% occupied, $0.07 median.
- **The binding LATAM handicaps are verification-grade connectivity and scale, not geography itself:**
  - verified share 63% vs 81–83%;
  - median upload 625 vs about 880–900 Mbps;
  - almost all LATAM machines are 1–2-GPU boxes.

**C. Workload latency and bandwidth (Vast optimization guide, accessed 2026-11-14).**
- Rental segments by duration:
  - serverless and inference: "hours to days";
  - experimentation and fine-tuning: "days to weeks";
  - training: "weeks to months+".
- **8× bundles get about 2× the search volume of 1× bundles.** Longer listed durations and auto-extend increase expected earnings.
- Training and batch jobs are latency-insensitive but **download-heavy.** Images, model weights and datasets run to tens or hundreds of GB, so **symmetric bandwidth matters more than ping.** Hence the 500/500 Mbps verification floor.
- Interactive inference endpoints prefer proximity to users, mostly US and EU (INFERENCE). A LATAM host should target training, fine-tuning and batch renters.
- A public IPv4 address is a hard verification requirement on Vast. CGNAT, common on LATAM residential lines, therefore blocks verification even if the machine can technically be listed.

**D. LATAM and Venezuela-specific first-hand reports.**
- Searches in Spanish ("alquilar GPU vast.ai ganancias", "rentar GPU Venezuela") and Portuguese ("vast.ai host Brasil lucro") returned **no first-hand LATAM host reports.** They returned only generic guides; for example, Xataka (2025-09-09) concludes "no te vas a hacer rico" ("you won't get rich").
- **No evidence was found of Venezuelan ex-crypto-miners pivoting to AI GPU rental.** This is consistent with **zero Venezuelan (and zero Colombian) machines on Vast.**
- The search budget ran out before I could check Venezuelan mining Telegram or Discord groups (§4).

### 2.6 Operational pain points (hosts)

| Pain point | Evidence | Label / source |
|---|---|---|
| **Verification gate** | Unverified 4090: ~$0.05/day vs ~$6/day verified. Verification takes "~2–4 weeks" (Woven AI) or "often months" (Habr 2024). It requires 500/500 Mbps and a public IPv4 address. | ANECDOTE / CONFIRMED docs (wovenai.ca; docs.vast.ai/host/verification-stages) |
| **Automatic deverification** | Any detected error, closed ports, low bandwidth, failing storage, NVML errors, container failures, or "detected abuse or policy violations" deverifies a machine temporarily. Most errors clear 1–2 h after the fix. Reducing hardware after creation (fewer GPUs or less RAM) triggers deverification. | CONFIRMED (Vast docs) |
| **Reliability penalties** | Restarts during rentals, lost connectivity and failed instance starts reduce reliability. Offline time is penalized. Ending a contract early "carries a serious penalty". Driver auto-updates must be disabled. | CONFIRMED (docs.vast.ai/host/hosting-overview; optimization guide) |
| **Lumpy demand** | 2×5090 rented 7–8 days, then ~0. 6×4090: remaining GPUs idle about 3 weeks. 3060: 0 to 22 h/day. 12.7% of machines change state within 7 minutes (S1→S2). | ANECDOTE / CONFIRMED snapshot |
| **Fragmentation** | A renter took 2 GPUs "from the centre" of a 6-GPU rig, after which the platform refused 4-GPU bundles (2024). Vast now recommends a mix of minimum-GPU settings. | ANECDOTE / CONFIRMED docs |
| **Payouts** | Vast: Wise, PayPal or Stripe only; weekly invoices on Fridays; **$20 minimum**; first payout up to 2 weeks. Hosts must be able to receive B2B payments in their country; "Vast.ai is not responsible for … restrictions … imposed by Wise, PayPal, Stripe". Salad: cash-out fees noticeable on small balances. | CONFIRMED (docs.vast.ai/host/payment); ANECDOTE (Trustpilot) |
| **Hardware wear and uptime** | The rental on/off load cycle may stress used cards more than steady mining (host opinion). A consumer mini-PC needed reboots twice a day. | ANECDOTE (bytwork; Trustpilot) |
| **Renter abuse / mining** | 2024: on Clore, "only miners rented". Vast lists "detected abuse" as a cause of deverification. **No 2025–2026 first-hand reports of illegal content or unpaid earnings on Vast** were found in accessible sources (Reddit inaccessible). | ANECDOTE / gap |
| **Security perception** | "A host can snoop on your workloads very easily" (HN, 2023). This caps what enterprise renters will run on community hosts. ISO 27001 datacenter hosts get the "Secure Cloud" label and better ranking. | ANECDOTE / CONFIRMED docs (datacenter-status) |
| **Datacenter tier is gated** | Requires ISO/IEC 27001, a registered business, a signed agreement, KYC, and ≥5 GPU servers. | CONFIRMED (docs.vast.ai/host/datacenter-status) |

### 2.7 Synthesis: realistic monthly net per GPU (ESTIMATE)

**Formula:** net = 730 h × [renter median × 0.80 × price factor × utilization − kW_load × $/kWh × utilization − kW_idle × $/kWh × (1 − utilization)].

**Inputs:**
- Renter medians from snapshot S1: 3060 $0.075; 3080 $0.136; 3090 $0.210; 4090 $0.468; 5090 $0.642; V100 $0.107; P40 $0.11; A100 PCIe $0.736; A100 SXM $0.857; H100 SXM $2.336.
- Host share 0.80.
- Power per GPU including a share of the system: 3060 0.20 kW; 3080 0.37; 3090 0.42; 4090 0.50; 5090 0.65; V100 0.32; P40 0.27; A100 PCIe 0.33; A100 SXM 0.50; H100 SXM 0.85. Idle 0.04–0.10 kW.

**Scenarios:**
- **Conservative:** 20% utilization, price factor 0.85. This represents a new or unverified host in months 1–2, as in bytwork. Unverified listings price about 15% below verified ones.
- **Typical:** 50% utilization, price factor 0.95. This represents a verified host in its first year, or one with reliability of 0.95–0.98, with a LATAM discount of about 5%.
- **Optimistic:** 80% utilization, price factor 1.00. This represents a verified host with reliability ≥0.99 and ≥1 Gbps, matching snapshot verified occupancy of 81–87% and RedPandaMining.

**Excluded:** hardware depreciation, internet, rent and labour.

| GPU class | Conservative, $0.10/kWh (gross) | Typical, $0.10/kWh (gross) | Optimistic, $0.10/kWh (gross) | Typical at $0.20/kWh | Typical at $0.05/kWh |
|---|---|---|---|---|---|
| RTX 3060 12GB | $2 ($7) | $12 ($21) | $23 ($35) | $3 | $16 |
| RTX 3080 10GB | $5 ($14) | $22 ($38) | $41 ($64) | $7 | $30 |
| **RTX 3090 24GB** | **$12** ($21) | **$41** ($58) | **$73** ($98) | $24 | $50 |
| **RTX 4090 24GB** | **$36** ($46) | **$110** ($130) | **$189** ($219) | $90 | $120 |
| **RTX 5090 32GB** | **$51** ($64) | **$152** ($178) | **$261** ($300) | $126 | $165 |
| Tesla V100 | $2 ($11) | $16 ($30) | $30 ($50) | $2 | $23 |
| Tesla P40 | $4 ($11) | $19 ($31) | $35 ($51) | $7 | $25 |
| A100 PCIe | $64 ($73) | $190 ($204) | $324 ($344) | $175 | $197 |
| A100 SXM4 80G | $73 ($85) | $217 ($238) | $370 ($400) | $195 | $227 |
| H100 SXM | $214 ($232) | $613 ($648) | $1,040 ($1,091) | $579 | $631 |

**Checks against first-hand data.**
- RedPandaMining's verified 4090 at ~$180/month gross and 5090 at ~$270 sit near the optimistic gross ($219 / $300).
- Bytwork's ~$60/month per 5090 matches the conservative gross ($64).
- Salad's fixed rates at 100% uptime ($82–145 for a 4090; $46–74 for a 3090) sit between typical and optimistic gross, with no price-setting risk but no utilization guarantee.

**Payback illustration (ESTIMATE; hardware prices are for other agents to confirm):** payback months = (GPU + share of chassis/PSU/CPU/RAM/SSD) ÷ monthly net.
- Used 3090 at about $700 all-in per GPU: **~17 months typical, ~10 optimistic, ~5 years conservative.**
- Used 4090 at about $1,900 all-in: **~17 months typical, ~10 optimistic.**
- Used V100 or P40 at about $150–250: **~8–16 months typical**, but on very thin absolute dollars ($16–19/month). These cards also face shrinking CUDA and framework support, and renters prefer 24 GB+ Ampere or newer.

---

## 3) Implications for the LATAM used-hardware rental business

1. **Verification is the business, not the hardware.** The same 4090 earns $0.05/day unverified and ~$6/day verified, and verified GPUs are 81% occupied against 50–53% for unverified or deverified. Vast's verification needs:
   - **500/500 Mbps wired, a public IPv4 address, >90% reliability**;
   - balanced, server-grade CPU, RAM and NVMe;
   - and it favours **multi-GPU boxes** (8× ≫ 2× ≫ 1×) and VM support.

   A Colombia, Venezuela or Ecuador site must first secure **symmetric fibre, a static IPv4 address and stable power (UPS or generator)**. LATAM's verified share is 63% (vs 81–83%) and median upload 625 Mbps (vs about 900). Those gaps are the real location handicap.
2. **Geography is not a big price penalty.** LATAM small hosts list at about **0.96×** the global same-GPU median and are **75% occupied, the same as North America.** Plan revenue at **90–100% of the global median**, not at a deep discount. Large LATAM boxes (Brazil 8× H200 and 8× 5090; Chile 4× 3090) are fully or nearly fully rented. Position for training, fine-tuning and batch work, not latency-sensitive inference.
3. **Old cards are a trap for absolute dollars.**
   - V100, P40, P100, 2080 Ti and 3060-class cards gross **about $10–60 per GPU per month** even when well utilized. P100 and 2080 Ti are only 32–53% occupied.
   - Salad cut 3090 and older rates in September 2026.
   - "Cheap" only works if the hardware is close to free and power costs ≤$0.05/kWh. Every slot also consumes chassis, PCIe, RAM and bandwidth that would earn more with a 24–32 GB card.
   - Demand in 2026 favours **RTX 3090/4090/5090, RTX A6000/6000 Ada/PRO 6000, A100/H100.** Verified 3090s are 87% occupied, A100 SXM 90%, H100 95%.
4. **There is no incumbent supply in Colombia or Venezuela.** This is not proof of demand, but there is no local competition either. Supply is zero in both countries and two unverified 3090s in Ecuador. **There is no visible evidence that Venezuelan miners have pivoted**, either because it is not viable (power reliability, connectivity, payouts) or because it is invisible to this method.
5. **Payout rails are a gating item for Venezuela.** Vast pays only via Wise, PayPal or Stripe and requires accounts that can receive B2B payments. Confirm country availability before investing. A Colombian, Ecuadorian or foreign legal entity receiving payouts may be required.
6. **Plan for a ramp and lumpiness.**
   - Model months 1–2 at the conservative band, about 20% utilization: verification takes 2–4 weeks or more.
   - Expect multi-day full rentals followed by idle weeks.
   - Use **idle-time default jobs** (e.g., mining) or Salad on separate boxes to cover power.
   - Sell disk: storage was about $14/month per host, more than 10% of one host's extra income.
7. **Scale matters for verification and for the datacenter tier.**
   - Fleets of **4–8 identical GPUs per box** rank and verify better, and 8× bundles get about 2× the search volume.
   - The "Secure Cloud" tier needs ISO 27001, a registered business and ≥5 servers. In practice that means colocation in a certified LATAM datacenter, not a home or warehouse site.
8. **Realistic unit economics** (typical case, verified, $0.10/kWh, per GPU per month, before capex and internet): 3090 about $41, 4090 about $110, 5090 about $150, A100 PCIe about $190. A 32-GPU fleet of used 3090s brings in roughly **$1,850/month typical and $3,100 optimistic in host revenue before power**, or about $1,300 and $2,350 after power. A 1 Gbps symmetric business line, static IP, colocation or UPS costs and labour must come out of that. At ≤$0.05/kWh (Venezuela-type subsidized power) the power line barely matters; at $0.20/kWh it halves the 3090 margin.

---

## 4) Confidence and gaps

| Item | Confidence | Why |
|---|---|---|
| Vast occupancy by GPU, verification, reliability and region (S1/S2) | **Medium-high** for 2026-11-14 | Complete, non-truncated public-API capture. Matches Hashrate.no (75.7% vs 74.2%). Stable across two snapshots. Caveats below. |
| Realised 2026 earnings per verified 4090/5090 | **Medium** | Two independent first-hand sources bracket each other. The video figure is second-hand via a blog. |
| LATAM location price effect (≈ 0–10%) | **Medium-low** | Consistent direction, but n=156 GPUs, mostly 1–2-GPU boxes; one weekend timepoint. |
| ROI trend 2023→2026 | **Low-medium** | No dated 2023–24 price series accessible. Evidence is anecdotal plus Salad's confirmed 2026 rate changes and a 2026 third-party price scrape. |
| Pain points | **Medium** | Docs are confirmed; the frequency of abuse, disputes and unpaid earnings is unknown because Reddit and Discord were not accessible. |

**Snapshot caveats.**
- "Occupied" = not available for **on-demand** rental. It can include **free self-rentals by hosts**, which Vast allows, and reserved contracts.
- It excludes interruptible (bid) usage and hosts' default jobs. In other words, **occupancy ≠ paid third-party utilization**, and is an upper bound for a new host.
- Prices are list asks. Hosts can offer **reserved discounts of up to 50%** for pre-paid commitments (docs.vast.ai/guides/reference/faq/rental-types.md), so realised $/h can sit below list.
- It is a single Saturday midday (UTC) timepoint, and offline or unlisted machines are invisible. **Survivorship bias** applies: hosts who quit because of low earnings are not in the sample, which is why unverified occupancy (~53%) far exceeds new-host anecdotes (~0–20%).

**Gaps.**
- **No Reddit data:** r/vastai, r/LocalLLaMA, r/homelab and r/gpumining were blocked.
- Search was exhausted before I could cover:
  - X/Twitter, YouTube transcripts and Discord quotes;
  - Vast host-fee policy history;
  - Venezuelan and Colombian mining-community channels;
  - io.net worker earnings (the explorer page is JavaScript-only and returned no data);
  - TensorDock host terms.
- **Not resolved:** whether Wise, PayPal or Stripe B2B payouts work in Venezuela, Colombia and Ecuador; local electricity and internet prices (other agents' topics).
- **Suggested follow-ups:**
  - Repeat the snapshot hourly for 7+ days, including weekdays, to measure diurnal and weekly utilization and churn. The scripts are in the scratchpad.
  - Ask 2–3 Brazilian, Chilean or Argentine Vast hosts directly for dashboards.
  - Get a host API key and pull Vast's own `metrics/gpu/locations` and `gpu-trends` endpoints, which require a host key (docs.vast.ai/host/market-metrics).

---

## 5) Sources (all accessed 2026-11-14 unless noted)

**Primary data captured**
- Vast.ai public offer-search API (`https://console.vast.ai/api/v0/bundles/`): complete on-demand snapshots S1 (12:22–12:29 UTC) and S2 (12:29–12:36 UTC) on 2026-11-14. Raw files: `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent09/dl/snapmid_1.json` and `snapmid_2.json`. Scripts: `.../agent09/scripts/vastsnap_mid.py`, `analyze.py`, `breakdown.py`, `breakdown2.py`, `locindex.py`, `model2.py`.
- Akash console API: https://console-api.akash.network/v1/gpu and https://console-api.akash.network/v1/gpu-prices
- Hashrate.no Vast tracker: https://www.hashrate.no/platforms/vast and https://www.hashrate.no/platforms/vast/gpus
- GPU price tracker (scrape of Vast's public API, Feb–Oct 2026): https://github.com/woodsonl/gpu-pricing-tracker (`data/observations.csv`)

**Platform documentation and official posts**
- Salad host rate change (published 2026-09-04, effective 2026-09-12): https://blog.salad.com/earning-rate-changes-september-2026
- Vast, "How Much Money Can You Earn…" (2026-05-18): https://vast.ai/article/how-much-money-can-you-earn-renting-out-your-gpu-on-vast-ai
- Vast, "Scaling a GPU Hosting Business…" (2026-10-19): https://vast.ai/article/scaling-a-gpu-hosting-business-data-center-vs-home-server-rack-operations
- Vast docs:
  - https://docs.vast.ai/host/understanding-verification.md
  - https://docs.vast.ai/host/verification-stages.md
  - https://docs.vast.ai/host/optimization-guide.md
  - https://docs.vast.ai/documentation/host/hosting-overview
  - https://docs.vast.ai/host/payment.md
  - https://docs.vast.ai/host/using-your-own-machine.md
  - https://docs.vast.ai/host/datacenter-status.md
  - https://docs.vast.ai/host/market-metrics.md
  - https://docs.vast.ai/guides/reference/faq/rental-types.md
  - https://docs.vast.ai/cli/reference/search-offers
  - https://docs.vast.ai/llms.txt
- Clore.ai RTX 3090 hosting page: https://clore.ai/host-3090.html
- RunPod docs index: https://docs.runpod.io/llms.txt (https://www.runpod.io/host returned 404)

**First-hand and anecdotal**
- bytwork.com, "GPU Payback Period for AI Computing Rentals" (updated 2026-10-21): https://bytwork.com/en/articles/ai-income
- Endless Mining, summary of a RedPandaMining video (May 2026): https://endlessmining.com/renting-your-gpu-for-ai-2026/
- Sam Hartley, DEV Community (Jun 2026, edited Oct): https://dev.to/samhartley_dev/i-rented-out-my-gpu-for-passive-income-heres-what-happened-after-my-first-week-1mbh
- Trustpilot, Salad reviews (Oct–Nov 2026): https://www.trustpilot.com/review/salad.com
- Trustpilot, Vast.ai reviews (Sep 2026; TrustScore 3.8, 266 reviews): https://www.trustpilot.com/review/vast.ai
- Habr comment thread (Jun 2024): https://habr.com/en/articles/821203/comments
- Hacker News: https://news.ycombinator.com/item?id=48455436 (2026-06-09); https://news.ycombinator.com/item?id=36026101 (May 2023)
- Passive Yield Lab (2026-05-02, LOW-CRED): https://passiveyieldlab.com/blog/cloud-gpu-rental-passive-income-2026/

**Context and low-credibility secondary pages (not used for conclusions)**
- https://ownyourmind.ai/use/gpu-provider-income/ (2026-06-27, updated 2026-10-20; modelled; cites Akash Q1 2026 utilization of ~33.7% per Messari)
- https://miningboard.com/guides/rent-gpu-for-ai-earnings (Nov 2026; unsourced "60–85%" utilization claims)
- https://www.cloudearn.net/vastai/ (2026; unsourced)
- https://auradigitalglobal.com/blog/vast-ai-gpu-server-earnings/ (modelled)
- https://wovenai.ca/ (vendor; verification "~2–4 weeks"; ingests ">24,000 offers, 5,000 machines" per cycle)
- https://www.xataka.com/robotica-e-ia/puedes-ganar-dinero-tu-gpu-cuando-no-usas-basta-que-se-prestes-a-quienes-entrenan-modelos-ia (2025-09-09)
- https://github.com/GeiserX/CashPilot/blob/main/docs/guides/vast-ai.md

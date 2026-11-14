# Agent 04: DePIN / Crypto-Incentivized Compute Networks, Supplier Economics

**Research date:** 2026-11-14
**Scope:** io.net, Akash, Render, Aethir, Spheron, Fluence, NetMind, Exabits, Nosana (brief), and the Bittensor compute subnets (Lium SN51, Chutes SN64, Targon SN4, plus the status of SN27 and SN12).
**Method:** Wherever possible, numbers come from live public APIs and dashboards pulled on 2026-11-14: the io.net explorer API, Akash console API, Lium provider-economics API, Chutes nodes API, Targon auctions API, Nosana markets API, TaoMarketCap API and the Aethir dashboard. The rest comes from official docs and governance proposals. Token prices come from CoinGecko, Kraken, Coinbase and Gate public APIs.
**Labels:**
- **CONFIRMED** means read from a primary source on the stated date.
- **ESTIMATE / INFERENCE** means my own calculation or interpretation.
- **SECONDARY** means a third-party aggregator.

> Note: the shared web-search budget ran out partway through this task. Everything after that point was gathered by fetching known primary URLs and APIs directly. A few items, such as current Render burn statistics and Exabits supplier terms, could therefore not be fully verified. They are flagged in Section 4.

---

## 1. Executive summary

- **The token subsidy has mostly gone, because token prices collapsed (CONFIRMED).** From the January 2025 average to 2026-11-14:

  | Token | Jan 2025 | Nov 14, 2026 | Change |
  |---|---|---|---|
  | IO | $3.14 | $0.107 | −97% |
  | ATH | $0.056 | $0.0043 | −92% |
  | NOS | $2.54 | $0.36 | −86% |
  | AKT | $2.75 | $0.52 | −81% |
  | RENDER | $6.44 | $1.49 | −77% |
  | TAO | $425 | $208 | −51% |
  | FLT | $0.19 | $0.0023 | −99% |

  Over the last 12 months, NMT fell 78% and SPON fell 95%. Any income denominated in a fixed number of tokens fell by the same proportion. For example, io.net's daily block-reward budget is about 83.5k IO/day. That is worth roughly **$9k/day today, against roughly $300k/day at January 2025 prices** (ESTIMATE).
- **Across the networks that still pay, emissions are now a minority of supplier income.** Measured shares of supplier income from emissions:
  - io.net: **≈20%**. In the 2026-11-14 09:00 epoch, block rewards were $1,117 against $4,543 of supplier USD earnings.
  - Lium (Bittensor SN51): **≈17%** network-wide. Over 30 days, $0.52M came from emissions and $2.57M from renter fees.
  - Aethir: **≈4%** (INFERENCE). Gross emissions were ~31.5M ATH (≈$135k) over 30 days, against ~$3.5M/month of host revenue share.
  - Akash: **≈0%**. There is no provider-incentive program, and the take rate was removed under BME in March 2026.
- **The exceptions are 100% emission-paid.**
  - Bittensor SN64 (Chutes) and SN4 (Targon) miners are paid entirely in subnet alpha tokens. Chutes paid ≈$1.13M/30d and Targon ≈$1.05M/30d.
  - Render operators are paid in newly minted RENDER. Customer burns only partly offset this, so I estimate the net subsidy at **50–70%** (ESTIMATE, low confidence).
- **Demand has moved to data-centre Hopper/Blackwell GPUs. Consumer and old cards sit idle.**
  - io.net has 1,013 active GPUs, out of 1.06M ever registered. **960 of them are H100s from 6 suppliers.** Only 8 RTX 4090s are active network-wide.
  - Chutes has 4,318 GPUs registered and 523 provisioned (12%). **All 261 of its RTX 3090/4090/5090s are idle.**
  - Targon only accepts 8-GPU TDX/SEV confidential-compute H100/H200/B200/B300/RTX PRO 6000 clusters.
  - Aethir Earth (AI) requires enterprise bare metal with a 99% SLA.
- **The best-documented consumer-GPU economics are on Lium (SN51).** These are 30-day averages, rental plus emission, per GPU-month:
  - RTX 3090: **$139** (13% subsidy)
  - RTX 4090: **$302** (17% subsidy; median provider $340)
  - RTX 5090: $388 (19%)
  - A100 SXM4 80GB: **$927** (10%)
  - A100 PCIe 80GB: $535
  - H100 SXM: **$1,294** (21%; median $1,400)
  - H200: $2,812
- **Akash demand is real but tiny and concentrated.**
  - 54 providers and 457 GPUs (291 leased, 64%) as of 2026-11-14.
  - Network spend is about $10k/day, and peaked at $288k/month in August–September 2026.
  - Live median bids per GPU-hour: H100 $2.56, A100-80G $1.49, RTX 4090 $0.36, RTX 3090 $0.16, V100 $0.21–0.31.
  - A secondary source says the top two payers account for ~90% of paid lease demand.
- **Several networks closed their supply side to small operators, or effectively died.**
  - **Fluence** closed its chain on 2026-04-01 and now accepts only Tier 3/4 data centres after a KYB review.
  - **Spheron** is now a B2B aggregator of 6 data-centre providers.
  - **NetMind** reward rates are still "Coming soon" in its docs. NMT has a $2.4M market cap and about $4k/day of volume.
  - **Bittensor SN27** is now "Komms" with zero emission; the Neural Internet compute subnet is gone. **SN12** (Compute Horde) emits about 0.09 TAO/day.
- **Stakes and fees are cheap in USD today.** That cuts both ways: the stake is cheap, but it also signals low token value.
  - io.net: 200 IO × the device multiplier. That is about $21 for an RTX 4090, or 2,000 IO ≈ $214 for an H100.
  - Aethir: 6,324 ATH (≈$27) per RTX 4090, 15,785 ATH (≈$68) per A100-80G, 45,095 ATH (≈$194) per H100.
  - Bittensor SN51 registration burn: 0.5 TAO (≈$104). Lium also offers a no-registration path.
- **Geographic and KYC barriers are moderate.** Colombia and Ecuador are not on any restricted list I found. **Venezuela is a grey zone:**
  - io.net's terms bar users "on a sanctions or restricted list... including but not limited to" a list that does not name Venezuela.
  - Aethir's KYC excludes the US and comprehensively OFAC/UN-sanctioned countries, which does not explicitly include Venezuela.
  - US/EU targeted sanctions on Venezuela create counterparty and off-ramp risk.
- **Bottom line:** the only DePIN networks worth putting in a LATAM used-hardware business plan are:
  - **Lium/SN51**, as a secondary channel. It has USD-priced rentals, a USDT payout option, accepts consumer GPUs, and has a subsidy of only about 17%.
  - Possibly **Akash** (self-run provider or Homenode) and **Nosana**, as opportunistic extra channels.

  Do not model any income that depends on emissions (io.net block rewards, Chutes, Targon, Render, Aethir PoC). It has fallen 75–97% in USD in 22 months and can fall further.

---

## 2. Detailed findings

### 2.1 Token price trend, 2025 to 2026 (CONFIRMED, exchange APIs)

Monthly averages of daily or weekly closes. FLT uses Gate 30-day candle closes. "Now" is the CoinGecko spot price on 2026-11-14.

| Token (network) | Jan 2025 | Jul 2025 | Jan 2026 | Jul 2026 | Now (2026-11-14) | Jan-25 → now | Market cap now |
|---|---|---|---|---|---|---|---|
| IO (io.net), Coinbase | $3.14 | $0.75 | $0.16 | $0.156 | **$0.107** | **−97%** | $46M |
| AKT (Akash), Kraken | $2.75 | $1.26 | $0.43 | $0.53 | **$0.516** | **−81%** | $155M |
| RENDER, Kraken | $6.44 | $3.80 | $1.99 | $1.46 | **$1.49** | **−77%** | $828M |
| ATH (Aethir), Kraken | $0.0565 | $0.0327 | $0.0092 | $0.0043 | **$0.0043** | **−92%** | $87M |
| TAO (Bittensor), Kraken | $425 | $385 | $246 | $198 | **$208** | **−51%** | $2.44B |
| NOS (Nosana), Kraken | $2.54 | $0.57 | $0.25 | $0.26 | **$0.358** | **−86%** | $36M |
| FLT (Fluence), Gate | $0.189 | $0.045 | $0.004 | $0.0014 | **$0.0023** | **−99%** | $0.8M |
| NMT (NetMind), CoinGecko | n/a | n/a | $0.157 | $0.045 | **$0.037** | −78% (12 months) | $2.4M |
| SPON (Spheron), CoinGecko | n/a | n/a | $0.014 | $0.0004 | **$0.00046** | −95% (12 months) | $0.1M |

What this means for supplier USD income:

- **Fixed-token emissions lost 51–99% of their USD value.** This applies to block rewards, availability rewards and alpha emissions.
- **Rewards with vesting add more price risk.** Aethir rewards vest 30% at once, 30% at 90 days and 40% at 180 days. A host earning in January 2025 and selling on vest dates realized much less than the "earned" figure.
- **USD-pegged schemes protect only the customer-paid part.** These are io.net's IDE (live 2026-06-01), Akash BME/ACT (live 2026-03-23), Aethir service fees (USD-priced), Lium rental fees (USD), Nosana (USD/hr markets) and Salad-on-Render (USD-accrued). The supplier still carries token risk between settlement and sale. On Aethir that window is a 45-day vest.

### 2.2 io.net (IO workers)

**Live network state (CONFIRMED, io.net explorer API, 2026-11-14):**

| Metric | Value |
|---|---|
| GPUs ever registered / "verified" | 1,061,267 / 327,085 |
| **Active GPUs** | **1,006–1,013** |
| Passive (connected, not working) | 366 |
| Devices in up/paused state | 169 |
| H100 80GB HBM3 active | 960 (120 devices, **6 suppliers**). All 960 are hired. |
| RTX 4090 active | **8** (1 device) |
| RTX A6000 | 5 active / 124 total (4%) |
| L40S | 8 active / 53 total |
| A100 (all variants) | about 1 active of about 70 listed |
| RTX PRO 6000 Blackwell | 2 active / 90 listed |
| H200 | 0 active / 9 listed |

**Customer revenue to suppliers vs block rewards:**

| Item | Value | Source |
|---|---|---|
| Monthly cluster earnings, May–Oct 2026 | $1.10M, $1.05M, $0.93M, $0.85M, $0.92M, $1.13M | API `network/info/cluster/monthly-earnings` |
| Last 30 days | $1.29M customer earnings over 966k compute-hours (**$1.33 per GPU-hour**; ~1,341 GPUs busy on average) | API daily series |
| One epoch (3 h, 2026-11-14 09:00–12:00) | Block rewards 10,437.5 IO = **$1,116.6**; supplier earnings **$4,543.4** | API `tokenomics/epochs/{id}` |
| **Subsidy share** | 1,116.6 / (1,116.6 + 4,543.4) = **19.7%** | INFERENCE from the API |
| IDE since 2026-06-01 | 14.02M IO emitted, 6.98M IO purchased, 2.91M IO burned | API `tokenomics/epochs` |
| "open_debt" field | $1,143,089. The meaning is not documented. It may be supplier earnings accrued but not yet paid. **Flag.** | API |

**Block reward per GPU-hour by model, epoch 2026-11-14 09:00, IO = $0.107 (CONFIRMED, my calculation from per-device reward records):**

| GPU | IO per GPU-hour | USD per GPU-hour | USD per GPU-month (730 h) |
|---|---|---|---|
| B300 SXM6 | 9.37 | $1.00 | $732 |
| H100 SXM / H100 PCIe | 3.47 | $0.371 | **$271** |
| RTX PRO 6000 Blackwell | 1.39 | $0.149 | $109 |
| L40S | 1.04 | $0.111 | $81 |
| **RTX 4090** | 0.434 | $0.046 | **$34** |
| L40 / RTX A6000 | 0.30–0.34 | $0.03 | $23–26 |
| A100 SXM4 80GB (1 GPU) | 0.126 | $0.013 | $10 (anomalously low; possibly partial uptime) |

**io.net listing prices per GPU-hour (CONFIRMED, `network/market-snapshot`):**

| GPU | Base price | Bare metal | VM | Kubernetes |
|---|---|---|---|---|
| H100 SXM | $1.19 | $1.79 | $1.99 | – |
| A100 SXM4 | $0.74 | – | $1.29 | – |
| L40S | $0.79 | – | – | – |
| RTX 4090 | $0.25 | – | $0.30 | $0.42 |
| T4 | $0.05 | – | – | – |

**Requirements (CONFIRMED, io.net docs):**
- Supported list includes the RTX 30/40/50 series, V100, T4, A100, H100/H200/B200 and Apple M3/M4.
- 12 GB RAM, 256 GB SSD, 100/75 Mbps, and Proof-of-Work verification.
- Block-reward eligibility needs uptime green for 5 hours, the minimum stake, and a self-custody Solana wallet. Exchange deposit addresses are not allowed.
- **Stake: 200 IO × max(1, multiplier) per GPU.** An H100 has multiplier 10, so 2,000 IO ≈ $214. Unstaking has a 14-day cooldown. Rewards can be slashed.
- Emission schedule: 300M IO over 20 years, decaying about 1.02% per month. Live epochs pay about 10,437 IO per 3 h, roughly 83.5k IO/day. Of this, 95% goes to GPUs and 5% to CPUs.

**Geographic restrictions (CONFIRMED, io.net Terms, effective 2026-09-21):**
- Users must not be on US/EU/UK sanctions lists or "physically located in a country on such a list... including but not limited to" Afghanistan, Belarus, CAR, Crimea, Cuba, Eritrea, Iran, Iraq, Lebanon, Libya, Mainland China, Myanmar, North Korea, Somalia, Syria, Sudan, Donetsk and Luhansk.
- Venezuela is not named, but the wording is open-ended. Colombia and Ecuador are not affected.

**Assessment:**
- io.net is now effectively a broker for a handful of H100 suppliers.
- A new RTX 4090 or A100 supplier would most likely sit "passive", earning only block rewards of about $34/month (4090) if eligible. That income is 100% subsidy and shrinks with the price of IO.

### 2.3 Akash Network (providers)

**Live network state (CONFIRMED, console-api.akash.network, 2026-11-14 12:00 UTC):**
- 54 active providers.
- GPUs: 457 total, 291 active (63.7% leased), 164 available.
- Active leases: 727. Daily spend: **$10,006**.
- Chain inflation 4% (goes to stakers and validators, not providers). Community pool: 4.07M AKT.

**Akash monthly spend and average GPUs leased (CONFIRMED, graph-data API):**

| Month | USD spent | Average GPUs leased |
|---|---|---|
| Jan 2025 | $357k | 580 |
| Feb 2025 | $357k | 620 |
| Sep 2025 | $214k | 302 |
| Jan 2026 | $104k | 112 |
| Feb 2026 | $64k (low) | 65 |
| Jun 2026 | $220k | 138 |
| Aug 2026 | $288k | 157 |
| Sep 2026 | $288k | 196 |
| Oct 2026 | $207k | 165 |
| Nov 1–14, 2026 | $120k | 206 |

**Live GPU bid prices per GPU-hour (CONFIRMED, `/v1/gpu-prices`, 2026-11-14):**

| GPU | Count (leased / total) | Median | Range |
|---|---|---|---|
| H100 SXM5 80G | 44 / 56 | **$2.56** | $2.55–3.16 |
| A100 SXM4 80G | 122 / 200 | **$1.49** | $1.07–1.91 |
| RTX PRO 6000 SE 96G | 66 / 89 | $2.18 | – |
| RTX 4090 | 2 / 2 | **$0.36** | – |
| RTX 5090 | 1 / 2 | $0.58 | – |
| RTX 3090 | 11 / 11 | **$0.16** | $0.09–0.17 |
| V100 SXM2 32G | 9 / 40 | $0.31 | – |
| V100 PCIe | – | $0.21 | – |
| T4 | – | $0.14 | – |
| P40 | – | $0.14 | – |

**Economics (CONFIRMED, governance and docs):**
- The legacy take rate (4% on AKT, 20% on USDC) was **retired by BME/Mainnet 17 on 2026-03-23**. Customers burn AKT to mint ACT, a USD-pegged credit. Providers redeem ACT for AKT at market price on settlement.
- **No provider-incentive program is active in 2025–26** (SECONDARY, ownyourmind.ai; no live program found in governance).
- Provider income is therefore about **100% customer-paid**. It is USD-denominated but settled in AKT, which has to be sold.
- Solana migration: Proposal 346 passed on 2026-11-02 with 97% in favour. The cutover date is not set, and staking inflation ends at cutover (SECONDARY).

**Homenode (consumer GPUs: RTX 3090, 4090, 5090 and RTX Pro 6000):**
- Early access opened 2026-02-25; open beta opened 2026-08-10.
- Earnings are pooled. Operators split **70% of cluster revenue** by GPU-count × uptime score, and Akash keeps a 30% fee.
- Payouts are computed in USD and paid in AKT. **Identity verification is required before payout** (CONFIRMED, homenode.akash.network/docs/earnings).
- Akash's own marketing estimate for an RTX 4090 is **$2,698/yr (≈$225/month)**, assuming $0.55/h at 80% utilization, net of the fee. Treat this as optimistic.

**Requirements:**
- A self-run provider needs Kubernetes, a public IP/domain and an always-on server-grade setup.
- It is permissionless, with **no KYC to provide** (SECONDARY).

**Assessment:**
- Akash has the cleanest economics (no subsidy) but a tiny market: 457 GPUs and about $3M/yr of spend in total.
- It is a viable extra channel for a few A100/H100 cards. It is not a primary market, especially for consumer cards: there are only 2 RTX 4090s on the whole network.

### 2.4 Render Network (node operators)

**Emissions (CONFIRMED, RNP-022, Year 3 BME allocation, created 2025-12-05, implemented):**
- 5.9M RENDER for Dec 2025–Dec 2026: 1.5M for grants, **1.5M for node rewards** (rendering plus compute), and 2.9M for the Foundation, operations and R&D.
- Rendering-node rewards: **15k RENDER/week job rewards plus 2.8k/week availability = 17.8k RENDER/week**. That is about **$115k/month** at $1.49 (ESTIMATE).

**Render Compute Network, the AI subnet (CONFIRMED, RNP-019, created 2025-03-31, implemented):**
- Customers fund jobs in USD or RENDER. **95% of customer credits buy RENDER and burn it; 5% goes to OTOY.** Operators draw from an **emissions tranche**.
- Availability: 2 RENDER per weekly epoch per node, prorated by uptime.
- Job reward: **10 RENDER per epoch for an RTX 4090 at 100% utilization** × a spec multiplier. RTX 5090 = 1.7, RTX 3090 is lower. The Foundation may raise this up to 3×.
- For an RTX 4090 at 100% utilization: 12 RENDER/week ≈ 52 RENDER/month ≈ **$77/month** at today's price, or up to about $230 if tripled (ESTIMATE).
- The customer-facing price benchmark is $0.35/h for an RTX 4090 and $0.31/h for an RTX 3090.
- Onboarding is by waitlist, with a Solana wallet. No stake at the start; the first $100 earned is held as an implicit stake.

**Salad migration (CONFIRMED, RNP-023, created 2026-03-26, "Approved + Roadmap"):**
- Salad has "**60,000 daily heartbeating GPUs**" and illustrative year-1 revenue of about **$4.3M**.
- Its "Chef" rewards are estimated at about **88,000 RENDER/month**, about $176k at the RNP's assumed $2 price. Related burns are about 95,000 RENDER/month, designed so that burns exceed mints.
- That works out to roughly **$3 per GPU per month** on average across Salad's consumer fleet (INFERENCE). This is strong evidence that consumer-GPU supply is massively oversupplied relative to demand.

**Subsidy share:**
- By design, all Render operator payments are newly minted. Customer burns offset the dilution, not the supplier's income.
- A secondary source puts burns at about 50k RENDER/month against about 500k emitted (late 2025).
- My estimated net subsidy share of operator income is **50–70%** (ESTIMATE, low confidence; I could not fetch the current burn dashboard).

**Assessment:** low, emission-heavy income for consumer GPUs, gated by a waitlist, with Salad's 60k GPUs as competition. Not worth including.

### 2.5 Aethir (Cloud Hosts vs Edge and Checker)

**Network (CONFIRMED, dashboard.aethir.com, 2026-11-14):**

| Metric | Value |
|---|---|
| **Annual recurring revenue** | **$47.68M** |
| Total network revenue since June 2024 | $197.6M |
| Containers | 433,505 in 94 countries (mostly gaming/edge containers) |
| Compute-hours delivered last week | 22.2M (≈$0.04 average revenue per container-hour) |
| **Cloud Host revenue share** | **89.13%** (adaptive since Tokenomics 2.0; previously a fixed 80%) |
| Gross ATH emissions, last 30 days | 31.48M ATH (≈$135k) |
| ATH burned since Nov 2026 launch | 6.26M |
| ATH staked by Cloud Hosts | 867M (≈$3.7M) |
| Checker licenses delegated | 84,618 |

**Host economics (CONFIRMED, docs):**
- **Service fees:** priced in USD, set uniformly by Aethir per region and spec, settled in ATH at the order-time rate, and **vesting for 45 days**.
- **Rewards:** Proof of Capacity and Proof of Delivery, split 50/50 by the utility ratio, with a 5% fee. They **vest 30% immediately, 30% at 90 days and 40% at 180 days**.
- **Slashing:**
  - More than 30 minutes offline in a day loses that day's service fee.
  - More than 60 minutes loses that day's rewards.
  - The SLA requires 99% monthly uptime and a 15-minute response to P0 incidents.

**Subsidy share (INFERENCE):**
- About $135k/30d of emissions against about $3.5M/month of host revenue share (ARR × 89% ÷ 12) gives roughly **4%**. Around early 2025, the same token count was worth about 13× more and emissions were higher, so the subsidy was far larger then.
- Caveat: the dashboard does not define whether "gross emissions" covers all host rewards.

**Requirements (CONFIRMED):**
- **Aethir Earth (AI):** application form, enterprise-grade GPUs, x86 bare metal, Ubuntu 20.04/22.04, public IP, the 99% SLA and the escalation obligations above. GPUs located in China or OFAC/UN-sanctioned regions are rejected.
- **Aethir Atmosphere (cloud gaming):** accepts RTX 3080–5090 Windows containers, but demand depends on region.
- **Stake** (coefficient as of 2025-12-22):

  | GPU | ATH stake | ≈ USD |
  |---|---|---|
  | RTX 3090 | 2,787 | $12 |
  | RTX 4090 | 6,324 | $27 |
  | A100 80G | 15,785 | $68 |
  | H100 | 45,095 | $194 |
  | 8× H100 | 360,763 | $1,550 |

- **KYC (ComPilot) is required to claim**, or KYB through Sumsub. It excludes the **USA** and comprehensively sanctioned regions (Cuba, Iran, North Korea, Syria, Crimea, DNR, LNR). Venezuela is not listed.
- **Edge and Checker are not compute supply.** Checker licenses sold out in March 2024 and a buyback paying in eATH started 2025-05-27. Aethir Edge is a proprietary device. Neither is a way to monetize your own used GPUs.

**Assessment:**
- Aethir pays mostly real revenue now, but only to enterprise hosts that can sign up to an SLA.
- The 45- to 180-day vesting in a token that fell 92% is a serious working-capital risk.
- Not realistic for a used-hardware start-up in LATAM, unless it runs a proper data-centre H100/H200 deployment.

### 2.6 Bittensor compute subnets

**Subnet status (CONFIRMED, TaoMarketCap API, block 9,504,556, 2026-11-14; TAO = $207.95):**

| Netuid | Name | Emission share | Miner TAO/day | ≈ USD/30d to miners | Registration burn | Status |
|---|---|---|---|---|---|---|
| 51 | **lium.io** (Celium successor) | **16.9%** (#1 subnet) | 427.8 | $2.67M (most of it burned; see below) | 0.5 TAO ≈ $104 | Active; GPU rental marketplace |
| 64 | **Chutes** | 8.7% | 181.4 | ≈$1.13M | 0.0005 TAO | Active; serverless inference |
| 4 | **Targon** | 8.0% | 168.3 | ≈$1.05M | 0.0005 TAO | Active; confidential-compute auctions |
| 27 | "Komms" (was Neural Internet) | 0% | 0 | $0 | – | **The compute subnet is gone** |
| 12 | Compute Horde | 0% | 0.09 | ~$0 | – | Effectively dead |

**Lium SN51: the most decision-relevant DePIN data point**

Per GPU-month, 30-day window to 2026-11-14 (CONFIRMED, `provider-api.lium.io/public/provider-economics`). "Rental share" is 95% of renter USD; idle pay and rented extra are emissions.

| GPU | Average renter price per hour | Utilization | Rental share | Idle pay | Rented extra | **Total** | **Subsidy %** | Live GPUs (rented) | Median provider |
|---|---|---|---|---|---|---|---|---|---|
| B200 | $6.27 | 78% | $3,381 | $471 | $297 | $4,149 | 18.5% | 126 (119) | $4,000 |
| H200 | $4.04 | 84% | $2,347 | $219 | $246 | $2,812 | 16.5% | 192 (179) | $2,800 |
| **H100 80GB SXM** | $2.14 | 69% | $1,022 | $185 | $87 | **$1,294** | **21.0%** | 117 (67) | $1,400 |
| H100 PCIe | $1.78 | 83% | $1,024 | $52 | $95 | $1,171 | 12.6% | 17 | – |
| **A100 SXM4 80GB** | $1.39 | 86% | $834 | $49 | $44 | **$927** | **10.1%** | 38 (38) | – |
| A100 PCIe 80GB | $0.69 | 99% | $476 | $2 | $57 | $535 | 11.1% | 14 | – |
| RTX PRO 6000 Blackwell Server | $1.71 | 77% | $910 | $162 | $83 | $1,155 | 21.2% | 138 | $1,100 |
| RTX 6000 Ada | $0.82 | 73% | $411 | $92 | $40 | $542 | 24.3% | 41 | $620 |
| L40S | $0.44 | 82% | $251 | $13 | $26 | $290 | 13.4% | 67 | – |
| RTX A6000 | $0.43 | 74% | $217 | $19 | $21 | $257 | 15.6% | 79 | – |
| RTX 5090 | $0.59 | 77% | $313 | $45 | $30 | $388 | 19.2% | 489 (301) | $510 |
| **RTX 4090** | $0.48 | 75% | $250 | $28 | $25 | **$302** | **17.3%** | 193 (82 live) | $340 |
| **RTX 3090** | $0.20 | 86% | $120 | $7 | $12 | **$139** | **13.3%** | 112 (83) | $160 |
| RTX 5070 Ti | $0.28 | 43% | $84 | $26 | $5 | $115 | 27.1% | 34 | – |

- **Network total, 30 days (INFERENCE from the same API):** $2.57M rental fees plus $0.52M emissions to providers, so a **16.7% subsidy share**.
- The SN51 validator burns most of the miner emission: the burn pool takes the share of the 93% ceiling that is not paid as idle pay. Only about 19% of the $2.67M/30d miner emission reaches providers. Lium has deliberately capped the subsidy.
- **Older cards (V100, P100, T4, 1080 Ti, 2080 Ti):** listed with base prices of $0.04–0.17/h, but **0 live GPUs** in the economics data. Effectively no demand.

**Lium requirements and payouts (CONFIRMED, docs.lium.io, docs dated 2026-10-15):**
- **Path A:** sign up with an e-mail or Google account. **No registration fee, no hotkey.** Rental fees and emissions are paid **daily in USDT on Ethereum**, with a 5% conversion fee, a $5 minimum and a $25k/day cap.
- **Path B:** your own SN51 hotkey (0.5 TAO burn). Paid in alpha, which you unstake to TAO with no unbonding.
- Node requirements:
  - Ubuntu 22.04 with the HWE kernel, or 24.04/26.04. Docker plus Sysbox.
  - **Public IP with ports 8080, 2200 and at least 3 rental ports open.** At least 100 Mbit/s, 8 GB RAM and 150 GB disk.
  - For idle pay, disk of at least 1.5× total VRAM. Discord must be connected and the e-mail confirmed.
- **Penalty:** a dropped rental on a "Secure" node costs 24 hours of that rental's price. On 8× H100 that is about $365.
- **No KYC or country restrictions appear in the provider docs.**

**Chutes SN64 (CONFIRMED, `api.chutes.ai/nodes/` and docs):**
- 4,318 GPUs registered, **523 provisioned (12%)**: H200 240, PRO 6000 195, B200 48, B300 40.
- All consumer and Ampere cards are idle: 3090 (112), 4090 (74), 5090 (75), A100 SXM (105), A6000 (231), and so on.
- Miners are paid **only in alpha emissions**, weighted by 7-day compute time plus bounties.
- Requirements: a K3s Kubernetes cluster, a CPU control node with 8 cores and 64 GB RAM, unique static IPs, and no Runpod or Vast hosts.
- Network average (INFERENCE): ≈$1.13M/30d ÷ 523 provisioned ≈ $2,160 per provisioned high-end GPU-month. ≈$0 for idle consumer cards.

**Targon SN4 (CONFIRMED, tower.targon.com/api/v2/auctions, 2026-11-14):**
- Auctions only for confidential VMs (Intel TDX or AMD SEV), **minimum cluster of 8 cards**.

  | Auction | Target price per card-hour | Cap | Target cards |
  |---|---|---|---|
  | H100 | $2.50 | $3.00–4.00 | 240 |
  | H200 | $2.90 | $3.50–4.50 | – |
  | B200 | $4.20 | – | – |
  | B300 | $6.50 | – | – |
  | RTX PRO 6000 Blackwell | $1.20 | – | – |
  | SEV CPU (EPYC) | $0.10 | – | – |

- Payment is **100% alpha emissions**. The per-card rate falls as more cards join, and unallocated emissions are burned.
- No consumer or Ampere GPUs are eligible.

### 2.7 Other networks (brief)

| Network | Supply side today | Pay basis | Accessible to a LATAM used-hardware operator? |
|---|---|---|---|
| **Nosana** (live `api.nosana.com/api/markets/`) | USD-denominated host rates per GPU-hour, paid in NOS, 10% network fee. Premium / Community tiers: RTX 4090 **$0.364**; RTX 3090 $0.17 / $0.13; A100-80G $0.82 / $0.61; H100 $1.36 / $1.02; RTX 5090 $0.45. Premium 4090/5090 also get an uptime reward of up to $1.76 / $2.18 per day. Target utilization 60%. | Mostly customer-priced, with a small uptime bonus | Yes, consumer GPUs. Premium markets need an application. Covered in depth by agent 03. |
| **Fluence** | **Chain closed 2026-04-01.** Providers must be **Tier 3/4 data centres with KYB**, bare metal, 10 GbE or better. FLT staking now earns rewards plus a share of protocol revenue. | USD cloud revenue | No |
| **Spheron** | Now an aggregated GPU cloud sourcing from **6 data-centre providers** (Verda and Spheron-branded regions). Providers integrate an orchestrator API or answer a "GPU demand board". SPON is worth $0.00046. | B2B | Only as a data centre |
| **NetMind** | Accepts consumer GPUs from GTX 10-series to 4090 and A100, at 100 Mbps or more. **NMT reward rates per hour are listed as "Coming soon" for every tier**, and the utilization reward is "not active". NMT has a $2.4M market cap and $4k/day of volume. | NMT | Technically yes, economically no (no liquidity to sell into) |
| **Exabits** | Website lists GB200/H100/H200/RTX 5090. No public supplier or token program found. | – | Unverified; assume B2B or institutional only |
| **Render** | See 2.4. | Minted RENDER | Waitlist; low pay |

### 2.8 Hardware, stake and KYC matrix

| Network | Consumer GPUs (3090/4090/5090) | Old data-centre GPUs (V100/T4/P40/A100-40G) | CPU-only | Stake or collateral | KYC / geography |
|---|---|---|---|---|---|
| io.net | Supported, but ~0 demand (8 active 4090s) | V100/T4/A100 supported; ~idle | Apple M3/M4 only | 200 IO × multiplier per GPU ($21 for a 4090; $214 for an H100), 14-day cooldown | Terms bar sanctioned or listed countries ("including but not limited to"); self-custody Solana wallet |
| Akash (provider) | Yes (2× 4090, 11× 3090 on the network) | V100 $0.21–0.31, T4/P40 $0.14; low utilization | Yes (CPU utilization ≈26%, Q1 2026, SECONDARY) | None for providers | Permissionless, no KYC (SECONDARY) |
| Akash Homenode | 3090/4090/5090/Pro 6000 | No | No | None | ID verification before payout |
| Render | Compute subnet: RTX 30/40/50 | Enterprise path (RNP-021) | No | None at start ($100 implicit hold) | Waitlist; Solana wallet |
| Aethir | Atmosphere (gaming) only | Earth needs enterprise GPUs | No | ATH per GPU (table above); slashable | KYC/KYB; excludes US and OFAC/UN comprehensive regions; rejects GPUs in China or sanctioned regions |
| Lium SN51 | Yes (5090: 489, 4090: 193, 3090: 112 live) | Listed but 0 live | No | None (Path A) or 0.5 TAO registration | E-mail/Google plus Discord; no KYC stated; public IP required |
| Chutes SN64 | Accepted but all idle | A100s idle | No | Registration (~0 TAO now) | Permissionless; static IPs |
| Targon SN4 | No | No | SEV EPYC v4 auction | Registration; 8-GPU TDX/SEV clusters | Permissionless |
| Nosana | Yes | A100/A40/A6000 | No | Premium markets by application | Solana wallet |
| Fluence / Spheron | No (data centre only) | Data centre only | Fluence CPU (data centre) | – | KYB (Fluence) |

### 2.9 Off-ramp practicality for a LATAM operator

General knowledge, not re-verified this session because the search budget was exhausted. Each exchange's country support must be checked before relying on it.

| Income token | Chain | Path to USD stablecoin | Notes |
|---|---|---|---|
| **Lium: USDT** (Path A) | Ethereum | Already USDT (5% Lium fee; ETH gas is paid by Lium) | **Simplest.** USDT then goes to local fiat (see below). |
| SN51 alpha (Path B) | Bittensor | Unstake to TAO (pool price, slippage on large amounts), then a TAO/USDT exchange (Kraken, Gate, MEXC and others) | Alpha pools are thin: about 545k TAO market cap for SN51 |
| IO | Solana | Jupiter DEX to USDC on Solana | Liquid enough; $46M market cap |
| AKT | Cosmos, moving to Solana SPL | Osmosis or a CEX now; Solana DEX after cutover | Migration and portal risk during the transition |
| ATH | Arbitrum / Ethereum | Uniswap or a CEX | Plus 45- to 180-day vesting before you can sell |
| RENDER / NOS | Solana | Jupiter to USDC | Liquid |
| NMT / SPON / FLT | Various | Very thin liquidity | Effectively not off-rampable at scale |

Converting stablecoins to local currency:
- **Ecuador** is dollarized, so the issue is only USDT/USDC to a USD bank account via an exchange or OTC desk.
- **Colombia:** USDT to COP through regulated local exchanges or P2P markets.
- **Venezuela:** USDT is the de facto unit of account and P2P USDT↔VES markets are deep. However, US/EU sanctions programs on Venezuela make many US/EU-regulated exchanges and DePIN foundations treat Venezuelan users as higher risk. Expect account blocks, so keep a Colombian or Ecuadorian legal entity and wallet for payouts. This is INFERENCE; verify with agent 10's legal findings.

---

## 3. Implications for the LATAM used-hardware rental business

1. **DePIN token rewards are no longer a business model, only a small top-up.**
   - Where networks still pay meaningfully, real customer revenue is now 80–100% of supplier income (io.net ~80%, Lium ~83%, Aethir ~96%, Akash ~100%).
   - Where income is 100% emissions (Chutes, Targon, Render), access is limited to high-end confidential-compute GPUs (Chutes, Targon) or is low and gated (Render).
   - Any plan that counts on "earning tokens while idle" should model that line at **$0 in the base case**. Token prices fell 51–99% in 22 months, and emissions decay by design: io.net about −1% per month, Aethir on a decay curve, Bittensor halvings.
2. **The used-hardware thesis runs into a demand cliff for consumer and old data-centre cards.**
   - Chutes: all 261 consumer GPUs idle.
   - io.net: 8 active RTX 4090s network-wide; A100s about 1 active out of about 70.
   - Akash: 2× 4090, 11× 3090, 40 V100s with 22% leased.
   - Salad, now on Render: about $3 per GPU-month on average across 60k GPUs.
   - Lium is the exception: its 4090/3090 fleet is 75–86% utilized. But that is a fleet of only 193 RTX 4090s and 112 RTX 3090s. Adding 50–100 more cards would push down prices and per-GPU idle pay, which is capped per tier and shared.
3. **Realistic DePIN revenue per card is far below hyperscaler-implied payback.**
   - Using Lium's 30-day actuals (the best case found): RTX 3090 **≈$140/month**, RTX 4090 **≈$300**, A100-80G SXM **≈$930**, H100 SXM **≈$1,300**, gross before power, bandwidth and penalties.
   - Akash would pay A100-80G **≈$660** and H100 **≈$1,470** at current median bids and utilization. That assumes you win leases in a market where about two customers drive about 90% of spend.
4. **Infrastructure prerequisites hurt in LATAM.**
   - Lium, Akash, Chutes and Aethir all need a **static public IP and inbound ports**. Residential connections in Colombia, Venezuela and Ecuador are often behind CGNAT, so plan for business fiber with a static IP.
   - Aethir and Lium penalize downtime hard:
     - Lium: a dropped Secure rental costs 24 hours of its price.
     - Aethir: more than 30–60 minutes offline per day forfeits that day's fees or rewards.
   - Grid reliability is therefore a direct revenue risk. Venezuela and Ecuador both had rationing episodes; see agent 08.
5. **Payment rails matter.** Lium's USDT-on-Ethereum payout, which avoids token risk on income and costs 5%, is the most practical for LATAM. Aethir's 45- to 180-day vesting and Akash's AKT-to-Solana migration add working-capital and operational risk. **Do not run payouts through a Venezuelan entity or identity.** Use Colombia or Ecuador.
6. **Where DePIN fits:** as an **overflow and idle-time channel** for GPUs whose main market is Vast/RunPod-style rental (agents 02 and 09), not as the main revenue driver.
   - For RTX 3090/4090/5090: list on Lium (and possibly Nosana or Akash Homenode) when they are not rented elsewhere.
   - For A100/H100, if the business ever acquires them: Lium and Akash are viable. Aethir and Targon require enterprise or confidential-compute data-centre builds.

### Final comparison table

"Realistic" means expected gross USD per GPU-month at current prices and observed utilization for a *new* small supplier. Live data from 2026-11-14 unless noted.

| Network | RTX 4090 / month | A100 80GB / month | H100 80GB / month | % of supplier income from emissions | Risk |
|---|---|---|---|---|---|
| **Lium (SN51)** | **$250–340** (avg $302, median $340) | **$535–930** (PCIe–SXM4) | **$1,170–1,400** (avg $1,294) | **10–24% by model (17% network)** | **Medium.** Token is USD-priced with a USDT option; the risk is competition from new supply. |
| **Akash** (own provider) | $130–260 (if leased at $0.36/h; only 2 on the network) | ~$660 (median $1.49/h × 61% leased) | ~$1,470 (median $2.56/h × 79%) | **~0%** | **Medium-High.** Tiny, concentrated demand; AKT settlement; Solana migration. |
| Akash Homenode | $150–225 (Akash's own estimate $225) | n/a | n/a | ~0% | Medium-High (beta, pooled, ID check) |
| Nosana | $160–265 (at 60–100% of $0.364/h) + ≤$53 uptime bonus | $360–600 (premium $0.82/h) | $600–995 (premium $1.36/h) | Low (uptime bonus only) | Medium-High (application-gated, NOS settlement) |
| io.net | **$35–200** (block reward $34 if idle-eligible; hire unlikely) | $10–550 (≈1 of 70 A100s active) | $270 idle-eligible; ~$1,140 if hired ($869 + $271) | **~20% network; 100% if idle** | **High.** Supply concentrated in 6 H100 suppliers; "open_debt" $1.14M; IO −97%. |
| Aethir | n/a (gaming-only path) | n/a public (enterprise bare metal) | ESTIMATE $900–1,300 if reserved (USD service fee × 89%) | **~4% now** (INFERENCE) | **High** for small operators (SLA, KYC, 45–180-day vesting, slashing) |
| Render | ~$77 (12 RENDER/week at 100% utilization; up to ~$230 if tripled) | n/a | n/a | **50–100%** (minted; ESTIMATE) | High |
| Chutes (SN64) | ≈$0 (all consumer GPUs idle) | ≈$0 (A100s idle) | Not public (H200/B200 TEE capture emissions) | **100%** (alpha) | High |
| Targon (SN4) | Not eligible | Not eligible | Up to ~$1,825 target ($2.50/h) for 8× H100 TDX clusters | **100%** (alpha) | High |
| Fluence / Spheron / NetMind / Exabits / SN27 / SN12 | n/a | n/a | n/a | – | Not accessible, illiquid, or defunct |

**Verdict:**
- **Include Lium (SN51) in the business plan as a secondary channel.** Model it with Lium's 30-day per-model figures, cut by 20–30% to allow for added supply and penalties. Treat its emission component (10–24%) as upside, not base case.
- **Include Akash only as an opportunistic channel for A100/H100-class cards.**
- **Treat Nosana and Akash Homenode as optional idle-fill channels for consumer cards**, cross-checked against agent 03.
- **Exclude** io.net (for consumer or old cards), Render, Aethir, Chutes, Targon, Fluence, Spheron, NetMind and Exabits from revenue projections. They are either effectively closed to small or used-hardware suppliers, or their supplier income is mostly token emissions that have already lost 75–99% of their USD value.

---

## 4. Confidence and gaps

**High confidence (live primary APIs, 2026-11-14):**
- io.net network, epoch and block-reward data.
- Akash capacity, bids and spend.
- Lium per-model economics.
- Chutes node inventory.
- Targon auctions.
- Nosana host rates.
- Bittensor subnet emissions and registration burns (TaoMarketCap).
- Aethir dashboard figures.
- All token price series.

**Medium confidence:**
- Aethir subsidy share. It depends on how the dashboard defines "gross emissions".
- io.net "monthly earnings" taken as customer USD flowing to suppliers. The field is labelled cluster earnings.
- The Akash Homenode estimate, which is Akash's own marketing.

**Low confidence or gaps:**
- **Render:** no fetched current burn dashboard. The net-subsidy estimate of 50–70% rests on RNP mechanics plus one secondary figure of about 50k RENDER/month burned in late 2025.
- **Aethir per-GPU prices:** H100/A100 service-fee rates were not public on the pages fetched, so the $900–1,300 H100 figure is an estimate.
- **io.net "open_debt" ($1.14M):** undocumented. It might indicate deferred supplier payouts and should be verified before relying on io.net.
- **Exabits:** no supplier terms could be retrieved; the site is JavaScript-only.
- **KYC and geography for Venezuela:** no network explicitly names Venezuela. The legal position depends on US/EU targeted sanctions and each exchange's policy (see agent 10).
- **Off-ramp exchange availability by country** could not be re-verified because the search budget was exhausted.
- **Bittensor halving and emission-schedule details** were not verified this session.
- Bittensor "miner TAO/day" is TaoMarketCap's TAO-equivalent valuation of alpha emissions. The realizable value is lower because of pool slippage.
- **Secondary sources** (ownyourmind.ai, cryptoaianalysis.com) were used only for context: the Akash payer concentration, the absence of Akash incentives, and the io.net IDE launch date. They are labelled where used.

---

## 5. Sources (all accessed 2026-11-14)

**Live APIs and dashboards (primary):**
- io.net explorer API: https://api.io.solutions/v1/io-explorer/network/info ; `/network/inventory-aggregated` ; `/network/market-snapshot` ; `/devices/hardware` ; `/tokenomics/epochs` ; `/tokenomics/epochs/2026-11-14-09` ; `/network/info/cluster/monthly-earnings` ; `/network/info/cluster/total-earnings-summary` ; `/clusters/computed_hours` ; `/staking/metrics`. Endpoints were discovered from https://explorer.io.net/
- Akash Console API: https://console-api.akash.network/v1/gpu-prices ; https://console-api.akash.network/v1/dashboard-data ; https://console-api.akash.network/v1/network-capacity ; https://console-api.akash.network/v1/graph-data/dailyUUsdSpent ; https://console-api.akash.network/v1/graph-data/activeGPU
- Lium: https://provider-api.lium.io/public/provider-economics ; https://lium.io/api/machines ; https://lium.io/api/executors
- Chutes: https://api.chutes.ai/nodes/ ; https://chutes.ai/llms.txt
- Targon auctions: https://tower.targon.com/api/v2/auctions
- Nosana markets: https://api.nosana.com/api/markets/
- TaoMarketCap: https://api.taomarketcap.com/internal/v1/subnets/table/ ; https://api.taomarketcap.com/public/v1/subnets/51/ (also /4/, /64/, /27/, /12/)
- Aethir dashboard: https://dashboard.aethir.com/protocol/overview ; https://dashboard.aethir.com/protocol/supply-metric ; https://dashboard.aethir.com/protocol/demand-metric ; https://dashboard.aethir.com/protocol/onchain-metric
- Prices:
  - CoinGecko: https://api.coingecko.com/api/v3/simple/price and `/coins/{id}/market_chart` (io, akash-network, render-token, aethir, bittensor, nosana, fluence-2, netmind-token, spheron-network)
  - Kraken OHLC: https://api.kraken.com/0/public/OHLC (AKTUSD, RENDERUSD, TAOUSD, ATHUSD, NOSUSD)
  - Coinbase: https://api.exchange.coinbase.com/products/IO-USD/candles
  - Gate: https://api.gateio.ws/api/v4/spot/candlesticks (FLT_USDT, IO_USDT and others)

**Official docs and governance (primary):**
- io.net docs: https://io.net/docs/guides/block-rewards/block-rewards.md ; https://io.net/docs/guides/staking/io-staking.md ; https://io.net/docs/guides/staking/solo-staked-devices.md ; https://io.net/docs/guides/workers/device-onboarding.md ; https://io.net/docs/guides/workers/supported-devices.md ; https://io.net/docs/guides/workers/rewards-wallets ; io.net Terms (effective 2026-09-21): https://io.net/terms
- Akash Homenode earnings: https://homenode.akash.network/docs/earnings ; Akash BME roadmap: https://akash.network/roadmap/aep-76/
- Render RNPs: https://github.com/rendernetwork/RNPs/blob/main/RNP-019.md ; https://github.com/rendernetwork/RNPs/blob/main/RNP-022.md ; https://github.com/rendernetwork/RNPs/blob/main/RNP-023.md
- Aethir docs: https://docs.aethir.com/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts/rewards-for-cloud-host.md ; https://docs.aethir.com/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts/service-fees-for-cloud-host.md ; https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts.md ; https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts/staking-as-cloud-host/staking-parameters.md ; https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts/slashing-mechanism.md ; https://docs.aethir.com/aethir-tokenomics/complete-kyc-verfication.md ; https://docs.aethir.com/aethir-tokenomics/ath-burn-mechanism.md ; https://docs.aethir.com/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide/manage-income.md ; https://docs.aethir.com/checker-guide/checker-node-nft-buyback-program/checker-node-nft-buyback-program.md
- Lium docs: https://docs.lium.io/providers/rewards/index.md ; https://docs.lium.io/providers/rewards/rental-fees.md ; https://docs.lium.io/providers/rewards/emission.md ; https://docs.lium.io/providers/rewards/payouts.md ; https://docs.lium.io/providers/quickstart.md ; https://docs.lium.io/providers/nodes/quickstart.md
- Chutes miner overview: https://chutes.ai/docs/miner-resources/overview ; Targon miner docs: https://docs.targon.com/providers/miner
- Fluence: https://fluence.dev/llms.txt ; https://fluence.dev/docs/connect_servers/overview.md ; https://fluence.dev/docs/stake/llms.txt
- Spheron: https://docs.spheron.ai/llms.txt ; https://docs.spheron.ai/concepts/regions-providers ; https://docs.spheron.ai/provider-integration
- NetMind Power: https://netmind-power.gitbook.io/netmind-power-documentation/add-machines/machine-requirement.md ; https://netmind-power.gitbook.io/netmind-power-documentation/web3-related/get-nmt-on-netmind-power/add-machines-reward.md
- Exabits: https://exabits.ai/ (homepage only)
- Nosana docs index: https://docs.nosana.com/llms.txt

**Secondary (context only, labelled in text):**
- https://ownyourmind.ai/projects/io-net/ ; https://ownyourmind.ai/projects/akash/ ; https://ownyourmind.ai/projects/render/
- https://cryptoaianalysis.com/io-net-io-analysis-2026/
- https://messari.io/report/state-of-akash-q1-2026-final (cited via ownyourmind; not fetched directly)

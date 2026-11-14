# Renting Used GPUs and Servers from Colombia, Ecuador or Venezuela: Market Benchmark and Viability Verdict

**Date:** 2026-11-14 · **Method:** 10 parallel research agents (reports in [`agent-reports/`](agent-reports/)). Live pulls from public marketplace APIs (Vast.ai: 8,928 machines / 26,501 GPUs; Clore.ai; Akash; Salad; io.net; Bittensor/Lium; Hetzner/OVH feeds), plus tariff sheets, regulator data and price trackers. The profit model, built from these numbers, is in [`model/unit_economics.py`](model/unit_economics.py).
**Labels used:** **[C]** confirmed from a primary source on the date given · **[E]** estimate or inference · `[0N]` the agent report a number comes from.

> **Data caveat.** The research tools shared one web-search quota, and it ran out partway through. Agents switched to fetching official APIs and documents directly, so the price and utilization data are strong. The weakest areas are Latin American used-hardware listings (MercadoLibre and eBay block automated access), colocation quotes and Venezuelan tariffs. Every marketplace figure is a **one-day snapshot (Saturday 2026-11-14)** in a market that has moved 40–50% in 90 days.

---

## 1. Bottom line

**At November 2026 hardware prices, buying used GPUs or servers and renting them on peer-to-peer (P2P) marketplaces is not a viable business. That holds even at the cheapest site in Latin America.** The model finds no consumer-GPU configuration that pays back within 36 months when bought at today's used-market prices.

The cause is a mismatch:

1. **Used hardware prices roughly doubled in 2026** because of the AI-driven memory shortage. A used RTX 3090 now sells for about $1,550 (early 2026: $700–850). A 4090 sells for $3,000–3,800 and a 5090 for about $5,500. A 32 GB DDR4 server memory module (RDIMM) sells for about $120–200, up roughly 300% year on year. `[07][05]`
2. **Rental prices for the same cards did not follow.** A 3090 on Vast.ai rents for $0.21/GPU-hour, about the same as in 2023. The host receives about 75% of that, or $0.16/h. `[01][09]` The big 2026 rental-price increases happened in datacenter GPUs (H100 +32%, B200 +48% year on year), and those are priced out of reach of a small operator. `[06]`

So **"the market hasn't found the value of old servers" does not hold.** The global market has priced them very high. The value now sits in *reselling* the hardware, not renting it. The agents also found no evidence that Colombia, Ecuador or Venezuela are cheaper: where like-for-like comparisons exist, local asking prices are at parity with US used prices or 1.1–3× above them, and datacenter GPUs are essentially absent locally. `[07]`

**When it can work.** All of these must hold at once:

| Condition | Threshold | Source |
|---|---|---|
| Hardware cost | RTX 4090/5090 at **≤ 30–35% of US used price**, or A100/H100 at **≤ 55–70%** (for a 24-month payback, lean site, base case) | model |
| Site | Ecuador highlands (Quito/Cuenca), **commercial meter** ($0.086–0.094/kWh), not residential ($0.68/kWh above 3,500 kWh/month) | `[08]` |
| Operation | Your own premises and labour. A staffed site ($900/month of fixed costs for 16 GPUs) erases the margin | model |
| Verification | 500/500 Mbps wired, public IPv4 (no carrier-grade NAT), reliability ≥ 0.99. Verified machines are 82% rented vs 47% unverified | `[01][10]` |
| GPU class | 24 GB+ VRAM, Ampere or newer. Avoid Pascal/Volta (P40/P100/V100): CUDA 13 and PyTorch 2.15 dropped them | `[10]` |
| Payouts | Through a Spanish/EU entity (Vast pays only via Wise/PayPal/Stripe; Stripe excludes Colombia and Venezuela) | `[01][10]` |
| Country | **Not Venezuela.** The crypto-mining ban is enforced by spotting high power use and then raiding; GPU racks look like mining rigs. Daily blackouts, no payout rails, sanctions on the power utility | `[08][10]` |

**The real opportunity the research turned up is reselling, not renting.** It applies if someone in Colombia, Ecuador or Venezuela is selling at stale prices (2024 or early-2026 levels). Examples: a bank or telecom disposing of old assets, a government auction, or an old MercadoLibre listing. In that case:
- buy and resell GPUs into the US/EU market;
- part out DDR4 servers. The RAM in one 256 GB R730 resells for about $800–1,200, more than 15 years of realistic CPU-rental income. `[05][07]`

That trade has its own costs: about 13% marketplace fees, export logistics, and the risk that the shortage unwinds. Used RDIMM and 5090 asking prices are already down 8–23% from their September peak.

---

## 2. What the marketplaces pay: the benchmark

### 2.1 Price per GPU-hour by channel (2026-11-14)

"Renter" is what the customer pays; "host" is what the supplier receives.

| GPU | Vast renter median `[01]` | **Vast host (×0.75)** | RunPod community (renter) `[02]` | Clore median rented `[02]` | Octa.space `[02]` | Salad host, avg incl. idle `[03]` | Akash median `[04]` | Lium, $/GPU-month incl. emissions `[04]` | Neocloud / index `[06]` |
|---|---|---|---|---|---|---|---|---|---|
| RTX 3060 | 0.073 | 0.055 | – | – | – | 0.031 | – | – | – |
| RTX 3090 | 0.213 | **0.16** | 0.22 | 0.13 | 0.24 | 0.115 | 0.16 | $139 | – |
| RTX 4090 | 0.480 | **0.36** | 0.34 | 0.27 | 0.32–0.38 | 0.272 | 0.36 | $302 | – |
| RTX 5090 | 0.667 | **0.50** | 0.69 | 0.50 | 0.57 | 0.376 | – | – | Ornn 0.68 |
| RTX A6000 | 0.480 | 0.36 | – | – | – | – | – | – | – |
| A100 80GB | 1.15 (SXM4); PCIe 0.73–0.95 `[06]` | 0.55–0.86 | 1.19 (PCIe) | – | – | – | 1.49 | $927 (SXM4) | Ornn 1.04 · Silicon Data 1.64 · Lambda 3.19 |
| H100 SXM | 2.33 | **1.75** | 2.69 | – | – | – | 2.56 | $1,294 | Ornn 3.29 · Silicon Data 3.10 · Lambda 4.59 |
| H200 / B200 | 5.19 / 10.00 | 3.89 / 7.50 | – | – | – | – | – | – | Ornn 6.73 / 9.72 |
| V100 | 0.080 | 0.06 | 0.19–0.23 | 0.055 | – | $0 (Tesla) | – | – | AWS 3.06 (2017 list price, irrelevant) |
| P40 / T4 | ≈0.20 (n=10, thin) / – | – | – | 0.02–0.10 / 0.019 | – | $0 | – | – | – |
| CPU server (R730, 56 threads, 256 GB) | no CPU market | – | – | – | – | – | $294/month *if fully leased*; ~$4/month realistic unaudited `[05]` | – | OVH rents the same spec for **$96/month** `[05]` |

**What is the industry standard?** For a small host, **Vast.ai is the reference price**: it is the largest open marketplace, and the others cluster around it or below it. Clore and Salad pay 25–45% less on consumer cards. Akash and Lium pay more for A100/H100, but their demand is concentrated (on Akash, two payers make up about 90% of spend `[04]`) or partly subsidised (Lium: 10–21% of income is token emissions).

### 2.2 Gross monthly income per GPU on Vast (host side, before power)

`[01]`

| GPU | 30% rented | 50% rented | 70% rented | 100% rented |
|---|---|---|---|---|
| RTX 3090 | $35 | $58 | $82 | ~$117 |
| RTX 4090 | $79 | $131 | $184 | ~$263 |
| RTX 5090 | $110 | $182 | $255 | ~$365 |
| V100 / 2080 Ti / 1080 Ti | – | $13–22 | $18–31 | ~$44 |

Actual 2026 reports agree:
- a verified 4090 earns about $180/month and a verified 5090 about $270/month `[09]`;
- a new, unverified 5×5090 host earned about $60/GPU/month in its first 23 days `[09]`;
- Salad averages $196/month for a 4090 and $82 for a 3090 `[03]`.

### 2.3 Do they pay differently by country?

**Barely, on P2P marketplaces.**
- **Pricing.** Demand is global and sorted by price. Latin American Vast offers sit at about **0.96× the global median** for the same GPU (full 8,928-machine pull) and are rented about as often (77% vs 73–75%). `[01]` A smaller sample put the discount at 10–35% for some cards `[06]`; the model uses 0.95×.
- **Size.** Latin America is **about 1% of Vast supply** (260 GPUs). Colombia has one machine (1× 5090, verified, rented), Ecuador two (1× 3090 each, unverified), Venezuela none. Brazil, Mexico, Argentina and Chile make up most of the region. `[01]`
- **What does penalise Latin American hosts** is verification and bandwidth: 63% are verified vs 81–83% in North America and Europe, with a median upload of about 625 Mbps vs about 900. `[09]`
- **Latency is not a blocker.** Measured: Caracas–Miami 35 ms, Quito–Miami 54 ms, Bogotá–Miami 57 ms. `[08]`
- **Regional premiums exist only in hyperscaler and local-cloud pricing.** AWS São Paulo charges +62–70% vs US East, and Silicon Data reports São Paulo buyers paying 3–4× a Chicago peer for local H100s. A host on a global marketplace can't capture that premium. Selling locally to Latin American companies that need data in-country (health, finance, government) would be a *different business*. It might be the more interesting one, but it was not researched here. `[06]`

### 2.4 Which chips are in demand

- **Renters pay for VRAM first.** `[06]`
  - 48 GB cards and H100s are 82–83% rented.
  - 24 GB cards (3090/4090) are 68–73%.
  - Cards with 16 GB or less are 42–57%.
- **Over 90 days, Blackwell and consumer cards rose; old datacenter cards fell.** `[01]` 5090 +51%, 3090 +39%, 4090 +37%, B200 +55%; V100 −57%, P100 −60%.
- **Old datacenter cards are close to end of rentable life.** `[10]`
  - CUDA 13 dropped Maxwell, Pascal and Volta. Their last driver line (R580) ends June 2028.
  - PyTorch 2.15 (28 Oct 2026) requires Turing or newer, and vLLM 0.20+ dropped V100.
  - Salad accepts only RTX 3060–5090, and pays $0 for Tesla cards. `[03]`

| Generation | Examples | Estimated remaining rental life `[10]` | Earns vs power cost |
|---|---|---|---|
| Pascal / Volta | P40, P100, V100 | 0–1.5 yrs | ≈ power cost (V100 $0.06/h host vs $0.03–0.05/h power) |
| Turing | T4, 2080 Ti | 2–3 yrs | marginal |
| Ampere | 3090, A-series, A100 | 3–5 yrs | positive but thin on consumer cards |
| Ada / Blackwell | 4090, 5090, L40S, PRO 6000 | 4–6 yrs | best for consumer cards |

### 2.5 What machine setup the platforms require (Vast verification)

`[01][10]`

- **GPU:** more than 7 GB VRAM per GPU, and more than 2.85 GiB/s of PCIe bandwidth per GPU. That rules out the x1 risers on ex-mining rigs, so each card needs a full x16/x8 slot.
- **CPU and RAM:**
  - System RAM ≥ 0.95× total VRAM: a 4×3090 box needs ≥ 96 GB, and an 8×3090 box about 183 GB. The "200–500 GB RAM server" is useful here, as the host for a multi-GPU box.
  - At least 2 CPU cores per GPU.
- **Network and OS:**
  - 500/500 Mbps wired, with a **public IPv4 address**. Carrier-grade NAT, common in Latin America, blocks hosting entirely.
  - Ubuntu Server on a dedicated machine (no gaming or mining on the side).
- **Reliability and status:**
  - Reliability above 90% is needed to verify; 0.99+ gets about 80% utilization.
  - Verification takes 2–4 weeks to months, and errors deverify a machine automatically. `[09]`
- **Datacenter tier** (1.46× price at the same utilization) needs an ISO 27001 facility, a registered business and at least 5 servers.
- **Power:** a 4×4090 box draws about 2.0 kW and a 4×5090 box about 2.5 kW. 8-GPU chassis (Supermicro 4028GR/4029GP-TRT, ASUS ESC8000) need 220 V and 2.5–3.5 kW. `[05]`

### 2.6 Which platforms a small Latin American operator can actually use

| Platform | Open to a small LATAM host? | Hosts keep | Payout | Verdict |
|---|---|---|---|---|
| **Vast.ai** | Yes | ~75% `[01]` | Wise/PayPal/Stripe, weekly, $20 minimum | **Primary channel.** Largest demand. Payouts via a Spanish entity |
| **Clore.ai** | Yes (any NVIDIA, incl. ex-mining) | 95% (CLORE-paid) / 80% (BTC/stablecoin) | Crypto, $10 minimum | Secondary. 26% rented excluding one V100 fleet; prices 25–40% below Vast `[02]` |
| **Lium (Bittensor SN51)** | Yes, no KYC, public IP needed | n/a (emissions + renter fees) | USDT daily | Secondary for 4090+/A100/H100. Cut figures 20–30% `[04]` |
| **Akash** | Yes (audited providers do far better) | ~100% (fee removed March 2026) | AKT/USDC | A100/H100 only. Demand concentrated `[04]` |
| **Octa.space** | Yes | 80% | USDC per session | Small (≈148 nodes) `[02]` |
| **Salad** | Yes (Colombia/Ecuador OK) | 80% | PayPal/gift cards/RENDER | One GPU per Windows PC; no farms of multi-GPU servers `[03]` |
| RunPod | **No** (community hosting closed 24 Feb 2026; Secure Cloud ≥100 kW) | – | – | Out `[02]` |
| TensorDock, Cudo, SF Compute, Hyperbolic, Fluence | No / dormant / datacenter only | – | – | Out `[02][04][05]` |
| io.net, Render, Aethir, Chutes, Targon | Technically yes | – | Tokens down 77–99% since Jan 2025 | Consumer and old cards sit idle (io.net has 8 active 4090s; Chutes' 261 consumer GPUs are 100% idle) `[04]` |

---

## 3. Cost side in Latin America

### 3.1 Hardware acquisition: the "LATAM undervalues old servers" hypothesis is not supported

`[07]`

| Item | Colombia | Ecuador | Venezuela | US used (Nov 2026) | LATAM ÷ US |
|---|---|---|---|---|---|
| Dell R730 (configured) | $1,447–1,779 | – | $3,500 (128 GB) | $900–1,600 | 1.1–3× |
| Old R610/R710 | – | $999–1,300 | $999–1,300 | near scrap | ≫1 |
| DDR4 32 GB RDIMM 2666 | $202 (live Bogotá shop [C]) | – | – | $199 asking median; $100–150 sold through August `[05]` | 1.0–1.4× |
| RTX 3090 | $1,055–1,357 (undated listings) | ~$700–1,900 | $650–1,400 (≈2024 listings) | $1,540–1,660 | 0.45–0.9× *apparent*, but stale: 1.1–1.6× vs the US price at listing date |
| V100 16 GB | $13.5k–16.6k (asking) | – | – | $350–440 | absurd |
| P40, T4, A100, A-series | not found | not found | not found | P40 $384; A100 80 GB $10,999 | – |

Importing from the US instead multiplies the US price by about:
- **Colombia:** 1.20× for GPUs and RAM, 1.40× for a 2U server. The tariff is 0% (HS 8471/8473) and VAT 19%; about 1.01–1.18× if a company recovers the VAT.
- **Ecuador:** 1.18–1.57×. VAT 15%, plus 0.5% FODINFA and the 5% currency-outflow tax (ISD).
- **Venezuela:** 1.07–1.56×.

Friction:
- Colombia requires a **prior import licence for used goods** (Decreto 925/2013), so cheap Venezuelan hardware can't simply be moved into Colombia.
- Ecuador's 4×4 courier regime caps imports at $400 and 4 kg per package, $1,600 per year.
- A Miami courier refuses mining equipment for Venezuela.

**Practical rule:** price any purchase at *US used price × landed multiplier*. Only chase local deals priced below about **0.35× (consumer) or 0.6× (A100/H100)** of US used prices; that is where the model starts to work.

### 3.2 Operating costs by city

`[08]`

| City | Commercial $/kWh | Power cost per GPU-month (≈0.4 kW incl. cooling) | Reliability | Cooling | Rank |
|---|---|---|---|---|---|
| **Quito / Cuenca (EC)** | **0.086–0.094** | **~$29** | Medium. 2024 cuts up to 14 h/day; Sep–Oct 2026 cuts hit medium/high-voltage companies, but low-voltage users were spared | Free cooling (14–15 °C, power usage effectiveness (PUE) ≈1.1–1.25) | **1** |
| Guayaquil (EC) | 0.086–0.094 | ~$42 | Medium | Hot, needs A/C (PUE 1.5–1.8) | 4 |
| Bogotá (CO) | 0.314 (incl. 20% contribution); excess consumption pays up to ~0.53 under the El Niño penalty since 1 Sep 2026 | $88–105 | Good now; projected deficit, critical around March 2027 | Free cooling | 3 (best colocation market) |
| Medellín / Cali / Barranquilla (CO) | 0.31–0.38 | up to $143 (Barranquilla) | Good | Barranquilla hot | 5–7 |
| Caracas / Valencia / Maracaibo (VE) | ~0.02–0.08 [E] (no tariff sheet found) | cheapest on paper | **Very poor**: daily outages for 82% of Caracas and 99% of Zulia households, up to 16 h | – | last |

Other operating facts:
- **Backup power:** a UPS plus generator for a 16-GPU site costs about $8–18k [E]. Diesel fuel alone costs about $0.24/kWh generated in Ecuador and $0.27/kWh in Colombia.
- **Connectivity:** 1 Gbps fibre costs $38–76/month. Budget extra for a business line with a public IP.
- **Colocation:** retail colocation for GPU densities would cost about $110–200 per GPU per month [E], which wipes out the margin. Self-hosting in a small commercial space is the realistic model.
- **Labour:** a part-time technician costs about $300–600/month [E].

### 3.3 Legal, tax and payments

`[10]`

- **Venezuela, no-go:**
  - OFAC still blocks the government under EO 13884, including CORPOELEC (the power utility). A US entity would need General License 35 just to pay the electricity bill.
  - Wise does not operate there, Stripe has no route, and PayPal offers no local-currency withdrawal. That leaves crypto only.
  - The "absolute" crypto-mining ban was reaffirmed on 7 May 2026, and a USD 1,000 bounty per reported miner was paid in Carabobo. GPU racks are indistinguishable from mining rigs to an inspector.
- **Colombia:**
  - Corporate tax is 35% (20% in a free-trade zone, only on export income and only for companies inside the zone).
  - Hosting and cloud services are VAT-excluded: none is charged, but VAT paid on hardware is not refunded.
  - Crypto reporting to DIAN, the tax authority, starts with tax year 2026.
- **Ecuador:** about 5% leaks to the currency-outflow tax (ISD), including a presumed ISD on export income kept abroad. There is no data-centre incentive regime.
- **Payouts:**
  - Vast pays only via Wise, PayPal or Stripe.
  - Stripe's standard cross-border payouts exclude Colombia and Venezuela. Wise pays out in Colombian pesos but does not list Ecuador or Venezuela. `[01]`
  - The two reports conflict on whether Ecuador works directly. **The cleanest route is a Spanish entity receiving payouts** and paying the Latin American operation, which then needs its own transfer-pricing and tax set-up.

---

## 4. Unit economics: model results

**Model:** [`model/unit_economics.py`](model/unit_economics.py) (results in [`model/results.md`](model/results.md) and [`model/results.csv`](model/results.csv)).

**Model setup:**
- **Box:** 4-GPU boxes, 4 boxes per site (16 GPUs), 36-month horizon.
- **Prices:** Vast live medians × 0.95 for Latin America, host keeps 75%. Price path (base case): −10% / −20% / −20% per year `[06]`.
- **Utilization:** 65% steady state for consumer cards, ramping up over the first 2 months while unverified `[01][09]`.
- **Hardware:** US used prices × landed multiplier `[07]`.
- **Sites:** tariffs, cooling overhead, generator share and fixed costs from `[08]`.

### 4.1 Base case at the best site (Quito/Cuenca, staffed: $900/month fixed for 16 GPUs)

| Rig (4-GPU box unless noted) | Capex (box + site share) | Net/month, yr 1 | Payback | 36-month profit |
|---|---:|---:|---:|---:|
| Old CPU server (R730, 256 GB) on Akash | $4,950 | −$224 | never | −$12,607 |
| 4× V100 16 GB | $7,000 | −$219 | never | −$10,862 |
| 4× RTX 3090 | $12,980 | −$37 | never | −$13,368 |
| 4× RTX 4090 | $21,740 | $293 | never | −$9,119 |
| 4× RTX 5090 | $32,780 | $512 | never | −$8,640 |
| 4× A100 80 GB PCIe on Vast | $59,180 | $803 | never | −$21,269 |
| 4× A100 80 GB PCIe on Akash/Lium | $59,180 | $1,857 | never (profit from residual) | +$9,405 |
| 4× H100 PCIe 80 GB (blend) [E capex ~$25k/GPU] | $127,100 | $3,222 | never | −$4,732 |

### 4.2 Same rigs, lean site (own premises and labour, $250/month fixed, UPS-only)

| Rig | Net/month, yr 1 | Payback | 36-month profit |
|---|---:|---:|---:|
| 4× RTX 3090 | $125 | never | −$6,018 |
| 4× RTX 4090 | $455 | never | −$1,769 |
| 4× RTX 5090 | $674 | never | −$1,290 |
| 4× A100 on Akash/Lium | $2,019 | 36 months | +$16,755 |
| 4× H100 (blend) | $3,385 | never | +$2,618 |

### 4.3 Site matters a lot (4× RTX 5090, base case, staffed)

| Site | Net/month, yr 1 | 36-month profit |
|---|---:|---:|
| Quito/Cuenca | $512 | −$8,640 |
| Guayaquil | $456 | −$11,617 |
| Bogotá | $133 | −$20,821 |
| Barranquilla | −$102 | −$29,879 |
| Caracas (seizure and payout risk *not* priced) | $610 | −$5,623 |

Colombian electricity ($0.31–0.38/kWh) makes every consumer-GPU rig unprofitable.

### 4.4 The decision number: maximum price you can pay per GPU

This is the highest price per GPU, in US terms before import, that still pays back in 24 months (base case).

| GPU | US used price today | Max bid, Quito staffed | Max bid, Quito lean | Lean max bid as % of market |
|---|---:|---:|---:|---:|
| V100 16 GB | $400 | none: loses money even if free | none | 0% |
| RTX 3090 | $1,550 | none: loses money even if free | none | 0% |
| RTX 4090 | $3,300 | none | **$984** | 30% |
| RTX 5090 | $5,500 | $705 | **$1,830** | 33% |
| A100 80 GB (Vast) | $11,000 | $2,004 | $3,129 | 28% |
| A100 80 GB (Akash/Lium) | $11,000 | $6,624 | **$7,749** | 70% |
| H100 PCIe 80 GB (blend) | ~$25,000 [E] | $12,449 | **$13,574** | 54% |

If hardware can be sourced locally at **60% of the US price** and run lean in Quito, the results improve:
- 4090/5090 pay back in about 32 months (36-month profit +$4–7.5k per box, about 37–45% ROI).
- A100 on Akash/Lium pays back in about 17 months (+$36k per box, about 121% ROI).
- H100 pays back in about 22 months (+$49k per box).

The datacenter-card cases depend on Akash/Lium demand, which is concentrated or partly subsidised.

### 4.5 Sanity checks against first-hand data

The model's per-GPU net in lean Quito is about:
- RTX 3090: $30/month (agent 09's "typical": $41, before fixed costs);
- RTX 4090: $115/month (agent 09: $110);
- RTX 5090: $170/month (agent 09: $152).

Agent 09's ~17-month 3090 payback assumed about $700 all-in (early-2026 prices). At today's $1,550, the same card does not pay back.

---

## 5. Go / no-go checklist

**Do not do:**
- Buy CPU-only servers (any amount of RAM) to rent. Unaudited Akash providers are 1.5% utilized, and the operator loses $1–16/month per box after power. `[05]`
- Buy Pascal/Volta cards (P40, P100, V100) or ex-mining rigs on x1 risers. `[10]`
- Buy RTX 3090s at $1,500+ for rental.
- Host in Colombia on today's tariffs, or anywhere in Venezuela.
- Model DePIN token income (io.net, Render, Aethir, Chutes, Targon) as revenue. `[04]`

**Could do, if the numbers in §4.4 are met:**
- RTX 4090/5090 bought at ≤30–35% of US used price, run lean in Quito/Cuenca on a commercial meter with UPS plus generator, listed on Vast (primary), with Clore/Lium as secondary.
- A100/H100 bought at ≤55–70% of US used price, on Akash/Lium plus Vast. This needs more capital and carries demand-concentration risk.

**Better use of cheap old servers if you find them:** part out and resell RAM, CPUs and GPUs into the US/EU while the 2026 shortage lasts. Prices are already 8–23% off the September peak, so speed matters.

---

## 6. Recommended next steps (low cost, before any purchase)

1. **Run a live check of local prices (30–60 minutes, a person in Colombia or Ecuador).** Log 20 current, dated MercadoLibre and Facebook Marketplace listings for 4090/5090/A100/R740/RDIMM. Also look for "bajas de activos", "subastas de equipos de cómputo" and "remates". This is the only thing that can confirm or kill the arbitrage idea. `[07]`
2. **Pilot before scaling:**
   - If any 4090/5090 is already owned or available cheaply, run one box in Quito or Cuenca on Vast for 60 days.
   - Measure verification time, actual utilization and payout friction.
   - Target: ≥ 65% rented after verification.
3. **Settle payouts first:** confirm with Vast support that a Spanish SL (Wise/Stripe) can be the payout entity for machines located in Ecuador.
4. **Get an ISP quote in Quito** for 500/500+ Mbps with a static public IPv4. No public IP means no Vast verification.
5. **Watch the timing signals** with a monthly re-run of the model:
   - Vast's public price feed (`[01]` has the endpoint);
   - the Silicon Data H100 index;
   - used-GPU trackers (ResalePrices, GPUDojo).

   The business improves if used hardware prices fall back toward 2025 levels while rental prices hold. Re-run the model with `python3 model/unit_economics.py` after editing the inputs.
6. **Possible pivot, not researched here:** a local B2B GPU cloud for Latin American organisations that need data kept in-country, where hyperscalers charge a 60–100% regional premium. `[06]` That sells to local customers at local prices, unlike P2P hosting.

---

## 7. Confidence and gaps

| Area | Confidence | Why |
|---|---|---|
| Marketplace prices and utilization | **High** for the date | Full live API pulls (Vast 26.5k GPUs, Clore, Akash, Salad, io.net, Lium). But it is a one-day snapshot of a market that moved 40–50% in 90 days |
| Vast host share (75%) | Medium–high | Inferred from rounding in 96% of prices; Vast's FAQ says the host receives the rate they set |
| Used hardware prices (US) | Medium | Multiple trackers agree (ResalePrices n=314, an EU price tracker). eBay sold listings were blocked. RDIMM asking prices ($200) vs sold ($100–150) differ |
| LATAM hardware prices | **Low** | MercadoLibre blocked; undated search snippets; one live Bogotá shop |
| Electricity tariffs (EC/CO) | High | Regulator tariff sheets (Oct–Dec 2026 Ecuador, Aug 2026 Bogotá) |
| Venezuela tariffs, colocation quotes, CGNAT policies, generator quotes | Low | Not found; estimates |
| Price forecast 2027–29 | Low–medium | Silicon Data forward curve plus vendor blogs; base case −10/−20/−20% |
| H100 used price | Low | Web snippets, $18–35k range; model uses $25k |
| Legal and tax | Medium | Primary sources where reachable; research, **not legal advice** |

---

## 8. Report index

| # | Report | Key takeaway |
|---|---|---|
| 01 | [Vast.ai host economics](agent-reports/01-vast-ai-host-economics.md) | Hosts keep ~75%. 3090 $0.213 / 4090 $0.48 / 5090 $0.667 renter medians. 74% rented overall (82% verified, 47% unverified). LATAM is ~1% of supply at 0.96× price |
| 02 | [Other P2P host marketplaces](agent-reports/02-other-p2p-host-marketplaces.md) | RunPod and TensorDock are closed or dormant. Clore and Octa are open but pay 25–40% less |
| 03 | [Consumer GPU-sharing apps](agent-reports/03-consumer-gpu-sharing-apps.md) | Salad: 4090 $196/month, 3090 $82/month gross. One GPU per PC; Tesla cards earn $0. Market small (~$176k/month total) |
| 04 | [DePIN / crypto networks](agent-reports/04-depin-crypto-compute-networks.md) | Tokens down 51–99%. Demand is H100-only. Lium and Akash are the only ones worth modelling |
| 05 | [Old CPU/RAM servers](agent-reports/05-old-cpu-ram-servers.md) | Not a rental asset (Akash unaudited 1.5% utilized; OVH rents 256 GB for $96/month). A strong parts asset: RAM worth $800–1,200 per 256 GB |
| 06 | [GPU price index and trends](agent-reports/06-gpu-rental-price-index-and-trends.md) | Datacenter GPU prices *rose* in 2026 (H100 +32%). Base/bear/bull price paths. VRAM drives occupancy |
| 07 | [LATAM hardware acquisition](agent-reports/07-latam-hardware-acquisition-costs.md) | No local discount found. US used prices roughly doubled. Landed cost 1.2–1.6× |
| 08 | [LATAM operating costs](agent-reports/08-latam-operating-costs.md) | Quito/Cuenca best ($0.09/kWh, free cooling). Colombia 3–4× pricier. Venezuela unreliable |
| 09 | [Real host earnings](agent-reports/09-real-host-earnings-and-utilization.md) | Verification and bandwidth matter more than location or price. Typical net: 4090 ~$110/month, 3090 ~$41/month |
| 10 | [Legal, payments, obsolescence](agent-reports/10-legal-payments-obsolescence-risks.md) | Venezuela no-go. Pascal/Volta lose software support. Vast verification requirements |

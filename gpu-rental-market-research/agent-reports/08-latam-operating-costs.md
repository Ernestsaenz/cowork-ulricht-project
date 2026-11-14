# Agent 08: Operating costs and infrastructure for a small GPU cluster in Colombia, Ecuador and Venezuela

**Research date:** 2026-11-14
**Scope:** Electricity tariffs, power reliability and backup, connectivity, colocation, climate and cooling, incentives, and labour, for 4–16 GPU clusters in Bogotá, Medellín, Cali, Barranquilla, Quito, Guayaquil, Cuenca, Caracas, Valencia and Maracaibo.

**Exchange rates used**
| Currency | Rate | Source / date |
|---|---|---|
| COP/USD | **3,300** (TRM 3,297.07 on 11 Nov 2026; 3,269.88 on 10 Nov) | Noticias Caracol / Superfinanciera via RCN, Nov 2026 |
| VES/USD official (BCV) | **897.53** (9 Nov 2026); 896.12 (6 Nov) | NTN24, Finanzas Digital |
| VES/USD parallel | ~**1,036** (Cúcuta border quote, early Nov 2026; gap of about 15% to BCV). The BCV rate rose about 200% year on year. | Search snippet (El Congresista / Finanzas Digital). LOW confidence |
| Ecuador | USD (dollarized) | — |

The COP has strengthened sharply in 2026: the TRM was around 3,900–4,100 for most of 2025. Colombian costs in USD therefore look about 15–20% higher than they would at 2025 exchange rates. If the peso weakens again, the USD figures fall in proportion.

**Labels:** **CONFIRMED** means a primary or official source with a date (tariff sheet, Registro Oficial, regulator Q&A, live measurement). **ESTIMATE** means my inference or a secondary source. Every number carries its date.

---

## 1) Executive summary

- **Ecuador has by far the cheapest legal commercial power of the two "normal" countries, but it is rationing again.** The official ARCONEL tariff for Oct–Dec 2026 (Registro Oficial 9º Supl. Nº 380, 30 Sep 2026) charges commercial low-voltage-with-demand users **USD 0.088/kWh (08–22 h) and 0.070/kWh (22–08 h) plus USD 4.18/kW-month in Quito**. Guayaquil is 0.092/0.074 + 4.06; Cuenca is 0.090/0.072 + 4.79. A 24/7 load works out to about **USD 0.086–0.090/kWh**. Avoid residential service: Ecuador's increasing blocks reach **USD 0.68/kWh above 3,500 kWh/month**, so a 10 kW load on a home meter averages about **USD 0.48/kWh**.
- **Colombia power is 3–4 times more expensive.** In Enel Bogotá's August 2026 sheet (CONFIRMED), the commercial rate at voltage level 1, including the 20% contribution surcharge, is **COP 1,036/kWh (USD 0.314)**, the same as estratos 5–6. Estrato 4 is **COP 864 (USD 0.262)**. Other utilities had estrato-4 unit costs of **COP 840–1,046/kWh** in June 2026 (Air-e 840, Emcali 869, Electrohuila 1,046). Commercial users pay those figures plus 20%, which gives **USD 0.31–0.38/kWh**.
- **Colombia has a temporary El Niño penalty that hits new GPU loads directly.** Under CREG Res. 101 120 and 101 126 of 2026, in force from 1 Sep 2026 for an initial 6 months and extendable, consumption above **110% of each user's historical target** pays an extra **+50% (estratos 4–6) or +70% (regulated commercial and industrial)**. New accounts get a "reference" target based on similar users. On the excess kWh a Bogotá commercial meter can therefore pay about **USD 0.53/kWh** (a cap exists but its value was not found). XM projects a **deficit of 3,906 GWh/year for 2026–27**, and the system's most critical point is expected around **March 2027**.
- **Reliability is the main risk in all three countries.** *Ecuador:* households had blackouts of up to 14 h/day in 2024. In Sep–Nov 2026, more than 9,000 high- and medium-voltage companies were cut in rotating blocks of 48 h, 72 h and up to **168 h (7 days)**, and had to self-generate. Households and small low-voltage users have so far been protected by presidential pledge. *Venezuela:* rationing of 5–8 h/day is widespread. In Zulia, **99% of households have daily interruptions**, Caracas 82% (Sep 2026), with cuts of up to 16 h. *Colombia:* no rationing yet, but the risk is high for Q1 2027.
- **Diesel backup is expensive per kWh except in Venezuela.** Diesel costs **COP 11,616/gal in Bogotá (USD 3.52/gal, USD 0.93/L)** and **USD 3.06/gal in Ecuador (USD 0.81/L)** in Nov 2026. Venezuela's industrial diesel was **USD 0.32/L** (Jul 2026, possibly reversed). Fuel alone costs about **USD 0.26–0.28/kWh (CO), 0.23–0.24 (EC) and 0.09–0.10 (VE)**. In Colombia, grid power and diesel are nearly the same price per kWh.
- **Connectivity is cheap, and latency to US-East is good.** Live WonderNetwork pings on 14 Nov 2026: **Caracas–Miami 35 ms, Quito–Miami 54 ms, Bogotá–Miami 57 ms**; to Madrid or Frankfurt, 135–174 ms. Home 1 Gbps fiber costs **USD 38–50/month in Ecuador** (CNT, Netlife, Claro, Puntonet; Apr 2026). Colombia FTTH 900 Mbps–1 Gbps costs **COP 107k–250k (USD 32–76)**. CGNAT and static-IP policies were not confirmed for any operator; budget for a business plan with a public IP.
- **Colocation exists only in Bogotá at a useful scale.** CBRE Q1 2026 puts Bogotá wholesale (250–500 kW deals) at **USD 150–230/kW-month**, with 18.7% vacancy. Retail is far pricier: HostDime Bogotá (Tier IV) charges **USD 175 (1U) / 200 (2U) / 300 (4U) per month, but each includes only 1 A @ 208 V (~0.2 kW)**. GPU servers need 1.5–3 kW, so those small packages do not fit. ESTIMATE for retail GPU colo: **USD 250–450/kW-month**, which is about USD 100–180 per GPU per month before electricity, enough to wipe out most consumer-GPU rental margins. Ecuador has Cirion (Quito QUI2, Guayaquil GUA1, 3–20 kW racks), Telconet (TCC III Guayaquil opened Sep 2026) and IPXON Quito (from 1U), none with public prices.
- **Bogotá, Quito and Cuenca have a real free-cooling advantage.** Mean temperature is about 14–15 °C at 2,560–2,850 m, so a small, well-ventilated room can run at an estimated PUE of about 1.1–1.25. Coastal cities (Guayaquil, Barranquilla, Maracaibo) need compressor air conditioning, at an estimated PUE of about 1.5–1.8. Altitude caveat: ASHRAE A2 equipment must derate maximum inlet temperature by 1 °C per 300 m above 900 m, which means about 29 °C in Bogotá and 28.5 °C in Quito, and air density is about 75–77% of sea level.
- **Incentives are weak at this scale.** *Colombia:* free-zone status gives 20% income tax only on export income under an internationalization plan (Law 2277/2022, Decree 47/2024); otherwise the rate is 35%. *Ecuador:* no data-center-specific tax regime yet; a CAF MoU (Feb 2026) only studies tech free zones. *Venezuela:* the special economic zone law (2022) adds "nothing novel". Bitcoin mining is banned, with a USD 1,000 bounty for informants in Carabobo (May 2026), which creates seizure risk for GPU racks.
- **Labour is cheap in all three countries.** Minimum wages for 2026 are **COP 1,750,905 + 249,095 transport allowance in Colombia (about USD 606)** and **USD 482 in Ecuador**. Full-time support technicians cost about COP 2–2.8M/month (USD 600–850) in Bogotá, USD 600–1,100 in Quito or Guayaquil, and USD 240–780 in Venezuela. ESTIMATE for a part-time Linux/hardware technician: **USD 350–600 (CO), 300–550 (EC), 150–350 (VE)** per month.

**Bottom line (power only, per GPU at about 0.40 kW IT load including host share):** about **USD 29–42/month in Quito, Cuenca or Guayaquil**, versus **USD 88–143/month in Colombian cities** (more under the El Niño surcharge), versus about **USD 20–25/month in Venezuela** (unreliable and legally risky). Ecuador, specifically Quito or Cuenca on a commercial low-voltage-with-demand tariff with generator backup, is the best realistic option on cost. Bogotá is the best option for colocation and reliability.

---

## 2) Detailed findings

### 2.1 Electricity tariffs

#### Colombia: Enel Colombia (Bogotá), CREG-regulated tariff, **August 2026** (CONFIRMED, official tariff sheet)
Values are COP/kWh at 3,300 COP/USD and exclude municipal public-lighting taxes. The fixed charge is zero (CREG 191/2014).

| Category | COP/kWh | USD/kWh |
|---|---|---|
| Residential E1 subsistence (0–130 kWh/month in Bogotá) | 408.11 | 0.124 |
| Residential E2 subsistence | 510.14 | 0.155 |
| Residential E3 subsistence | 734.06 | 0.222 |
| Residential E1–E3 above subsistence, and **E4 (all consumption)** = unit cost (CU) | **863.61** | **0.262** |
| **Residential E5, E6** (CU + 20% contribution) | **1,036.33** | **0.314** |
| **Commercial/industrial with contribution, Level 1 (Enel-owned network)** | **1,036.33** | **0.314** |
| Commercial with contribution, Level 1, customer-owned transformer | 977.38 | 0.296 |
| Commercial with contribution, **Level 2 (11.4/13.2 kV, own substation)** | 865.76 | 0.262 |
| Commercial with contribution, Level 3 (34.5 kV) | 783.30 | 0.237 |
| Industrial/official **without** contribution, Level 1 | 863.61 | 0.262 |
| Industrial without contribution, Level 2 | 721.47 | 0.219 |
| Time-of-use option, commercial Level 1: peak (9–12 h, 18–21 h) / off-peak | 1,050.39 / 1,034.51 | 0.318 / 0.313 |

CU components at Level 1 (Aug 2026): generation 374.99, transmission 49.31, distribution 278.13, commercialization 83.34, losses 71.73 and restrictions 6.09 COP/kWh. Generation is only about 43% of the total, so time-of-use options save very little (about 1.5%).

- **The 20% contribution:** E5, E6 and commercial users pay CU × 1.2. Industrial users (registered manufacturing activity codes) and official users are exempt. **Inference:** a GPU-rental business would be classified as a service (data processing and hosting), so it would pay the 20% as a commercial user unless it qualifies otherwise. Have a Colombian accountant confirm this.
- **Other utilities, June 2026** (Valora Analitik citing Sergio Cabrales, Uniandes; published 8 Sep 2026): estrato-4 CU was Air-e (Barranquilla) **840.2**, Emcali (Cali) **868.6**, EEP Cartago 857.4, and Electrohuila 1,046 at the top, all COP/kWh. Commercial would be about ×1.2: **Air-e ≈ COP 1,008 (USD 0.306)**, **Emcali ≈ 1,042 (USD 0.316)**. Air-e had raised its CU from 796 to **840.15** in June 2026 bills (El Colombiano, 23 Jun 2026).
- **EPM (Medellín):** the official 2026 commercial sheet was not found. The estrato-3 billed tariff was **COP 790.49/kWh in Dec 2025** (El Colombiano). ESTIMATE for commercial: COP 950–1,050 (USD 0.29–0.32). EPM declined to adopt the government's 2026 tariff formula (Infobae, Feb 2026).
- **Trend:** the energy bill rose 7.24% between January and September 2026 (Bogotá press, via search). The Inflect market page quotes "industrial electricity about USD 0.11–0.14/kWh" for Bogotá (Jan 2026). That likely reflects large non-regulated contracts, which are **not accessible** to a 4–16 GPU load. Inference from CREG rules: the non-regulated market requires about 0.1 MW of demand or 55 MWh/month, versus 1.6–6.5 kW for this project. This threshold is from general knowledge and was not re-verified.
- **El Niño savings program** (CONFIRMED from Enel Colombia's official Q&A, citing **CREG Res. 101 120 and 101 126 of 2026**; Bloomberg Línea, 1 Sep 2026):
  - Applies to regulated residential, commercial and industrial users from **1 Sep 2026 for an initial 6 months**, extendable.
  - Each user's target is the median of historical daily consumption. **New users get a reference target from similar users.**
  - Consumption below 90% of target earns a share of a savings pool. Between 90% and 110% is neutral. **Above 110%, an extra charge applies to the excess kWh only: factor 1.30 (estratos 1–3), 1.50 (estratos 4–6), 1.70 (regulated commercial and industrial)**, calculated as (factor − 1) × tariff × excess kWh. A cap exists but its value was not found.
  - **Effect on a new GPU load in Bogotá:** about COP 1,295/kWh (USD 0.39) on an E4 home meter and about **COP 1,762/kWh (USD 0.53)** on a commercial Level 1 meter, for the excess kWh.

#### Ecuador: ARCONEL single tariff charges, **October–December 2026** (CONFIRMED, Registro Oficial 9º Suplemento Nº 380, 30 Sep 2026, Resolution ARCONEL-009/2026 reforming the 2026 tariff schedule)

| Category (per distributor) | Demand charge USD/kW-month | Energy USD/kWh | Commercialization USD/month |
|---|---|---|---|
| **Quito (EEQ)**: commercial low voltage, no demand meter | — | 0.081 (1–300 kWh), 0.104 (>300) | 1.414 |
| **Quito**: commercial low voltage **with demand** | 4.182 | 0.088 | 1.414 |
| **Quito**: commercial low voltage with demand, **time-of-use** | 4.182 | **0.088 (08–22 h) / 0.070 (22–08 h)** | 1.414 |
| Quito: commercial medium voltage with demand | 4.129 | 0.123 | 1.414 |
| **Guayaquil (CNEL UN Guayaquil)**: commercial low voltage, no demand meter | — | 0.082 / 0.110 | 1.414 |
| Guayaquil: commercial low voltage with demand / time-of-use | 4.055 | 0.092 / (0.092 and 0.074) | 1.414 |
| Guayaquil: commercial medium voltage with demand | 4.003 | 0.123 | 1.414 |
| **Cuenca (CentroSur group)**: commercial low voltage, no demand meter | — | 0.092 / 0.103 | 1.414 |
| Cuenca: commercial low voltage with demand / time-of-use | 4.790 | 0.090 / (0.090 and 0.072) | 1.414 |
| Commercial **high voltage** with time-of-use (crisis tariff, Oct–Dec 2026) | 4.400 | **0.3005 / 0.2808** | 1.414 |
| Residential, Quito and Guayaquil (increasing blocks) | — | 0.078–0.105 up to 500 kWh; 0.1285 (501–700); 0.145 (701–1,000); 0.171 (1,001–1,500); 0.275 (1,501–2,500); 0.436 (2,501–3,500); **0.681 (>3,500)** | 1.414 |

- **Effective price for a 24/7 flat load (my calculation):** Quito low voltage with demand, time-of-use: **USD 0.086/kWh** (0.094 without time-of-use). Cuenca 0.089. Guayaquil 0.090. Medium voltage is *more* expensive at about 0.129. Add municipal surcharges collected on the bill (street lighting, waste collection, fire department), which were not verified; ESTIMATE +5–15%.
- **Residential is a trap:** a 7,300 kWh/month load (about a 10 kW cluster) on a Quito residential meter costs about **USD 3,500/month, an average of USD 0.48/kWh** (my calculation from the blocks above).
- **Crisis tariff for large users:** from 1 Oct 2026, high-voltage classes AV1 and AV2 (189 large industries) pay an average of **USD 0.30 and 0.29/kWh**, up from about 0.12, for Oct–Dec 2026 consumption (Primicias, Teleamazonas, 30 Sep–1 Oct 2026). Medium- and low-voltage categories were not raised. The average national price under the 2026 base schedule is **USD 0.1061/kWh** (ARCONEL cost study, Dec 2025).

#### Venezuela: CORPOELEC (LOW confidence; no official tariff schedule found)
- No 2026 CORPOELEC tariff schedule with USD/kWh figures was found. Enerdata puts **household power at about USD 0.04/kWh in 2025**, flat since 2015 and government-controlled since 2003. GlobalPetrolPrices shows 0.000, which is unusable.
- The shopping-centre association Cavececo reported a **28% commercial tariff increase between January and March 2026**.
- **Reform:** on 10 Nov 2026 the National Assembly passed, in second reading, a reform of the electricity law (Ley Orgánica del Sistema y Servicio Eléctrico). **Tariffs will be "indexed to the strongest currency"**, with subsidies only for those who cannot pay. Private companies may generate, import and sell power, mainly to large consumers. Fines can reach 2% of gross income. Theft above 5,000 kWh/month carries 2–6 years in prison (elDiario, 10 Nov 2026). Expect USD-indexed and higher tariffs in 2027.
- ESTIMATE for commercial today: **USD 0.02–0.08/kWh**, highly uncertain and subject to billing anomalies (estimated bills, since meters are often not read).

### 2.2 Power reliability and backup

| Country | Status (dated) | Source |
|---|---|---|
| **Ecuador** | **2024:** household blackouts of up to 14 h/day. **2026:** Mar–Apr, the 4 largest high-voltage users self-generated 4–6 h/day. From **22 Sep 2026**, rationing began with 185 high-voltage users. On 2 Oct, **9,089 companies (about 8,900 medium-voltage)** were notified of 48 h blocks, later 72 h, then **168 h (14–20 Oct) with a mandate to draw "zero MW" from the grid** (EEQ Quito). Large users only were cut again 1–4 Nov 2026. **Households: President Noboa pledged no residential cuts this dry season (5 Oct 2026).** Mazar reservoir was at 2,123.5 m on 30 Oct (critical level 2,115 m). CENACE flagged November as the hardest dry-season month and modelled a possible deficit of up to 450 MW. A 1,000 MW interconnection line with Peru was due in November. Estimated deficit is about 1,391 MW; 655 MW of thermal capacity is expected by Apr 2027. | Teleamazonas 1 Oct; Rio Times 3 and 5 Oct; Vistazo 14 Oct; El Comercio 30 Oct 2026; Cuenca Dispatch 6 Apr 2026 |
| **Venezuela** | Daily cuts of 5–8 h in much of the country; a 45-day saving plan from late March 2026 (Caracas Chronicles, 15 May 2026). **Zulia: 99% of households interrupted daily; Andes 98%; Caracas 82%.** Outages "can last days without notice" (EFE / elDiario, 5 Sep 2026). Cuts of up to **16 h** triggered protests (elDiario, 25 Sep 2026). Industry lost about 26% of working hours in Q1 2026, and only 5% of manufacturers can fully self-generate (Conindustria, Aug 2026). GE Vernova alliance signed 2 Sep 2026; Karpowership barges (200 MW) for Zulia. | Sources listed |
| **Colombia** | No rationing as of Nov 2026. Reservoirs at about **77.9% on 6 Nov 2026** (government target above 80% before the dry season). XM: 95% probability of El Niño 2026–27 and a projected **deficit of 3,906 GWh/year**; the most critical point is expected around **March 2027**. NOAA puts the chance of a very strong El Niño at 63% for Nov–Jan. The CREG savings program (above) is the first lever; the "Plan Energía YA" was announced by the government. | Portafolio, RCN, Vanguardia (24 Oct 2026), Forbes CO (1 Sep 2026) |

**Backup costs (mostly ESTIMATES from retail references):**
| Item | Data point | USD/kW (ESTIMATE) |
|---|---|---|
| Diesel generator, small open-frame with ATS (Colombia) | Bauker 5.5 kW diesel with ATS, Homecenter CO, **COP 4,899,900** (2026 listing) ≈ USD 1,485 | ~270/kW (consumer grade, not 24/7 rated) |
| Diesel generator, silent 20 kVA (~16 kW) | Spain retail €11,107 ex-VAT (Autosolar, 2026) | ~650–850/kW. ESTIMATE installed in LATAM with ATS: **USD 400–900/kW** |
| Online double-conversion UPS, 10 kVA | €909 (Qoltec 8 kW, Latvia, Dec 2025) to MXN 154,055 (Tripp Lite 3-phase, Mexico, Jun 2026) | **USD 100–800/kW** depending on brand; batteries for 10–15 min extra |
| Solar PV, commercial | 30 kWp for COP 60–100M, i.e. **COP 2.0–3.3M/kWp (USD 600–1,000/kWp)**. FNCE equipment is VAT-excluded in Colombia (colombiatramita 2026 guide) | Daytime only; does not cover night load without batteries |
| **Diesel price** | **Colombia: COP 11,616/gal Bogotá (CREG Circular 371/2026, Nov 2026) = USD 3.52/gal = USD 0.93/L.** National 13-city average COP 11,320. **Ecuador: USD 3.06/gal from 12 Nov to 11 Dec 2026 (Decree 531) = USD 0.81/L.** **Venezuela: industrial diesel USD 0.32/L (EFE, 17 Jul 2026; Crónica Uno reports a possible reversal to Bs 3/L)**; retail about USD 0.004/L (DailyFuels, Oct 2026) with scarcity. | Fuel cost per kWh generated at 0.28–0.30 L/kWh (ESTIMATE): **CO 0.26–0.28; EC 0.23–0.24; VE 0.09–0.10** |

Rule of thumb for a 16-GPU cluster at about 6.5 kW IT load plus about 1 kW of cooling: a **10–15 kVA online UPS plus a 15–20 kVA silent diesel genset with ATS ≈ USD 8,000–18,000 installed** (ESTIMATE). In Ecuador, a 7-day 24/7 self-generation event (as in 14–20 Oct 2026) at 7.5 kW burns about 1,260 kWh, roughly 360–380 L ≈ **USD 300** of diesel.

### 2.3 Connectivity

**Latency** (CONFIRMED, WonderNetwork data-centre-to-data-centre averages measured 14 Nov 2026; residential last-mile adds 3–15 ms):
| From \ To | Miami | New York | Washington/Ashburn | Dallas | Madrid | Frankfurt | London |
|---|---|---|---|---|---|---|---|
| **Bogotá** | **57.5** | 72.3 | 79.8 | 92.5 | 168.8 | 167.8 | 152.5 |
| **Quito** | **54.4** | 82.2 | 74.8 | 76.6 | 173.8 | 163.1 | 154.9 |
| **Caracas** | **34.7** | 49.2 | 54.1 | 62.9 | 145.6 | 134.8 | 122.6 |
Intra-region: Bogotá–Medellín 7.8 ms; Bogotá–Quito 13.3 ms; Bogotá–Caracas 37.7 ms. All three countries are fine for batch, training and fine-tuning work. For interactive inference sold to US-East buyers, Caracas is best and Bogotá/Quito acceptable. Europe is far (about 135–175 ms).

**Fiber prices** (mostly residential; business plans with SLA and static IPs are quoted individually and were not found):
| Market | Plan | Price | Date / source |
|---|---|---|---|
| Colombia | Movistar FTTH 500 Mbps (symmetric) | from COP 84,900 (USD 26) | colombiamove, 28 Jun 2026 |
| Colombia | Movistar FTTH 900 Mbps (bundled with mobile) | from COP 106,990 (USD 32) | same |
| Colombia | Claro 900 Mbps FTTH triple play | about COP 116,900 (USD 35) | same |
| Colombia | ETB FTTH 200 Mbps regular | COP 41,930 (USD 13) | same |
| Colombia | General range for 1 Gbps | up to about COP 220k–250k (USD 67–76) | comparison sites, Apr 2026 |
| Colombia | Movistar 2 Gbps | select Bogotá zones only | colombiamove 2026 |
| Ecuador | 1 Gbps: CNT 38, Netlife 42, Claro 45, Puntonet 50 (USD, 15% VAT included) | 12-month contract −10%, 24-month −18%; install USD 40 | cuantomecuesta.com/ec, Apr 2026 |
| Venezuela | SimpleFibra 500 Mbps USD 52.99 (200 Mbps 32.99) | billed in Bs at the BCV rate, VAT included | El Caribe (undated, probably 2025–26) |
| Venezuela | CANTV fiber USD 9–100; Airtek Maracaibo 200–600 Mbps USD 25–35 | CANTV plans need community approval | NTN24 (undated); La Patilla 2022 |

- **CGNAT and static IP: NOT CONFIRMED** for any Colombian, Ecuadorian or Venezuelan operator; no primary source was found. ESTIMATE from general market knowledge: Claro and Tigo HFC residential lines in Colombia and Ecuador frequently use CGNAT. Movistar and ETB FTTH more often hand out a public dynamic IPv4. Business plans with a /29 or a static IP typically cost 1.5–3 times the residential price, an estimated **USD 80–200/month for 300 Mbps–1 Gbps with a static IP**. Dedicated enterprise internet access with an SLA costs several hundred USD or more. Marketplaces that require inbound ports or static IPs make a business plan close to mandatory; NAT-friendly ones (e.g. SaladCloud-style agents) can run on residential lines. Verify per marketplace.
- No explicit data caps were found on fixed fiber in these markets. ESTIMATE: fair-use clauses only.

### 2.4 Colocation

| Location | Provider / data point | Price / density | Date / source |
|---|---|---|---|
| **Bogotá (market)** | CBRE Global Data Center Trends 2026 | **USD 150–230/kW-month** (wholesale, 250–500 kW); vacancy 18.7%; available capacity 8.3 MW | CBRE, Q1 2026 data |
| Bogotá | **HostDime** (Tier IV, 6 MW, PUE 1.5, up to 20 kW/rack) | **1U USD 175, 2U 200, 4U 300 per month, each with only 1 A @ 208 V (~0.2 kW)**, 50 Mbps, /29. ¼ (12U), ½ (22U, 5 A @ 220 V) and full (48U, 13 A) cabinets by quote | hostdime.com, accessed 14 Nov 2026 |
| Bogotá | Equinix BG1, KIO BOG1 (rooms designed for 4 kW/rack), EdgeConneX (20+ kW/cabinet, 100+ kW for AI), ODATA, Cirion, EdgeUno, InterNexa, Claro, NAP Colombia, Zona Franca de Bogotá data center complex | Quote only | Inflect (Jan 2026), EdgeConneX sheet (2025), KIO spec sheet |
| Medellín, Cali, Barranquilla | Over 88–98% of Colombian rack capacity is in Bogotá (Arizton / ResearchAndMarkets) | Minimal retail colocation options | ResearchAndMarkets, Jan 2026 |
| **Quito** | Cirion QUI2 (Tier III, about 265 m², Carcelén); IPXON (1U to full rack); Telconet Quito data center "in preparation" | No public prices | Cirion spec sheet; datacenters.com; Baxtel, Sep 2026 |
| **Guayaquil** | Cirion GUA1 (mini-racks, racks 3–20 kW, cages; about 1.6 MW IT); **Telconet TCC III opened Sep 2026** | No public prices | datacentermap; SubTel Forum, Sep 2026 |
| Caracas | No data found | — | — |

- **Small colocation is available** (1U, 2U, 4U, ¼ rack) in Bogotá, Quito and Guayaquil, but **packaged power allowances are about 0.2 kW**. A 4U GPU server at 1.5–3 kW must buy extra power at a negotiated rate. ESTIMATE for retail GPU colo: **USD 250–450/kW-month all-in**, i.e. about **USD 400–1,300/month per 4U GPU server**.
- **Implication (ESTIMATE):** at about 0.45 kW per consumer GPU including overhead, colo costs about **USD 110–200 per GPU per month**. That is comparable to or above what a consumer GPU (e.g. RTX 3090/4090 class) earns on P2P marketplaces at realistic utilization (rental rates are covered by other agents). **Colocation only makes sense for high-value data-centre GPUs (A100/H100 class).** For cheap used GPUs, self-hosting in a commercial space is the realistic model.

### 2.5 Climate and cooling (ESTIMATES)

The city temperatures below are standard climatological normals from general reference data, not re-verified this session: the search budget ran out before the climate lookups.

| City | Altitude | Mean annual temp. | Humidity / notes | Small-room PUE (ESTIMATE) |
|---|---|---|---|---|
| **Bogotá** | 2,640 m | ~14 °C | Mild, frequent rain; free air cooling nearly all year | **1.10–1.25** (filtered fan-wall or economizer) |
| **Quito** | 2,850 m | ~14 °C | Mild | **1.10–1.25** |
| **Cuenca** | 2,560 m | ~15 °C | Mild | **1.10–1.25** |
| Medellín | 1,495 m | ~22 °C | Warm days | 1.25–1.40 |
| Caracas | ~900 m | ~21–22 °C | Warm | 1.25–1.40 |
| Cali | ~1,000 m | ~24–25 °C | Hot afternoons | 1.35–1.50 |
| Valencia (VE) | ~480 m | ~25 °C | Hot | 1.40–1.55 |
| Guayaquil | ~5 m | ~26–27 °C | Hot, very humid | 1.50–1.70 |
| Barranquilla | ~20 m | ~28 °C | Hot, humid, salty air | 1.55–1.75 |
| Maracaibo | ~10 m | ~28–29 °C | Among the hottest cities in LATAM | 1.60–1.80 |

- **Altitude caveat (CONFIRMED rule, vendor documentation citing ASHRAE):** class A2 equipment derates maximum inlet temperature by 1 °C per 300 m above 900 m. Classes A3 and A4 derate faster, at 1 °C per 175 m and per 125 m.
- **Calculated effect:** maximum allowable inlet is about **29 °C in Bogotá, 28.5 °C in Quito and 29.5 °C in Cuenca**, against an A2 nominal of 35 °C. That is still far above ambient.
- **Air density is lower:** about **0.77 of sea level in Bogotá and 0.75 in Quito** (standard atmosphere), so GPU fans move less heat per unit of airflow. Consumer GPUs packed densely may run hotter or throttle. Plan open-frame or well-spaced chassis, and verify the vendor altitude rating (many servers are rated to 3,048 m with derating).
- **Power cost effect:** in the coastal cities, cooling overhead adds about 35–60% to the electricity bill versus Bogotá or Quito. This is already included in the scenario table in 2.8.

### 2.6 Incentives

| Country | Regime | Relevance for a small GPU host |
|---|---|---|
| **Colombia** | **Free zones (zonas francas):** 20% income tax (general rate 35%) for qualified industrial users, but since Law 2277/2022 art. 11 and Decree 47/2024 the 20% requires an annual internationalization and sales plan. It applies to export income, i.e. services delivered cross-border, with domestic-income caps; otherwise the rate is 35%. Plans for 2025 onward are due by 30 Sep of the prior year. Zona Franca de Bogotá has a data center complex (USD 90M) offering the 20% rate. | Medium-low. Selling GPU time to foreign marketplaces is a cross-border service export, which fits the export-income logic, but qualifying as a free-zone user means locating inside a free zone, with investment and job commitments. ESTIMATE: only worthwhile beyond about USD 0.5–1M of capex. Separately (general knowledge, verify): exported services are VAT-exempt (Estatuto Tributario art. 481), and FNCE (solar) equipment is VAT-excluded with income-tax deductions under Law 1715/2014 and Law 2099/2021. |
| **Ecuador** | No data-center-specific tax advantages (Inflect). A CAF–Ecuador MoU (26 Feb 2026) covers technical assistance for data centers and tech free zones, but no law exists yet. General new-investment income-tax exemptions exist (SRI, Oct 2025) but target "productive investments" via investment contracts. ESTIMATE / verify: electricity supply is VAT 0% in Ecuador. | Low today. Watch for a tech-free-zone (ZEDE) framework in 2027. |
| **Venezuela** | Special Economic Zones law (2022); incentive limits set in 2025 (Res. 015-25). An academic review says it adds "nothing novel" beyond existing tax and customs law. **Crypto mining is banned nationally** (Caracas Chronicles, May 2026). Carabobo authorities offer a **USD 1,000 bounty per report** of miners (iProUP, May 2026), and SUNACRIP has seized 12,304 ASICs. The Nov 2026 electricity reform allows private power supply to large consumers. | Negative. GPU racks drawing kilowatts can be mistaken for mining rigs, so there is seizure and legal risk. Sanctions and payment rails (USDT, US-based marketplaces paying a Venezuelan entity) add compliance risk (not researched here). |

### 2.7 Labour

| Country | Reference | Part-time Linux/hardware technician (ESTIMATE, ~20 h/week or on-call) |
|---|---|---|
| **Colombia** | Minimum wage 2026 **COP 1,750,905 + COP 249,095 transport allowance = COP 2.0M (USD 606)** (Decree 1469/2025, +23%; a transitional Decree 159/2026 suggests a legal challenge). Bogotá job ads, Oct–Nov 2026: support technician COP 2.0–2.5M; IT analyst COP 2.8M plus benefits; Windows/Linux infrastructure COP 3.5–4M; Linux/Windows admin COP 5.5–6M (elempleo.com). Employer on-costs add about 50% (ESTIMATE). | **COP 1.2–2.0M (USD 360–600)/month** as an independent contractor; remote hands at a colo are often included or billed per incident |
| **Ecuador** | Minimum wage (SBU) 2026 **USD 482**. Job ads: Quito "Técnico en Sistemas" USD 600–900; Support N1 USD 700–1,100; Guayaquil network technician USD 1,000; entry helper USD 300–500 (cazvid, 2026). | **USD 300–550/month** |
| **Venezuela** | Minimum integral income about **USD 240/month**, paid mostly as bonuses. Average private wage about USD 283 (Fedecámaras Q1 2026). Private technicians USD 240–781 full-time (CazVid guide, Jun 2026). | **USD 150–350/month** |

### 2.8 Power-cost scenarios (ESTIMATE; flat 24/7 load at 100% utilization; PUE from 2.5; tariffs from 2.1)

| City (tariff basis) | USD/kWh | PUE | 4 GPU (~1.6 kW IT) | 8 GPU (~3.2 kW IT) | 16 GPU (~6.5 kW IT) | Per GPU (0.40 kW IT) |
|---|---|---|---|---|---|---|
| Bogotá, commercial Level 1 (CU + 20%) | 0.314 | 1.15 | $422 | $844 | $1,713 | $105/mo ($0.144/GPU-h) |
| Bogotá, home E4 (CU) | 0.262 | 1.15 | $352 | $704 | $1,430 | $88/mo |
| Bogotá commercial, **excess under El Niño program** | up to 0.534 | 1.15 | up to ~$720 | up to ~$1,435 | up to ~$2,910 | up to ~$180/mo |
| Medellín, commercial (EPM, estimated) | ~0.31 | 1.30 | $471 | $941 | $1,912 | $118/mo |
| Cali, commercial (Emcali CU × 1.2) | 0.316 | 1.45 | $535 | $1,070 | $2,174 | $134/mo |
| Barranquilla, commercial (Air-e CU × 1.2) | 0.306 | 1.60 | $572 | $1,144 | $2,323 | $143/mo |
| **Quito, commercial low voltage with demand, time-of-use** | 0.086 | 1.15 | **$116** | **$231** | **$469** | **$29/mo ($0.040/GPU-h)** |
| Cuenca, same category | 0.089 | 1.15 | $120 | $239 | $486 | $30/mo |
| Guayaquil, same category | 0.090 | 1.60 | $168 | $336 | $683 | $42/mo |
| Caracas (tariff estimated; plus generator hours) | ~0.05 | 1.30 | ~$76 | ~$152 | ~$308 | ~$19/mo |
| Maracaibo (tariff estimated; plus generator hours) | ~0.05 | 1.65 | ~$96 | ~$193 | ~$391 | ~$24/mo |

Notes:
- In Ecuador, add generator fuel for rationing events. A full 7-day self-generation event at a 16-GPU site costs about USD 300 in diesel.
- In Venezuela, if 25–33% of hours run on generator at industrial diesel prices, the blended cost is about USD 0.06–0.07/kWh, before genset depreciation.
- A 6.5 kW continuous load usually exceeds a typical residential service connection, so a service upgrade or a commercial connection is needed.

---

## 3) Implications for the LATAM used-hardware rental business

1. **Electricity dominates operating cost for consumer GPUs, and Colombia is uncompetitive on it.** At about USD 0.26–0.31/kWh plus up to +70% on excess consumption during the El Niño program (at least until about March 2027), a used RTX-class GPU in Bogotá costs about USD 0.12–0.20 per GPU-hour in power alone. That is roughly what such GPUs fetch on P2P marketplaces. Colombia works as a **sourcing market** for used hardware, if prices there are good (another agent's topic), not as a hosting location.
2. **Ecuador (Quito or Cuenca) is the best hosting location on cost:** about USD 0.086–0.09/kWh on a commercial low-voltage-with-demand meter, free cooling at altitude, 1 Gbps fiber for about USD 40–50/month, Miami about 54 ms away, USD economy (no FX risk), and cheap labour. The caveat is a **structural hydro deficit**: plan for a UPS plus a diesel genset with ATS (about USD 8–18k for 16 GPUs) and for days-long outages if residential rationing returns as in 2024.
   - **Stay on a low-voltage commercial connection.** Medium- and high-voltage users were the ones cut for 48 h to 7 days in Sep–Oct 2026, and medium voltage is pricier per kWh.
   - **Never use a residential meter**: blocks above 3,500 kWh are priced at USD 0.68/kWh.
3. **Bogotá is the only market with a real colocation ecosystem.** Colo costs (ESTIMATE USD 250–450/kW-month retail; CBRE wholesale USD 150–230) only pencil out for data-centre-class GPUs where revenue per kW is high. For a 4–16 used-consumer-GPU business, a small self-run commercial space with good fiber is more economical.
4. **Venezuela looks cheap on paper (power, diesel, labour, best latency to Miami) but is the riskiest choice.** Daily multi-hour outages, especially in Maracaibo and Zulia, plus a national crypto-mining ban with bounties and seizures make kilowatt-scale GPU racks a confiscation risk. Add a tariff reform that will index electricity to USD, currency volatility (BCV rate up about 200% year on year) and sanctions/payment frictions. It is not recommended for hosting, though it may still be a sourcing market for hardware.
5. **Connectivity is not a blocker** in any of the three countries. Latency to US-East is 35–80 ms. Budget a business line with a public static IP if the target marketplaces need inbound ports. Treat Europe as a secondary market (about 135–175 ms).
6. **Tax incentives are not a reason to choose a location at this scale.** Colombia's free-zone 20% rate requires free-zone residency and applies only to export income. Ecuador and Venezuela have no usable data-center regime.

**Ranking for hosting a 4–16 GPU cluster** (best first): **Quito ≈ Cuenca > Bogotá > Guayaquil > Medellín > Cali > Barranquilla > Caracas > Valencia > Maracaibo.** Bogotá ranks above Guayaquil only if colocation or grid stability outweighs a 3.5× power price; on pure operating cost, Guayaquil beats every Colombian city.

---

## 4) Confidence and gaps

| Item | Confidence | Gap / next step |
|---|---|---|
| Enel Bogotá tariffs | **High** (official sheet, Aug 2026) | Sep–Nov 2026 sheets were blocked by Enel's bot protection. Bills rose 7.24% Jan–Sep 2026. |
| Other Colombian utilities (EPM, Emcali, Air-e, Celsia) | Medium (secondary, June 2026 CU only) | Get official EPM, Emcali and Air-e commercial sheets for Oct–Nov 2026. |
| CREG El Niño surcharge | **High** (Enel Q&A citing CREG 101 120 and 101 126 of 2026) | Cap value and exact reference target for new accounts not found. |
| Ecuador tariffs | **High** (Registro Oficial, 30 Sep 2026, valid Oct–Dec 2026) | 2027 schedule pending (due about Dec 2026). Municipal surcharges on the bill not verified. |
| Venezuela tariffs | **Low** | No official schedule found; the USD-indexed reform is pending its implementing regulation. |
| Reliability (EC/VE/CO) | High for events, medium for outlook | Ecuador residential policy beyond Nov 2026; Colombian rationing decisions in Q1 2027. |
| Fiber prices | Medium (comparison sites, Apr–Jun 2026) | Business plans with static IP / SLA not found. **CGNAT policy unverified.** |
| Colocation | Medium (CBRE, HostDime list) | No Ecuador or Venezuela price quotes. Bogotá retail per-kW for GPU density needs quotes from HostDime, KIO, Equinix, Cirion, IPXON and Telconet. |
| Backup equipment costs | Low–medium (retail listings, partly non-LATAM) | Get local genset and UPS quotes (Colombia: RETIE-certified; Ecuador: prices inflated during the crisis). |
| Climate / PUE | Medium (climatological normals not re-verified; PUE is my estimate) | Measure inlet temperatures in a pilot. |
| Labour | Medium (job ads, minimum wages confirmed) | No part-time contracts found; part-time figures are pro-rata estimates. |
| Exchange rates | High for COP and BCV; low for the VES parallel rate | COP moved from about 4,000 to about 3,300 in 2026, which matters for every Colombian USD figure. |

*Process note: the shared web-search budget for this session ran out before the climate lookups and some remaining checks, so a few items rely on general knowledge and are labelled ESTIMATE.*

---

## 5) Sources (all accessed 2026-11-14)

**Colombia: tariffs, regulation, FX, fuel, labour**
- Enel Colombia, official tariff sheet for August 2026 (CREG-regulated): https://www.enel.com.co/content/dam/enel-co/español/personas/1-17-1/2026/pliego%20tarifario%20digital%20_agosto_2026.pdf
- Enel Colombia, Q&A "Programa Incentivo Uso Eficiente de Energía Eléctrica 2026" (CREG 101 120 and 101 126 of 2026): https://www.enel.com.co/content/dam/enel-co/meta-de-consumo/QA_INCENTIVO_USO_EFICIENTE_DE_ENERG%C3%8DA_EL%C3%89CTRICA.pdf
- Bloomberg Línea, CREG surcharge plan (1 Sep 2026): https://www.bloomberglinea.com/latinoamerica/colombia/recargo-en-la-factura-de-energia-en-colombia-desde-septiembre-asi-funciona-el-nuevo-plan-de-ahorro-de-la-creg/
- Valora Analitik, estrato-4 tariffs by utility, June 2026 data (published 8 Sep 2026): https://www.valoraanalitik.com/?p=610477
- El Colombiano, Air-e raises CU to COP 840.15 (23 Jun 2026): https://www.elcolombiano.com/negocios/air-e-aumenta-tarifa-energia-costa-caribe-kwh-sube-840-GC38099348
- El Colombiano, EPM estrato-3 tariff COP 790.49 (Dec 2025): https://www.elcolombiano.com/negocios/precios-de-energia-colombia-bajaron-cuatro-veces-frente-2025-IP33786860
- Infobae, EPM rejects the government tariff formula (20 Feb 2026): https://www.infobae.com/colombia/2026/02/20/tarifas-en-la-mira-epm-le-dijo-no-al-esquema-de-gustavo-petro-y-el-pulso-politico-subio-de-tono/
- Portafolio, XM rationing-risk warning (deficit of 3,906 GWh/year): https://www.portafolio.co/energia/xm-advierte-riesgo-de-racionamiento-por-deficit-de-energia-frente-a-la-demanda-y-retrasos-en-nuevos-proyectos-497564
- Portafolio, XM's 31 days to store water: https://www.portafolio.co/energia/xm-alerta-por-los-31-dias-que-le-quedan-al-pais-para-almacenar-agua-antes-del-verano-505491
- Vanguardia, reservoir levels (24 Oct 2026): https://www.vanguardia.com/economia/nacional/2026/10/24/el-nivel-de-los-embalses-preocupa-asi-estan-las-reservas-de-agua-en-colombia-ante-el-nino/
- Noticias RCN, Colombia's energy deficit: https://www.noticiasrcn.com/economia/colombia-enfrenta-deficit-energetico-en-medio-del-fenomeno-de-el-nino-1042850
- Forbes Colombia, savings program (1 Sep 2026): https://forbes.co/2026/09/01/sostenibilidad/ahorrar-energia-tendra-beneficio-y-consumir-de-mas-un-cobro-adicional/
- Noticias Caracol, TRM on 11 Nov 2026: https://www.noticiascaracol.com/economia/precio-del-dolar-hoy-11-de-noviembre-de-2026-en-colombia-volvio-a-subir-la-trm-so35
- Noticias RCN, TRM on 10 Nov 2026: https://www.noticiasrcn.com/economia/dolar-en-colombia-hoy-martes-10-de-noviembre-de-2026-1080463
- CREG Circular 371 of 2026 (fuel prices, Nov 2026): https://gestornormativo.creg.gov.co/gestor/entorno/docs/originales/Circular_CREG_371_2026/
- Minuto60, diesel price in Bogotá for November: https://minuto60.com/economia/precio-gasolina-noviembre-colombia-asi-quedo-ciudades/18118
- Portafolio, fuel prices unchanged in November: https://www.portafolio.co/energia/precios-de-gasolina-y-diesel-seguiran-sin-cambios-en-noviembre-asi-quedaron-las-tarifas-por-ciudades-505475
- Consultorsalud, minimum wage 2026 (Decrees 1469 and 1470 of 2025): https://consultorsalud.com/aumento-del-salario-minimo-en-colombia-2026/
- Elempleo.com, job ads: https://www.elempleo.com/co/ofertas-trabajo/profesional-de-infraestructura-ti-windows-server-y-linux-bogota-1886780527 and https://www.elempleo.com/co/ofertas-trabajo/tecnico-soporte-1886743912
- Asuntos Legales, free-zone 20% rate and Decree 47/2024: https://www.asuntoslegales.com.co/consumidor/asi-puede-mantener-la-tarifa-preferencial-del-impuesto-sobre-la-renta-en-zonas-francas-con-nuevo-decreto-3799312
- La República, Zona Franca de Bogotá data center complex: https://www.larepublica.co/empresas/zona-franca-de-bogota-invertira-us-90-millones-en-nuevo-complejo-de-data-centers-2847162
- Colombiatramita, solar costs 2026: https://colombiatramita.co/servicios-publicos/paneles-solares-colombia/
- Homecenter Colombia, Bauker 5.5 kW diesel generator: https://www.homecenter.com.co/homecenter-co/product/263620/planta-electrica-diesel-55kw-5500w-110-220v-115lt-bauker/263620/

**Ecuador**
- Registro Oficial 9º Suplemento Nº 380 (30 Sep 2026), ARCONEL tariff charges Oct–Dec 2026 (PDF hosted by Expreso): https://www.expreso.ec/uploads/files/2026/09/30/Tarifas%20Arconel%20ef4f903e-c21b-42aa-83a8-9f88b1418f44%20-2-.pdf
- gob.ec, Resolution ARCONEL-029-2025 (2026 tariff schedule): https://www.gob.ec/regulaciones/resolucion-nro-arconel-029-2025-anexos-cert-pliego-tarifario-servicio-publico-energia-electrica-ano-2026
- El Diario EC, 2026 system costs (average USD 0.1061/kWh): https://www.eldiario.ec/centro/ecuador-aprobo-los-costos-de-la-energia-electrica-spee-para-2026-la-agencia-de-regulacion-y-control-de-electricidad-arconel-20251206/
- Primicias, new high-voltage tariff from October 2026: https://www.primicias.ec/economia/nueva-tarifa-kilovatio-hora-empresas-alto-consumo-electricidad-octubre-133809/
- Teleamazonas, disconnections extended to 72 h (1 Oct 2026): https://www.teleamazonas.com/actualidad/noticias/economia/ecuador-extiende-desconexion-electrica-grandes-industrias-cae-nivel-mazar-129418/
- Rio Times, industry tariff and blackouts (3 Oct 2026): https://www.riotimesonline.com/ecuador-industry-tariff-review-blackouts-2026/
- Rio Times, household pledge (5 Oct 2026): https://www.riotimesonline.com/ecuador-blackouts-noboa-household-pledge-2026/
- Vistazo, 7-day cuts for high- and medium-voltage users (14 Oct 2026): https://www.vistazo.com/actualidad/2026-10-14-empresas-alto-mediano-voltaje-ecuador-cortes-energia-siete-dias-consecutivos-PF11275749
- El Comercio, 4-day disconnections in November (30 Oct 2026): https://www.elcomercio.com/actualidad/negocios/empresas-de-ecuador-tendran-desconexiones-de-4-dias-desde-noviembre/
- Cuenca Dispatch, self-generation by large users (6 Apr 2026): https://thecuencadispatch.com/big-power-users-switch-to-self-generation-as-ecuador-protects-household-electricity-supply/
- Primicias, diesel USD 3.06 from 12 Nov 2026: https://www.primicias.ec/economia/precios-gasolinas-diesel-reduccion-cinco-centavos-noviembre-136725/
- Cuantomecuesta, Ecuador fiber prices (Apr 2026): https://cuantomecuesta.com/ec/internet-fibra/
- Vistazo, minimum wage USD 482: https://www.vistazo.com/2025-12-15-salario-basico-usd-482-2026-ecuador-incremento-dolares-IC10565269
- Cazvid, Quito technician job ads: https://cazvid.com/es/empleo/tecnico-en-sistemas-en-quito-pichincha-ecuador and https://cazvid.com/empleo/tecnico-de-soporte-n1-en-quito-pichincha-ecuador
- DPL News, CAF–Ecuador data center MoU (26 Feb 2026): https://dplnews.com/?p=307161
- Inflect, Ecuador data center market: https://inflect.com/datacenters/latam/ecuador
- SubTel Forum, Telconet Guayaquil data center: https://subtelforum.com/telconet-opens-guayaquil-data-center-as-csn-1-advances/
- Datacentermap, Cirion GUA1: https://www.datacentermap.com/ecuador/guayaquil/cirion-gua1/
- Cirion QUI2 spec sheet: https://lp.ciriontechnologies.com/hubfs/Other%20Files/Downloadable%20Assets/data-sheet-web/cirion-technologies-data-center-spec-sheet-qui2-eng.pdf
- Datacenters.com, IPXON Quito: https://www.datacenters.com/ipxon-networks-quito

**Venezuela**
- elDiario, tariff indexation and electricity law reform (10 Nov 2026): https://eldiario.com/2026/11/10/jorge-rodriguez-tarifas-electricas-estaran-indexadas/
- elDiario / EFE, electricity crisis (5 Sep 2026): https://eldiario.com/2026/09/05/crisis-electrica-venezuela-2/
- elDiario, cuts of up to 16 h (25 Sep 2026): https://eldiario.com/2026/09/25/cortes-luz-protestas/
- Caracas Chronicles (15 May 2026): https://www.caracaschronicles.com/2026/05/15/delcys-fragile-reopening-meets-the-old-power-crisis/
- elDiario, Conindustria on self-generation (11 Aug 2026): https://eldiario.com/2026/08/11/autogeneracion-sector-industrial/
- Cleary Gottlieb, electricity reform memo (2026): https://www.clearygottlieb.com/-/media/files/alert-memos-2026/venezuelas-electricity-reform-takeaways-for-investors.pdf
- Enerdata, Venezuela energy profile: https://www.enerdata.net/estore/country-profiles/venezuela.html
- Finanzas Digital, Cavececo on the 28% commercial increase: https://finanzasdigital.com/cavececo-ocupacion-centros-comerciales-2026/
- NTN24, BCV rate on 9 Nov 2026: https://www.ntn24.com/noticias-economia/el-dolar-y-el-euro-en-venezuela-estan-por-las-nubes-asi-cotizan-este-lunes-9-de-noviembre-664838
- Finanzas Digital, BCV rate on 6 Nov 2026: https://finanzasdigital.com/tasa-de-cambio-bcv-06-noviembre-2026/
- The Logistics World / EFE, industrial diesel USD 0.32/L (17 Jul 2026): https://thelogisticsworld.com/actualidad-logistica/venezuela-finaliza-subsidio-total-al-diesel-para-el-sector-industrial
- DailyFuels, Venezuela fuel prices (Oct 2026): https://dailyfuels.com/venezuela/?lang=es
- iProUP, USD 1,000 bounty for reporting miners in Carabobo (May 2026): https://www.iproup.com/economia-digital/67693-venezuela-paga-1000-dolar-denunciar-mineros-bitcoin-decomiso-carabobo-mayo-2026
- Criptonoticias, ASIC seizures: https://criptonoticias.com/mineria/venezuela-mineros-bitcoin-criptomonedas-decomiso
- KPMG, special economic zone incentives (Jul 2025): https://kpmg.com/us/en/taxnewsflash/news/2025/07/tnf-venezuela-requirements-for-special-economic-zones-incentives.html
- El Caribe, SimpleFibra plans: https://www.elcaribe.com.do/panorama/internacionales/planes-de-internet-que-ofrece-simpletv-en-venezuela-y-sus-precios/
- NTN24, CANTV fiber prices: https://www.ntn24.com/noticias-actualidad/cantv-ofrece-servicio-de-internet-por-fibra-optica-conozca-los-precios-400775
- CazVid, technician salaries in Venezuela (Jun 2026): https://cazvid.com/es/blog/cuanto-gana-un-tecnico-en-venezuela

**Cross-country: connectivity, colocation, cooling**
- WonderNetwork live pings, measured 14 Nov 2026: https://wondernetwork.com/pings/Bogota , https://wondernetwork.com/pings/Quito , https://wondernetwork.com/pings/Caracas
- Colombiamove, Colombian home internet comparison (28 Jun 2026): https://colombiamove.com/blog/internet-hogar-colombia-comparativa-2026/
- Hacecuentas, Colombian fiber price calculator: https://hacecuentas.com/co/calculadora-precio-internet-fibra-tigo-claro-etb-2026-promo
- CBRE, Global Data Center Trends 2026: https://www.cbre.com/insights/reports/global-data-center-trends-2026
- HostDime, Colombia colocation: https://www.hostdime.com/colombia-colocation
- Inflect, Bogotá data centers: https://inflect.com/datacenters/colombia/bogota
- EdgeConneX, Bogotá data sheet: https://edgeconnex.com/wp-content/uploads/2025/04/Bogota-Data-Sheet.pdf
- ResearchAndMarkets, Colombia data center portfolio (Jan 2026): https://www.globenewswire.com/news-release/2026/01/07/3214329/0/en/Colombia-Colocation-Data-Center-Portfolio-Report-2025-2029-Detailed-Analysis-of-25-Existing-Data-Centers-9-Upcoming-Data-Centers-and-19-Major-Operators-Investors.html
- Lenovo SR665, altitude derating (ASHRAE classes): https://pubs.lenovo.com/sr665/temp_humidity_altitue_spec
- IBM, environmental design criteria: https://www.ibm.com/docs/P9ESS/p9ebe/p9ebe_tempandhumiditydesign.htm
- Autosolar, 20 kVA silent generator: https://autosolar.es/generadores-diesel/generador-diesel-insonorizado-20kva-gds20t-400230v
- Markit, Tripp Lite 10 kVA UPS (Mexico): https://www.markit.eu/mx/es/s3m10k2b/v2p24475672
- AIO, Qoltec 10 kVA UPS: https://aio.lv/en/product--qoltec-53044--1935351.md

---

## Comparison table

| Country / city | USD/kWh (best realistic option) | Reliability rating (A best – E worst) | Fiber USD/month (~1 Gbps) | Colocation availability | Cooling advantage | Overall rank (4–16 GPUs) |
|---|---|---|---|---|---|---|
| **Ecuador / Quito** | **0.086–0.094** (commercial low voltage with demand, Oct–Dec 2026) | **C**: households protected in 2026, but 14 h/day cuts in 2024; medium/high-voltage firms cut 2–7 days in Oct 2026 | **38–45** (home); business with static IP ~80–150 (estimate) | Small: Cirion QUI2, IPXON (1U+); Telconet Quito planned | **High** (2,850 m, ~14 °C; PUE ~1.1–1.25) | **1** |
| **Ecuador / Cuenca** | **0.089** | **C** (Mazar/Paute complex nearby; same national grid) | ~38–50 | Minimal | **High** (2,560 m, ~15 °C) | **2** |
| **Colombia / Bogotá** | **0.262** (home E4) / **0.314** (commercial) / up to **0.53** on excess kWh under the El Niño surcharge | **B−**: no rationing so far; high El Niño risk to about Mar 2027 | 32–76 (home 900 Mbps–1 Gbps); business ~100–200 (estimate) | **Best**: HostDime Tier IV (1U USD 175 at 0.2 kW), Equinix, KIO, EdgeConneX, ODATA; wholesale USD 150–230/kW-month | **High** (2,640 m, ~14 °C) | **3** |
| **Ecuador / Guayaquil** | **0.090** | **C** | 38–50 | Medium: Cirion GUA1 (3–20 kW racks), Telconet TCC III (Sep 2026) | **Low** (hot, humid; PUE ~1.5–1.7) | **4** |
| **Colombia / Medellín** | ~**0.29–0.32** (EPM commercial, estimated) | **B−** | 32–76 | Limited | Medium (1,495 m, ~22 °C) | **5** |
| **Colombia / Cali** | ~**0.316** (Emcali CU × 1.2) | **B−** | 32–76 | Minimal | Low–medium (~24–25 °C) | **6** |
| **Colombia / Barranquilla** | ~**0.306** (Air-e CU × 1.2) | **C+**: Caribbean grid with weaker distribution and a financially stressed utility (estimate) | 32–76 | Minimal | **Low** (~28 °C, humid, salty) | **7** |
| **Venezuela / Caracas** | ~**0.02–0.08** (estimate; USD indexation coming) plus generator hours | **D**: 82% of households had daily interruptions (Sep 2026) | ~53 (500 Mbps); 1 Gbps scarce | Very limited, unknown pricing | Medium (~900 m, ~21–22 °C) | **8** |
| **Venezuela / Valencia** | ~0.02–0.08 (estimate) | **D−**: cuts plus a crypto-miner bounty (Carabobo) | ~25–55 | None found | Low (~25 °C) | **9** |
| **Venezuela / Maracaibo** | ~0.02–0.08 (estimate) | **E**: 99% of households interrupted daily, cuts up to 16 h | 25–35 (Airtek, 2022 data) | None found | **Very low** (~28–29 °C) | **10** |

Ranking logic: power cost per GPU-hour carries about 40% of the weight, reliability and legal risk 30%, cooling 10%, colocation and connectivity 10%, and labour and incentives 10%. Quito and Cuenca win on cost despite their reliability risk, which is solvable with an estimated USD 8–18k of UPS and genset for 16 GPUs. Bogotá wins only if colocation or grid stability is required.

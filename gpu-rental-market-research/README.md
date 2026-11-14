# GPU / Server Rental Market Research (Colombia, Ecuador, Venezuela)

**Question:** Is it viable to buy old servers and GPUs in Colombia, Venezuela or Ecuador, build small clusters, and rent them to peer-to-peer and decentralized compute marketplaces (Vast.ai, Salad, Clore, Akash, io.net, and others)?

**Answer (2026-11-14):** Not at today's hardware prices. It works only if hardware is sourced well below the global used market (about 30–35% of US price for 4090/5090, about 55–70% for A100/H100), and run lean in Quito or Cuenca on a commercial power meter. See the synthesis.

## Contents

| Path | What it is |
|---|---|
| [`00-MASTER-SYNTHESIS.md`](00-MASTER-SYNTHESIS.md) | **Start here.** Verdict, price benchmark tables, cost side, model results, go/no-go checklist, next steps |
| [`agent-reports/`](agent-reports/) | 10 detailed research reports (01–10), each with sources and confidence labels |
| [`model/unit_economics.py`](model/unit_economics.py) | Profit model per 4-GPU box. All assumptions are at the top, each tagged with its source report. Edit and re-run |
| [`model/results.md`](model/results.md) · [`model/results.csv`](model/results.csv) | Output of the model run (base, bull and bear scenarios; site comparison; maximum purchase price; lean-site and cheap-hardware sensitivities) |

## Re-running the model

```bash
python3 model/unit_economics.py          # print tables
python3 model/unit_economics.py --csv    # also write model/results.csv
```

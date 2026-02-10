# argo_seir-eakf-modeling

This repository contains an end-to-end Jupyter notebook for reproducing the analysis outputs written to `./outputs4/`.

**Primary notebook to run:**
- `ARGOX_E2E_FINAL v2.ipynb`  (recommended / most up-to-date)
- `ARGOX_E2E_FINAL.ipynb`     (older)

## What you can reproduce
Running `ARGOX_E2E_FINAL v2.ipynb` end-to-end will generate outputs into:

- `./outputs4/`

## Repository layout (key items)
- `ARGOX_E2E_FINAL v2.ipynb` — main end-to-end notebook
- `config/state_locs.csv` — state centroid/locations config used by helper logic
- `cache/config/state_fips_map.csv` — FIPS → state mapping used in mobility build
- `cache/rt_state_weekly.csv` — weekly state R(t) input used in alignment/plots
- `cache/mobility_state_weekly_total_fromSafeGraph.csv` — weekly state mobility totals (prebuilt)

The `outputs4/` folder is **generated** and not tracked.

## Setup
### 1) Clone
```bash
git clone git@github.com:bcristol93/argo_seir-eakf-modeling.git
cd argo_seir-eakf-modeling

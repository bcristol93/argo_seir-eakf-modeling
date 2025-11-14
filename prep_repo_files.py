# prep_repo_files.py
# Run this once from the repo root to create .gitignore, requirements.txt, README.md

# --- .gitignore ---
gitignore_text = """__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.env/
.DS_Store
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_text)

# --- requirements.txt ---
requirements_text = """pandas>=2.2
numpy>=2.0
matplotlib>=3.8
scikit-learn>=1.4
xarray>=2024.1
netCDF4>=1.6
tqdm>=4.66
"""

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements_text)

# --- README.md ---
readme_text = """# End-to-end ARGOX + SEIR–EAKF Pipeline

This repo contains an end-to-end implementation of the ARGOX + SEIR–EAKF pipeline.

## Contents

- `ARGOX_E2E_FINAL.ipynb` — main notebook  
- `config_locations.py` — builds `cache/config/state_fips_map.csv`  
- `mobility_helper.py` — mobility pre-processing and plotting helpers  
- `mobility df/` — processed mobility data used as inputs  
- `cache/` — cached inputs and intermediate data (ILI, GT, AH, Rt, SEIR–EAKF, etc.)  
- `out/argox/` — ARGOX outputs (Rt weekly csv, predictions, terms)  
- `outputs/` — figure PNGs and quicklook plots  

All notebook paths are relative to the repo root, so this should run on Mac, Linux, or Windows without modifications.

## Running

```bash
pip install -r requirements.txt
jupyter lab
"""
# -*- coding: utf-8 -*-
"""
State-level configuration for ARGO/ARGOX runs + FIPS utilities.
Creates cache/config/state_fips_map.csv on import if missing.
"""

from pathlib import Path
import pandas as pd

# ------------------------------------------------------------
# Flu seasons (for plotting or time windows)
SEASONS = [2019, 2020, 2021, 2022, 2023, 2024, 2025]

# === Core state list ===
STATE_LIST = [
    "PA", "TX", "CA", "NY", "FL", "IL", "GA", "NC", "OH", "MI",
    "VA", "WA", "MA", "AZ", "NJ", "CO", "TN", "MN", "MO", "IN"
]
TARGET_STATES = STATE_LIST

# === Google Trends geos/terms ===
STATE_TO_GT = {s: f"US-{s}" for s in STATE_LIST}
DEFAULT_GT_TERMS = [
    "flu", "influenza", "flu symptoms", "fever", "cough",
    "tamiflu", "oseltamivir", "sore throat", "body aches",
    "flu shot", "flu vaccine", "flu clinic"
]

# ------------------------------------------------------------
# FIPS <-> state abbreviation mapping (50 states + DC)
_ABBR_TO_FIPS = {
    "AL":1,  "AK":2,  "AZ":4,  "AR":5,  "CA":6,  "CO":8,  "CT":9,  "DE":10, "DC":11,
    "FL":12, "GA":13, "HI":15, "ID":16, "IL":17, "IN":18, "IA":19, "KS":20, "KY":21,
    "LA":22, "ME":23, "MD":24, "MA":25, "MI":26, "MN":27, "MS":28, "MO":29, "MT":30,
    "NE":31, "NV":32, "NH":33, "NJ":34, "NM":35, "NY":36, "NC":37, "ND":38, "OH":39,
    "OK":40, "OR":41, "PA":42, "RI":44, "SC":45, "SD":46, "TN":47, "TX":48, "UT":49,
    "VT":50, "VA":51, "WA":53, "WV":54, "WI":55, "WY":56
}
_FIPS_TO_ABBR = {v: k for k, v in _ABBR_TO_FIPS.items()}

def abbr_to_fips(abbr: str) -> int:
    """Return integer state FIPS for a two-letter abbreviation."""
    return _ABBR_TO_FIPS[abbr.upper()]

def fips_to_abbr(fips: int) -> str:
    """Return two-letter abbreviation for an integer state FIPS."""
    return _FIPS_TO_ABBR[int(fips)]

def ensure_state_fips_csv(cache_root: str | Path = "cache") -> Path:
    """Ensure cache/config/state_fips_map.csv exists with columns state_fips,state_abbr."""
    cfg_dir = Path(cache_root) / "config"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    csv_path = cfg_dir / "state_fips_map.csv"
    if not csv_path.exists():
        df = pd.DataFrame(
            {"state_fips": list(_FIPS_TO_ABBR.keys()),
             "state_abbr": [ _FIPS_TO_ABBR[f] for f in _FIPS_TO_ABBR ]}
        ).sort_values("state_fips")
        df.to_csv(csv_path, index=False)
        print(f"[config_locations] Created {csv_path}")
    else:
        try:
            df = pd.read_csv(csv_path)
            assert {"state_fips", "state_abbr"} <= set(df.columns)
        except Exception:
            df = pd.DataFrame(
                {"state_fips": list(_FIPS_TO_ABBR.keys()),
                 "state_abbr": [ _FIPS_TO_ABBR[f] for f in _FIPS_TO_ABBR ]}
            ).sort_values("state_fips")
            df.to_csv(csv_path, index=False)
            print(f"[config_locations] Rewrote malformed {csv_path}")
    return csv_path

# Create CSV on import
ensure_state_fips_csv()

if __name__ == "__main__":
    print("Loaded config_locations.py")
    print("States:", STATE_LIST[:5], "… (total:", len(STATE_LIST), ")")
    print("Example GT mapping:", {k: STATE_TO_GT[k] for k in list(STATE_TO_GT)[:3]})

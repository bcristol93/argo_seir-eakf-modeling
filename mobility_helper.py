
# -*- coding: utf-8 -*-
"""
Mobility helpers. Mobility is OPTIONAL; set use_mobility=False to disable.
"""

import pandas as pd

def load_mobility(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    # expected columns: origin_fips, dest_fips, week, visits (or similar)
    for col in ["origin_fips", "dest_fips"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.extract(r"(\d+)")[0].str.zfill(5)
    return df

def inflows_by_week(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sum incoming visits to destination county per week (INCLUDING intra-county).
    Returns columns: week, dest_fips, total_inflow
    """
    if "week" not in df.columns:
        raise ValueError("Mobility frame must include a 'week' column (weekly date).")
    infl = (df.groupby(["week","dest_fips"])["visits"]
              .sum().rename("total_inflow").reset_index())
    return infl

def series_for_fips(inflows: pd.DataFrame, fips: str) -> pd.Series:
    """
    Extract a weekly inflow series for a single destination FIPS.
    """
    s = (inflows.loc[inflows["dest_fips"]==fips]
                .set_index("week")["total_inflow"]
                .sort_index())
    s.index = pd.to_datetime(s.index)
    return s.asfreq("W-MON")

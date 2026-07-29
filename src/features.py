import pandas as pd
import numpy as np

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selects model features by excluding leakage, admin, and demographic columns.

    """
    TARGET = "esi"
    DEMOGRAPHICS = ["age", "gender", "ethnicity", "race", "lang", "religion",
                    "maritalstatus", "employstatus", "insurance_status"]
    ADMIN = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
    LEAKAGE = ["disposition", "previousdispo"]

    # Filter features based on notebook logic
    features = [c for c in df.columns if c != TARGET and c not in LEAKAGE + ADMIN + DEMOGRAPHICS]
    
    return df[features]

def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineers clinical indices (Shock Index, SpO2/RR) and red-flag flags.
    
    """
    out = df.copy()

    # Ratios & combinations
    out["shock_index"]    = out["triage_vital_hr"] / out["triage_vital_sbp"]      
    out["pulse_pressure"] = out["triage_vital_sbp"] - out["triage_vital_dbp"]      
    out["spo2_rr_ratio"]  = out["triage_vital_o2"] / out["triage_vital_rr"]        

    # Red-flag flags
    out["is_tachypneic"]     = (out["triage_vital_rr"]   > 20).astype(int)   
    out["is_hypoxic"]        = (out["triage_vital_o2"]   < 92).astype(int)   
    out["is_febrile"]        = (out["triage_vital_temp"] >= 100.4).astype(int)  
    out["is_bradycardic"]    = (out["triage_vital_hr"]   < 60).astype(int) 
    out["is_hyperglycaemic"] = (out["triage_vital_glucose"] > 180).astype(int) 
    out["resp_distress"]     = ((out["is_hypoxic"] == 1) | (out["is_tachypneic"] == 1)).astype(int)

    # Severity score
    red_flag_cols = ["is_tachypneic", "is_hypoxic", "is_febrile", "is_bradycardic", "is_hyperglycaemic", "resp_distress"]
    out["red_flag_count"] = out[red_flag_cols].sum(axis=1)

    return out

def encode_demographics(df: pd.DataFrame, use_demographics: bool = False) -> pd.DataFrame:
    """
    Applies one-hot encoding to demographic features and preserves age/gender.
    
    """
    if not use_demographics:
        return df
    
    # 1. One-hot encode ethnicity and race
    demo_1hot = pd.get_dummies(df[["ethnicity", "race"]], prefix=["eth", "race"], dtype=int)
    
    # 2. Combine with original features
    # Ensure we don't drop age and gender
    out = pd.concat([df.drop(columns=["ethnicity", "race"]), demo_1hot], axis=1)
    
    return out
import pandas as pd
import numpy as np

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selects model features by excluding leakage, admin, and demographic columns.
    Matches the 'choose columns; exclude leakage/admin/demographics' structure.
    """
    TARGET = "esi"
    DEMOGRAPHICS = ["age", "gender", "ethnicity", "race", "lang", "religion",
                    "maritalstatus", "employstatus", "insurance_status"]
    ADMIN = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
    LEAKAGE = ["disposition", "previousdispo"]

    # Filter features based on your notebook logic
    features = [c for c in df.columns if c != TARGET and c not in LEAKAGE + ADMIN + DEMOGRAPHICS]
    
    return df[features]

def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()
    
    # Shock Index = HR / SBP
    if 'triage_vital_hr' in df.columns and 'triage_vital_sbp' in df.columns:
        df["shock_index"] = df["triage_vital_hr"] / df["triage_vital_sbp"]
        
    # SpO2 / RR ratio
    if 'triage_vital_o2' in df.columns and 'triage_vital_rr' in df.columns:
        df["o2_rr_ratio"] = df["triage_vital_o2"] / df["triage_vital_rr"]
        
    # Red-flag flags
    df["flag_tachycardia"] = (df["triage_vital_hr"] > 120).astype(int)
    
    return df

def encode_demographics(df: pd.DataFrame, use_demographics: bool = False) -> pd.DataFrame:
    """
    Applies one-hot encoding to demographic features.
    """
    if not use_demographics:
        return df
        
    return pd.get_dummies(df, columns=["gender"], prefix="demog")
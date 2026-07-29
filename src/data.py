import pandas as pd
import numpy as np 
import os

#Function used to load raw data
def load_raw(path: str) -> pd.DataFrame:
    """
    Loads the raw dataset from the specified CSV path.
    """
    # Check if the file exists to make your pipeline fail loudly
    if not os.path.exists(path):
        raise FileNotFoundError(f"Could not find the dataset at: {path}")
        
    return pd.read_csv(path)


#Function Used to Clean Raw Data

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw clinical data. 
    Handles vitals coercion, ESI filtering, gender encoding, and median imputation.
    """
    df = df.copy()
    
    # 1. Drop stray index columns
    df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")], errors="ignore")

    # 2. Normalize glucose column names and force vitals to be NUMBERS
    if "triage_glucose" in df.columns and "triage_vital_glucose" not in df.columns:
        df = df.rename(columns={"triage_glucose": "triage_vital_glucose"})

    VITALS = ["triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp", 
              "triage_vital_rr", "triage_vital_o2", "triage_vital_temp", "triage_vital_glucose"]
    
    for col in VITALS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 3. Clean ESI labels (Ensure numeric and only 1-5)
    df["esi"] = pd.to_numeric(df["esi"], errors="coerce")
    df = df[df["esi"].isin([1, 2, 3, 4, 5])].copy()

    # 4. Blank out physically impossible vitals
    # Temperature (90-110 F) and O2 (<= 100)
    if "triage_vital_temp" in df.columns:
        df.loc[(df["triage_vital_temp"] < 90) | (df["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    
    if "triage_vital_o2" in df.columns:
        df.loc[df["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # 5. Encode gender (Handles "m"/"male" -> 0, "f"/"female" -> 1)
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower().map(
            {"male": 0, "m": 0, "female": 1, "f": 1})

    # 6. Fill missing numbers with median
    # Only filling columns that exist in the dataframe to avoid errors
    cols_to_impute = [c for c in (VITALS + ["age", "gender"]) if c in df.columns]
    for col in cols_to_impute:
        df[col] = df[col].fillna(df[col].median())

    # 7. Final type casting
    df["esi"] = df["esi"].astype(int)
    
    return df



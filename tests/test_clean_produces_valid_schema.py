from src.data import load_raw, clean
from src.features import add_clinical_features, encode_demographics, select_features
from src.model import build_model
from sklearn.model_selection import train_test_split


def test_clean_produces_valid_schema():
    """
    Checks if the data is the shape the model expects after cleaning.
    """
    raw = load_raw("yaleemmlc_admissionprediction_triage.csv")
    df = clean(raw) 
    
    # 1. Verify ESI labels are within the valid 1-5 range
    assert df["esi"].isin([1,2,3,4,5]).all()
    
    # 2. Verify there are no missing gaps in vital signs
    assert df["triage_vital_hr"].isna().sum() == 0 
    
    # 3. Verify gender is correctly encoded as 0 or 1
    assert set(df["gender"].unique()) <= {0,1}
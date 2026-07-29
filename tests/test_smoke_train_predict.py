from src.data import load_raw, clean
from src.features import add_clinical_features, encode_demographics, select_features
from src.model import build_model
from sklearn.model_selection import train_test_split

def test_smoke_train_predict():
    raw = load_raw("yaleemmlc_admissionprediction_triage.csv")
    df = clean(raw)
    df = add_clinical_features(df)
    df = encode_demographics(df, use_demographics=False)

    X = select_features(df)
    y = df["esi"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = build_model(
        "random_forest",
        {"n_estimators": 100, "max_depth": 10, "class_weight": "balanced"},
        seed=42
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    assert len(preds) == len(y_test)
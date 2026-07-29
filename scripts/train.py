import yaml
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

# Importing  modular components
from src.data import load_raw, clean
from src.features import add_clinical_features, select_features, encode_demographics
from src.model import build_model, tune_model, evaluate

def main(config_path):
    # 1. Load Configuration
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    
    print(f"--- Pipeline starting with seed: {cfg['seed']} ---")

    # 2. Data Loading & Cleaning
    raw_df = load_raw(cfg["data"]["raw_path"])
    df = clean(raw_df)
    
    # 3. Feature Engineering
    # Clinical features -> Demographics
    df = add_clinical_features(df)
    df = encode_demographics(df, use_demographics=cfg["features"]["use_demographics"])
    
    # 4. Prepare X and y
    target = cfg["data"]["target"]
    if target not in df.columns:
        raise KeyError(f"Target column '{target}' not found in dataframe")

    y = df[target]
    X = select_features(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=cfg["seed"]
    )
    
    # 5. Model Building & Tuning
    # Using the first model listed in final_models
    model_name = cfg["final_models"][0]
    base_model = build_model(model_name, cfg["models"][model_name]["default_params"], seed=cfg["seed"])
    
    print(f"Training {model_name}...")
    # Using RandomizedSearchCV as defined in your model.py
    best_model = tune_model(
        base_model, X_train, y_train, 
        param_dist=cfg["models"][model_name]["param_grid"],
        seed=cfg["seed"]
    )
    
    # 6. Evaluation
    metrics = evaluate(best_model, X_test, y_test)
    
    print("--- Evaluation Results ---")
    for metric, value in metrics.items():
        print(f"{metric.capitalize()}: {value:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Carisurg training pipeline.")
    parser.add_argument("--config", default="config.yaml", help="Path to config file")
    args = parser.parse_args()
    
    main(args.config)
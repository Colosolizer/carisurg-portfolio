import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

def build_model(name: str, params: dict, seed: int = 42):
    """
    Constructs a model based on the name provided in config.
    """
    if name == "random_forest":
        return RandomForestClassifier(**params, random_state=seed, n_jobs=-1)
    
    else:
        raise ValueError(f"Model {name} not supported.")

def tune_model(model, X_train, y_train, param_dist, n_iter=8, cv=3, seed=42):
    """
    Performs RandomizedSearchCV to find the best hyperparameters.
    """
    search = RandomizedSearchCV(
        model,
        param_distributions=param_dist,
        n_iter=n_iter,
        cv=cv,
        scoring="f1_macro",
        random_state=seed,
        n_jobs=-1
    )
    search.fit(X_train, y_train)
    return search.best_estimator_

def evaluate(model, X_test, y_test):
    """
    Evaluates the model on six axes and measures inference time.
    """
    # Measure inference time
    start_time = time.time()
    preds = model.predict(X_test)
    inference_time = (time.time() - start_time) / len(X_test)
    
    # Calculate metrics
    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, average="macro", zero_division=0),
        "recall": recall_score(y_test, preds, average="macro", zero_division=0),
        "f1": f1_score(y_test, preds, average="macro"),
        "inference_time_ms": inference_time * 1000
    }
    
    return metrics
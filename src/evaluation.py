import json
from pathlib import Path

import numpy as np


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute R² score.
    """
    errors = np.sum((y_pred - y_true) ** 2)
    sst = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (errors / sst)


def adjusted_r2_score(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    n_features: int,
) -> float:
    """
    Compute adjusted R² score.
    """
    r2 = r2_score(y_true, y_pred)
    n_samples = len(y_true)
    return 1 - ((1 - r2) * (n_samples - 1) / (n_samples - n_features - 1))


def save_metrics(metrics: dict, output_path: str) -> None:
    """
    Save evaluation metrics as JSON.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
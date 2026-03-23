import json
from pathlib import Path

import numpy as np
import pandas as pd


COLUMNS_TO_DROP = [
    "Date",
    "Time",
    "PT08.S1(CO)",
    "PT08.S2(NMHC)",
    "PT08.S3(NOx)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - drop unused columns
    - drop empty columns
    - remove duplicates
    - replace invalid values (-200) with NaN
    - drop remaining missing values
    """
    df = df.copy()

    df = df.drop(columns=COLUMNS_TO_DROP, errors="ignore")
    df = df.dropna(axis=1, how="all")
    df = df.drop_duplicates()
    df = df.replace(-200, np.nan)
    df = df.dropna()

    return df


def scale_features(x: np.ndarray) -> np.ndarray:
    """
    Standardize features using mean and standard deviation.
    """
    x = x.astype(float)
    mean = np.mean(x, axis=0)
    std = np.std(x, axis=0)

    # Prevent division by zero
    std[std == 0] = 1.0

    return (x - mean) / std


def split_features_target(
    df: pd.DataFrame,
    target_column: str = "C6H6(GT)",
    drop_extra: str = "AH",
) -> tuple[np.ndarray, np.ndarray]:
    """
    Split dataframe into features X and target y.
    """
    x = df.drop(columns=[target_column, drop_extra], errors="ignore").values
    y = df[target_column].values
    return x, y


def save_processed_data(
    df: pd.DataFrame,
    csv_path: str,
    json_path: str,
) -> None:
    """
    Save cleaned dataset to CSV and JSON.
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    csv_file.parent.mkdir(parents=True, exist_ok=True)
    json_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(csv_file, index=False)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, indent=2)
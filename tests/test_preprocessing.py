import numpy as np
import pandas as pd

from src.preprocessing import clean_data, scale_features


def test_scale_features_shape():
    x = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    scaled = scale_features(x)
    assert scaled.shape == x.shape


def test_clean_data_removes_invalid_rows():
    df = pd.DataFrame(
        {
            "Date": ["2024-01-01", "2024-01-02"],
            "Time": ["10:00", "11:00"],
            "C6H6(GT)": [1.2, 2.3],
            "AH": [10.0, 12.0],
            "PT08.S1(CO)": [100, 200],
            "valid_col": [5, -200],
        }
    )

    cleaned = clean_data(df)
    assert -200 not in cleaned.values
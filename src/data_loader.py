import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load the air quality dataset using the correct separator and decimal format.
    """
    return pd.read_csv(path, sep=";", decimal=",")
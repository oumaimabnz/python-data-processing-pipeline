from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set(color_codes=True)


def plot_correlation_heatmap(df: pd.DataFrame, output_path: str) -> None:
    """
    Save correlation heatmap.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    corr = df.corr()
    sns.heatmap(corr, cmap="BrBG", annot=True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def plot_pairplot(df: pd.DataFrame, output_path: str, hue_column: str = "AH") -> None:
    """
    Save pairplot.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    pairplot = sns.pairplot(df, hue=hue_column, height=2.5)
    pairplot.savefig(path)
    plt.close("all")


def plot_loss_curve(cost_values: list[float], output_path: str) -> None:
    """
    Save gradient descent loss curve.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.title("Loss values")
    plt.plot(cost_values)
    plt.ylabel("Loss")
    plt.xlabel("Iteration")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
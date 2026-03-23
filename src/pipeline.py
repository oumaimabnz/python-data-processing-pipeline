from sklearn.model_selection import train_test_split

from src.data_loader import load_data
from src.evaluation import adjusted_r2_score, r2_score, save_metrics
from src.model import LinearRegression
from src.preprocessing import (
    clean_data,
    save_processed_data,
    scale_features,
    split_features_target,
)
from src.visualization import (
    plot_correlation_heatmap,
    plot_loss_curve,
    plot_pairplot,
)


def run_pipeline() -> None:
    # 1. Load raw data
    df = load_data("data/raw/AirQualityUCI.csv")

    # 2. Clean data
    cleaned_df = clean_data(df)

    # 3. Save processed outputs
    save_processed_data(
        cleaned_df,
        "data/processed/cleaned_data.csv",
        "data/processed/cleaned_data.json",
    )

    # 4. Visualization
    plot_correlation_heatmap(
        cleaned_df,
        "outputs/plots/correlation_heatmap.png",
    )
    plot_pairplot(
        cleaned_df,
        "outputs/plots/pairplot.png",
        hue_column="AH",
    )

    # 5. Prepare features and target
    x, y = split_features_target(cleaned_df)
    x_scaled = scale_features(x)

    # 6. Train/test split
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled,
        y,
        train_size=0.7,
        random_state=1,
    )

    # 7. Train model
    model = LinearRegression(l_rate=0.002, iterations=1000)
    model.fit_gradient_descent(x_train, y_train)
    model.fit_normal_equation(x_train, y_train)

    # 8. Predictions
    y_pred_gd = model.predict_gradient_descent(x_test)
    y_pred_nq = model.predict_normal_equation(x_test)

    # 9. Metrics
    metrics = {
        "gradient_descent": {
            "r2": r2_score(y_test, y_pred_gd),
            "adjusted_r2": adjusted_r2_score(y_test, y_pred_gd, x_test.shape[1]),
        },
        "normal_equation": {
            "r2": r2_score(y_test, y_pred_nq),
            "adjusted_r2": adjusted_r2_score(y_test, y_pred_nq, x_test.shape[1]),
        },
    }

    save_metrics(metrics, "outputs/metrics/evaluation.json")

    # 10. Loss curve
    plot_loss_curve(model.cost, "outputs/plots/loss_curve.png")

    print("Pipeline executed successfully.")
    print("Metrics:", metrics)
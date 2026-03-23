import numpy as np

from src.model import LinearRegression


def test_gradient_descent_prediction_length():
    x = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([2.0, 4.0, 6.0, 8.0])

    model = LinearRegression(l_rate=0.01, iterations=500)
    model.fit_gradient_descent(x, y)
    preds = model.predict_gradient_descent(x)

    assert len(preds) == len(y)


def test_normal_equation_prediction_length():
    x = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([2.0, 4.0, 6.0, 8.0])

    model = LinearRegression()
    model.fit_normal_equation(x, y)
    preds = model.predict_normal_equation(x)

    assert len(preds) == len(y)
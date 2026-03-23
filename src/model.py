import numpy as np


class LinearRegression:
    def __init__(self, l_rate: float = 0.002, iterations: int = 1000):
        self.l_rate = l_rate
        self.iterations = iterations
        self.cost: list[float] = []
        self.theta: np.ndarray | None = None
        self.thetas: np.ndarray | None = None

    def fit_gradient_descent(self, x: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Train model using gradient descent.
        """
        self.cost = []
        self.theta = np.zeros(1 + x.shape[1])
        n = x.shape[0]

        for _ in range(self.iterations):
            y_pred = self.theta[0] + np.dot(x, self.theta[1:])
            mse = (1 / n) * np.sum((y_pred - y) ** 2)
            self.cost.append(mse)

            d_theta1 = (2 / n) * np.dot(x.T, (y_pred - y))
            d_theta0 = (2 / n) * np.sum(y_pred - y)

            self.theta[1:] = self.theta[1:] - self.l_rate * d_theta1
            self.theta[0] = self.theta[0] - self.l_rate * d_theta0

        return self

    def predict_gradient_descent(self, x: np.ndarray) -> np.ndarray:
        """
        Predict using gradient descent parameters.
        """
        if self.theta is None:
            raise ValueError("Model has not been trained with gradient descent yet.")
        return self.theta[0] + np.dot(x, self.theta[1:])

    def fit_normal_equation(self, x: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Train model using the normal equation.
        """
        z = np.ones((x.shape[0], 1))
        x_bias = np.append(z, x, axis=1)
        self.thetas = np.linalg.pinv(x_bias.T.dot(x_bias)).dot(x_bias.T).dot(y)
        return self

    def predict_normal_equation(self, x: np.ndarray) -> np.ndarray:
        """
        Predict using normal equation parameters.
        """
        if self.thetas is None:
            raise ValueError("Model has not been trained with normal equation yet.")
        z = np.ones((x.shape[0], 1))
        x_bias = np.append(z, x, axis=1)
        return np.dot(x_bias, self.thetas)
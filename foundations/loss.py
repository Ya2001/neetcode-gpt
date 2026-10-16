import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:

        return round(-(np.mean(y_true * np.log(np.clip(y_pred, 1e-7, 1 - 1e-7)) + (1 - y_true) * np.log(1 - np.clip(y_pred, 1e-7, 1 - 1e-7)))),4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:

        return round (-(np.sum(y_true * np.log(np.clip(y_pred, 1e-7, 1 - 1e-7))) / len(y_true)), 4)

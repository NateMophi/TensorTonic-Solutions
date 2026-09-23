import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    n = len(y_true)
    actual = y_pred[np.arange(n), y_true]
    return np.mean(-np.log(actual))
    
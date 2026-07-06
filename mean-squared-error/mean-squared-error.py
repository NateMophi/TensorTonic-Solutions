import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred, y_true = np.array(y_pred), np.array(y_true)
    MSE = np.sum((y_pred - y_true)**2)/len(y_true)
    return MSE

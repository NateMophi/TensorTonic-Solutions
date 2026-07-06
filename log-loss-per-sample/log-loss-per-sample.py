import math
import numpy as np

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    p_hat = np.where(y_pred==0, eps, y_pred)
    p_hat = np.where(p_hat==1, 1-eps, p_hat)
    p_hat = np.where(p_hat<eps, eps, p_hat)

    L = -(y_true*np.log(p_hat) + (1-y_true)*np.log(1-p_hat))
    return list(L)
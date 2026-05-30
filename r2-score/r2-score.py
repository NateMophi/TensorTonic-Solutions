import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    
    
    m = np.mean(y_true)
    num = np.sum((y_true - y_pred)**2)
    den = np.sum((y_true - m)**2)
    if np.max(y_true) == np.min(y_true):
        if y_true.all() == y_pred.all():
            return 1.0
        else:
            return 0.0
    return 1 - num/den
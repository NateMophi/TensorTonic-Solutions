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

    
    numerator = np.sum((y_true - y_pred)**2)
    denominator = np.sum((y_true - np.mean(y_true))**2)
    if denominator==0 and y_pred.all()==y_true.all():
        return 1.0
    elif denominator==0 and y_pred.all()!=y_true.all():
        return 0.0
    else:
        R_sq = 1 - numerator/denominator
        return R_sq
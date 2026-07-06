import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    if len(fpr) != len(tpr):
        return None
    
    fpr, tpr = np.array(fpr), np.array(tpr)
    AUC = np.trapezoid(tpr, fpr)
    return AUC
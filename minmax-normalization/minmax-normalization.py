import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    if X.ndim ==1:
        min_x = np.min(X)
        max_x = np.max(X)
        
    if X.ndim == 2:
        min_x = np.min(X, axis=axis, keepdims=True)
        max_x = np.max(X, axis=axis, keepdims=True)

    numerator = X - min_x
    denominator = np.maximum(max_x - min_x, eps)

    

    return numerator/denominator
import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    x = np.asarray(X)
    if x.ndim !=2 :
        return None
    
    row, cols = x.shape
    if row < 2:
        return None
    

    u = np.mean(x, axis=0)
    x_centered = x - u 

    cov = np.dot(1 / (row - 1), np.dot(x_centered.T, x_centered))

    return cov


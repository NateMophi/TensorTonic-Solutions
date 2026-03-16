import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    if X.ndim!=2:
        return None
    
    N, D = X.shape
    if N < 2:
        return None
        
    mean = np.mean(X, axis=0)
    X_center = X - mean

    cov_mat = (1 / (N - 1)) * np.dot(X_center.T, X_center)
    return cov_mat
    
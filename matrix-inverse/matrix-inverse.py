import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    
    rows, cols = A.shape
    det = np.linalg.det(A)
    if rows != cols or det==0 or A.ndim != 2:
        return None
    return np.linalg.inv(A)
    
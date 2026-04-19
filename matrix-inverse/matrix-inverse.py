import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A)
    rows, cols = A.shape
    if rows != cols:
        return None
    if A.ndim !=2:
        return None
    if np.linalg.det(A) !=0:     
        A_inv = np.linalg.inv(A)
        return A_inv

import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    n = len(matrix)
    if n == 0:
        return None
    try:
        matrix = np.array(matrix)
        rows, cols = matrix.shape
        if matrix.ndim <= 1 or rows != cols :
            return None
        eig = np.linalg.eigvals(matrix)
        return eig
    except ValueError:
        return None
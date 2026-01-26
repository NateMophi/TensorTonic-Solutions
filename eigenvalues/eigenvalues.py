import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here    
    matrix = np.asarray(matrix)
    
    if len(matrix)==0:
        return None

    if matrix.ndim !=2:
        return None

    rows, cols = matrix.shape
    if rows!=cols:
        return None

    eig_vals = np.linalg.eigvals(matrix)
    np.lexsort(eig_vals)
    
    return eig_vals
    
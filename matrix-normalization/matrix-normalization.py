import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    matrix = np.array(matrix)
    if matrix.ndim !=2:
        return None

    def l1(M):
        norm = np.sum(np.abs(M), axis=axis, keepdims=True)
        norm = np.where(norm==0, 1, norm)
        return norm

    def l2(M):
        norm = np.sqrt(np.sum(M**2, axis=axis, keepdims=True))
        #norm = np.linalg.norm(M, axis=axis, keepdims=True)
        norm = np.where(norm==0, 1, norm)
        return norm

    def maxNorm(M):
        norm = np.max(np.abs(M), axis=axis, keepdims=True)
        norm = np.where(norm==0, 1, norm)
        return norm        
    
    if norm_type=="l1":
        NORM = l1(matrix)
    elif norm_type=="l2":
        NORM = l2(matrix)
    elif norm_type =="max":
        NORM = maxNorm(matrix)

    return matrix/NORM
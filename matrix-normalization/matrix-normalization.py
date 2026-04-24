import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix)
    if matrix.ndim !=2:
        return None
    if axis!=None and axis>=2:
        return None

    def l1(M):
        norm = np.sum(np.abs(M), keepdims=True, axis= axis)
        norm = np.where(norm==0,1, norm)
        return norm
    def l2(M):
        norm = np.sqrt(np.sum(M**2, axis=axis, keepdims=True))
        norm = np.where(norm==0,1, norm)
        return norm
    def MaxNorm(M):
        norm = np.max(np.abs(M), axis=axis, keepdims=True)
        norm = np.where(norm==0,1, norm)
        return norm

    if norm_type == "l1":
        return matrix/l1(matrix)
    
    if norm_type == "l2":
        return matrix/l2(matrix)
    
    if norm_type == "max":
        return matrix/MaxNorm(matrix)
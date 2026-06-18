import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.array(v)
    if v.ndim == 1:
        norm = np.linalg.norm(v)
    if v.ndim == 2:
        norm = np.linalg.norm(v, axis=1)
    return norm
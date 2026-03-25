import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    dot = np.dot(v, w)
    norm = np.dot(np.linalg.norm(v), np.linalg.norm(w))
    if norm < 10**-10:
        return np.nan
    cos_theta = dot / norm
    theta = np.clip(np.arccos(cos_theta))
    return theta
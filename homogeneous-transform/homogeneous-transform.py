import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T, p = np.array(T), np.array(points)
    if p.ndim == 1:
        p = np.reshape(p, (1, 3))
        prows, pcols = p.shape
        p_h = np.hstack((p, np.ones((prows, 1))))
        p_h_prime = (T@p_h.T).T
        p_prime = p_h_prime[:,0:3]
        return np.reshape(p_prime, (3,))
        
    if p.ndim == 2:
        prows, pcols = p.shape
        p_h = np.hstack((p, np.ones((prows, 1))))
        p_h_prime = (T@p_h.T).T
        p_prime = p_h_prime[:,0:3]
        return p_prime
        

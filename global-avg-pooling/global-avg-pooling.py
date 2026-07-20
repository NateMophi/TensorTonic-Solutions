import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    
    if x.ndim == 3:
        m = np.mean(x, axis=(1,2))
        return m
    if x.ndim == 4: 
        m = np.mean(x, axis=(2,3))
        return m
    if x.ndim != 3 or x.ndim!=4:
        raise ValueError
        
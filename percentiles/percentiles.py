import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x, q = np.array(x),  np.array(q)
    x = np.sort(x)
    
    
    return np.percentile(x, q, method="linear")
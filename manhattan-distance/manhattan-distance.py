import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    #if len(y) != len(x):
    #    return None
        
    x, y = np.array(x), np.array(y)
    
    return float(np.sum(np.abs(x - y)))
import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x,y = np.array(x), np.array(y)
    n1, n2 = len(x), len(y)
    if n1 != n2 or x.ndim !=1 or y.ndim!=1:
        raise ValueError
    
    return float(np.dot(x, y))
import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y)
    i, C = np.unique(y, return_counts = True)
    p_i = C/sum(C)
    H = -np.sum(np.dot(p_i, np.log2(p_i)))
    return H
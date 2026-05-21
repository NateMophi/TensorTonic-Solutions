import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    M = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i==j:
                M[i,j] = v[i]
    return M

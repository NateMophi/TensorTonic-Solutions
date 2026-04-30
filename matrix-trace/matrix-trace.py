import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    sum = 0
    rows, cols = A.shape
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum+=A[i, j]
    return sum

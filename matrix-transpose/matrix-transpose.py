import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    N, M = A.shape
    A_transpose = np.zeros((M, N))
    for i in range(N):
        for j in range(M):
            A_transpose[j,i] = A[i,j]

    return A_transpose
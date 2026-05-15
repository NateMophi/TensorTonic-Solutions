import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y = np.array(y)
    N = len(y)
    K = num_classes
    if K == None:
        K = np.max(y) + 1

    M = np.zeros((N, K))
    M[np.arange(N), y] = 1
    return M
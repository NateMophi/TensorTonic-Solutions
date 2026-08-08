import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    X = np.array(X)
    stride = pool_size
    H, W = X.shape
    H_out, W_out = H/pool_size, W/pool_size
    H_out, W_out = int(H_out), int(W_out)
    M = np.zeros((H_out, W_out))
    for i in range(H_out):
        for j in range(W_out):
            # window = X[i:i+pool_size, j:j+pool_size]
            window = X[i*stride: i*stride+pool_size, j*stride: j*stride+pool_size]
            M[i,j] = np.max(window)
    return M.tolist()
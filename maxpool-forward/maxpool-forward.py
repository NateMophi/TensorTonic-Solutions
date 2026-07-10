import numpy as np
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.array(X)
    H, W = X.shape
    H_out, W_out = 1+(H-pool_size)/stride, 1+(W-pool_size)/stride
    H_out, W_out = int(H_out), int(W_out)
    O = np.zeros((H_out, W_out))
    for i in range(H_out):
        for j in range(W_out):
            window = X[i*stride: i*stride+pool_size, j*stride: j*stride+pool_size]
            O[i,j] = np.max(window)
    return O.tolist()
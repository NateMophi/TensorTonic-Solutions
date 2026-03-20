import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if x.ndim == 1:
        diff = x - np.max(x)
        num = np.exp(diff)
        denom =  np.sum(num)

    if x.ndim == 2:
        diff = x - np.max(x, axis=1, keepdims=True)
        num = np.exp(diff)
        denom =  np.sum(num, axis=1, keepdims=True)
        
    return num/denom
import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.array(x)
    
    if x.ndim==2:
        mu = np.mean(x, axis=0, keepdims=True)
        var = np.var(x, axis=0, keepdims=True)
        x_i = (x - mu) / np.sqrt(var + eps)
        y_i = gamma*x_i + beta
        return y_i
    if x.ndim==4:
        mu = np.mean(x, axis=(0,2,3), keepdims=True)
        var = np.var(x, axis=(0,2,3), keepdims=True)
        gamma, beta = np.reshape(gamma,(1,x.shape[1],1, 1)), np.reshape(beta,(1,x.shape[1],1, 1))
        x_i = (x - mu) / np.sqrt(var + eps)
        y_i = gamma*x_i + beta
        return y_i
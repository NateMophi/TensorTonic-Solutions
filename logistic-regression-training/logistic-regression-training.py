import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    n_samples, n_features = X.shape
    N =  n_samples
    w, b = np.zeros(n_features), 0
    
    
    for i in range(steps):
        z = X @ w + b
        p = _sigmoid(z) 

        w_delta = np.dot(X.T, p - y) / N
        b_delta = np.mean(p-y)

        w = w - lr*w_delta
        b = b - lr*b_delta

    return w, b
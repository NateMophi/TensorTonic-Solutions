import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X, y = np.array(X), np.array(y)
    rows, cols = X.shape
    w = np.linalg.inv(X.T @ X + lam * np.eye(cols)) @ X.T@y
    return w
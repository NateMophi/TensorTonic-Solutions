import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    x_bar = np.mean(x)
    var = (1/(n-1)) * np.sum((x - x_bar)**2)
    return var, var**0.5
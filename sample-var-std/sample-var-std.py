import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    mean = np.mean(x)
    variance = 1/(n-1) * np.sum((x - mean)**2)
    return variance, np.sqrt(variance)
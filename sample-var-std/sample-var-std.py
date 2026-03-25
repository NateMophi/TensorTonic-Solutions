import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    
    n = len(x)
    x = np.array(x)
    s2 = (1/(n-1)) * np.sum((x - np.mean(x))**2)
    return (s2, np.sqrt(s2))
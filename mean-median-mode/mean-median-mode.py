import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x.sort()
    C = Counter(x)

    modes = []
    for k,v in C.items():
        if v == max(C.values()):
            modes.append(k)

    mode = min(modes)
    
    x = np.array(x)
    mean, median = np.mean(x), np.median(x)
    return mean, median, mode
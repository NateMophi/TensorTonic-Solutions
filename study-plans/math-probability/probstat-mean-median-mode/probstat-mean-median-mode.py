import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    x = np.array(x)
    val, counts = np.unique(x, return_counts=True)
    return {"mean":float(np.mean(x)), "median":float(np.median(x)), "mode":float(val[np.argmax(counts)])}
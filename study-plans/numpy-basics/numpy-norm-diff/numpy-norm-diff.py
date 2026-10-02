import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a, b = np.array(a), np.array(b)
    if len(a)!=0 or len(b)!=0:
        return np.abs(np.clip(a, lo, hi) - np.clip(b, lo, hi))/(hi - lo)

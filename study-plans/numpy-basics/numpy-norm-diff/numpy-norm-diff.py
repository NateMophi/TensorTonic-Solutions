import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a, b = np.array(a), np.array(b)
    return np.abs(np.clip(a, lo, hi) - np.clip(b, lo, hi))/(hi - lo)

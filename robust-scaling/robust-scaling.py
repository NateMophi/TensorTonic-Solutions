import numpy as np

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    V = sorted(values)
    V, values = np.array(V), np.array(values)
    N = len(V)
    if N == 1:
        return [0]
    median = np.median(V)

    Q1 = np.median(V[:N//2])
    Q3 = np.median(V[(N+1)//2:])
        
    x_scaled = np.where(Q3-Q1==0, values-median, (values-median)/(Q3-Q1))
    return x_scaled
import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    n = len(x)
    E = []
    for i in range (0, n):
        E .append(x[i]*p[i])

    if sum(p)!= 1:
        raise ValueError
    return sum(E)

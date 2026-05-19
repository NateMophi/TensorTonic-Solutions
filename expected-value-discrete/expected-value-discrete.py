import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x, p = np.array(x), np.array(p)
    if x.shape!=p.shape:
        raise ValueError
    if np.sum(p)!=1:
        raise ValueError
    E = np.sum(x*p)
    return E

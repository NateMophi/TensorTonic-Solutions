import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    
    """Q.E.D"""
    k = np.array(k)
    return (np.dot((1-p)**(k-1), p), 1/p)
import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)
    geo_pmf = np.where(x==1, p, 1-p)
    geo_mean, geo_var = p, np.dot(p, 1-p)

    return  geo_pmf, geo_mean, geo_var
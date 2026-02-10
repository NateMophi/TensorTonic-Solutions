import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    PMF = np.dot(np.exp(-lam), lam**k)/np.prod(range(1, k+1))

    CDF = 0
    for i in range(k+1):
        CDF += np.sum(np.dot(np.exp(-lam), lam**i) / np.prod(range(1, i+1)))

    return PMF,CDF
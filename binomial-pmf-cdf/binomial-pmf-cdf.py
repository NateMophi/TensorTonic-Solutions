import numpy as np
import scipy
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here    
    if p==0 or p==1:
        pmf = 0

    if n == k or k == 0:
        pmf = np.dot(p**k, (1-p)**(n-k))

    else:
        pmf = np.dot(scipy.special.comb(n, k), np.dot(p**k, (1-p)**(n-k)) ) 

    cdf = 0
    for i in range(0, k+1):
        cdf += np.dot(scipy.special.comb(n, i), np.dot(p**i, (1-p)**(n-i)) )

    return (pmf, cdf)
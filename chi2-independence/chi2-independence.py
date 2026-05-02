import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)
    row_sum, col_sum = np.sum(C, axis=1), np.sum(C, axis=0)
    total = np.sum(C)
    
    E = np.outer(row_sum, col_sum) / total

    chi = np.sum((C - E)**2 / E)
    
    return (chi, E)
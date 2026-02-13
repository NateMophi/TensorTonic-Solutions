import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here

    row_sum, col_sum = np.sum(C, axis=1), np.sum(C, axis=0)
    N = np.sum(C)
    E = np.outer(row_sum, col_sum)/N

    chi = np.sum((C - E)**2/E)
    return chi, E
import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    GiniR, GiniL = 0, 0
    y_left, y_right = np.array(y_left), np.array(y_right)
    NL, NR = len(y_left), len(y_right)
    if NL==0 :
        GiniL=0
    if NR==0:
        GiniR=0
    N=NL+NR
    if N==0.0:
        return 0.0
    
    UR, rCount = np.unique(y_right, return_counts= True)
    UL, lCount = np.unique(y_left, return_counts= True)
    for i in range(len(UR)):
        P = rCount[i]/NR
        GiniR += P**2
    GiniR = 1-GiniR
    for j in range(len(UL)):
        P2 = lCount[j]/NL
        GiniL += P2**2
    GiniL=1-GiniL
    return (NL/N) * GiniL + (NR/N) * GiniR
        
        
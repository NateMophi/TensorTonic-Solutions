import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    A = []
    mean = sum(series)/len(series)
    var = sum((x - mean)**2 for x in series)
    if var == 0:
        return [1.0]+[0.0]*max_lag
    n = len(series)
    for k in range(max_lag+1):
        r = 0
        for t in range(n-k):
            r+=(series[t] - mean)*(series[t+k] - mean)
        A.append(r/var)
    return A
        
        
    
    
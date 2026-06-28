def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    A = []
    SA = []
    for p in range(period):
        val = []
        n = 0
        while p+n*period < len(series):
            val.append(series[p + n*period])
            n+=1
        SA.append(val)
    for L in SA:
        M = sum(L)/len(L)
        A.append(M)
    return A

def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for d in range(1, order+1):
        n = len(series)
        for t in range(n-d):
            series[t] = series[t+1] - series[t]
        # series.pop()
    return series[:n-order]
    
def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    n = len(series)
    PCT = []
    for i in range(1, n):
        if series[i-1]==0:
            pct=0
        else:
            pct = (series[i] - series[i-1]) / series[i-1]
        PCT.append(pct)
    return PCT
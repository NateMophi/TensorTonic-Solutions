def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    # Write code here
    n, k = len(values), len(weights)
    WMA = [0]*(n-k+1)
    for i in range(n-k+1):
        for j in range(k):
            WMA[i]+= ((weights[j]*values[i+j])) / sum(weights)
    return WMA
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    w_sum = sum(weights)
    n, k = len(values), len(weights)
    WMA = [0]*(n-k+1)
    for i in range(n-k+1):
        for j in range(k):
            WMA[i]+=(weights[j]*values[i+j])/w_sum
    return WMA
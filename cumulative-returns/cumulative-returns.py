def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    n = len(returns)
    W = 1
    R = []
    for t in range(n):
        W = W*(1+returns[t])
        R.append(W-1)
    return R
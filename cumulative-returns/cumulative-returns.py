def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    t = len(returns)
    C = []
    W_t = 1
    for i in range(t):
        W_t*= (1+returns[i])
        C.append(W_t-1)
    return C
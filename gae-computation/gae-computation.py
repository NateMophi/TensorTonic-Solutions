def gae(rewards, values, gamma, lam):
    """
    Compute Generalized Advantage Estimation.
    """
    # Write code here
    # TD = []
    T = len(rewards)
    TD = [0]*T
    for t in range(T):
        TD[t] = rewards[t] + gamma*values[t+1] - values[t]
        # TD.append(delta)

    A = [0]*T
    A[-1] = TD[-1]
    for t in range(T-2, -1, -1):
        A[t] = TD[t] + gamma*lam*A[t+1]
        
    return A
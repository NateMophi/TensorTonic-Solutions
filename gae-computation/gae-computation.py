def gae(rewards, values, gamma, lam):
    """
    Compute Generalized Advantage Estimation.
    """
    # Write code here
    T = len(rewards)
    Delta = []
    A = [0]* T
    for t in range(T):
        Delta.append(rewards[t] + gamma*values[t+1] - values[t])
    A[T-1] = Delta[T-1]
    for i in range(T-2, -1, -1):
        A[i] = Delta[i] + gamma*lam * A[i+1]
    return A
        
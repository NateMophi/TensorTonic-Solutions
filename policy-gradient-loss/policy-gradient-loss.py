def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    # Write code here
    T = len(log_probs)
    G = [0] * T
    G[-1] = rewards[-1]
    for t in range(T-2, -1, -1):
        G[t] = rewards[t] + gamma*G[t+1]
    # for t in range(T-1):
    #     discount = rewards[t] + gamma*G[t]
    #     G.append(discount)
    # G = G[::-1]
    G_avg = sum(G)/T

    A = [g - G_avg for g in G]
    
    L = -sum(lp*a for lp,a in zip(log_probs, A))/T
    
    return L

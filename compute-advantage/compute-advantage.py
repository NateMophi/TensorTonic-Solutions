import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    V = np.array(V)
    n = len(rewards)
    G = n * [0]
    G[-1] = rewards[-1]
    for t in range(n-2, -1, -1):
        G[t] = rewards[t] + G[t+1]*gamma
    G = np.array(G)
    return G - V

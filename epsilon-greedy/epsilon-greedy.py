import numpy as np

def epsilon_greedy(q_values: list, epsilon: float, seed: int = 0) -> int:
    """
    Returns the action index as an integer.
    """
    # Write code here
    q_values = np.array(q_values)
    rng = np.random.default_rng(seed)
    u = rng.random()
    a = np.where(u<epsilon, rng.integers(q_values.size), np.argmax(q_values))
    return int(a)
    
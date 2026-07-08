import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    K = len(predictions)
    q = [(1-epsilon)+ epsilon/K if i==target else epsilon/K for i in range(K)]
    q = np.array(q)
    L = -np.sum(np.dot(q, np.log(predictions)))
    return L
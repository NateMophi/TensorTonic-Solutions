import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1, rater2 = np.array(rater1), np.array(rater2)
    p_o = np.mean(rater1 == rater2)
    labels = np.unique(np.concatenate([rater1, rater2]))

    p_e = 0.0
    for label in labels:
        r1 = np.mean(rater1 == label)
        r2 = np.mean(rater2 == label)
        p_e += r1*r2    
    k = (p_o - p_e) / (1 - p_e)
    return k
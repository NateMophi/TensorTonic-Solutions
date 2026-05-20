def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    U = len(recommendations)
    if U == 0:
        return 0.0
    hits = 0
    for rec, truth in zip(recommendations, ground_truth):
        rec = rec[:k]
        for t in truth:
            if t in rec:
                hits+=1
        
    return hits/U
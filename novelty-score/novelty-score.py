def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    R = len(recommendations)
    if R == 0:
        return 0
    
    popularity = 0
    for i in range(R):
        popularity = popularity + -math.log2(item_counts[i]/n_users)
        
    novelty = (1/R) * popularity 
    return novelty
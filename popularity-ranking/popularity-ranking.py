def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    WR = []
    m = min_votes
    C = global_mean
    for avg_rating, vote_count in items:
        R = avg_rating
        v = vote_count
        weighted_rating = (v / (v+m))*R + (m/ (v+m))*C
        WR.append(weighted_rating)
    return WR
    
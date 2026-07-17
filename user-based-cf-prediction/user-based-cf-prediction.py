def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    # Write code here
    s = similarities
    if max(s)<0:
        return 0.0
    r = sum([s[i]*ratings[i] for i in range(len(ratings)) if s[i]>0]) / sum([s[i] for i in range(len(ratings)) if s[i]>0])
    return r
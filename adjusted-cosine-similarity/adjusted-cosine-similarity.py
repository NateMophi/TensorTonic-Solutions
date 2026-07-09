def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    """
    Compute adjusted cosine similarity between two items.
    """
    # Write code here
    # non_zero_user_ratings = [[val for val in rating if val!=0] for rating  in ratings_matrix]
    # mean_ratings = [sum(rating)/len(rating) for rating in non_zero_user_ratings]
    U = [[val for val in rating if val!=0 and rating[item_i]!=0 and rating[item_j]!=0] for rating in ratings_matrix]
    num, d1, d2 = 0, 0, 0
    for r in U:
        if r:
            r_bar = sum(r)/len(r)
            num+= (r[item_i] - r_bar)*(r[item_j] - r_bar)
            d1+= (r[item_i] - r_bar)**2
            d2+= (r[item_j] - r_bar)**2
        denom = (d1**0.5)*(d2**0.5)
    return num/denom if denom!=0 else 0
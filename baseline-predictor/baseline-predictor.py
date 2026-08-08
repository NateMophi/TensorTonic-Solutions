def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # Write code here
    r = []
    non_zero_user_ratings = [[rating for rating in ratings if rating!=0] for ratings in ratings_matrix]
    non_zero_item_ratings = [[rating for rating in ratings if rating!=0] for ratings in zip(*ratings_matrix)]
    mu = sum([sum(rating)/len(rating) for rating in non_zero_user_ratings])/len(non_zero_user_ratings)
    UB = [(sum(rating)/len(rating))- mu for rating in non_zero_user_ratings]
    IB = [(sum(rating)/len(rating))- mu for rating in non_zero_item_ratings]
    for u,i in target_pairs:
        r.append(mu + UB[u] + IB[i])
    return r
def baseline_predict(ratings_matrix: list, target_pairs: list) -> list:
    """
    Returns the baseline predictions for the requested user-item pairs.
    """
    # Write code here
    non_zero_user_ratings= [[rating for rating in ratings if rating !=0] for ratings in ratings_matrix]
    non_zero_item_ratings = [[rating for rating in ratings if rating !=0] for ratings in zip(*ratings_matrix)]
    mu = sum([rating for ratings in ratings_matrix for rating in ratings if rating!=0 ])/len([rating for ratings in ratings_matrix for rating in ratings if rating!=0 ])

    user_means = [sum(rating)/len(rating) if len(rating)!=0 else 0 for rating in non_zero_user_ratings]
    item_means = [sum(rating)/len(rating) if len(rating)!=0 else 0 for rating in non_zero_item_ratings]
    
    user_bias = [rating-mu if rating>0 else rating-0 for rating in user_means]
    item_bias = [rating-mu if rating>0 else rating-0 for rating in item_means]
    R = [mu + user_bias[u] + item_bias[i] for u,i in target_pairs]
    return R
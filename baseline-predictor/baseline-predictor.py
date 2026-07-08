def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # Write code here
    Bias = []
    non_zero_ratings = [val for user in ratings_matrix for val in user if val!=0]
    non_zero_user_ratings = [[val for val in user if val!=0] for user in ratings_matrix]
    
    global_mean = sum(non_zero_ratings)/len(non_zero_ratings)
    non_zero_user_ratings = [[val for val in user if val!=0] for user in ratings_matrix]
    non_zero_item_ratings = [[val for val in user if val!=0] for user in zip(*ratings_matrix)]

    user_means = [sum(rating)/len(rating) for rating in non_zero_user_ratings]
    item_means = [sum(rating)/len(rating) for rating in non_zero_item_ratings]
    
    for u, i in target_pairs:
        b_u, b_i = user_means[u] - global_mean, item_means[i] - global_mean
        r = global_mean + b_u + b_i 
        Bias.append(r)
    return Bias
                
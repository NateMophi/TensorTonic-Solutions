def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    """
    R = ratings_matrix.copy()
    non_zero_user_ratings = [[val for val in ratings if val!=0] for ratings in ratings_matrix]
    non_zero_item_ratings = [[val for val in ratings if val!=0] for ratings in zip(*ratings_matrix)]

    rows, cols = len(ratings_matrix),len(ratings_matrix[0])
    if mode=="user":
        for i in range(rows):
            for j in range(cols):
                if R[i][j]==0 and len(non_zero_user_ratings[i])!=0:
                    R[i][j] = sum(non_zero_user_ratings[i])/len(non_zero_user_ratings[i])
    if mode=="item":
        for i in range(rows):
            for j in range(cols):
                if R[i][j]==0 and len(non_zero_item_ratings[j])!=0:
                    R[i][j] = sum(non_zero_item_ratings[j])/len(non_zero_item_ratings[j])
                # if R[i][j]==0 and len(non_zero_item_ratings)==0:
    return R
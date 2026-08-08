def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    R = ratings_matrix.copy()
    user_ratings = [[rating for rating in ratings if rating!=0] for ratings in ratings_matrix]
    item_ratings = [[rating for rating in ratings if rating!=0] for ratings in zip(*ratings_matrix)]
    
    rows, cols = len(R), len(R[0])
    if mode=="user":
        for i in range(rows):
            if len(user_ratings[i])==0:
                continue
            m = sum(user_ratings[i])/len(user_ratings[i])
            for j in range(cols):
                if R[i][j]==0:
                    R[i][j]=m
    if mode=="item":
        for j in range(cols):
            if len(item_ratings[j])==0:
                continue
            m = sum(item_ratings[j])/len(item_ratings[j])
            for i in range(cols):
                if R[i][j]==0:
                    R[i][j]=m
    return R
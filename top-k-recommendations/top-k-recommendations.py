def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    # I = []
    L = [(index, score) for index, score in enumerate(scores) if index not in rated_indices]
    L.sort(key=lambda x: -x[1])
    L = [index for index, score in L[:k]]
    return L
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = recommended[:k]
    relevant = set(relevant)
    
    hits = 0
    for i in range(k):
        if recommended[i] in relevant:
            hits+=1
    precison_k = hits/k

    
    rev_length = len(relevant)
    hits2 = 0
    for j in relevant:
        if j in recommended:
            hits2+=1
    recall_k = hits2/rev_length
    
    return [precison_k, recall_k]
            
    
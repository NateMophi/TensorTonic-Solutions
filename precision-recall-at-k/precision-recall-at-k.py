def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    n = len(relevant)
    precision = [recommended[i] for i in range(k) if recommended[i] in relevant]
    precision_k, recall_k = len(precision)/k, len(precision)/n
    return [precision_k, recall_k]
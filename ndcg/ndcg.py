import math

def ndcg(relevance_scores: list, k: int) -> float:
    """
    Returns NDCG as a float.
    """
    # Write code here
    DCG, IDCG = [], []
    ideal_scores = sorted(relevance_scores, reverse=True)
    for i, rel in enumerate(relevance_scores[:k], start=1):
        DCG.append((2**rel - 1)/math.log2(i+1))
    for j, rel in enumerate(ideal_scores[:k], start=1):
        IDCG.append((2**rel - 1)/math.log2(j+1))
    if sum (IDCG) == 0:
        return 0
    else:
        return sum(DCG)/sum(IDCG)
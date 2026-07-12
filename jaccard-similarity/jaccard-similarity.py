def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    if len(set_a)==0 and len(set_b)==0:
        return 0
    intersection = set([x for x in set_a if x in set_b])
    union = set(set_a+set_b)
    return len(intersection)/len(union)
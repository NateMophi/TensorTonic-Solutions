def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    D = {}
    for sentence in sentences:
        for token in sentence:
            if token not in D:
                D[token] = 1
            else:
                D[token]+=1
    return D
import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    n = len(vocab)
    F = list()
    
    for i in vocab:
        count = 0
        for j in tokens:
            if j == i:
                count+=1

        F.append(count)
    return np.array(F, dtype=int)
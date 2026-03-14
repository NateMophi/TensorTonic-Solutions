import numpy as np
def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs)==0:
        return []
    
    if max_len != None:
        L = max_len
    else:
        L = max(len(x) for x in seqs)


    for s in seqs:
        while len(s) < L:
            s.append(pad_value)
    
    for s in seqs:
        while len(s) > L:
            s.pop()
    return np.array(seqs)

# InEfficient Solution I'm suspecting...
def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    n = len(values)
    i = 0
    M = []
    while i+window_size <= n:
        w = values[i:i+window_size]
        M.append(sum(w)/len(w))
        i+=1
        # j+=1
    return M
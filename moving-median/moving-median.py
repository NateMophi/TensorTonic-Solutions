def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    medians = []
    X = []
    # gap = len(values) - window_size
    L = 0
    R = 0
    while R+window_size<len(values)+1:
        window = values[L:R+window_size]
        window = sorted(window)
        # if window_size%2 ==0:
            # mid = window[(window_size//2)-1] + window[(window_size//2)]
            # medians.append(mid/2)
        # if window_size%2 !=0:
            # mid = window[window_size//2]
            # medians.append(mid)
        medians.append(window)
        L+=1
        R+=1
    for m in medians:
        if window_size%2==0:
            mid = m[(window_size//2)-1]+m[(window_size//2)]
            X.append(mid/2)
        if window_size%2!=0:
            mid = m[(window_size//2)]
            X.append(mid)
    return X
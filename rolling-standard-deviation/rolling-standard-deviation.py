def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    S = []
    i, j = 0, window_size
    while j <= len(values):
        mean = sum(values[i:j])/len(values[i:j])
        var = 0
        for x in values[i:j]:
            var += (x-mean)**2 / len(values[i:j]) 
        S.append(var**0.5)
        i+=1
        j+=1
    return S
    # return var**0.5
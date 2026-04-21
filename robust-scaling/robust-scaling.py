def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    x_scaled = []
    
    n = len(values)
    Q1, Q3 = 0, 0
    if n%2 == 1:
        median = sorted(values)[n//2]
    else:
        median = (sorted(values)[n//2] + sorted(values)[n//2 -1]) / 2
    for i in values:
        if i < median:
           Q1 += i
    
    if n > 2:
        Q1 = Q1/2
    
    for i in values[::-1]:
        if i > median:
           Q3 += i

    if n > 2:
        Q3 = Q3/2

    for val in values:
        numerator = val - median
        IQR = Q3 - Q1
        if IQR == 0:
            x_scaled.append(numerator)
        else:
            x_scaled.append(numerator/IQR)
    return x_scaled
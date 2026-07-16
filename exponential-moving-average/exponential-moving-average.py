def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    EMA = [0]*len(values)
    EMA[0]=values[0] 
    for t in range(1,len(values)):
        EMA[t] =alpha*values[t] + (1-alpha)*EMA[t-1]
    return EMA
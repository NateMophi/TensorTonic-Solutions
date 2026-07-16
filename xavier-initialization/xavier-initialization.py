def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    L = (6/(fan_in+fan_out))**0.5
    X = [[val*2*L-L for val in weight] for weight in W]
    return X
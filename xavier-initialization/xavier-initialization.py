def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    L = (6/(fan_in+fan_out))**0.5
    X = []
    for weight in W:
        W_prime = []
        for val in weight:
            W_prime.append(val*2*L-L)
        X.append(W_prime)
    return X
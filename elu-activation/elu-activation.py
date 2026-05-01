def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    ELU = list()
    for i in x:
        if i > 0:
            ELU.append(i)
        elif i <= 0:
            ELU.append(alpha * (math.exp(i) - 1))
    return ELU
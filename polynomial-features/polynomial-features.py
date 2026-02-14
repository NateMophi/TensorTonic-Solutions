def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    L = []
    for val in values:
        poly = []
        for i in range(degree+1):
            poly.append(val**i)
        L.append(poly)

    return L
        
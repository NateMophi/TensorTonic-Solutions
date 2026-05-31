def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    theta = [(2 * math.pi * v)/period for v in values]
    encoded = [[math.sin(angle), math.cos(angle)] for angle in theta]
    return encoded
    
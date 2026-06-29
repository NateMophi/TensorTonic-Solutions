def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    G = []
    for row in image:
        L = []
        for i,j,k in row:
            Y = 0.299*i + 0.587*j + 0.114*k
            L.append(Y)
        G.append(L)
    return G
                
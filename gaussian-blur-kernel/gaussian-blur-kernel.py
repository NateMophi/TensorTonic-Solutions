def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    center = size//2
    unnormalized = []
    for i in range(size):
        T = []
        for j in range(size):
            x, y = j-center, i-center
            G = math.exp(-(x**2 + y**2)/(2*sigma**2))
            T.append(G)
        unnormalized.append(T)
    total = 0
    for L in unnormalized:
        total+=sum(L)
    normalized = [[x/total for x in norm] for norm in unnormalized ]
    return normalized
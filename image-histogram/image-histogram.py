def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    Z = [0]*256
    for row in image:
        for pixel in row:
            # if Z[pixel]==pixel:
            Z[pixel]+=1
            # else:
                # continue
    
    return Z
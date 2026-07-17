def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    I = []
    H,W = len(image), len([row[0] for row in image])
    cy, cx = (H-1)/2, (W-1)/2
    theta = math.radians(angle_degrees)
    for i in range(H):
        pixel = []
        for j in range(W):
            dy, dx = i-cy, j-cx
            src_y = round(cy + dy*math.cos(theta) + dx*math.sin(theta))
            src_x = round(cx - dy*math.sin(theta) + dx*math.cos(theta))
            if (0 <= src_y < H and 0 <= src_x < W):
                pixel.append(image[src_y][src_x])
            else:
                pixel.append(0)
        I.append(pixel)
    return I
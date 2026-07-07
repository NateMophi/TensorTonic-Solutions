def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size/feature_size
    centers = []
    coordinates = []
    A = []
    for i in range(int(image_size/stride)):
        for j in range(int(image_size/stride)):
            centers.append((i, j))
    for i,j in centers:
        cx, cy = (j + 0.5)*stride, (i+0.5)*stride
        coordinates.append((cx, cy))
    for x, y in coordinates: 
        for s in scales:
            for r in aspect_ratios:
                w, h = s * r**0.5, s/(r)**0.5
                x1, y1 = x - w/2, y - h/2
                x2, y2 = x + w/2, y + h/2
                A.append([x1, y1, x2, y2])
    return A
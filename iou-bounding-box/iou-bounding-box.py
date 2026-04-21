def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    # Coordinates
    inter_x1, inter_y1 = max(box_a[0], box_b[0]), max(box_a[1], box_b[1])
    inter_x2, inter_y2 = min(box_a[2], box_b[2]), min(box_a[3], box_b[3])

    # Intersection Area
    breath = max(0, inter_x2 - inter_x1)
    length = max(0, inter_y2 - inter_y1)
    Intersection = length * breath

    # Union Area
    box_a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    box_b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    Union = box_a_area + box_b_area - Intersection
    
    return Intersection/Union
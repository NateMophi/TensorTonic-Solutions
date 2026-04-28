def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    # predictions, y = np.array(predictions), np.array(targets)
    # p_t = np.where(y==1, predictions, 1 - predictions)
    p_t = []
    FL = []
    for p, y in zip(predictions, targets):
        if y==1:
            p_t.append(p)
        else:
            p_t.append(1-p)
    for i in p_t:
        FL.append(-alpha * (1 - i)**gamma * math.log(i))
    # FL = -alpha * (1 - p_t)**gamma * log(p_t)
    return sum(FL)/len(FL)
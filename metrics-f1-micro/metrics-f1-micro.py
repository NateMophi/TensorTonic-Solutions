def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    if len(y_true) != len(y_pred):
        raise ValueError

    TP = sum(y_true == y_pred for y_true, y_pred in zip(y_true, y_pred))
     
    F = len(y_true) - TP
    num, denom = (2 * TP), (2 * TP) + F + F

    if denom == 0:
        return 0
    return num/denom
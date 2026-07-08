def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    F =[]
    for row in matrix:
        filtered = [val for val in row if val!=0]
        if len(filtered) == 0:
            F.append(row)
        else:
            means = sum(filtered)/len(filtered)
            norm = [val - means if val!=0 else 0 for val in row]
            F.append(norm)
    return F
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    n = len(targets)
    M = []
    
    for cat in categories:
        e = 0
        idx = [i for i, val in enumerate(categories) if cat==val]
        for x in idx:
            e+=targets[x]
        e = e/len(idx)
        M.append(e)
    return M
            
            
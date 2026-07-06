def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    unique = list()
    for L in recommendations:
        for x in L:
            unique.append(x)
    return len(set(unique))/n_items
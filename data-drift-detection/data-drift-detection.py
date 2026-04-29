def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    normalized_ref = []
    normalized_prod = []
    drift = None
    D = {}
    for i in reference_counts:
        normalized_ref.append(i / sum(reference_counts))
    for j in production_counts:
        normalized_prod.append( j / sum(production_counts))
    TVD = 0
    for x,y in zip(normalized_prod, normalized_ref):
        TVD += abs(x - y)
    TVD*=0.5   
    if TVD > threshold:
        drift = True
    else:
        drift = False
    D.update({"score":TVD})
    D.update({"drift_detected":drift})
    return D
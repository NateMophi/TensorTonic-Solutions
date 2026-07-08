import numpy as np
def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    X = np.array(X, dtype= float)
    X_imp = X.copy()

    if X.ndim ==1 :
        mask = np.isnan(X)
        valid = X[~mask]
        stats = np.mean(valid) if strategy=="mean" else np.median(valid)
        X_imp[mask] = stats if len(valid)>0 else 0.0
        
    else:
        for columns in range(X.shape[1]):
            c = X[:, columns]
            mask = np.isnan(c)
            valid = c[~mask]
            stats = np.mean(valid) if strategy=="mean" else np.median(valid)
            X_imp[mask, columns] = stats if len(valid)>0 else 0.0 
    return X_imp
    

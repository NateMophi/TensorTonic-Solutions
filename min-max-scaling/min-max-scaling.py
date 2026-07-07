import numpy as np

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = np.array(data)
    num = data - np.min(data, axis=0)
    denom = np.max(data, axis=0) - np.min(data, axis=0)
    if denom.all(axis=0) == 0:
        data_scaled = num / 1
        return data_scaled.tolist()

    else:
        data_scaled = num/denom
        return data_scaled.tolist()
    
   

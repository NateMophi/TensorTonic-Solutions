# Slice the window when iterating thru i and j:

`window = X[ i*stride:i*stride + pool_size, j*stride:j*stride + pool_size ] `

`O[i, j] = np.max(window)`
import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    
    g = np.array(g)
    g_norm = np.linalg.norm(g)

    if max_norm < 0 or max_norm==0:
        return g
            
    if g_norm <= max_norm:
        return g
    else:
        g2 = g.copy()
        return np.dot(g2, max_norm/g_norm)

    
    #g_clipped = np.where(g_norm <= max_norm, g, np.dot(g, max_norm/g_norm))
    # return g_clipped
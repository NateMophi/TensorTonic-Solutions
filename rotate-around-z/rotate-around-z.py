import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    points = np.array(points)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                 [np.sin(theta), np.cos(theta), 0],
                 [0, 0, 1]])

    if points.ndim ==1 :
        points_reshaped = points.reshape(1, 3)
        x_col = points_reshaped[:,0]
        y_col = points_reshaped[:,1]
        z_col = points_reshaped[:,2]

        x_1 = x_col*np.cos(theta) - y_col*np.sin(theta)
        y_1 = x_col*np.sin(theta) + y_col*np.cos(theta)
        z_1 = z_col
        P = np.hstack((x_1, y_1, z_1))
        return P.reshape(3,)
        
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    
    x_t = np.dot(x, np.cos(theta)) - np.dot(y , np.sin(theta))
    y_t = x * np.sin(theta) + y * np.cos(theta)
    z_t = z
    
    return np.stack((x_t, y_t, z_t), axis=1)
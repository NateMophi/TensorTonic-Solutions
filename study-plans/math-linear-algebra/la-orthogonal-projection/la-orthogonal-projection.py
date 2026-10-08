import numpy as np

def projection_matrix(A: list) -> np.ndarray:
    """
    Returns the float64 projector onto the column space of A.
    """
    A = np.array(A)
    Gram = A.T @ A
    P = np.linalg.solve(Gram, A.T)
    return np.dot(A, P)
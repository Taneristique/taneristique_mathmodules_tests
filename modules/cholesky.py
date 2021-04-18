import numpy as np
def cholesky(A):
    """Upper or lower-triangular Cholesky factor of a. Returns a matrix object if a is a matrix object."""
    return np.linalg.cholesky(A)
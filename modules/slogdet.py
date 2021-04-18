import numpy as np
def slogdet(a):
    """#Computes the sign and (natural) logarithm of the determinant of an array than returns it"""
    (sign, logdet) = np.linalg.slogdet(a)
    return (sign,logdet)

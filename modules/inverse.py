import numpy as np
from scipy import linalg

class matrix_invert:
    """prints inverse of a matrix"""
    def __init__(self,a):
        self.a = a
    def do(self):
        print(linalg.inv(self.a))
    def check(self):
        print(self.a.dot(linalg.inv(self.a))) #double check


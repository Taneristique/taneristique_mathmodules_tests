from numpy import exp, abs, angle

def polar2z(r,theta):
    """prints cartesian correspondence of a polar coordinate"""
    print( r * exp( 1j * theta ))

def z2polar(z):
    """vice versa"""
    print ( abs(z), angle(z) )

from modules import *
A=np.array([[20,6],[3,10]]) #write your matrice arrays here in "A" variable
determinant(A)

B=np.array([[1,2],[3,4]]) #Will find inverse of a matrix
inverse=matrix_invert(B)
inverse.do()
polar2z(2,5) #polar coordinates to cartesian coordinates
z2polar(5)   #cartesian coordinates to polar coordinates

a = np.array([1+2j,3+4j])
b = np.array([5+6j,7+8j])
c = dot(a,b) #alternative matrix product with different broadcasting rules
print(c) 

a = np.ones([9, 5, 7, 4]) #the both inputs are one dimensional
b = np.ones([9, 5, 4, 3])
product = matmul(a,b)   #returns the matrix product of the inputs. This is a scalar only when both x1, x2 are 1-d vectors
print(product) 

a = np.array([[1, 0],[0, 1]])
b = np.array([1, 2])
product = matmul(a,b)   #returns the matrix product of the inputs. This is a scalar only when both x1, x2 are 1-d vectors
print(product) 

a = np.array([[1, 2], [3, 4]])
r=slogdet(a) #Compute the sign and (natural) logarithm of the determinant of an array.
print(r) 

i = np.array([[0, 1], [-1, 0]]) # matrix equiv. of the imaginary unit
print(matpow(i, 3)) # should = -i

A = [[1,-2j],[2j,5]]
print(cholesky(A)) #Upper or lower-triangular Cholesky factor of a. Returns a matrix object if a is a matrix object.

A = Matrix([[1, 0], [0, 1]])
print(sounds_definite(A))

A = Matrix([[-1, 0], [0, -1]])
print(sounds_definite(A))

A = Matrix([[1, 2], [2, -1]])
print(sounds_definite(A))



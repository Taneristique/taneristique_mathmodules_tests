from sympy import Matrix, symbols
from sympy.plotting import plot3d

def sounds_definite(B):
    """takes a matrix than returns if it is positive definite,negative definite,semi definite or not definite than ask user if they would want to draw it as 3d
    if user responds 'no' returns ok see you! if user says yes it shows 3dplot of matrix, otherwise unexpected value f...!!!!!"""
    a, b = symbols('a b')
    x = Matrix([a, b])
    if(B.is_positive_definite==True):
        print("It is positive definite.But B is positive semi definite statement is", B.is_positive_definite, '.')  
        answer=input("Would you want to draw it as 3d?")
        if(answer=="yes"):
            return plot3d((x.T*B*x)[0, 0], (a, B[0,0], B[0,1]), (b, B[1,0], B[1,1]))
        elif(answer=="no"):
            return "ok see you!"
        else:
            return "unexpected value f...!!!!!"
    elif(B.is_negative_definite==True):
        print("It is negative definite.But B is negative semi definite statement is", B.is_negative_definite, '.')
        if(B.is_negative_semidefinite=="True"):
            print("It is also positive semi definite.")
        answer=input("Would you want to draw it as 3d?")
        if(answer=="yes"):
            return plot3d((x.T*B*x)[0, 0], (a, B[0,0], B[0,1]), (b, B[1,0], B[1,1]))
        elif(answer=="no"):
            return "ok see you!"
        else:
            return "unexpected value f...!!!!!"
    elif(B.is_positive_semidefinite==True):
        print("It is positive semi definite.")
        answer=input("Would you want to draw it as 3d?")
        if(answer=="yes"):
            return plot3d((x.T*B*x)[0, 0], (a, B[0,0], B[0,1]), (b, B[1,0], B[1,1]))
        elif(answer=="no"):
            return "ok see you!"
        else:
            return "unexpected value f...!!!!!"
    elif(B.is_negative_semidefinite):
        print("It is negative semi definite.")
        answer=input("Would you want to draw it as 3d?")
        if(answer=="yes"):
            return plot3d((x.T*B*x)[0, 0], (a, B[0,0], B[0,1]), (b, B[1,0], B[1,1]))
        elif(answer=="no"):
            return "ok see you!"
        else:
            return "unexpected value f...!!!!!"
    else:
        print("It is indefinite because","B.is_indefinite is", B.is_indefinite)
        answer=input("Would you want to draw it as 3d?")
        if(answer=="yes"):
            return plot3d((x.T*B*x)[0, 0], (a, B[0,0], B[0,1]), (b, B[1,0], B[1,1]))
        elif(answer=="no"):
            return "ok see you!"
        else:
            return "unexpected value f...!!!!!"
import numpy as np


# x^2 -x -12 = 0

a = 1
b = -1
c = -12

def raiz(a,b,c):
    return np.sqrt(b**2 - 4*a*c)

def f(a,b,c):
    print((-b + raiz(a,b,c))/(2*a))
    print((-b - raiz(a,b,c))/(2*a))

f(a,b,c)
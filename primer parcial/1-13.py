import numpy as np


# x^2 -x -12 = 0

a = 1
b = -1
c = -12
r1 = 0
r2 = 0
vr = 4.00054

def raiz(a,b,c):
    return np.sqrt(b**2 - 4*a*c)

def f(a,b,c):
    r1 = ((-b + raiz(a,b,c))/(2*a))
    r2 = ((-b - raiz(a,b,c))/(2*a))
    
    if r1 > r2:
        return r1
    else:
        return r2

f(a,b,c)

def ET(vr, va):
    return abs(vr - va)

def ER(vr, va):
    return abs((vr - va)/vr)

def ERP(vr, va):
    return abs((vr - va)/vr) * 100

print("error relativo porcentual: ", ERP(vr, f(a,b,c)))

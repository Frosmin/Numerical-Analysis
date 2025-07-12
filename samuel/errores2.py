import numpy as np

# x^2 -x -12 = 0
def raiz(a,b,c):
    return np.sqrt(b**2 - 4*a*c)
a = 1
b = -1
c = -12
r1 = 0
r2 = 0
vr1 = 2.999878
vr2 = -4.000123
r1 = ((-b + raiz(a,b,c))/(2*a))
r2 = ((-b - raiz(a,b,c))/(2*a))

def ET(vr, va):
    return abs(vr - va) 

def ER(vr, va):
    return abs((vr - va)/vr)

def ERP(vr, va):
    return abs((vr - va)/vr) * 100

print("error 1 -------------------------------------------------------------------------------------------------")
print("error real absoluto: ", ET(vr1, r1))
print("error relativo: ",ER(vr1, r1))
print("error relativo porcentual: ", ERP(vr1, r1))

print("error 2 -------------------------------------------------------------------------------------------------")
print("error real absoluto: ", ET(vr2, r2))
print("error relativo: ",ER(vr2, r2))
print("error relativo porcentual: ", ERP(vr2, r2))



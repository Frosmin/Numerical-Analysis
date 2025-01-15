import numpy as np


def bisecion(a,b,e,i):
    if a > b :
        a,b == b,a
    
    
    if i == 0:
        return (a+b)/2
    else:
       c = diferencia(a,b)
       a1 = ecuacion(a)
       b1 = ecuacion(b)
       c1 = ecuacion(c)
    if a1 * c1 < 0:
            return bisecion(a1,c1,e,i-1)
    else:
            return bisecion(c1,b1,e,i-1)
    
    
    
def diferencia(a,b):
    return (a+b)/2


def error(a,b,e):
    return (np.log((b-a)/e))/np.log(2)


def ecuacion(x):
    if x > 700:
        return float("inf")
    
    try:
        return (2*x*np.exp(x))-3
    except OverflowError:
        return "Error"

# print(error(0,2,0.001))
# print(ecuacion(2))
print(bisecion(0,1,0.001,11))
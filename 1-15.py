import numpy as np
import math

# def bisecion(a,b,e,i):
#     if a < b :
#         a,b = b,a
    
    
#     if i == 0 or (a-b) < e:
#         return (a+b)/2
#     else:
#        c = (a+b)/2
#        a1 = ecuacion(a)
#        b1 = ecuacion(b)
#        c1 = ecuacion(c)
#     if a1 * c1 < 0:
#             return bisecion(a1,c1,e,i-1)
#     else:
#             return bisecion(c1,b1,e,i-1)
    
    
def error(a,b,e):
    return (np.log((b-a)/e))/np.log(2)

def ecuacion(x):
    if x > 100:
        return float("inf")
    
    try:
        return (2*x*np.exp(x))-3
    except OverflowError:
        return "Error"

def bisecion(a, b, e, i):
    if a > b:
        a, b = b, a
    
    if i == 0:
        return (a+b)/2
        
    c = (a + b)/2
    fa = ecuacion(a)
    fc = ecuacion(c)
    
    if abs(fc) < e:
        return c
        
    if fa * fc < 0:
        return bisecion(a, c, e, i-1)  
    return bisecion(c, b, e, i-1)     
print(f"resultado: " + str(bisecion(0,2,0.00000001,error(0,2,0.00000001))))





#codigo facil :D

fx = lambda x: 2*x*np.exp(x) - 3
def bisection2(fx, a ,b ,t):
    e = b-a
    while e > t:
        c = (a+b)/2
        fa = fx(a)
        fc = fx(c)
        res = fa * fc
        if res < 0:
            b = c
        if res > 0:
            a = c
        e = b-a
    return c
print (f"resultado: " + str(bisection2(fx, 0, 2, 0.00000001)))
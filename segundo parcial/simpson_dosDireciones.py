import numpy as np

def y(fx,hy,a,b,x,n):
    
    res = 0
    i= 0
    while i < n+1:
        if i == 0:
            p = 1
            res += p * fx(x,a)
            i += 1
            a += hy
        elif a == b:
            p = 1
            res += p * fx(x, a)
            i += 1
            a += hy
        elif i % 2 != 0:
            p = 4
            res += p * fx(x, a)
            i += 1
            a += hy
        else:
            p = 2
            res += p * fx(x, a)
            i += 1
            a += hy
    return (hy/3)*res 

def x(fx,hx,hy,a,b,c,d,n):
    res = 0
    i = 0
    while i < n+1: 
        if i == 0:
            p = 1
            res += p * y(fx,hy,c,d,a,n)
            i += 1
            a += hx
        elif a == b:
            p = 1
            res += p * y(fx,hy,c,d,a,n)
            i += 1
            a += hx
        elif i % 2 != 0:
            p = 4
            res += p * y(fx,hy,c,d,a,n)
            i += 1
            a += hx
        else:
            p = 2
            res += p * y(fx,hy,c,d,a,n)
            i += 1
            a += hx
    return (hx/3)*res




def simpson(fx,a,b,c,d,n):
    hx = (b-a)/n
    hy = (d-c)/n
    print(x(fx,hx,hy,a,b,c,d,n))



a = 1
b = 3
c = 2
d = 4
n = 4
fx = lambda x, y: x*((x**2) + y)

simpson(fx,a,b,c,d,n)
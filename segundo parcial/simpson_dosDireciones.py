import numpy as np

fx = lambda x, y: x*((x**2) + y)

def f (x,y):
    return x*((x**2) + y)



def y(fx,hy,a,b,x,n):
    
    res = 0
    i= 0
    while i < n+1:
        if i == 0:
            p = 1
            res += p * fx(x,a)
            #print(p * fx(x,a))
            i += 1
            a += hy
        elif a == b:
            p = 1
            res += p * fx(x, a)
            #print(p * fx(x,a))
            i += 1
            a += hy
        elif i % 2 != 0:
            p = 4
            res += p * fx(x, a)
            #print(p * fx(x,a))
            i += 1
            a += hy
        else:
            p = 2
            res += p * fx(x, a)
            #print(p * fx(x,a))
            i += 1
            a += hy
    return (hy/3)*res 



def x(fx,hx,hy,a,b,c,d,n):
    res = 0
    i = 0
    while i < n+1:
        if i == 0:
            p = 1
            res += p * y(fx,hy,a,b,c,n)
            #print(p * y(fx,hy,a,b,c,n))
            i += 1
            c += hx
        elif c == b:
            p = 1
            res += p * y(fx,hy,a,b,c,n)
            #print(p * y(fx,hy,a,b,c,n))
            i += 1
            c += hx
        elif i % 2 != 0:
            p = 4
            res += p * y(fx,hy,a,b,c,n)
            #print(p * y(fx,hy,a,b,c,n))
            i += 1
            c += hx
        else:
            p = 2
            res += p * y(fx,hy,a,b,c,n)
            #print(p * y(fx,hy,a,b,c,n))
            i += 1
            c += hx
    return (hx/3)*res


hx = 0.5
hy = 0.5    
a = 1
b = 3
c = 2
d = 4
n = 4


print (x(fx,hx,hy,a,b,c,d,n))


# print(fx(3,4))


#print (fx(2.5,4))
# import numpy as np

# def y(fx,hy,c,d,x,n):
    
#     res = 0
#     i= 0
#     while i < n+1:
#         if i == 0 or i == n:
#             p = 1
#         elif i % 2 != 0:
#             p = 4
#         else:
#             p = 2
#         i += 1
#         res += p * fx(x,c)
#         c += hy
#     return (hy/3)*res 

# def x(fx,hx,hy,a,b,c,d,n):
#     res = 0
#     i = 0
#     while i < n+1: 
#         if i == 0 or i == n:
#             p = 1
#         elif i % 2 != 0:
#             p = 4
#         else:
#             p = 2
#         res += p * y(fx,hy,c,d,a,n)
#         i += 1
#         a += hx
#     return (hx/3)*res

# def simpson(fx,a,b,c,d,n):
#     hx = (b-a)/n
#     hy = (d-c)/n
#     print(x(fx,hx,hy,a,b,c,d,n))

# a = 1
# b = 3
# c = 2
# d = 4
# n = 4
# fx = lambda x, y: x*((x**2) + y)

# simpson(fx,a,b,c,d,n)





import numpy as np





def x(fx, hx, hy, a, b, c, d, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    res = 0
    for i in range(n + 1):
        x_val = a + i * hx  #para aumentar hx :D
        if i == 0 or i == n:
            p = 1
        elif i % 2 != 0:
            p = 4
        else:
            p = 2
        res += p * y(fx, hy, c, d, x_val, n)
    return (hx/3) * res

def y(fx, hy, c, d, x, n):
    res = 0
    c_original = c
    for i in range(n + 1):
        y_val = c_original + i * hy
        if i == 0 or i == n:
            p = 1
        elif i % 2 != 0:
            p = 4
        else:
            p = 2
        res += p * fx(x, y_val)
    return (hy/3) * res

def simpson(fx,a,b,c,d,n):
    hx = (b-a)/n
    hy = (d-c)/n
    print(x(fx,hx,hy,a,b,c,d,n))
    
a = 0
b = 2
c = 1
d = 3
n = 2
fx = lambda x, y: np.sin(x**2 +2*y)

simpson(fx,a,b,c,d,n)

# fx = lambda x, y: x*((x**2) + y)
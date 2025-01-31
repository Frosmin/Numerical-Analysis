import numpy as np 


fx = lambda x,y : (6*(x**2)) * y



def euler(fx, x0, y0, h, n):
    for i in range(n):
        y = y0 + fx(x0, y0) * h
        x0 += h
        y0 = y 
    return y




y0 = 0
x0 = 2
max = 4 
h = 0.25
n = int((max - x0)/h)

print(euler(fx, x0, y0, h, 2))

print(fx(2,0))




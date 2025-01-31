import numpy as np 


fx = lambda x,y : (6*(x**2)) * y



def euler(fx, x0, y0, h, n):
    for i in range(n+1):
        y = y0 + fx(x0, y0) * h
        print(f"x{i} = {x0}    y{i} = {y} ")
        x0 += h
        y0 = y 
        
    return y




y0 = 0
x0 = 2
max = 4 
h = 0.25
n = int((max - x0)/h)

#n valor que quieres sacar numero de iteracion iteracion final 
print(euler(fx, x0, y0, h, n))









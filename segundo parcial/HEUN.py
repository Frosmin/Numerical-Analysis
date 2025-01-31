import numpy as np 


# fx = lambda x,y : (6*(x**2)) * y
fx = lambda x,y: 5/(x**2) +1


def euler(fx, x0, y0, h, n):
    for i in range(n+1):
        y = y0 + fx(x0, y0) * h
        print(f"x{i} = {x0}    y{i} = {y} ")
        x0 += h
        y0 = y 
        
    return y



def heun(fx,x0,y0,h,n):
    for i in range(n+1):
        y1 = y0 + ((fx(x0,y0) + fx(x0+h,euler(fx,x0,y0,h,i))/2) * h)
        # print(f"x{i} = {x0}    y{i} = {y1} ")
        x0 += h
        y0 = y1
    return y1



# y0 = 0
# x0 = 2
# max = 4 
# h = 0.25
# n = int((max - x0)/h)


y0 = 0
x0 = 2
max = 4 
h = 0.25
n = int((max - x0)/h)

#n valor que quieres sacar numero de iteracion iteracion final 
print(euler(fx, x0, y0, h, n))
# print(heun(fx, x0, y0, h, n))









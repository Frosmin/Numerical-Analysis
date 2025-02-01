import numpy as np

f = lambda x,y: 3*(x**2)*y

k1f = lambda x,y: f(x,y)
k2f = lambda x,y,h: f(x + h/2, y + h/2*k1f(x,y))  
k3f = lambda x,y,h: f(x + h/2, y + h/2*k2f(x,y,h))
k4f = lambda x,y,h: f(x + h,   y + h*k3f(x,y,h))

yn = lambda k1,k2,k3,k4,h,y: y+ h/6*(k1 + 2*k2 + 2*k3 + k4)



def RK4(f, y0, x0 ,n, maximon, h):
    for i in range(n+1):
        k1 = k1f(x0, y0)
        k2 = k2f(x0, y0, h)
        k3 = k3f(x0, y0, h)
        k4 = k4f(x0, y0, h)
        y = yn(k1,k2,k3,k4,h,y0)

        print(f"k1 = {k1}")
        print(f"k2 = {k2}")
        print(f"k3 = {k3}")
        print(f"k4 = {k4}")
        print(f"y{n} = {y}")
        print("------------------------")
        y0 = y    
        x0 += h
    return y

y0 = 0.5
x0 = -2 
maximo = -0.2
h = 0.3
n = int((maximo - x0)/h)
print(RK4(f, y0, x0 ,n, maximo, h))


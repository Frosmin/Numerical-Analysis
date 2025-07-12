import numpy as np
import math

f = lambda x,y: math.log(x**y)


k1f = lambda x,y: f(x,y)
k2f = lambda x,y,h: f(x + h/2, y + h/2*k1f(x,y))  
k3f = lambda x,y,h: f(x + h/2, y + h/2*k2f(x,y,h))
k4f = lambda x,y,h: f(x + h,   y + h*k3f(x,y,h))
yn = lambda k1,k2,k3,k4,h,y: y+ h/6*(k1 + 2*k2 + 2*k3 + k4)

error = lambda xr,xa: abs((xr-xa)/xr)*100 
valor_real = lambda x ,c : np.exp(x**3 + c)  # y = e^(x^3 + C)

def ERP (xa,xr):
    return abs((xr-xa)/xr)*100
def RK4(f, y0, x0 ,n, maximon, h,c):
    for i in range(n):
        k1 = k1f(x0, y0)
        k2 = k2f(x0, y0, h)
        k3 = k3f(x0, y0, h)
        k4 = k4f(x0, y0, h)
        y = yn(k1,k2,k3,k4,h,y0)

        print(f"k1 = {k1}")
        print(f"k2 = {k2}")
        print(f"k3 = {k3}")
        print(f"k4 = {k4}")
        print(f"y{i+1} = {y}")
        
        y0 = y    
        x0 += h
        #print(f"Valor real: {valor_real(x0, c)}")
        #print(f"ERP: {ERP(y,valor_real(x0, c))} %" )
        print("------------------------")
    return y

c = 7.30985
y0 = 1
x0 = 1
maximo = 2
h = 0.25
n = int((maximo - x0)/h)
print(RK4(f, y0, x0 ,n, maximo, h,c))


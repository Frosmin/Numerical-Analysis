import numpy as np


fx = lambda x: -np.log(2-x)

error = lambda x2, x1: abs((x2-x1)/x2)

def punto_fijo(fx, x0, t):
    i=0
    x1 = fx(x0)
    while error(x1,x0) >t:
        i+=1
        x0 = x1
        x1 = fx(x0)
    print(i)
    return x1



print(punto_fijo(fx, 1.5, 0.0000000001))
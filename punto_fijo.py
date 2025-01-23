import numpy as np
import math



























# fx = lambda x: 2-np.e ** -x
# fx1 = lambda x: x * np.cos(x+1)+4

# fx2 =lambda x: -4/np.cos(x+1)
# error = lambda x2, x1: abs((x2-x1)/x2)

# def punto_fijo(fx, x0, t):
#     i=0
#     x1 = fx(x0)
#     while error(x1,x0) >t:
#         i+=1
#         x0 = x1
#         x1 = fx(x0)
#         print(x1)
#     print(f"iteraciones: " +str(i))
#     return x1
# print(f"resultado: " + str(punto_fijo(fx2, 1, 0.001)))



def f(x):
    return -4/np.cos(x+1) #ecuaxion ya despejada


def punto_fijo(f, x0, tolerancia, max_iter=100):
    i = 0
    while i < max_iter:
        x1 = f(x0)
        if abs((x1-x0)/x1) < tolerancia:
            print(f"Convergió en {i} iteraciones")
            return x1
        x0 = x1
        i += 1
        print(f"Iteración {i}: x = {x1}")
    
    raise Exception("No convergió en el máximo de iteraciones")
try:
    resultado = punto_fijo(f, 7, 0.001)
    print(f"\nRaíz encontrada: {resultado}")
except Exception as e:
    print(e)









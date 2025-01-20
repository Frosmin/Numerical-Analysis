import numpy as np
import math



























fx = lambda x: 2-np.e ** -x
fx1 = lambda x: x * np.cos(x+1)+4

error = lambda x2, x1: abs((x2-x1)/x2)

def punto_fijo(fx, x0, t):
    i=0
    x1 = fx(x0)
    while error(x1,x0) >t:
        i+=1
        x0 = x1
        x1 = fx(x0)
    print(f"iteraciones: " +str(i))
    return x1
print(f"resultado: " + str(punto_fijo(fx, 1, 0.001)))








# fx1 = lambda x: math.acos(-4 / x) - 1

# # Función de error relativo
# error = lambda x2, x1: abs((x2-x1)/x2)

# def punto_fijo(fx, x0, t, max_iter=1000):
#     i = 0
#     x1 = fx(x0)
    
#     try:
#         while error(x1,x0) > t and i < max_iter:
#             i += 1
#             x0 = x1
#             x1 = fx(x0)
#             print(f"Iteración {i}: x = {x1:.6f}")
            
#         if i == max_iter:
#             print("Advertencia: Máximo de iteraciones alcanzado")
        
#         print(f"Total iteraciones: {i}")
#         return x1
        
#     except ValueError:
#         print("Error: Valor fuera del dominio")
#         return None

# # Prueba
# print(f"Resultado: {punto_fijo(fx1, 1, 0.001):.6f}")


# import math

# # Definimos la función g(x) correspondiente a la forma de punto fijo
# def g(x):
#     return math.acos(-4 / x) - 1

# # Función para aplicar el método del Punto Fijo
# def punto_fijo(x0, tol=1e-6, max_iter=100000000):
#     iteraciones = 0
#     while iteraciones < max_iter:
#         x1 = g(x0)
#         if abs(x1 - x0) < tol:
#             return x1, iteraciones
#         x0 = x1
#         iteraciones += 1
#     raise ValueError("El método no converge después de {} iteraciones".format(max_iter))

# # Valor inicial cercano al origen
# x0 = 0.1
# try:
#     raiz, iteraciones = punto_fijo(x0)
#     print("Raíz encontrada: {:.6f} en {} iteraciones".format(raiz, iteraciones))
# except ValueError as e:
#     print(e)





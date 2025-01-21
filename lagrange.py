# import numpy as np
# import matplotlib.pyplot as plt

# # Puntos dados
# x = np.array([-1, 1.5, 4, -2.5])
# y = np.array([0, 2, 1, 3])

# def lagrange(x_points, y_points, x):
#     n = len(x_points)
#     L = 0
    
#     for i in range(n):
#         # Calcular el polinomio Li(x)
#         Li = 1
#         for j in range(n):
#             if i != j:
#                 Li *= (x - x_points[j])/(x_points[i] - x_points[j])
#         L += y_points[i] * Li
    
#     return L

# # Generar puntos para graficar
# x_new = np.linspace(min(x)-0.5, max(x)+0.5, 100)
# y_new = [lagrange(x, y, i) for i in x_new]

# # Graficar
# plt.figure(figsize=(10, 6))
# plt.plot(x_new, y_new, 'b-', label='Polinomio interpolador')
# plt.plot(x, y, 'ro', label='Puntos dados')
# plt.grid(True)
# plt.legend()
# plt.title('Interpolación de Lagrange')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# # Mostrar el resultado evaluando en algunos puntos
# print("Evaluación en x=0:", lagrange(x, y, 0))
# print("Evaluación en x=1:", lagrange(x, y, 1))


import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, simplify

# Puntos dados
x_points = np.array([-1, 1.5, 4, -2.5])
y_points = np.array([0, 2, 1, 3])

# Crear variable simbólica
x = symbols('x')

def get_lagrange_polynomial():
    n = len(x_points)
    L = 0
    
    for i in range(n):
        # Calcular el polinomio Li(x)
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - x_points[j])/(x_points[i] - x_points[j])
        L += y_points[i] * Li
    
    # Expandir y simplificar el polinomio
    polynomial = expand(L)
    simplified = simplify(polynomial)
    return simplified

# Obtener y mostrar el polinomio
polinomio = get_lagrange_polynomial()
print("\nPolinomio de Lagrange:")
print(polinomio)
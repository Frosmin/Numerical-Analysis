import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, simplify, lambdify






















x_puntos = np.array([-1, 1.5, 4, -2.5])
y_points = np.array([0, 2, 1, 3])
x = symbols('x')
def lagrange():
    n = len(x_puntos)
    L = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - x_puntos[j])/(x_puntos[i] - x_puntos[j])
        L += y_points[i] * Li
    polinomio = expand(L)
    simplificacion = simplify(polinomio)
    return simplificacion
polinomio = lagrange()
print("\nPolinomio de Lagrange:")
print(polinomio)


f = lambdify(x, polinomio, 'numpy')

# Generar puntos para la gráfica
x_graf = np.linspace(min(x_puntos)-0.5, max(x_puntos)+0.5, 100)
y_graf = f(x_graf)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_graf, y_graf, 'b-', label='Polinomio interpolador')
plt.plot(x_puntos, y_points, 'ro', label='Puntos dados')
plt.grid(True)
plt.legend()
plt.title('Interpolación de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
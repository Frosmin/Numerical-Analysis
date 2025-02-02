import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, simplify





def Li(x, i, x_puntos):
    """Calcula el término i del polinomio de Lagrange"""
    n = len(x_puntos)
    Li = 1
    for j in range(n):
        if j != i:
            Li *= (x - x_puntos[j])/(x_puntos[i] - x_puntos[j])
    return Li

def polinomio_lagrange(x, x_puntos, y_points):
    """Calcula el polinomio de Lagrange"""
    n = len(x_puntos)
    resultado = 0
    for i in range(n):
        resultado += y_points[i] * Li(x, i, x_puntos)
    return resultado

# Puntos de interpolación
# x_puntos = np.array([-2, -1, 0, 2])
# y_points = np.array([0, 3, 3, 6])

x_puntos = np.array([-1, 0, 1, 3, 6])
y_points = np.array([3, 7, 3, 5, 1])

# Cálculo simbólico del polinomio
x = symbols('x')
polinomio = 0
print("\nTérminos del polinomio de Lagrange:")
for i in range(len(x_puntos)):
    termino = y_points[i] * Li(x, i, x_puntos)
    print(f"L{i}(x) * y{i} = {expand(termino)}")
    polinomio += termino

print("\nPolinomio de Lagrange completo:")
polinomio_simplificado = simplify(expand(polinomio))
print(polinomio_simplificado)

# Visualización gráfica
x_graf = np.linspace(min(x_puntos)-0.5, max(x_puntos)+0.5, 100)
y_graf = [polinomio_lagrange(xi, x_puntos, y_points) for xi in x_graf]

plt.figure(figsize=(10, 6))
plt.plot(x_graf, y_graf, 'b-', label='Polinomio de Lagrange')
plt.plot(x_puntos, y_points, 'ro', label='Puntos dados')
plt.grid(True)
plt.legend()
plt.title('Interpolación de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
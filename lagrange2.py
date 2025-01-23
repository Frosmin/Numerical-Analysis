import numpy as np
import matplotlib.pyplot as plt
import sympy as sp





















x_puntos = np.array([-2, -1, 0, 2])
y_puntos = np.array([0, 3, 3, 6])
x = sp.Symbol('x')
def obtener_polinomio_lagrange(x_puntos, y_puntos):
    n = len(x_puntos)
    polinomio = 0
    for i in range(n):
        termino = y_puntos[i]
        for j in range(n):
            if i != j:
                termino *= (x - x_puntos[j])/(x_puntos[i] - x_puntos[j])
        polinomio += termino
    return sp.expand(polinomio)


polinomio = obtener_polinomio_lagrange(x_puntos, y_puntos)
print("\nPolinomio de Lagrange:")
print(polinomio)















# Crear puntos para graficar el polinomio
x = np.linspace(-2.5, 2.5, 100)
y = (x**3)/2 - x/2 + 3

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='p(x) = x³/2 - x/2 + 3')
plt.plot(x_puntos, y_puntos, 'ro', label='Puntos dados')
plt.grid(True)
plt.legend()
plt.title('Polinomio de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
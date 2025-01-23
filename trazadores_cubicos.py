import numpy as np
import matplotlib.pyplot as plt

# Puntos dados
x = np.array([-1, 0, 1, 3, 6])
y = np.array([3, 7, 3, 5, 1])


# x = np.array([-1, -2, 0, 2, 4])
# y = np.array([3, 0, 3, 6, 1])


# Número de intervalos
n = len(x) - 1

# Matriz del sistema
h = np.diff(x)  # Diferencias entre puntos
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)

# Condiciones naturales (segunda derivada en extremos es 0)
A[0, 0] = 1
A[-1, -1] = 1

# Ecuaciones para la continuidad de la segunda derivada
for i in range(1, n):
    A[i, i-1] = h[i-1]
    A[i, i] = 2 * (h[i-1] + h[i])
    A[i, i+1] = h[i]
    b[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

# Resolver el sistema
c = np.linalg.solve(A, b)

# Calcular coeficientes b y d
b = np.zeros(n)
d = np.zeros(n)
for i in range(n):
    b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2*c[i] + c[i+1]) / 3
    d[i] = (c[i+1] - c[i]) / (3*h[i])

# Coeficientes a
a = y[:-1]

# Mostrar los polinomios
for i in range(n):
    print(f"S_{i}(x) = {a[i]} + {b[i]}*(x - {x[i]}) + {c[i]}*(x - {x[i]})^2 + {d[i]}*(x - {x[i]})^3")

# Graficar los trazadores
for i in range(n):
    xs = np.linspace(x[i], x[i+1], 100)
    ys = a[i] + b[i]*(xs - x[i]) + c[i]*(xs - x[i])**2 + d[i]*(xs - x[i])**3
    plt.plot(xs, ys, label=f"S_{i}(x)")

plt.scatter(x, y, color='red', label="Puntos")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trazadores cúbicos")
plt.grid()
plt.show()

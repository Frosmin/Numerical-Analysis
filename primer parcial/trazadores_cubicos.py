import numpy as np
import matplotlib.pyplot as plt

# x = np.array([-1, -2, 0, 2, 4])
# y = np.array([3, 0, 3, 6, 1])
# Puntos dados














x = np.array([-1, 0, 1, 3, 6])
y = np.array([3, 7, 3, 5, 1])
n = len(x) - 1
h = np.diff(x)  
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)
A[0, 0] = 1
A[-1, -1] = 1
for i in range(1, n):
    A[i, i-1] = h[i-1]
    A[i, i] = 2 * (h[i-1] + h[i])
    A[i, i+1] = h[i]
    b[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
c = np.linalg.solve(A, b)
b = np.zeros(n)
d = np.zeros(n)
for i in range(n):
    b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2*c[i] + c[i+1]) / 3
    d[i] = (c[i+1] - c[i]) / (3*h[i])
a = y[:-1]
for i in range(n):
    print(f"S_{i}(x) = {a[i]} + {b[i]}*(x - {x[i]}) + {c[i]}*(x - {x[i]})^2 + {d[i]}*(x - {x[i]})^3")










#grafica
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

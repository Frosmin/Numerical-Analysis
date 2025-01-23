import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, simplify, lambdify



def diferencias_divididas(x, y):
    n = len(x)
    F = np.zeros([n, n])
    F[:,0] = y
    for j in range(1,n):
        for i in range(n-j):
            F[i,j] = (F[i+1,j-1] - F[i,j-1])/(x[i+j] - x[i])
            
    return F[0,:]
def polinomio_newton(x, coef, punto):
    n = len(x)
    resultado = coef[0]
    producto = 1
    for i in range(1, n):
        producto *= (punto - x[i-1])
        resultado += coef[i] * producto
        
    return resultado
# Datos


# x = np.array([-1, 3/2, 4, -2.5])
# y = np.array([0, 2, 1, 3])

x = np.array([-1, -2, 0, 2])
y = np.array([3, 0, 3, 6])



coeficientes = diferencias_divididas(x, y)
print("Coeficientes de las diferencias divididas:")
print(coeficientes)
print("\nPolinomio interpolante de Newton:")
print(f"P(x) = {coeficientes[0]:.4f}", end="")
for i in range(1, len(coeficientes)):
    if coeficientes[i] != 0:
        print(f" + ({coeficientes[i]:.4f})", end="")
        for j in range(i):
            print(f"(x - {x[j]:.4f})", end="")
print()










x_sym = symbols('x')
def lagrange(x_points, y_points):
    n = len(x_points)
    L = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x_sym - x_points[j])/(x_points[i] - x_points[j])
        L += y_points[i] * Li
    polinomio = expand(L)
    simplificacion = simplify(polinomio)
    return simplificacion

# Usar los mismos puntos que en Newton
x_points = np.array([-1, -2, 0, 2])
y_points = np.array([3, 0, 3, 6])

polinomio = lagrange(x_points, y_points)
print("\nPolinomio de Lagrange:")
print(polinomio)

f = lambdify(x_sym, polinomio, 'numpy')







#trazadores

# Puntos dados



x = np.array([-1, -2, 0, 2, 4])
y = np.array([3, 0, 3, 6, 1])


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







def lagrange(x, y):
    x_sym = symbols('x')
    n = len(x)
    polinomio = 0
    
    for i in range(n):
        termino = y[i]
        for j in range(n):
            if i != j:
                termino *= (x_sym - x[j])/(x[i] - x[j])
        polinomio += termino
    
    return simplify(expand(polinomio))







# Datos de entrada
x = np.array([-1, -2, 0, 2])
y = np.array([3, 0, 3, 6])

# Cálculos previos para trazadores cúbicos
n = len(x) - 1  # número de intervalos
h = np.diff(x)
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)

# Matriz del sistema
A[0, 0] = 1
A[-1, -1] = 1
for i in range(1, n):
    A[i, i-1] = h[i-1]
    A[i, i] = 2*(h[i-1] + h[i])
    A[i, i+1] = h[i]
    b[i] = 3*((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])

# Resolver sistema para obtener c
c = np.linalg.solve(A, b)

# Calcular coeficientes b y d
b_coef = np.zeros(n)
d = np.zeros(n)
for i in range(n):
    b_coef[i] = (y[i+1] - y[i])/h[i] - h[i]*(2*c[i] + c[i+1])/3
    d[i] = (c[i+1] - c[i])/(3*h[i])
a = y[:-1]

# Graficación
plt.figure(figsize=(12, 8))

# 1. Curva de Newton
x_grafica = np.linspace(min(x)-0.5, max(x)+0.5, 200)
y_newton = [polinomio_newton(x, coeficientes, punto) for punto in x_grafica]
plt.plot(x_grafica, y_newton, 'k-', label='Newton', linewidth=2)

# 2. Curva de Lagrange
x_sym = symbols('x')
polinomio = lagrange(x, y)
f = lambda x_val: float(polinomio.subs(x_sym, x_val))
y_lagrange = [f(xi) for xi in x_grafica]
plt.plot(x_grafica, y_lagrange, 'y--', label='Lagrange', linewidth=2)

# 3. Curva de Trazadores Cúbicos
for i in range(n):
    xs = np.linspace(x[i], x[i+1], 100)
    ys = a[i] + b_coef[i]*(xs - x[i]) + c[i]*(xs - x[i])**2 + d[i]*(xs - x[i])**3
    if i == 0:
        plt.plot(xs, ys, 'r-.', label='Trazadores Cúbicos', linewidth=2)
    else:
        plt.plot(xs, ys, 'r-.', linewidth=2)

plt.plot(x, y, 'ko', label='Puntos dados', markersize=8)
plt.grid(True)
plt.legend(fontsize=10)
plt.title('Comparación de Métodos de Interpolación', fontsize=12)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.show()
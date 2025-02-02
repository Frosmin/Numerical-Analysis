import numpy as np
import matplotlib.pyplot as plt






















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
x = np.array([-1, -2, 0, 2])
y = np.array([3, 0, 3, 6])



# x = np.array([-1, 3/2, 4, -2.5])
# y = np.array([0, 2, 1, 3])
coeficientes = diferencias_divididas(x, y)
# print("Coeficientes de las diferencias divididas:")
# print(coeficientes)
print("\nPolinomio interpolante de Newton:")
print(f"P(x) = {coeficientes[0]:.4f}", end="")
for i in range(1, len(coeficientes)):
    if coeficientes[i] != 0:
        print(f" + ({coeficientes[i]:.4f})", end="")
        for j in range(i):
            print(f"(x - {x[j]:.4f})", end="")
print()









# Grafica
x_grafica = np.linspace(min(x)-0.5, max(x)+0.5, 200)
y_grafica = [polinomio_newton(x, coeficientes, punto) for punto in x_grafica]
plt.figure(figsize=(10, 6))
plt.plot(x_grafica, y_grafica, 'b-', label='Polinomio interpolante')
plt.plot(x, y, 'ro', label='Puntos dados')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio Interpolante de Newton')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x * np.cos(x + 1) + 4

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)  # Desde -10 hasta 10 con 1000 puntos

# Calcular los valores de y
y = f(x)

# Graficar la función
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
plt.plot(x, y, label=r'$f(x) = x \cos(x+1) + 4$', color='b')  # Gráfico de la función
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Eje x
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Eje y
plt.title("Gráfica de $f(x) = x \cos(x+1) + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


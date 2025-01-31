import sympy as sp

# Definir variables
x, y = sp.symbols('x y')

# Definir la función a integrar
f = sp.sin(2*x**2 + 2*y)

# Definir los límites de integración
x_limits = (x, 1, 2)
y_limits = (y, 0, 1)

# Calcular la integral doble
integral_doble = sp.integrate(f, x_limits)
resultado = sp.integrate(integral_doble, y_limits)

# Evaluar numéricamente el resultado
resultado_numerico = resultado.evalf()

# Mostrar resultado
print("Resultado de la integral doble:", resultado_numerico)
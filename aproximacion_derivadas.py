import numpy as np
#dos puntos 







fx = lambda x: np.e**((x**2)+x)
h=0.1
x=1.1

def derivada_dos_puntos(fx, x, h):
    resultado1 = (fx(x+h) - fx(x))/h
    resultado2 = (fx(x+h) - fx(x-h))/(2*h)
    resultado3 = (fx(x) - fx(x-h))/h
    print(f" adelante x={x} es: {resultado1:.6f}")
    print(f" centro x={x} es: {resultado2:.6f}")
    print(f" atras x={x} es: {resultado3:.6f}")
    return 
# derivada_dos_puntos(fx,x,h)

def derivada_tres_puntos(fx, x, h):
    adelante = (-3*fx(x) + 4*fx(x+h) - fx(x+2*h))/(2*h)
    
    # Hacia atrás
    atras = (fx(x-2*h) - 4*fx(x-h) + 3*fx(x))/(2*h)
    
    # Central
    central = (fx(x+h) - fx(x-h))/(2*h)
    
    print(f"\nDerivadas por diferencias finitas de 3 puntos:")
    print(f"Adelante : {adelante:.6f}")
    print(f"Atrás : {atras:.6f}")
    print(f"Central : {central:.6f}")
    return

# derivada_tres_puntos(fx,x,h)

def derivada_cinco_puntos_adelante(fx, x, h):
    resultado = (-25*fx(x) + 48*fx(x+h) - 36*fx(x+2*h) + 16*fx(x+3*h) - 3*fx(x+4*h))/(12*h)
    print(f"\nDerivada de 5 puntos hacia adelante en x={x}: {resultado:.6f}")
    return resultado

# Ejemplo de uso
fx = lambda x: np.e**((x**2)+x)
h = 0.1
x = 1.1

derivada_cinco_puntos_adelante(fx, x, h)
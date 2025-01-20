import numpy as np

# Definimos las funciones
def f1(x, y):
    return (x-2)**2 + (y-1)**2 + x*y -3 

def f2(x, y):
    return x*np.e**(x+y) + y-3

# Definimos el Jacobiano
def jacobian(x, y):
    return np.array([[2*(x-2)+y, 2*(y-1)+x],
                     [x*np.e**(x+y)+np.e**(x+y) ,x*np.e**(x+y)+1 ]])


def newton_raphson_system(x0, y0, tol=0.0001, max_iter=100):
    x, y = x0, y0
    for i in range(max_iter):
        
        F = np.array([f1(x, y), f2(x, y)])
        J = jacobian(x, y)
        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("El Jacobiano no es invertible.")
            return None
        
        x, y = x + delta[0], y + delta[1]
        
        if np.linalg.norm(delta, ord=2) < tol:
            # print(f"Convergencia alcanzada en {i+1} iteraciones.")
            return x, y
    
    print("No se alcanzó la convergencia.")
    return None

x0, y0 = 0.5, 1 
sol1 = newton_raphson_system(x0, y0)

if sol1 is not None:
    x, y = sol1
    print(f"\nPrimera solución:")
    print(f"x = {x:.6f}")
    print(f"y = {y:.6f}")


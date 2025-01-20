import numpy as np










def f1(x, y):
    return x**2 + y**2 - 16
def f2(x, y):
    return x + y + 2
def jacobiana(x, y):
    return np.array([[2*x, 2*y],
                    [1, 1]])
def newton_raphson_sistema(x0, y0, tol=0.001, max_iter=100):
    x, y = x0, y0
    for i in range(max_iter):
        
        F = np.array([f1(x, y), f2(x, y)])
        J = jacobiana(x, y)
        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("El Jacobiano no es invertible.")
            return None
        
        x, y = x + delta[0], y + delta[1]
        
        if np.linalg.norm(delta, ord=2) < tol:
            return x, y
    print("No se alcanzó la convergencia.")
    return None
sol1 = newton_raphson_sistema(-4, 2)
sol2 = newton_raphson_sistema(1.60, -3.60)



if sol1 is not None:
    x1, y1 = sol1
    print("\nPrimera solución:")
    print(f"x = {x1:.6f}")
    print(f"y = {y1:.6f}")
if sol2 is not None:
    x2, y2 = sol2
    print("\nSegunda solución:")
    print(f"x = {x2:.6f}")
    print(f"y = {y2:.6f}")

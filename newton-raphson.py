import numpy as np
import math

# fx = lambda x :  (np.e ** -x) + x - 2
# fix = lambda x: (-np.e**-x) + 1 


fx =lambda x: x * math.cos(x + 1) + 4 #normal
fix = lambda x: math.cos(x + 1) - x * math.sin(x + 1) #derivada


error = lambda x2, x1: abs((x2-x1)/x2)
def newton_raphson(fx, fix, x0, t):
    x1 = x0 - (fx(x0)/fix(x0))
    if error(x1, x0) < t:
        return x1
    else:
        return newton_raphson(fx, fix , x1, t)
    
    
print(newton_raphson(fx, fix, 7, 0.001))
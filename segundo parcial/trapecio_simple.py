







import numpy as np





def error_relativo_porcentual (valorReal, valorAprox):
    return abs((valorReal - valorAprox)/valorReal)*100

def hh (a,b,N):
    return (b-a)/N

# fx = lambda x: 2*(x**3)-7*x+10
fx = lambda x: np.cos((np.sqrt(16-x**2))/x)

def trapecio(a,b,N,fx):
    h = hh(a,b,N)
    suma = 0
    for i in range(1,int(N)):
        suma += fx(a + i*h)
    return h/2*(fx(a) + 2*suma + fx(b))

a = -1.5
b = -1
N1 = 6
# N2 = 5
# N3 = 50
# N4 = 6 
valorReal = -0.46011

resultado1 = trapecio(a,b,N1,fx)
#resultado2 = trapecio(a,b,N2,fx)
print (f"Para {N1} {resultado1} error relativo porcentual: {error_relativo_porcentual(valorReal,resultado1)}%")
#print (f"Para N=5 {resultado2} error relativo porcentual: {error_relativo_porcentual(valorReal,resultado2)}%")

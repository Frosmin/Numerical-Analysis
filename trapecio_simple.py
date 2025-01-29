













def error_relativo_porcentual (valorReal, valorAprox):
    return abs((valorReal - valorAprox)/valorReal)*100
def hh (a,b,N):
    return (b-a)/N
fx = lambda x: 2*(x**3)-7*x+10
def trapecio(a,b,N,fx):
    h = hh(a,b,N)
    suma = 0
    for i in range(1,int(N)):
        suma += fx(a + i*h)
    return h/2*(fx(a) + 2*suma + fx(b))

a = -2
b = 0
N1 = 1
N2 = 5
N3 = 50
valorReal = 26

resultado1 = trapecio(a,b,N1,fx)
resultado2 = trapecio(a,b,N2,fx)
resultado3 = trapecio(a,b,N3,fx)
print (f"Para N=1 {resultado1} error relativo porcentual: {error_relativo_porcentual(valorReal,resultado1)}%")
print (f"Para N=5 {resultado2} error relativo porcentual: {error_relativo_porcentual(valorReal,resultado2)}%")
print (f"Para N=50 {resultado3} error relativo porcentual: {error_relativo_porcentual(valorReal,resultado3)}%")
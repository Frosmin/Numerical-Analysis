import math

ecuacion1 = lambda x, n : 2*x - n*x**2
xi = lambda n: 1/n

n = 3.9
x = 0.2
valor_verdadero = xi(n)

primero = x
segundo = ecuacion1(primero, n)

resultado = x
print("ejer 1 ---------------------------------------------------------------------------------------------")
while primero != segundo:
    primero = segundo
    segundo = ecuacion1(segundo, n) 
    print(segundo)

print(segundo)




##############################################################################################################
# xi2 = lambda n: math.sqrt(n)
# ecuacion2 = lambda x, n: 0.45*(x+n/x)

# n2 = 3
# x2 = 2
# EP = 0.000000012 
# valor_verdadero2 = xi2(n2)


# x0 = x2
# x1 = ecuacion2(x0, n2)


# resultado2 =  0


# print("ejer 2 ---------------------------------------------------------------------------------------------")
# while abs(x0 - x1) > EP:
#     x0 = x1
#     x1 = ecuacion2(x1, n2) 
#     print(x1)

# print(x1)





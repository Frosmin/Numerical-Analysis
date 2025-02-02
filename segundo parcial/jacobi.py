import numpy as np

def norma_unitaria(matriz):
    tam_columnas = len(matriz[0])
    tam_filas = len(matriz)
    mayor = 0
    for i in range(tam_columnas):
        suma =0
        for j in range (tam_filas):
            suma += abs(matriz[j][i])
        if suma > mayor:
            mayor = suma
    return mayor
   
    
#sumatoria de filas y sacar el maximo
def norma_infinita(matriz):
    tam_columnas = len(matriz[0])
    tam_filas = len(matriz)
    mayor = 0
    for i in range(tam_filas):
        suma = 0
        for j in range(tam_columnas):
            suma += abs(matriz[i][j])
        if suma > mayor:
            mayor = suma
    return mayor


def jacobi (x1,x2,x3,error):
    k = 0
    
    rx1 = 1
    rx2 = 1
    rx3 = 1
    
    rx1_anterior = 0
    rx2_anterior = 0
    rx3_anterior = 0
    while (abs(rx1 - rx1_anterior) + abs(rx2 - rx2_anterior) + abs(rx3 - rx3_anterior)) > error:
        rx1_anterior = rx1
        rx2_anterior = rx2
        rx3_anterior = rx3
        rx1_nuevo = x1(rx2,rx3)
        rx2_nuevo = x2(rx1,rx3)
        rx3_nuevo = x3(rx1,rx2)
        rx1 = rx1_nuevo
        rx2 = rx2_nuevo
        rx3 = rx3_nuevo
        k += 1
        
    print(f"\nResultados:\nx1 = {rx1}\nx2 = {rx2}\nx3 = {rx3}")
x1 = lambda x2, x3 : 1/5*(5 + 3*x2 - x3)
x2 = lambda x1, x3 : 1/4*(6 - 2*x1 + x3)
x3 = lambda x1, x2 : 1/8*(4 - 2*x1 + 3*x2)
error= 0.009




jacobi(x1,x2,x3,error)

# Sistema de ecuaciones:
# 2x + 4y - 1z = 6
# 5x - 3y + 1z = 5
# 2x - 3y + 8z = 4


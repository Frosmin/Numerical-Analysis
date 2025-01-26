import numpy as np 

#[columna][fila]


def matriz_inversa(matriz):
    # Verificar matriz cuadrada
    n = len(matriz)
    if n != len(matriz[0]):
        return None
        
    # Crear matriz aumentada [A|I]
    aumentada = []
    for i in range(n):
        fila = matriz[i].copy()
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        aumentada.append(fila)
    
    # Aplicar Gauss-Jordan
    for i in range(n):
        pivote = aumentada[i][i]
        if pivote == 0:
            return None
        for j in range(2*n):
            aumentada[i][j] /= pivote
            
        for k in range(n):
            if k != i:
                factor = aumentada[k][i]
                for j in range(2*n):
                    aumentada[k][j] -= factor * aumentada[i][j]
    
    # Extraer inversa
    inversa = []
    for i in range(n):
        inversa.append(aumentada[i][n:])
    return inversa




#sumatoria de columnas y sacar el maximo
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


def condicion(norma_normal , norma_inversa):
    return norma_normal * norma_inversa


matriz= [[1, 1/2, 1/3],
         [1/4, 1/5, 1/6],
         [1/7, 1/8, 1/9]]



inv = matriz_inversa(matriz)
# if inv is None:
#     print("La matriz no tiene inversa")
# else:
#     print("\nMatriz inversa:")
#     for fila in inv:
#         print([round(x, 4) for x in fila])
    
 
print(norma_unitaria(matriz))
print(norma_unitaria(inv))

print(norma_infinita(matriz))
print(norma_infinita(inv))


    


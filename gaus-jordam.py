import numpy as np 

def imprimir_matriz(matriz):
    for fila in matriz:
        print([round(x, 4) for x in fila])

def gauss_jordan(matriz):
    n = len(matriz)
    
    for i in range(n):
        pivote = matriz[i][i]
        for j in range(n + 1):
            matriz[i][j] = matriz[i][j] / pivote
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n + 1):
                    matriz[k][j] -= factor * matriz[i][j]
    
    return matriz

def obtener_matriz_solucion(matriz):
    n = len(matriz)
    solucion = [[0] for _ in range(n)]
    for i in range(n):
        solucion[i][0] = matriz[i][-1]
    return solucion

matriz2 = [[4,2,5,18],
           [2,5,8,27.3],
           [2,4,3,16.20]]

print("Matriz aumentada original:")
imprimir_matriz(matriz2)

solucion = gauss_jordan(matriz2)
print("\nMatriz después de Gauss-Jordan:")
imprimir_matriz(solucion)

print("\nMatriz de solución:")
matriz_solucion = obtener_matriz_solucion(solucion)
imprimir_matriz(matriz_solucion)


#ejemplo
matriz = [
    [2, 1, 5],  # 2x + y = 5
    [3, 4, 6]   # 3x + 4y = 6
]
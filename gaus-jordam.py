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



matriz2 = [[4,2,5,18],
           [2,5,8,27.3],
           [2,4,3,16.20]]

solucion = gauss_jordan(matriz2)
imprimir_matriz(matriz2)

print("\nSolución del sistema:")
for i in range(len(matriz2)):
    print(f"x{i+1} = {round(solucion[i][-1], 4)}")


#ejemplo
matriz = [
    [2, 1, 5],  # 2x + y = 5
    [3, 4, 6]   # 3x + 4y = 6
]
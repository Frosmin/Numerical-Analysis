import numpy as np 

#[columna][fila]



def matriz_inversa(matriz):
    # Verificar matriz cuadrada
    n = len(matriz)
    if n != len(matriz[0]):
        return "La matriz debe ser cuadrada"
        
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
        # Hacer pivote = 1
        pivote = aumentada[i][i]
        if pivote == 0:
            return "La matriz no tiene inversa"
        for j in range(2*n):
            aumentada[i][j] /= pivote
            
        # Hacer ceros en columna
        for k in range(n):
            if k != i:
                factor = aumentada[k][i]
                for j in range(2*n):
                    aumentada[k][j] -= factor * aumentada[i][j]
    
    # Extraer inversa (mitad derecha)
    inversa = []
    for i in range(n):
        inversa.append(aumentada[i][n:])
        
    return inversa


matriz= [[1,2,3,],
         [0,0,7],
         ]

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
   
    
    
print(norma_unitaria(matriz))


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

print(norma_infinita(matriz))
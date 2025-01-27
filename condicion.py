import numpy as np 

#[columna][fila]


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

#ejemplo
matriz = [
    [2, 1, 5],  # 2x + y = 5
    [3, 4, 6]   # 3x + 4y = 6
]


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


def error_de_matriz(matriz, matriz_con_error):
     # Calcula la diferencia entre matrices
    matriz_error = np.subtract(matriz, matriz_con_error)
    return matriz_error



matriz= [[1, 1/2, 1/3],
         [1/4, 1/5, 1/6],
         [1/7, 1/8, 1/9]]

matriz_con_error = [[0.9, 1/2, 1/3],
                     [1/4, 1/5, 1/6],
                     [1/7, 1/8, 1/9]]






inv = matriz_inversa(matriz)
# if inv is None:
#     print("La matriz no tiene inversa")
# else:
#     print("\nMatriz inversa:")
#     for fila in inv:
#         print([round(x, 4) for x in fila])
    
    
norma_normal_unitaria = norma_unitaria(matriz)
norma_inversa_unitaria = norma_unitaria(inv)

norma_normal_infinita = norma_infinita(matriz)
norma_inversa_infinita = norma_infinita(inv)

# print(norma_unitaria(matriz))
# print(norma_unitaria(inv))

# print(norma_infinita(matriz))
# print(norma_infinita(inv))



    # condicion
condicion_unitaria = condicion(norma_normal_unitaria, norma_inversa_unitaria)
condicion_infinita = condicion(norma_normal_infinita, norma_inversa_infinita)
print ("Condicion unitaria normal")
print(condicion_unitaria)
print ("Condicion infinita normal")
print(condicion_infinita)

    #error
error_matriz = error_de_matriz(matriz, matriz_con_error)
#print (error_matriz)
error_relativo_unitario =  norma_unitaria(error_matriz)/norma_unitaria(matriz)
error_relativo_infinita =  norma_infinita(error_matriz)/norma_infinita(matriz)

# print("error relativo unitario")
# print(error_relativo_unitario)
# print("error relativo infinita")
# print(error_relativo_infinita)


cota_unitaria = condicion_unitaria * error_relativo_unitario
cota_infiinta = condicion_infinita * error_relativo_infinita
print ("cota unitaria para el error en la solucion:")
print(f"{cota_unitaria*100}%")   
print ("cota infinita para el error en la solucion:") 
print(f"{cota_infiinta*100}%")





#determinar el error relativo de la solucion y compararlo con el error relativo de la matriz de coeficientes del sistema
matriz = [
    [2, 1, 5],  # 2x + y = 5
    [3, 4, 6]   # 3x + 4y = 6
]
sistema = [[1, 1/2, 1/3, 4],
         [1/4, 1/5, 1/6, 5],
         [1/7, 1/8, 1/9, 6]]

sistema_modificado =   [[0.9, 1/2, 1/3, 4],
                    [1/4, 1/5, 1/6, 5],
                    [1/7, 1/8, 1/9, 6]]

Ax =obtener_matriz_solucion(gauss_jordan(sistema))
# print(Ax)

Ax_modificado = obtener_matriz_solucion(gauss_jordan(sistema_modificado))
# print(Ax_modificado)

error_solucion = error_de_matriz(Ax_modificado,Ax )



print("Norma del error relativo de la solucion unitaria y infinita:")
#norma error relativo de la solucion
erro_relativo_solucion_unitaria = norma_unitaria(error_solucion)/norma_unitaria(Ax_modificado)
print(f"{erro_relativo_solucion_unitaria*100}%")
error_realtivo_solucion_infinita = norma_infinita(error_solucion)/norma_infinita(Ax_modificado) 
print(f"{error_realtivo_solucion_infinita*100}%")

print("Norma del error relativo de la matriz coeficientes")
print(f"{error_relativo_unitario*100}%")
print(f"{error_relativo_infinita*100}%")

print("sistema mal condicionado")
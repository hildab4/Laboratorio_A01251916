import numpy as np
import cv2
import matplotlib.pyplot as plt

#mat = np.matrix('1 2 3 4 5 6; 7 8 9 10 11 12; 0 0 1 16 17 18; 0 1 0 7 23 24; 1 7 6 5 4 3')
#kernel = np.matrix('1 1 1; 0 0 0; 2 10 3')

def convolucion (mat, kernel):
    #Convierte ambas entradas a matrices con ayuda de numpy
    mat = np.matrix(mat)
    kernel = np.matrix(kernel)
    #Obtiene las dimensiones de la matriz resultante
    row = (np.shape(mat)[0] - (np.shape(kernel)[0]/2) * 2) + 1
    col = (np.shape(mat)[1] - (np.shape(kernel)[1]/2) * 2) + 1
    
    #Crea la matriz resultante, con valores de cero
    final = np.zeros((int(row), int(col)), dtype = int)

    #Se inicializan ambos ciclos for
    num1 = 0
    for i in range (np.shape(mat)[0] - np.shape(kernel)[0] + 1):
        for j in range (np.shape(mat)[1] - np.shape(kernel)[1] + 1):
            #Se obtiene la matriz del producto punto
            num1 += np.multiply((mat[i:i + (np.shape(kernel)[0]),
                                     j:j + (np.shape(kernel)[1])]), kernel)
            #Se coloca la suma de estos valores en la matriz resultante
            final[i][j] = num1.sum()
            #Se le asigna el valor de cero a la variable, para repetir el proceso
            num1 = 0
    #Se imprime la matriz resultante
    print(final)

#Pide al usuario la matriz original y el filtro a aplicar
mat = input('Matriz 1')
kernel = input('Filtro')
#Llama a la función, mandando ambas matrices
convolucion(mat, kernel)
        
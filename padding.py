#Importar librerías
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

#Dimensiones de la matriz de la imagen 920x1900

def padding (mat, rows, cols):
    #Convertir la lista de listas a matriz con numpy
    mat = np.matrix(mat)
    #Cantidad de renglones y columnas más que la matriz original
    m = math.floor((rows - np.shape(mat)[0]) / 2)
    n = math.floor((cols - np.shape(mat)[1]) / 2)
    
    #Se genera la matriz final con las dimensiones especificadas
    final = np.zeros((rows, cols))
    
    #Se inicia el ciclo for
    for i in range (np.shape(mat)[0]):
        for j in range (np.shape(mat)[1]):
            #Se suma m y n para ignorar ciertos renglones y columnas
            final[i + m][j + n] = mat[i, j]
    #Se imprime la matriz final
    print(final)
    plt.imshow(final, cmap='gray')
    plt.title("Imagen con Padding")
    plt.show()
    
#Pedir la matriz original (imagen), y las dimensiones de la matriz solicitada
imagen = input('Nombre archivo ')
img = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
rows = int(input('Filas '))
cols = int(input('Columnas '))
#Llamar la función padding, mandando la matriz y las dimensiones 
padding(img, rows, cols)
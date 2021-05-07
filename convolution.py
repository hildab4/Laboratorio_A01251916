#Importar librerías
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Nombre archivo = foto.jpg
#Filtro = [[-1 0 1]; [-2 0 2]; [-1 0 1]] y edge
#Filtro = [[-1 -2 -1]; [0 0 0]; [1 2 1]] x edge
#Filtro = [[-1 -1 -1]; [-1 8 -1]; [-1 -1 -1]] edge

def convolucion (img, kernel):
    #Convierte ambas entradas a matrices con ayuda de numpy
    mat = np.matrix(img)
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
    plt.imshow(final, cmap='gray')
    plt.title("Imagen usando Kernel")
    plt.show()

#Pide al usuario la matriz original (imagen) y el filtro a aplicar
imagen = input('Nombre archivo ')
img = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
kernel = input('Filtro ')
#Llama a la función, mandando ambas matrices
convolucion(img, kernel)
        
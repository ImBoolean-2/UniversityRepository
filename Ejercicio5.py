# Crear un código en Python para que permita juntar segmentar la imagen (Manzana.jpg) que se encuentra en la carpeta drive proporcionada en clase.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargamos la imagen
image = cv2.imread('resources/Manzana.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Gaussiano para reducir el ruido
image = cv2.GaussianBlur(image, (5, 5), 0)

# Detectar los bordes usando Canny
edges = cv2.Canny(image, threshold1=30, threshold2=100)

# Crear una máscara con los bordes detectados
mask = np.zeros_like(image)
mask[edges > 0] = 255

# Aplicar la máscara a la imagen original
segmented = cv2.bitwise_and(image, image, mask=mask)

# Guardar la imagen segmentada
cv2.imwrite('result/Manzana_resultado.jpg', segmented)

print ("")
print("✅ Imagen segmentada correctamente | 💾 Guardada en result")
print ("")

plt.imshow(segmented)
plt.show()
# https://programacionpython80889555.wordpress.com/2021/05/18/eliminar-fondo-de-una-imagen-en-python-con-opencv/
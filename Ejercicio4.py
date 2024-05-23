# Ejercicio 4 Crear un código en Python para que permita juntar las imágenes “Abrazo 1.jpg” y Abrazo 1.jpg” que se encuentran en la carpeta drive proporcionada en clase.

from PIL import Image
import matplotlib.pyplot as plt

## Abrimos las 2 imagenes usando la lbreria pillow desde resources
image1 = Image.open('resources/Abrazo 1.jpg')
image2 = Image.open('resources/Abrazo 2.jpg')

## Le asignamos el doble de ancho para que quepan los 2
nueva_img = Image.new('RGB', (image1.width + image2.width, image1.height))

## En esta nueva imagen Asignamos las posiciones en las cuales las vamos a pegar
nueva_img.paste(image1, (0, 0))
nueva_img.paste(image2, (image1.width, 0))

## La guardamos en la carpeta Result
nueva_img.save('result/joined_abrazos.jpg')

print ("")
print("✅ Imagen segmentada correctamente | 💾 Guardada en result")
print ("")
plt.imshow(nueva_img)
plt.show()
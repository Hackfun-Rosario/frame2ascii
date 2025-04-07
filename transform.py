#-*- encoding: utf8 -*-
import numpy as np
from PIL import Image
from os import listdir as ls

## los directorios como constantes
FRAMESDIR = "frames"
OUTPUT = "transformed"
# levantamos la lista como nombres de archivos (para debug basta con hacer print)
framelist = ls(FRAMESDIR) 

## estos son los simbolos utilizados
## 
sym = "•|+#&?$@%"
SYMLEN = len(sym)

# iteramos por cada archivo
for filename in framelist:
  # with se encarga de abrir y cerrar cada archivo automáticamente
  with Image.open(f'{FRAMESDIR}/{filename}') as frame:
    # convertimos la imagen a un array de numpy.
    # se usan valores flotantes y no enteros para normalizar después
    # la matriz tiene forma: [ [ [] * 3 canales ] * ancho ] * altura
    img = np.array(frame, dtype="float").reshape(frame.height, frame.width, 3)

    # reducimos el array tomando uno de cada 20 elementos vertical y 10 horizontalmente
    # (el formato de filtro es [inicio:fin:pasos])
    # y dejamos el valor del verde (1)
    array_reducido = img[::20, ::10, 1]

    # como convertimos de RGB a GRIS dividimos por el rango más alto (255)
    # que tiene cada canal de color, nos quedan valores entre 0 y 1.0 (normalización)
    array_reducido /= 255
    # multiplicamos cada valor por el número de símbolos a utilizar
    array_reducido *= SYMLEN

    # giardamos la matriz generada como un texto con saltos de línea
    text = ""

    # convertimos el tipo del array a unsigned integer de 8 bits (redondea y evitamos los decimales)
    # guardamos cada línea horizontal como línea de texto
    for l in array_reducido.astype("uint8"):
      text += "".join([sym[_] for _ in l]) + "\n"

  ## salimos de la iteración y guardamos el archivo de texto con el mismo nombre más ".txt" al final
  with open(f'{OUTPUT}/{filename}.txt', 'a') as f:
    f.write(text)

print("se acabó lo que se-daba, dijo el anestesista")
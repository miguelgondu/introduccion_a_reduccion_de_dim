from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargando la imagen como un arreglo de numpy.
img = np.asarray(Image.open("butterfly.jpg"))

# Imprimiendo sus contenidos y tamaño.
print(img)
print(img.shape)

# Graficándola usando matplotlib.
# plt.imshow(img)
# plt.show()

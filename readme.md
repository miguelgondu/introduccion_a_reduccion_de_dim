# Una pequeña introducción a la reducción de la dimensionalidad usando scikit-learn y numpy.

Este repositorio contiene el código de la pequeña introducción a la reducción de la dimensionalidad, usado en una presentación para *Manizales codes in Python* que puedes ver [aquí]().

Una versión en PDF de las diapositivas se puede encontrar en este repositorio también bajo `slides.pdf`.

## Prerequisitos

Para correr el código, te recomiendo crear un ambiente nuevo (Python >= 3.9) y correr

```
pip install numpy matplotlib sklearn
```

## El código

En `utils.py` puedes encontrar una función `load_dataset() -> np.ndarray` que carga un conjunto de datos compuesto por los dígitos 1 de la base de datos MNIST. Para descargarlos, sigue el link en la documentación.

## Referencias de la presentación
- base de datos del museo de historia natural: https://data.nhm.ac.uk/dataset/collection-specimens/resource/05ff2255-c38a-40c9-b657-4ccb55ab2feb?view_id=6ba121d1-da26-4ee1-81fa-7da11e68f68e&filters=project%3Apapilionoidea+new+types+digitisation+project
- El blog de Marian: https://marian42.de/
- El paper de Isomap: https://wearables.cc.gatech.edu/paper_of_week/isomap.pdf
- La base de datos usada en el código: MNIST, downloaded using Keras from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

## Más recursos sobre reducción de la dimensionalidad
- Charla de Leland McInnes sobre R.D. https://youtu.be/9iol3Lk6kyU
- Capítulo 10 de Mathematics for Machine Learning. https://mml-book.github.io/book/mml-book.pdf
- Capítulo 12 del Bishop. https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/

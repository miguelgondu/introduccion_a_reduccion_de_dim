"""
Data and plotting utilities.
"""
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.axes import Axes


def load_dataset(only_one: bool = True) -> np.ndarray:
    """
    Returns the images depicting digit 1
    of the MNIST dataset.

    Where to download mnist.npz:
    https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
    """

    arr = np.load("mnist.npz")
    digits = arr["x_train"]
    classes = arr["y_train"]

    if only_one:
        data = digits[classes == 1]
    else:
        data = digits

    return data


def plot_images(z: np.ndarray, images: np.ndarray, ax: Axes):
    """
    A function that plots all images in {images}
    at coordinates {z}.

    Some black magic for better scatterplots.

    Taken and adapted from:
    https://stackoverflow.com/questions/59373626/matplotlib-scatter-different-images-mnist-instead-of-plots-for-tsne
    """
    for zi, img in zip(z, images):
        im = OffsetImage(img, zoom=0.5)
        ab = AnnotationBbox(im, zi, xycoords="data", frameon=False)
        ax.add_artist(ab)
        ax.update_datalim([zi])
        ax.autoscale()

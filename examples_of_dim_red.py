"""
In this script we test reducing the dimensionality of
the MNIST images of the digit 1.
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from utils import plot_images, load_dataset


def fit_a_PCA_and_show():
    """
    Fits a PCA to MNIST images of the digit 1.
    """
    imgs = load_dataset()
    random_indxs = np.random.permutation(len(imgs))
    subsampled_imgs = imgs[random_indxs[:1000]]

    pca = PCA(n_components=2)
    latent_codes = pca.fit_transform(subsampled_imgs.reshape(-1, 28 * 28))

    _, ax = plt.subplots(1, 1)
    plot_images(latent_codes, imgs, ax)
    plt.show()


def fit_a_TSNE_and_show():
    """
    Fits t-SNE to MNIST images of the digit 1.
    """
    # Load the images
    imgs = load_dataset()

    # Get a subsample of 1000 images
    # chosen at random.
    random_indxs = np.random.permutation(len(imgs))
    subsampled_imgs = imgs[random_indxs[:1000]]

    tsne = TSNE(n_components=2)
    latent_codes = tsne.fit_transform(subsampled_imgs.reshape(-1, 28 * 28))

    _, ax = plt.subplots(1, 1)
    plot_images(latent_codes, imgs, ax)
    plt.show()
    pass


if __name__ == "__main__":
    # fit_a_PCA_and_show()
    fit_a_TSNE_and_show()

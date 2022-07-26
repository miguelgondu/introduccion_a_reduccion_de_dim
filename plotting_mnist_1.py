"""
In this script we implement a visualization
of the first 36 images of the digit 1 in MNIST.
"""

import matplotlib.pyplot as plt

from utils import load_dataset

def plot_examples():
    imgs = load_dataset()

    fig, axes = plt.subplots(6, 6)
    for img, ax in zip(imgs, axes.flatten()):
        ax.imshow(img)
        ax.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_examples()

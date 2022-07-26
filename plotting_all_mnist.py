import matplotlib.pyplot as plt

from utils import load_dataset


def plot_examples():
    imgs = load_dataset(only_one=False)

    fig, axes = plt.subplots(6, 6)
    for img, ax in zip(imgs, axes.flatten()):
        ax.imshow(img)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_examples()

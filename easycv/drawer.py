import matplotlib.pyplot as plt
from .image import Image
from .utils import *

class ImageDrawer:
    @staticmethod
    def show(imgs: list[Image], figsize: tuple = (10,10)):
        img_cnt = len(imgs)
        assert img_cnt > 0, 'No images to show.'
        assert len(figsize) == 2, 'figsize must has two elements.'
        a, b = number_decompose_closest(img_cnt)

        _, axes = plt.subplots(nrows=b, ncols=a, figsize=figsize)

        axes = axes.flatten()

        for i, ax in enumerate(axes):
            if i < img_cnt:
                if imgs[i]._image_type == 'rgb':
                    ax.imshow(imgs[i].pixels.transpose(1,2,0))
                elif imgs[i]._image_type == 'grayscale':
                    ax.imshow(imgs[i].pixels.squeeze(), cmap='gray', vmin=0, vmax=255)
                # Turn off the axis showing.
                ax.axis('off')
                ax.set_title(imgs[i].image_name)
            else:
                ax.axis('off')
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def show_pdf(images: list[Image], figsize=(10,10)):
        img_cnt = len(images)
        assert img_cnt > 0, 'No images to show.'
        assert len(figsize) == 2, 'figsize must has two elements.'
        a, b = number_decompose_closest(img_cnt)

        _, axes = plt.subplots(nrows=b, ncols=a, figsize=figsize)
        axes = axes.flatten()

        for i, ax in enumerate(axes):
            if i < img_cnt:
                histograms = images[i].PDF
                x = range(256)
                if images[i]._image_type == 'rgb':
                    colors = ['red', 'green', 'blue']
                    for ch, color in zip(histograms, colors):
                        ax.plot(x, ch, color=color, alpha=0.7)
                elif images[i]._image_type == 'grayscale':
                    ax.plot(x, histograms[0], color='black')
                ax.set_title(images[i].image_name)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show_cdf(images: list[Image], figsize=(10,10)):
        img_cnt = len(images)
        assert img_cnt > 0, 'No images to show.'
        assert len(figsize) == 2, 'figsize must has two elements.'
        a, b = number_decompose_closest(img_cnt)

        fig, axes = plt.subplots(nrows=b, ncols=a, figsize=figsize)
        axes = axes.flatten()

        for i, ax in enumerate(axes):
            if i < img_cnt:
                histograms = images[i].CDF
                x = range(256)
                if images[i]._image_type == 'rgb':
                    colors = ['red', 'green', 'blue']
                    for ch, color in zip(histograms, colors):
                        ax.plot(x, ch, color=color, alpha=0.7)
                elif images[i]._image_type == 'grayscale':
                    ax.plot(x, histograms[0], color='black')
                ax.set_title(images[i].image_name)
        plt.tight_layout()
        plt.show()
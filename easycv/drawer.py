import matplotlib.pyplot as plt
from .image import Image
from .utils import *
class ImageDrawer:
    def __init__(self):
        pass

    def show(self, imgs: list[Image], figsize: tuple = (10,10)):
        img_cnt = len(imgs)
        assert img_cnt > 0, 'No images to show.'
        assert len(figsize) == 2, 'figsize must has two element.'
        a, b = number_decompose_closest(img_cnt)

        fig, axes = plt.subplots(nrows=b, ncols=a, figsize=figsize)

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
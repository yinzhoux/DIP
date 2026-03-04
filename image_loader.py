from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt
class Image:
    def __init__(self, image_path: str, image_type: str):
        '''
        Initialize a Image object.
        Parameters:
            @image_path: Path of the image to load.
            @image_type: Type of the image to load ('rgb' or 'grey').
        '''
        self._image_type = image_type

        img = pig.open(image_path)
        self._bands = img.getbands()
        
        if image_type == 'rgb':
            assert self.bands_cnt == 3
            self.pixels = np.array(img.convert('RGB'))
        elif image_type == "gray":
            assert self.bands_cnt == 1
            raise NotImplementedError

    def show(self):
        '''
        Show the image with matplot library.
        '''
        plt.imshow(self.pixels)
        # Turn off the axis showing.
        plt.axis('off')
        plt.show()

    def save_to(self, path_to_save: str):
        '''
        Save image file.
        Parameters:
            @path_to_save: Path to save the image file.
        '''
        plt.imsave(path_to_save)

    @property
    def size(self):
        '''
        Size of the image.
        Return:
            [Height, Width].
        '''
        return self.pixels.shape[:2]
    @property
    def type(self):
        '''
        Type of the image.('rgb' or 'grey')
        '''
        return self._image_type
    @property
    def bands_cnt(self):
        '''
        Number of bands of the image.
        '''
        return len(self._bands)
    @property
    def bands(self):
        '''
        Band names of the image.
        Example:
            If the image has the type of 'rgb', this property will be ['R', 'G', 'B'].
        '''
        return self._bands
from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt
from .point_op import translation
from copy import deepcopy
class Image:
    def __init__(self):
        self.inited = False

    def from_file(self, image_path: str, image_type: str):
        '''
        Initialize a Image object with file.
        Parameters:
            @image_path: Path of the image to load.
            @image_type: Type of the image to load ('rgb' or 'grey').
        '''

        img = pig.open(image_path)
        self._bands = img.getbands()
        
        if image_type == 'rgb':
            assert self.bands_cnt == 3
            self.pixels = np.array(img.convert('RGB')).transpose(2, 0, 1)
        elif image_type == "grey":
            assert self.bands_cnt == 1
            raise NotImplementedError

        self._image_type = image_type
        self.inited = True

    def from_array(self, pixels: np.ndarray, image_type: str):
        assert pixels.ndim == 3, 'pixels must has the shape [height, width, band]'

        if image_type == 'rgb':
            assert pixels.shape[2] == 3, "rgb image must has three bands"
            self.pixels = pixels.transpose(2, 0, 1)
            self.pixels.transpose(2, 0, 1)
            self._bands = ['R', 'G', 'B']
        elif image_type == 'grey':
            assert pixels.shape[0] == 1, "greyband image must has one band"
            self.pixels = pixels
            self._bands = ['Brightness']
        
        self._image_type = image_type
        self.inited = True

    def show(self):
        '''
        Show the image with matplot library.
        '''
        plt.imshow(self.pixels.transpose(1,2,0))
        # Turn off the axis showing.
        plt.axis('off')
        plt.show()

    def save_to(self, path_to_save: str):
        '''
        Save image file.
        Parameters:
            @path_to_save: Path to save the image file.
        '''
        plt.imsave(path_to_save, self.pixels.transpose(1,2,0))

    def translation_band(self, band: str, delta: int):
        assert band in self._bands, f'band {band} not exists.'
        band_id = self._bands.index(band)
        new_image = deepcopy(self)
        new_image.pixels[band_id] = translation(new_image.pixels[band_id], delta)
        return new_image
    
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
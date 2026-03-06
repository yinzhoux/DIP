from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt
from .point_op import translation, rotation
from copy import deepcopy
class Image:
    def __init__(self):
        self.inited = False

    def from_file(self, image_path: str, image_type: str):
        '''
        Initialize a Image object with file.
        Parameters:
            @image_path: Path of the image to load.
            @image_type: Type of the image to load ('rgb' or 'grayscale').
        '''

        img = pig.open(image_path)
        self._bands = img.getbands()
        
        if image_type == 'rgb':
            assert self.bands_cnt == 3
            self.pixels = np.array(img.convert('RGB')).transpose(2, 0, 1)
        elif image_type == "grayscale":
            assert self.bands_cnt == 1
            raise NotImplementedError

        self._image_type = image_type
        self.inited = True

    def from_array(self, pixels: np.ndarray, image_type: str):
        assert pixels.ndim == 3, 'pixels must has the shape [height, width, band]'

        if image_type == 'rgb':
            assert pixels.shape[2] == 3, "rgb image must has three bands"
            self.pixels = pixels.transpose(2, 0, 1)
            self._bands = ['R', 'G', 'B']
        elif image_type == 'grayscale':
            assert pixels.shape[0] == 1, "grayband image must has one band"
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

    def save_to(self, path_to_save: str, convert_to_grayscale: bool = False):
        '''
        Save image file.
        Parameters:
            @path_to_save: Path to save the image file.
            @convert_to_grayscale: If original image is RGB, save the grayscale
                image if True.
        '''
        if self._image_type == 'rgb':
            if not convert_to_grayscale:
                plt.imsave(path_to_save, self.pixels.transpose(1,2,0))
            else:
                plt.imsave(path_to_save, self.pixels.transpose(1,2,0).mean(axis=2), cmap='gray', vmin=0, vmax=255)
        elif self._image_type == 'grayscale':
            plt.imsave(path_to_save, self.pixels.transpose(1,2,0).squeeze())

    def save_pixels_to(self, path_to_save: str, convert_to_grayscale: bool = False):
        '''
        Save image pixels file.
        Parameters:
            @path_to_save: Path to save the image file.
            @convert_to_grayscale: If original image is RGB, save the grayscale
                image if True.
        '''
        if self._image_type == 'rgb':
            if not convert_to_grayscale:
                np.save(path_to_save, self.pixels.transpose(1,2,0))
            else:
                np.save(path_to_save, self.pixels.transpose(1,2,0).mean(axis=2))
        elif self._image_type == 'grayscale':
            np.save(path_to_save, self.pixels.transpose(1,2,0).squeeze())


    def translation_band(self, band: str, delta: int):
        '''
        Translate band curve.
        Parameters:
            @band: Band to translate. For RGB image, it's element in
                   ['R', 'G', 'B'].
            @delta: value of translation. Must between -255~255.\
        Return:
            New image after translation.
        '''
        assert delta >= -255 and delta <= 255, 'delta must between -255~255.'
        assert band in self._bands, f'band {band} not exists.'
        band_id = self._bands.index(band)
        new_image = deepcopy(self)
        new_image.pixels[band_id] = translation(new_image.pixels[band_id], delta)
        return new_image
    
    def rotation_band(self, band: str, fix: int, slope: float):
        '''
        Rotate band curve.
        Parameters:
            @band: Band to rotate. For RGB image, it's element in
                   ['R', 'G', 'B'].
            @fix: Fixed point value when rotating.
            @slope: Slope value of rotating.
        '''
        assert band in self._bands, f'band {band} not exists.'
        # it's ok that fix value out of range(0, 255).
        
        band_id = self._bands.index(band)
        new_image = deepcopy(self)
        new_image.pixels[band_id] = rotation(new_image.pixels[band_id], fix, slope)
        return new_image
    
    def brightness_edit(self, delta: int):
        '''
        Increase or decrease brightness.
        Parameters: 
            @delta: value of translation. Must between -255~255.
        Return:
            New image after brightness editing.
        '''
        assert delta >= -255 and delta <= 255, 'delta must between -255~255.'
        
        new_img = deepcopy(self)
        for band in self.bands:
            new_img = new_img.translation_band(band, delta)
        return new_img
    
    def contrast_edit(self, fix: int, slope: float):
        '''
        Increase or decrease contrast.
        Parameters:
            @fix: Fixed point value when rotating.
            @slope: Slope value of rotating.
        '''
        new_img = deepcopy(self)
        for band in self.bands:
            new_img = new_img.rotation_band(band, fix, slope)
        return new_img
        
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
        Type of the image.('rgb' or 'gray')
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
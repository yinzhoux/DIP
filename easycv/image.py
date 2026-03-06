from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt
class Image:
    def __init__(self):
        self.inited = False

    def from_file(self, image_path: str, image_type: str, image_name: str = None):
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
        if image_name == None:
            self.image_name = image_path
        else:
            self.image_name = image_name

    def from_array(self, pixels: np.ndarray, image_type: str, image_name: str = None):
        assert pixels.ndim == 3, 'pixels must has the shape [height, width, band]'

        if image_type == 'rgb':
            assert pixels.shape[2] == 3, "rgb image must has three bands"
            self.pixels = pixels.transpose(2, 0, 1)
            self._bands = ['R', 'G', 'B']
        elif image_type == 'grayscale':
            assert pixels.shape[2] == 1, "grayscale image must has one band"
            self.pixels = pixels.transpose(2, 0, 1)
            self._bands = ['Brightness']
        
        self._image_type = image_type
        self.inited = True
        if image_name == None:
            self.image_name = 'image_from_pixels'
        else:
            self.image_name = image_name


    def show(self):
        '''
        Show the image with matplot library.
        '''
        if self._image_type == 'rgb':
            plt.imshow(self.pixels.transpose(1,2,0))
        elif self._image_type == 'grayscale':
            plt.imshow(self.pixels.squeeze(), cmap='gray', vmin=0, vmax=255)
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
            plt.imsave(path_to_save, self.pixels.transpose(1,2,0).squeeze(), cmap='gray', vmin=0, vmax=255)

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

#region property
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
        Type of the image.('rgb' or 'grayscale')
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
#endregion property
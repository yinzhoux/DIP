from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt
class Image:
    inited = False
    __pdf__ = None
    __cdf__ = None

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
            self.pixels = np.array(img.convert('RGB')).transpose(2, 0, 1).clip(max=255, min=0)
        elif image_type == "grayscale":
            assert self.bands_cnt == 1
            self.pixels = np.array(img.convert(mode='L')).clip(max=255, min=0)

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
                img = pig.fromarray(self.pixels.transpose(1,2,0))
                img.save(path_to_save)
            else:
                img = pig.fromarray(self.pixels.transpose(1,2,0).mean(axis=2).astype(np.uint8), mode='L')
                img.save(path_to_save)

        elif self._image_type == 'grayscale':
            img = pig.fromarray(self.pixels, mode='L')
            img.save(path_to_save)

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

    def to_grayscale(self):
        '''
        Convert the image to grayscale image.
        @Return:
            Image with type of grayscale.
        '''
        pixels = np.mean(self.pixels, axis=0, keepdims=True)
        new_img = Image()
        new_img.from_array(pixels.transpose((1,2,0)), image_type='grayscale', image_name=self.image_name+'-grayscale')

        return new_img

#region property
    @property
    def size(self):
        '''
        Size of the image.
        Return:
            [Height, Width].
        '''
        return self.pixels.shape[1:]
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
            For grayscale image, the property will be ['Brightness']
        '''
        return self._bands
    
    @property
    def PDF(self):
        '''
        Get the histogram of all the bands of the image.
        '''
        assert self.inited, 'Image not initialized.'
        self.__pdf__ = []
        for band_id in range(self.bands_cnt):
            histo, _ = np.histogram(self.pixels[band_id], bins=256, range=(0,256))
            histo = histo.astype(np.float32) / (np.sum(histo))
            self.__pdf__.append(histo)
        self.__pdf__ = np.array(self.__pdf__)

        return self.__pdf__
    
    @property
    def CDF(self):
        '''
        Get the cumulative density function of the image pixel values. 
        '''
        assert self.inited, 'Image not initialized.'
        mask = np.tri(256, 256, dtype=np.float32)
        mask = np.transpose(mask)
        self.__cdf__ = self.PDF @ mask

        return self.__cdf__
#endregion property
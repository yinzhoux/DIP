from PIL import Image as pig
import numpy as np
from matplotlib import pyplot as plt

def from_file(image_path: str, image_name: str = None):
    '''
    Initialize a Image object with file.
    Parameters:
        @image_path: Path of the image to load.
        @image_type: Type of the image to load ('rgb' or 'grayscale').
    '''
    img = pig.open(image_path)

    if len(img.getbands()) == 3:
        return from_array(np.array(img.convert('RGB')).clip(max=255, min=0), image_type='rgb', image_name=image_path)
    elif len(img.getbands()) == 1:
        return from_array(np.array(img.convert(mode='L')).clip(max=255, min=0), image_type='grayscale', image_name=image_path)

def from_array(pixels: np.ndarray, image_type: str, image_name: str = None):
    '''
    Create a image from pixels.
    Parameters:
        @pixels: With the shape of HWC.
        @image_type: 'rgb' or 'grayscale'.
        @image_name
    '''
    if image_type == 'rgb':
        assert pixels.ndim == 3, 'pixels must has the shape [height, width, band]'
    elif image_type == 'grayscale':
        assert pixels.ndim == 2, 'grayscale picture must has the shape [height, width]'

    to_return = Image()

    if image_type == 'rgb':
        assert pixels.shape[2] == 3, "rgb image must has three bands"
        to_return.pixels = pixels.transpose(2, 0, 1)
        to_return._bands = ['R', 'G', 'B']
    elif image_type == 'grayscale':
        to_return.pixels = pixels[np.newaxis, :, :]
        to_return._bands = ['Brightness']
    
    to_return._image_type = image_type
    to_return.inited = True
    if image_name == None:
        to_return.image_name = 'image_from_pixels'
    else:
        to_return.image_name = image_name

    return to_return


class Image:
    inited = False
    __pdf__ = None
    __cdf__ = None

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
        pixels = np.mean(self.pixels, axis=0, keepdims=True).clip(0,255).astype(np.uint8)
        new_img = from_array(pixels.transpose((1,2,0)), image_type='grayscale', image_name=self.image_name+'-grayscale')
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
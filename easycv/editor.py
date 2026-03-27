from .image import Image
import numpy as np
from copy import deepcopy
from .operators.point_op import translation, rotation, stretch, gamma_trans
from .operators.distribution_op import PDF2LUT
from .operators.convolution_kernel import Kernel
from .operators.convolution_op import apply_filter_to_image, apply_filter_to_band
class ImageEditor:
    @staticmethod
    def translation_band(image: Image, band: str, delta: int):
        '''
        Translate band curve.
        Parameters:
            @image: Image to edit.
            @band: Band to translate. For RGB image, it's element in
                   ['R', 'G', 'B'].
            @delta: value of translation. Must be between -255 and 255.
        Return:
            New image after translation.
        '''
        assert image.inited, 'Image does not be initialized.'
        assert delta >= -255 and delta <= 255, 'delta must be between -255 and 255.'
        assert band in image.bands, f'band {band} not exists.'
        band_id = image.bands.index(band)
        new_image = deepcopy(image)
        new_image.pixels[band_id] = translation(new_image.pixels[band_id], delta)
        return new_image
    
    @staticmethod
    def rotation_band(image: Image, band: str, fix: int, slope: float):
        '''
        Rotate band curve.
        Parameters:
            @image: Image to edit.
            @band: Band to rotate. For RGB image, it's element in
                   ['R', 'G', 'B'].
            @fix: Fixed point value when rotating.
            @slope: Slope value of rotating.
        '''
        assert image.inited, 'Image does not be initialized.'
        assert band in image.bands, f'band {band} not exists.'
        # it's ok that fix value out of range(0, 255).
        
        band_id = image.bands.index(band)
        new_image = deepcopy(image)
        new_image.pixels[band_id] = rotation(new_image.pixels[band_id], fix, slope)
        return new_image
    
    @staticmethod
    def stretch_band(image: Image, band: str, min: int = 0, max: int = 255):
        '''
        Remap value range.
        Parameters:
            @image: Image to edit.
            @band: Band to stretch.
            @min: minimum of new range.
            @max: maximum of new range.
        '''
        assert image.inited, 'image is not initialized.'
        assert band in image.bands, f'band {band} not exists.'
        assert min < max and min >= 0 and max <= 255, 'stretch map range error.'

        band_id = image.bands.index(band)
        new_image = deepcopy(image)
        new_image.pixels[band_id] = stretch(new_image.pixels[band_id], min, max)
        return new_image
    
    @staticmethod
    def gamma_band(image: Image, band: str, gamma: float):
        '''
        Gamma compressing or expansion on single band.
        Parameters:
            @image
            @band
            @gamma
        '''
        assert image.inited, 'image is not initialized.'
        assert band in image.bands, f'band {band} not exists.'
        assert gamma >= 0, f'gamma {gamma} < 0.'

        band_id = image.bands.index(band)
        new_image = deepcopy(image)
        new_image.pixels[band_id] = gamma_trans(new_image.pixels[band_id], gamma)
        return new_image

    @staticmethod
    def histogram_match_band(image: Image, band: str, target: np.array):
        '''
        Match specific band of image to target distribution.
        Parameters:
            @image: Image to edit.
            @band: Band to edit. For RGB image, the value is 'R', 'G' or 'B'.
                   For grayscale image, the value is 'grayscale'.
            @target: The target distribution to match. It's a PDF array.
        '''
        assert target.shape[0] == 256 and \
               target.ndim == 1, f'target distribution invalid format'
        
        band_id = image.bands.index(band)
        new_image = deepcopy(image)
        
        src_dist = new_image.PDF[band_id]
        dst_dist = target
        lut = PDF2LUT(src_dist, dst_dist)
        new_image.pixels[band_id] = lut[new_image.pixels[band_id]]
        new_image.pixels = np.array(new_image.pixels)
        return new_image

    @staticmethod
    def conv_band(image: Image, band: str, kernel: np.array):
        '''
        Perform filter with kernel on image. Stride must be (1,1) to ensure
        the convoluted band has the same shape with the original band.
        Parameters:
            @image: image to be filtered.
            @band: Band to edit. For RGB image, the value is 'R', 'G' or 'B'.
                   For grayscale image, the value is 'grayscale'.
            @kernel: np.array. Must be 2 dimension.
            @padding
        '''
        assert Kernel.iskernel(kernel), f'invalid kernel.'
        
        new_img = deepcopy(image)
        band_id = new_img.bands.index(band)
        convoluted_band = apply_filter_to_band(new_img.pixels[band_id], kernel)
        assert convoluted_band.shape == new_img.size, f'convoluted band shape {convoluted_band.shape} do not match the original band shape {new_img.size}'
        new_img.pixels[band_id] = convoluted_band
        return new_img

    @staticmethod
    def brightness_edit(image: Image, delta: int):
        '''
        Increase or decrease brightness.
        Parameters: 
            @image: Image to edit.
            @delta: value of translation. Must between -255~255.
        Return:
            New image after brightness editing.
        '''
        assert delta >= -255 and delta <= 255, 'delta must be between -255 and 255.'
        
        new_img = deepcopy(image)
        for band_id in range(new_img.bands_cnt):
            new_img.pixels[band_id] = translation(new_img.pixels[band_id], delta)
        return new_img
    
    @staticmethod
    def contrast_edit(image: Image, fix: int, slope: float):
        '''
        Increase or decrease contrast.
        Parameters:
            @image: Image to edit.
            @fix: Fixed point value when rotating.
            @slope: Slope value of rotating.
        '''
        new_img = deepcopy(image)
        for band_id in range(new_img.bands_cnt):
            new_img.pixels[band_id] = rotation(new_img.pixels[band_id], fix, slope)
        return new_img
        
    @staticmethod
    def stretch(image: Image, min: int = 0, max: int = 255):
        '''
        Contrast stretch.
        Parameters:
            @image: Image to edit.
            @min: minimum of new range.
            @max: maximum of new range.
        '''

        assert image.inited, 'image is not initialized.'
        assert min < max and min >= 0 and max <= 255, 'stretch range error.'

        new_image = deepcopy(image)
        for band_id in range(new_image.bands_cnt):
            new_image.pixels[band_id] = stretch(new_image.pixels[band_id], min, max)
        return new_image
    
    @staticmethod
    def gamma_edit(image: Image, gamma: float = 1):
        '''
        Gamma expansion or compression.
        Parameters:
            @image: Image to edit.
            @gamma
        '''

        assert gamma >= 0
        new_img = deepcopy(image)
        for band_id in range(new_img.bands_cnt):
            new_img.pixels[band_id] = gamma_trans(new_img.pixels[band_id], gamma)
        return new_img
    
    @staticmethod
    def histogram_matching(image: Image, target: Image):
        '''
        Histogram matching from `target` to `image`.
        @Parameters:
            @image
            @target
        '''

        assert image.bands_cnt == target.bands_cnt, f'image type dismach.'

        new_image = deepcopy(image)
        src_dist = image.PDF
        dst_dist = target.PDF

        luts = [
            PDF2LUT(src_dist[i], dst_dist[i])
            for i in range(image.bands_cnt)
        ]

        new_image.pixels = [
            luts[i][new_image.pixels[i]]
            for i in range(new_image.bands_cnt)
        ]

        new_image.pixels = np.array(new_image.pixels).clip(max=255, min=0)

        return new_image
    
    @staticmethod
    def conv(image: Image, kernel: np.array):
        '''
        Convert the image to grayscale and perform convolution on it.
        Parameters:
            @image: image to perform convolution.
            @kernel
            @stride
            @padding
        '''

        new_img = deepcopy(image)
        new_img.pixels = apply_filter_to_image(new_img.pixels.transpose(1,2,0), kernel).transpose(2,0,1)
        return new_img
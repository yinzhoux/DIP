from .image import Image
from copy import deepcopy
from .operators.point_op import translation, rotation, stretch, gamma_trans
class ImageEditor:
    def __init__(self):
        pass

    def translation_band(self, image: Image, band: str, delta: int):
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
    
    def rotation_band(self, image: Image, band: str, fix: int, slope: float):
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
    
    def stretch_band(self, image: Image, band: str, min: int = 0, max: int = 255):
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
    
    def gamma_band(self, image: Image, band: str, gamma: float):
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

    def brightness_edit(self, image: Image, delta: int):
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
    
    def contrast_edit(self, image: Image, fix: int, slope: float):
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
        
    def stretch(self, image: Image, min: int = 0, max: int = 255):
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
    
    def gamma_edit(self, image: Image, gamma: float = 1):
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


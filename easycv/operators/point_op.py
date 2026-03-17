import numpy as np  
import math

def translation(pixels: np.ndarray, delta: int):
    assert pixels.ndim == 2, f'input has the shape {pixels.shape}, point process only deals with single band'
    assert pixels.dtype == 'uint8', 'point value must has type uint8'

    return (pixels.astype('int16') + delta).clip(0, 255).astype('uint8')

def rotation(pixels: np.ndarray, fix: int, slope: float):
    assert pixels.ndim == 2, f'input has the shape {pixels.shape}, point process only deals with single band'
    assert pixels.dtype == 'uint8', 'point value must has type uint8'

    rotated = (pixels.astype('float32') - fix) * slope + fix    
    rotated = rotated.clip(0, 255).astype('uint8')
    return rotated

def stretch(pixels: np.ndarray, min: int = 0, max: int = 255):
    assert pixels.ndim == 2, f'input has the shape {pixels.shape}, point process only deals with single band'
    assert pixels.dtype == 'uint8', 'point value must has type uint8'
    assert min < max and min >= 0 and max <= 255, 'stretch range error.'

    Imin: int = pixels.min()
    Imax: int = pixels.max()

    ratio = (pixels.astype('float16') - Imin) / np.max([(Imax - Imin), 1])
    new_pixels =  ratio * (max - min) + min
    return new_pixels.clip(min, max).astype('uint8')

def gamma_trans(pixels: np.ndarray, gamma: float):
    assert gamma >= 0, f'gamma value {gamma} < 0.'
    assert pixels.ndim == 2, f'input has the shape {pixels.shape}, point process only deals with single band'

    return (np.pow(pixels.astype('float32')/255, gamma)*255).clip(0, 255).astype('uint8')

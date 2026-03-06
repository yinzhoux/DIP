import numpy as np  

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
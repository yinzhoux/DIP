import numpy as np  

def translation(pixels: np.ndarray, delta: int):
    assert pixels.ndim == 2, f'input has the shape {pixels.shape}, point process only deals with single band'
    assert pixels.dtype == 'uint8', 'point value must has type uint8'

    return (pixels + delta).clip(0, 255)
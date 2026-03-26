'''
This file is based on the 2D convolution implementation from [detkov/Convolution-From-Scratch].
Original Copyright (c) 2020 Nikita Detkov.[1](https://github.com/detkov/Convolution-From-Scratch)

Modified by Yinzhoux(https://github.com/yinzhoux) for kernel with type of np.ndarray and
fast calculating with scipy instead of for-loop.
'''

import numpy as np
from typing import List, Tuple, Union
from scipy import ndimage

def add_padding(matrix: np.ndarray, 
                padding: Tuple[int, int]) -> np.ndarray:
    """Adds padding to the matrix. 

    Args:
        matrix (np.ndarray): Matrix that needs to be padded. Type is List[List[float]] casted to np.ndarray.
        padding (Tuple[int, int]): Tuple with number of rows and columns to be padded. With the `(r, c)` padding we addding `r` rows to the top and bottom and `c` columns to the left and to the right of the matrix

    Returns:
        np.ndarray: Padded matrix with shape `n + 2 * r, m + 2 * c`.
    """
    n, m = matrix.shape
    r, c = padding
    
    padded_matrix = np.zeros((n + r * 2, m + c * 2))
    padded_matrix[r : n + r, c : m + c] = matrix
    
    return padded_matrix


def _check_params(matrix, kernel, stride, dilation, padding):
    params_are_correct = (isinstance(stride[0], int)   and isinstance(stride[1], int)   and
                          isinstance(dilation[0], int) and isinstance(dilation[1], int) and
                          isinstance(padding[0], int)  and isinstance(padding[1], int)  and
                          stride[0]   >= 1 and stride[1]   >= 1 and 
                          dilation[0] >= 1 and dilation[1] >= 1 and
                          padding[0]  >= 0 and padding[1]  >= 0)
    assert params_are_correct, 'Parameters should be integers equal or greater than default values.'
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)

    if not isinstance(kernel, np.ndarray):
        kernel = np.array(kernel)
    return matrix, kernel


def conv2d(matrix: Union[List[List[float]], np.ndarray], 
             kernel: Union[List[List[float]], np.ndarray], 
             stride: Tuple[int, int] = (1, 1), 
             dilation: Tuple[int, int] = (1, 1), 
             padding: Tuple[int, int] = (0, 0)) -> np.ndarray:
    """Makes a 2D convolution with the kernel over matrix using defined stride, dilation and padding along axes.

    Args:
        matrix (Union[List[List[float]], np.ndarray]): 2D matrix to be convolved.
        kernel (Union[List[List[float]], np.ndarray]): 2D odd-shaped matrix (e.g. 3x3, 5x5, 13x9, etc.).
        stride (Tuple[int, int], optional): Tuple of the stride along axes. With the `(r, c)` stride we move on `r` pixels along rows and on `c` pixels along columns on each iteration. Defaults to (1, 1).
        dilation (Tuple[int, int], optional): Tuple of the dilation along axes. With the `(r, c)` dilation we distancing adjacent pixels in kernel by `r` along rows and `c` along columns. Defaults to (1, 1).
        padding (Tuple[int, int], optional): Tuple with number of rows and columns to be padded. Defaults to (0, 0).

    Returns:
        np.ndarray: 2D Feature map, i.e. matrix after convolution.
    """
    matrix, kernel = _check_params(matrix, kernel, stride, dilation, padding)
    return ndimage.convolve(matrix, kernel, mode='constant', cval=0.0)

def apply_filter_to_image(image: np.ndarray, 
                          kernel: np.ndarray) -> np.ndarray:
    """Applies filter to the given image.

    Args:
        image (np.ndarray): 3D matrix to be convolved. Shape must be in HWC format.
        kernel (np.ndarray): 2D odd-shaped matrix (e.g. 3x3, 5x5, 13x9, etc.).

    Returns:
        np.ndarray: image after applying kernel with type of np.uint8.
    """
    b = kernel.shape
    return np.dstack([conv2d(image[:, :, z], kernel, padding=(b[0]//2,  b[1]//2)) 
                      for z in range(image.shape[-1])]).clip(0, 255).astype('uint8')

def apply_filter_to_band(pixels: np.ndarray, 
                          kernel: np.ndarray) -> np.ndarray:
    """Applies filter to the given image.

    Args:
        image (np.ndarray): 3D matrix to be convolved. Shape must be in HWC format.
        kernel (np.ndarray): 2D odd-shaped matrix (e.g. 3x3, 5x5, 13x9, etc.).

    Returns:
        np.ndarray: image after applying kernel with type of np.uint8.
    """

    b = kernel.shape
    return conv2d(pixels, kernel, padding=(b[0]//2,  b[1]//2)).clip(0, 255).astype(np.uint8)

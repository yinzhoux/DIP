from easycv import *
import numpy as np
from . import test_config

def test_rgb_image_from_file():
    image = from_file(
        image_path=test_config.test_picture_path, 
        image_name='stranthen')

    assert image.type == 'rgb'
    assert len(image.bands) == 3    

def test_grayscale_image_from_file():
    image = from_file(
        image_path=test_config.test_grayscale_picture_path,
        image_name='grayscale stranthen'
    )

    assert image.type == 'grayscale'
    assert len(image.bands) == 1
    assert image.pixels.shape[0] == 1

def test_image_from_array():
    image = from_array(
        pixels=np.array(test_config.test_rgb_pixels).transpose(1,2,0), # transpose to HWC.
        image_type='rgb',
        image_name='test color grid'
    )

def test_pixels_save():
    image = from_array(
        pixels=np.array(test_config.test_rgb_pixels.transpose(1,2,0)), 
        image_type='rgb',
        image_name='test color grid'
    )

    save_dir = f'{test_config.BASE_DIR}/images/test_pixels_save.txt'
    image.save_pixels_to(save_dir)
from easycv import *
import numpy as np
import test_config as tc

def test_brightness_editing():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    image1 = ImageEditor.translation_band(image, band='Brightness', delta=100)
    image2 = ImageEditor.brightness_edit(image, delta=100)
    assert np.sum(image1.pixels - image2.pixels) < 1

def test_gamma_editing():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    image1 = ImageEditor.gamma_band(image, band='Brightness', gamma=0.5)
    image2 = ImageEditor.gamma_edit(image, gamma=0.5)
    assert np.sum(image1.pixels - image2.pixels) < 1

def test_contrast_editing():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    image1 = ImageEditor.rotation_band(image, band='Brightness', fix=128, slope=1.5)
    image2 = ImageEditor.contrast_edit(image, fix=128, slope=1.5)
    assert np.sum(image1.pixels - image2.pixels) < 1

def test_contrast_stretching():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    image1 = ImageEditor.stretch_band(image, band='Brightness', min=100, max=200)
    image2 = ImageEditor.stretch(image, min=100, max=200)
    assert np.sum(image1.pixels - image2.pixels) < 1

def test_histogram_statistics():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    assert np.sum(image.PDF - np.ones(shape=(256,), dtype=np.float16)/256.0) <= 1e-2
    assert np.sum(image.CDF - np.linspace(0, 1, num=256)) <= 1e-2

def test_histogram_editing():
    image = from_array(tc.test_oneline_pixels, image_type='grayscale', image_name='oneline spectrum')
    pass
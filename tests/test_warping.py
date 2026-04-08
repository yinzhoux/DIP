from easycv import *
from . import test_config as tc
import numpy as np

def test_image_warping():
    image = from_file(image_path=tc.test_picture_path, image_name='test_warper')
    scaling_matrix = np.array([
        [0.7,0,0],
        [0,0.5,0],
        [0,0,1]
    ])
    translating_matrix = np.array([
        [1,0,800],
        [0,1,1280],
        [0,0,1]
    ])
    rotating_degree = np.pi/4
    rotating_matrix = np.array([
        [np.cos(rotating_degree), -np.sin(rotating_degree), 0],
        [np.sin(rotating_degree), np.cos(rotating_degree), 0],
        [0,0,1]
    ])
    shearing_matrix = np.array([
        [1, 0.5, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    random = np.random.random(size=(3,3))
    
    scaled = ImageWarper.standard_warp(image, scaling_matrix, size=image.size)
    translated = ImageWarper.standard_warp(image, translating_matrix, size=image.size)
    rotated = ImageWarper.standard_warp(image, rotating_matrix, size=image.size)
    sheared = ImageWarper.standard_warp(image, shearing_matrix, size=image.size)
    random = ImageWarper.standard_warp(image, random, size=image.size)
    ImageDrawer.show([image, scaled, translated, rotated, sheared,random])
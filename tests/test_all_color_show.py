import numpy as np
from easycv.image import Image
import matplotlib.pyplot as plt

height, width = 256, 256
band_cnt = 3

step_band = np.arange(0, 256, 1, dtype='uint8')
zer_band = np.zeros(shape=(height, width), dtype='uint8')
grid = np.meshgrid(step_band, step_band, indexing='ij')
grid = np.array(grid)

rg = np.array((grid[0], grid[1], zer_band)).transpose(1,2,0)
rb = np.array((grid[0], zer_band, grid[1])).transpose(1,2,0)
gb = np.array((zer_band, grid[0], grid[1])).transpose(1,2,0)

rg_img = Image()
rg_img.from_array(rg, image_type='rgb')
rb_img = Image() 
rb_img.from_array(rb, image_type='rgb')
gb_img = Image()
gb_img.from_array(gb, image_type='rgb')

rg_img.show()
rb_img.show()
gb_img.show()
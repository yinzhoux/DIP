from easycv.image import Image
import numpy as np  

pixels = [
    [[100,0],[0,100]],
    [[0,100],[100,0]],
    [[100,0],[0,100]]
]

pixels = np.array(pixels)
pixels = pixels.transpose((1,2,0))
img = Image()
img.from_array(pixels=pixels, image_type='rgb')

print(img.pixels.shape)
print(img.size)
print(img.type)
print(img.bands_cnt)
print(img.bands)

img.show()
from easycv.image_loader import Image
import numpy as np

img = Image()
img.from_file('../images/stranthen.jpg', image_type='rgb')
img1 = img.brightness_edit(-100)
img.show()
img1.show()
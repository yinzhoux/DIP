from easycv.image_loader import Image
import numpy as np

img = Image()
img.from_file('../images/stranthen.jpg', image_type='rgb')
img.show()
img1 = img.contrast_edit(127, 0.5)
img1.show()
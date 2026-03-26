from easycv.image import Image
from easycv.drawer import ImageDrawer

image_path = '../../images/stranthen.jpg'
image = Image()
drawer = ImageDrawer()
image.from_file(image_path=image_path, image_type='rgb')

print(image.pixels.shape)
print(image.size)
print(image.type)
print(image.bands_cnt)
print(image.bands)

image.save_to('../../images/greyscale.jpg', convert_to_grayscale=True)
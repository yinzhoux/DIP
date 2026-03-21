from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')
img1 = editor.translation_band(img, band='R', delta=100)
# print(img.histogram)
drawer.show_histogram([
    img, img1
], figsize=(10, 5))
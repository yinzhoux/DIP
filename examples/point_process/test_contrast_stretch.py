from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')

img1 = editor.stretch_band(img, 'R', 50, 255)
img2 =editor.stretch(img, 0, 255)
drawer.show([
    img, img1, img2
])
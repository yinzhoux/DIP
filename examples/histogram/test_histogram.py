from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')
img1 = editor.translation_band(img, band='R', delta=100)

drawer.show([
    img, img1
])
drawer.show_pdf([
    img, img1
])
drawer.show_cdf([
    img, img1
])
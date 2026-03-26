from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')

img1 = editor.gamma_edit(img, 0.5)
img2 = editor.gamma_edit(img, 1.5)
img3 = editor.gamma_band(img, 'R', 0.5)

drawer.show([
    img, img1, img2, img3
])
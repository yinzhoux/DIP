from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')
img_contrast_1 = editor.contrast_edit(img, 64, 1.8)
img_contrast_2 = editor.contrast_edit(img, 127, 1.8)
img_contrast_3 = editor.contrast_edit(img, 192, 1.8)

drawer.show([
    img, img_contrast_1, img_contrast_2, img_contrast_3
], figsize=(14,14))
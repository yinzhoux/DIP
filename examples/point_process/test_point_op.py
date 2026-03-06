from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
editor = ImageEditor()
drawer = ImageDrawer()

img = Image()
img.from_file('../../images/stranthen.jpg', image_type='rgb')
img_r_plus_30 = editor.translation_band(img, 'R', 30)
img_brig_30 = editor.brightness_edit(img, 30)
img_r_rota_15 = editor.rotation_band(img, 'G', 127, 1.5)
img_contrast_1p8 = editor.contrast_edit(img, 127, 1.8)
img_contrast_p3 = editor.contrast_edit(img, 127, 0.3)

drawer.show([
    img, img_r_plus_30, img_brig_30, img_r_rota_15, img_contrast_1p8, img_contrast_p3
], figsize=(14,14))
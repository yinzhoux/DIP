from easycv.image import Image
from easycv.editor import ImageEditor
from easycv.drawer import ImageDrawer
from easycv.operators.distri_op import Distribution

import numpy as np

editor = ImageEditor()
drawer = ImageDrawer()

src_img = Image()
src_img.from_file('../../images/stranthen.jpg', image_type='rgb')
dst1_img = Image()
dst2_img = Image()
dst3_img = Image()
dst1_img.from_file('../../images/test1.jpg', image_type='rgb')
dst2_img.from_file('../../images/test2.jpg', image_type='rgb')
dst3_img.from_file('../../images/test3.jpg', image_type='rgb')

new1_img = editor.histogram_matching(src_img, dst1_img)
new2_img = editor.histogram_matching(src_img, dst2_img)
new3_img = editor.histogram_matching(src_img, dst3_img)
drawer.show([
    src_img, dst1_img, new1_img, dst2_img, new2_img,dst3_img, new3_img
])
drawer.show_pdf([
    src_img, dst1_img, new1_img, dst2_img, new2_img,dst3_img, new3_img
])


from easycv.image import Image
from easycv.drawer import ImageDrawer
from easycv.editor import ImageEditor
from easycv.operators import convolution_kernel
editor = ImageEditor()
drawer = ImageDrawer()
path = '../../images/stranthen.jpg'
img = Image()
img.from_file(path, image_type='rgb')

new_img = editor.conv(img, kernel=convolution_kernel.Kernel.ImpulseKernel(size=[101,101], poss=[[0,0]]))
new_img1 = editor.conv(img, kernel=convolution_kernel.Kernel.ImpulseKernel(size=[101,101], poss=[
    [0,0], [50,50]
]))
new_img2 = editor.conv(img, kernel=convolution_kernel.Kernel.ImpulseKernel(size=[101,101], poss=[
    [0,0], [50,50], [100,100]
]))
drawer.show([img, new_img, new_img1, new_img2])
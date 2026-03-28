from easycv.image import Image
from easycv.drawer import ImageDrawer
from easycv.editor import ImageEditor
from easycv.operators import convolution_kernel
editor = ImageEditor()
drawer = ImageDrawer()
path = '../../images/stranthen.jpg'
img = Image()
img.from_file(path, image_type='rgb')

new_img = editor.conv(img, kernel=convolution_kernel.Kernel.BlurKernel(size=(17,19)))
new_img1 = editor.conv(img, kernel=convolution_kernel.Kernel.GaussianBlurKernel(size=19, sigma=10))
new_img2 = editor.conv_band(img, 'R', kernel=convolution_kernel.Kernel.GaussianBlurKernel(size=41, sigma=40))
drawer.show([img, new_img, new_img1, new_img2])
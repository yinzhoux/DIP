from easycv import *
from .. import test_config as tc
def test_blur():
    img = from_file(tc.test_picture_path, image_name='test blur')
    new_img = ImageEditor.conv(img, kernel=Kernel.BlurKernel(size=(17,19)))
    new_img1 = ImageEditor.conv(img, kernel=Kernel.GaussianBlurKernel(size=19, sigma=10))
    new_img2 = ImageEditor.conv_band(img, 'R', kernel=Kernel.GaussianBlurKernel(size=41, sigma=40))
    ImageDrawer.show([img, new_img, new_img1, new_img2])
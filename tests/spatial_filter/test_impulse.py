from easycv import *
from .. import test_config as tc
import numpy as np

def test_impluse():
    img = from_file(tc.test_picture_path, image_name='test impluse')

    new_img = ImageEditor.conv(img, kernel=Kernel.ImpulseKernel(size=[101,101], poss=[[0,0]]))
    new_img1 = ImageEditor.conv(img, kernel=Kernel.ImpulseKernel(size=[101,101], poss=[
        [0,0], [50,50]
    ]))
    new_img2 = ImageEditor.conv(img, kernel=Kernel.ImpulseKernel(size=[101,101], poss=[
        [0,0], [50,50], [100,100]
    ]))
    ImageDrawer.show([img, new_img, new_img1, new_img2])
from easycv import *
from .. import test_config as tc
import numpy as np

def test_edge_detection():
    img = from_file(tc.test_picture_path, image_name='test edge detection')

    vertical_edge = ImageEditor.conv(img, kernel=Kernel.VerticalDifferenceKernel())
    vertical_edge.image_name = 'vetical edge detection'
    horizontal_edge = ImageEditor.conv(img, kernel=Kernel.HorizontalDifferenceKernel())
    horizontal_edge.image_name = 'horizontal edge detection'
    diagonal_edge = ImageEditor.conv(img, kernel=Kernel.DiagonalDifferenceKernel())
    diagonal_edge.image_name = 'diagonal edge detection'
    vertical_horizontal_edge = ImageEditor.conv(img, kernel=Kernel.VerticalDifferenceKernel()+Kernel.HorizontalDifferenceKernel())
    vertical_horizontal_edge.image_name = 'vertical and horizontal edge detection'
    all_edge = ImageEditor.conv(img, kernel=
                        Kernel.VerticalDifferenceKernel() +
                        Kernel.HorizontalDifferenceKernel() +
                        Kernel.DiagonalDifferenceKernel() + 
                        Kernel.InverseDiagonalDifferenceKernel()
                        )
    all_edge.image_name = 'all edge detection'
    prewitt_edge = ImageEditor.conv(img, kernel=Kernel.PrewittKernel()+Kernel.PrewittKernel(vertial=False))
    prewitt_edge.image_name = 'prewitt edge detection'
    sobel_edge = ImageEditor.conv(img, kernel=Kernel.SobelKernel()+Kernel.SobelKernel(vertical=False))
    sobel_edge.image_name = 'sobel edge detection'
    isotrofic_sobel_edge = ImageEditor.conv(img, kernel=Kernel.IsotroficSobelKernel()+Kernel.IsotroficSobelKernel(vertical=False))
    isotrofic_sobel_edge.image_name = 'isotrofic sobel edge detection'
    ImageDrawer.show([
        img, vertical_edge, horizontal_edge, diagonal_edge, vertical_horizontal_edge, all_edge, prewitt_edge, sobel_edge, isotrofic_sobel_edge
    ])

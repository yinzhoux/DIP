from easycv.image import Image
from easycv.drawer import ImageDrawer
from easycv.editor import ImageEditor
from easycv.operators import convolution_kernel
editor = ImageEditor()
drawer = ImageDrawer()
path = '../../images/building.jpg'
img = Image()
img.from_file(path, image_type='rgb')

vertical_edge = editor.conv(img, kernel=convolution_kernel.Kernel.VerticalDifferenceKernel())
vertical_edge.image_name = 'vetical edge detection'
horizontal_edge = editor.conv(img, kernel=convolution_kernel.Kernel.HorizontalDifferenceKernel())
horizontal_edge.image_name = 'horizontal edge detection'
diagonal_edge = editor.conv(img, kernel=convolution_kernel.Kernel.DiagonalDifferenceKernel())
diagonal_edge.image_name = 'diagonal edge detection'
vertical_horizontal_edge = editor.conv(img, kernel=convolution_kernel.Kernel.VerticalDifferenceKernel()+convolution_kernel.Kernel.HorizontalDifferenceKernel())
vertical_horizontal_edge.image_name = 'vertical and horizontal edge detection'
all_edge = editor.conv(img, kernel=
                       convolution_kernel.Kernel.VerticalDifferenceKernel() +
                       convolution_kernel.Kernel.HorizontalDifferenceKernel() +
                       convolution_kernel.Kernel.DiagonalDifferenceKernel() + 
                       convolution_kernel.Kernel.InverseDiagonalDifferenceKernel()
                       )
all_edge.image_name = 'all edge detection'
prewitt_edge = editor.conv(img, kernel=convolution_kernel.Kernel.PrewittKernel()+convolution_kernel.Kernel.PrewittKernel(vertial=False))
prewitt_edge.image_name = 'prewitt edge detection'
sobel_edge = editor.conv(img, kernel=convolution_kernel.Kernel.SobelKernel()+convolution_kernel.Kernel.SobelKernel(vertical=False))
sobel_edge.image_name = 'sobel edge detection'
isotrofic_sobel_edge = editor.conv(img, kernel=convolution_kernel.Kernel.IsotroficSobelKernel()+convolution_kernel.Kernel.IsotroficSobelKernel(vertical=False))
isotrofic_sobel_edge.image_name = 'isotrofic sobel edge detection'
drawer.show([
    img, vertical_edge, horizontal_edge, diagonal_edge, vertical_horizontal_edge, all_edge, prewitt_edge, sobel_edge, isotrofic_sobel_edge
])

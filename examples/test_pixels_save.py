from easycv.image import Image

img = Image()
img.from_file('../images/stranthen.jpg', image_type='rgb')
img.save_pixels_to('../images/stranthen.npy')
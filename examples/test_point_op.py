from easycv.image_loader import Image

img = Image()
img.from_file('../images/stranthen.jpg', image_type='rgb')
img.show()
img1 = img.translation_band(band='R', delta=10)
img1.show()
img1.save_to(f'../images/test_r+10.jpg')
img2 = img.translation_band(band='R', delta=-10)
img2.show()
img2.save_to(f'../images/test_r-10.jpg')
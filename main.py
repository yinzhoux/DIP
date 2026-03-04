from image_loader import Image
image_path = './images/stranthen.jpg'
image = Image(image_path=image_path, image_type='rgb')

print(image.pixels.shape)
print(image.size)
print(image.type)
print(image.bands_cnt)
print(image.bands)

image.show()
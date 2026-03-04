from image_loader import ImageLoader
image_path = './images/stranthen.jpg'
image = ImageLoader(image_path=image_path)

print(image.pixels.shape)
print(image.size)
from PIL import Image
import numpy as np

class ImageLoader:
    def __init__(self, image_path: str):
        img = Image.open(image_path)
        self.bands = img.getbands()
        self.bands_cnt = len(self.bands)
        self._img_data = [list(img.getdata(band)) for band in range(self.bands_cnt)]
        self.size = img.size
        self.pixels = np.array(self._img_data)
        print(self.pixels.shape)
        np.reshape(self.pixels, (self.bands_cnt, self.size[0], self.size[1]))
        print(self.pixels.shape)
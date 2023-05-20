import numpy as np
from PIL import Image


class GetRGB:
    def __init__(self, file_image):
        self._img = Image.open(file_image).convert('RGB')
        self._width, self._height = self._img.size
        self._red = np.zeros((self._width, self._height))
        self._green = np.zeros((self._width, self._height))
        self._blue = np.zeros((self._width, self._height))
        self._img_red = np.zeros(256)
        self._img_green = np.zeros(256)
        self._img_blue = np.zeros(256)
        self._set_array_rgb(self._img)

    def _set_array_rgb(self, img):
        img_array = np.array(img)
        self._red_array = np.zeros_like(img_array)
        self._red_array[:, :, 0] = img_array[:, :, 0]
        self._red_array[:, :, 1] = 0
        self._red_array[:, :, 2] = 0
        self._green_array = np.zeros_like(img_array)
        self._green_array[:, :, 0] = 0
        self._green_array[:, :, 1] = img_array[:, :, 1]
        self._green_array[:, :, 2] = 0
        self._blue_array = np.zeros_like(img_array)
        self._blue_array[:, :, 0] = 0
        self._blue_array[:, :, 1] = 0
        self._blue_array[:, :, 2] = img_array[:, :, 2]

    def get_img_size(self):
        return self._img.size

    def get_img_red(self):
        return Image.fromarray(self._red_array)

    def get_img_green(self):
        return Image.fromarray(self._green_array)

    def get_img_blue(self):
        return Image.fromarray(self._blue_array)

    def set_rgb(self):
        pixels = self._img.load()
        for w in range(self._width):
            for h in range(self._height):
                r, g, b = pixels[w, h]
                self._red[w, h] = r
                self._green[w, h] = g
                self._blue[w, h] = b

    def set_histogram(self):
        for w in range(self._width):
            for h in range(self._height):
                self._img_red[int(self._red[w, h])] += 1
                self._img_green[int(self._green[w, h])] += 1
                self._img_blue[int(self._blue[w, h])] += 1

    def get_histogram_red(self):
        return self._img_red

    def get_histogram_green(self):
        return self._img_green

    def get_histogram_blue(self):
        return self._img_blue

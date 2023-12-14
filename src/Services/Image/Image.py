import cv2 as cv
import pandas as pd
import numpy as np

from src.Services.Image.Utils import Split
from src.Services.Image.Utils import Zoom
from src.Services.Image.Utils import Checkboard


class Image:
    __im_a: np.ndarray
    __im_b: np.ndarray

    def __init__(self):
        self.__im_a = None
        self.__im_b = None


    def load_images(self, path_a: str = None, path_b: str = None):
        if path_a is not None:
            self.__im_a = self.__load_img(path_a)
        if path_b is not None:
            self.__im_b = self.__load_img(path_b)

        self.__reshape()

    def swap_images(self):
        if self.__im_a is not None and self.__im_b is not None:
            a = self.__im_a
            self.__im_a = self.__im_b
            self.__im_b = a
            return

        if self.__im_a is None:
            self.__im_a = self.__im_b
            self.__im_b = None
            return

        if self.__im_b is None:
            self.__im_b = self.__im_a
            self.__im_a = None
            return


    def free_memory(self):
        self.__im_a = None
        self.__im_b = None

    def split_image(self, x_position: float, path_a: str = None, path_b: str = None, size_of_marker = 5):
        if path_a is not None or path_b is not None:
            self.load_images(path_a=path_a, path_b=path_b)

        res = Split.get_split_img(x_position, self.__im_a, self.__im_b, size_of_marker=size_of_marker)
        return res

    def checkboard(self, x_chunks: int, y_chunks: int, path_a: str = None, path_b: str = None):
        if path_a != None or path_b != None:
            self.load_images(path_a=path_a, path_b=path_b)

        if x_chunks == None:
            x_chunks = 2

        if y_chunks == None:
            y_chunks = x_chunks

        res = Checkboard.get_checkboard_image(x_chunks, y_chunks, self.__im_a, self.__im_b)
        return res

    def zoom(self, zoom_factor: float, x: float, y: float):
        if self.__im_a is not None:
            return Zoom.zoom_image(self.__im_a, zoom_factor, x, y)
        return None

    def __reshape(self):
        if self.__im_a is not None and self.__im_b is not None and self.__im_a.shape != self.__im_b.shape:
            self.__im_b = cv.resize(self.__im_b, (self.__im_a.shape[1], self.__im_a.shape[0]), interpolation=cv.INTER_CUBIC)


    def __load_img(self, path: str):
        img = cv.imread(path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return img

    def load_img(self, path: str = None):
        if path is not None:
            self.__im_a = self.__load_img(path)
        return self.__im_a

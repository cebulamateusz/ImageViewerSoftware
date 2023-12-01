import cv2 as cv
import pandas as pd
import numpy as np

from Utils import Split
from Utils.Zoom import Zoom
from Utils import Checkboard


class Image:
    __im_a: np.ndarray
    __im_b: np.ndarray

    __im_c: np.ndarray  # used only for zoom mode
    __im_d: np.ndarray  # used only for zoom mode

    def __init__(self):
        self.__im_a = None
        self.__im_b = None
        self.__im_c = None
        self.__im_d = None

    def load_images(self, im_a = None, im_b = None, im_c = None, im_d = None):
        if im_a is not None:
            self.__im_a = im_a
        if im_b is not None:
            self.__im_b = im_b
        if im_c is not None:
            self.__im_c = im_c
        if im_d is not None:
            self.__im_d = im_d

        self.__reshape()

    def split_image(self, x_position: float, im_a = None, im_b = None, size_of_marker = 5):
        if im_a is not None or im_b is not None:
            self.load_images(im_a=im_a, im_b=im_b)

        res = Split.get_split_img(x_position, self.__im_a, self.__im_b, size_of_marker=size_of_marker)
        return res

    def checkboard(self, x_chunks: int, y_chunks: int, im_a = None, im_b = None):
        if im_a != None or im_b != None:
            self.load_images(im_a=im_a, im_b=im_b)

        if x_chunks == None:
            return None

        if y_chunks == None:
            y_chunks = x_chunks

        res = Checkboard.get_checkboard_image(x_chunks, y_chunks, self.__im_a, self.__im_b)
        return res

    def zoom(self):
        return None



    def __reshape(self):
        if self.__im_a is not None and self.__im_b is not None and self.__im_a.shape != self.__im_b.shape:
            self.__im_b = cv.resize(self.__im_b, (self.__im_a.shape[1], self.__im_a.shape[0]), interpolation=cv.INTER_CUBIC)

        if self.__im_a is not None and self.__im_c is not None and self.__im_a.shape != self.__im_c.shape:
            self.__im_c = cv.resize(self.__im_c, self.__im_a.shape, interpolation=cv.INTER_LINEAR)

        if self.__im_a is not None and self.__im_d is not None and self.__im_a.shape != self.__im_d.shape:
            self.__im_d = cv.resize(self.__im_d, self.__im_a.shape, interpolation=cv.INTER_LINEAR)

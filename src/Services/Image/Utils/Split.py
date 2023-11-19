import cv2 as cv
import numpy as np


class Split:
    def __init__(self):
        print('asd')

    def get_split_img(self, x: float, im_a: np.ndarray, im_b: np.ndarray, size_of_marker = 5):
        if x is None or im_a is None or im_b is None:
            return None

        split_point = int(im_a.shape[1] * x)
        res = im_a.copy()
        res[:, split_point:, :] = im_b[:, split_point:, :].copy()
        res[:,split_point-size_of_marker:split_point+size_of_marker,:] = 0
        return res

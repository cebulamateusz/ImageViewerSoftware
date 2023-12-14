import cv2 as cv
import numpy as np

def get_split_img(x: float, im_a: np.ndarray, im_b: np.ndarray, size_of_marker = 5):
    if x is None or (im_a is None and im_b is None):
        return None

    if im_a is None:
        im_a = np.zeros(im_b.shape, dtype=np.uint8)

    elif im_b is None:
        im_b = np.zeros(im_a.shape, dtype=np.uint8)


    split_point = int(im_a.shape[1] * x)
    res = im_a.copy()
    res[:, split_point:, :] = im_b[:, split_point:, :].copy()
    res[:,split_point-size_of_marker:split_point+size_of_marker,:] = 0
    return res

import cv2 as cv
import pandas as pd
import numpy as np


def get_checkboard_image(n_x: int, n_y: int, im_a: np.ndarray, im_b: np.ndarray):
    if im_a is None and im_b is None:
        return None

    if im_a is None:
        im_a = np.zeros(im_b.shape, dtype=np.uint8)

    if im_b is None:
        im_b = np.zeros(im_a.shape, dtype=np.uint8)

    step_x = int(im_a.shape[1] / n_x)
    step_y = int(im_a.shape[0] / n_y)

    res = im_a.copy()
    x = 0

    while x < n_x:
        y = 0
        while y < n_y-1:
            res[y * step_y:(y + 1) * step_y, x * step_x:(x + 1) * step_x, :] = im_b[y * step_y:(y + 1) * step_y, x * step_x:(x + 1) * step_x, :]
            y += 2

        x += 1
        y = 1

        while y < n_y-1:
            res[y * step_y:(y + 1) * step_y, x * step_x:(x + 1) * step_x, :] = im_b[y * step_y:(y + 1) * step_y, x * step_x:(x + 1) * step_x, :]
            y += 2

        x += 1

    x = (n_x % 2 - 1) * (-1)

    while x < n_x:
        res[(n_y-1) * step_y:, x * step_x:(x + 1) * step_x, :] = im_b[(n_y-1) * step_y:, x * step_x:(x + 1) * step_x, :]
        x += 2
    return res

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from src.Widgets.CheckerboardView.CheckerboardView import Ui_CheckerboardView
from src.Services.Image.Image import Image


class CheckerboardWidget(QWidget, Ui_CheckerboardView):
    __normalized_mp: tuple = (0.5, 0.5)
    __image_path1: str = None
    __image_path2: str = None
    __image_class: Image = None

    def __init__(self, *args, obj=None, **kwargs):
        super(CheckerboardWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pbLoadImg1.clicked.connect(self.loadImage1)
        self.pbLoadImg2.clicked.connect(self.loadImage2)
        self.__image_class = Image()
        self.resizeEvent = self.on_resize
        self.labelMinSize = self.lbImage.size()
        self.lbImage.setMinimumSize(self.labelMinSize)
        self.pbSwapImages.clicked.connect(self.swap_images)

    def loadImage1(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path1 = path
            self.load_checkerboard_image()
        print(self.__image_path1)

    def loadImage2(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path2 = path
            self.load_checkerboard_image()
        print(self.__image_path2)

    def load_checkerboard_image(self):
        img = self.__image_class.checkboard(5, 5, self.__image_path1, self.__image_path2)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.lbImage.setPixmap(QPixmap(qImg).scaled(self.lbImage.size(), Qt.KeepAspectRatio))

    def on_resize(self, event):
        # When the window is resized, update the label size to match the available space
        if not self.__image_path1 or not self.__image_path2:
            return
        img = self.__image_class.checkboard(x_chunks=5, y_chunks=5)

        if isinstance(img, np.ndarray) and img.size > 1:
            label_size = self.lbImage.size()
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888))

            # Scale the image to the available space while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio)

            # Update the label with the scaled image
            self.lbImage.setPixmap(scaled_pixmap)
            #self.adjustSize()

    def swap_images(self):
        temp = self.__image_path1
        self.__image_path1 = self.__image_path2
        self.__image_path2 = temp
        self.load_checkerboard_image()

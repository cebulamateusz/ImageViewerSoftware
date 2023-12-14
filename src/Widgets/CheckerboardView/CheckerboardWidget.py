import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from src.Widgets.CheckerboardView.CheckerboardView import Ui_CheckerboardView
from src.Services.Image.Image import Image


class CheckerboardWidget(QWidget, Ui_CheckerboardView):
    __normalized_mp: tuple = (0.5, 0.5)
    __x_chunks: int = 4
    __y_chunks: int = 4
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
        self.sbXaxis.valueChanged.connect(self.on_chunk_size_changed)
        self.sbYaxis.valueChanged.connect(self.on_chunk_size_changed)
        self.__x_chunks = self.sbXaxis.value()
        self.__y_chunks = self.sbYaxis.value()

    def on_chunk_size_changed(self):
        self.__x_chunks = self.sbXaxis.value()
        self.__y_chunks = self.sbYaxis.value()
        self.on_resize(None)

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
        img = self.__image_class.checkboard(self.__x_chunks, self.__y_chunks, self.__image_path1, self.__image_path2)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size())
        self.lbImage.setPixmap(QPixmap(qImg).scaled(self.lbImage.size(), Qt.KeepAspectRatio))

    def on_resize(self, event):
        # When the window is resized, update the label size to match the available space
        if not self.__image_path1 or not self.__image_path2:
            return
        img = self.__image_class.checkboard(x_chunks=self.__x_chunks, y_chunks=self.__y_chunks)

        if isinstance(img, np.ndarray) and img.size > 1:
            label_size = self.lbImage.size()
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size()))

            # Scale the image to the available space while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio)

            # Update the label with the scaled image
            self.lbImage.setPixmap(scaled_pixmap)
            #self.adjustSize()

    def swap_images(self):
        self.__image_class.swap_images()
        img = self.__image_class.checkboard(x_chunks=self.__x_chunks, y_chunks=self.__y_chunks)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size())
        self.lbImage.setPixmap(QPixmap(qImg).scaled(self.lbImage.size(), Qt.KeepAspectRatio))

    def close(self):
        self.__image_class.free_memory()
        self.__image_class = None
        self.lbImage.close()
        super(CheckerboardWidget, self).close()

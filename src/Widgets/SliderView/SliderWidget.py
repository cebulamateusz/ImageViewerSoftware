import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from src.Widgets.SliderView.SliderView import Ui_SliderView
from src.Services.Image.Image import Image


class SliderWidget(QWidget, Ui_SliderView):
    __normalized_mp: tuple = (0.5, 0.5)
    __image_path1: str = None
    __image_path2: str = None
    __image_class: Image = None


    def __init__(self, *args, obj=None, **kwargs):
        super(SliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.lbImage.mousePressEvent = self.get_normalized_position
        self.pbLoadImg1.clicked.connect(self.loadImage1)
        self.pbLoadImg2.clicked.connect(self.loadImage2)
        self.__image_class = Image()
        self.resizeEvent = self.on_resize
        self.labelMinSize = self.lbImage.size()
        self.lbImage.setMinimumSize(self.labelMinSize)

    def loadImage1(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file", "",
                                                            "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path1 = path
            self.load_split_image()


        print(self.__image_path1)

    def loadImage2(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file", "",
                                                            "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path2 = path
            self.load_split_image()
        print(self.__image_path2)

    def get_normalized_position(self, event):
        mouse_pos = event.pos()
        label_width = self.lbImage.width()
        label_height = self.lbImage.height()

        self.__normalized_mp = (mouse_pos.x() / label_width, mouse_pos.y() / label_height)

        img = self.__image_class.split_image(self.__normalized_mp[0])
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.lbImage.setPixmap(QPixmap(qImg).scaled(self.lbImage.size(), Qt.KeepAspectRatio))

        print(f"Relative position within label: ({self.__normalized_mp[0]}, {self.__normalized_mp[1]})")

    def load_split_image(self, x: float = 0.5):
        img = self.__image_class.split_image(x, self.__image_path1, self.__image_path2)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.lbImage.setPixmap(QPixmap(qImg).scaled(self.lbImage.size(), Qt.KeepAspectRatio))

    def on_resize(self, event):
        # When the window is resized, update the label size to match the available space
        img = self.__image_class.split_image(self.__normalized_mp[0])
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



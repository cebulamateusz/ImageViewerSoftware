import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *

from src.Services.Image.Image import Image
from src.Widgets.Image.ImageView import Ui_Image


class ImageWidget(QWidget, Ui_Image):
    __image_path: str = None

    def __init__(self, *args, obj=None, **kwargs):
        super(ImageWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.lbImage.mousePressEvent = self.get_normalized_position
        self.pbLoad.clicked.connect(self.loadImage)
        self.__image_class = Image()
        self.resizeEvent = self.on_resize
        self.labelMinSize = self.lbImage.size()
        self.lbImage.setMinimumSize(self.labelMinSize)

    def get_normalized_position(self, event):
        mouse_pos = event.pos()
        label_width = self.lbImage.width()
        label_height = self.lbImage.height()

        self.__normalized_mp = (mouse_pos.x() / label_width, mouse_pos.y() / label_height)
        # todo: pass coordinates to image and refresh it

        print(f"Relative position within label: ({self.__normalized_mp[0]}, {self.__normalized_mp[1]})")

    def loadImage(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path = path
            img = self.__image_class.load_img(self.__image_path)
            if isinstance(img, np.ndarray) and img.size > 1:
                label_size = self.lbImage.size()
                height, width, channel = img.shape
                bytesPerLine = 3 * width
                pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888))

                # Scale the image to the available space while keeping aspect ratio
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio)

                # Update the label with the scaled image
                self.lbImage.setPixmap(scaled_pixmap)
        print(self.__image_path)

    def on_resize(self, event):
        # When the window is resized, update the label size to match the available space
        if not self.__image_path:
            return
        img = self.__image_class.load_img()

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

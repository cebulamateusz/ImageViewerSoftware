import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QCursor
from PyQt5.QtWidgets import *

from src.Services.Image.Image import Image
from src.Widgets.Image.ImageView import Ui_Image


class ImageWidget(QWidget, Ui_Image):
    my_signal = pyqtSignal(QEvent)
    signal_move = pyqtSignal(QEvent)
    __image_path: str = None


    def __init__(self, *args, obj=None, **kwargs):
        super(ImageWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pbLoad.clicked.connect(self.loadImage)
        self.__image_class = Image()
        self.resizeEvent = self.on_resize
        self.labelMinSize = self.lbImage.size()
        self.lbImage.setMinimumSize(self.labelMinSize)
        self.__zoom_factor = 2.5
        self.iszoomed = False
        self.grabbed = False
        self.mouse_timer = QTimer(self)
        self.mouse_timer.setInterval(10)  # Trigger at most 120 times per second
        self.mouse_timer.timeout.connect(self.on_mouse_timer_timeout)

    def close(self):
        self.__image_class.free_memory()
        self.__image_class = None
        self.lbImage.close()
        self.mouse_timer = None
        super(ImageWidget, self).close()

    def mouseDoubleClickEvent(self, event, **kwargs):
        self.my_signal.emit(event)

    def mousePressEvent(self, event, **kwargs):
        if event.button() == Qt.LeftButton:
            self.grabbed = True

    def mouseReleaseEvent(self, event, **kwargs):
        if event.button() == Qt.LeftButton:
            self.grabbed = False

    def enterEvent(self, event):
        self.mouse_timer.start()

    def leaveEvent(self, event):
        self.mouse_timer.stop()

    def on_mouse_timer_timeout(self):
        if self.grabbed and self.iszoomed:  # Check if the mouse is grabbed
            mouse_pos = QCursor.pos() - self.lbImage.mapToGlobal(QPoint(0, 0))
            self.signal_move.emit(QMouseEvent(QEvent.MouseMove, mouse_pos, Qt.NoButton, Qt.NoButton, Qt.NoModifier))

    def loadImage(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path = path
            img = self.__image_class.load_img(self.__image_path)
            if isinstance(img, np.ndarray) and img.size > 1:
                label_size = self.lbImage.size()
                height, width, channel = img.shape
                bytesPerLine = 3 * width
                pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size()))

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
            pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size()))

            # Scale the image to the available space while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio)

            # Update the label with the scaled image
            self.lbImage.setPixmap(scaled_pixmap)
            #self.adjustSize()

    def set_zoom_factor(self, zoom_factor: float):
        self.__zoom_factor = zoom_factor

    def zoom_in(self, event, move = False):
        if self.iszoomed and not move:
            self.iszoomed = False
            self.on_resize(None)
            return
        mouse_pos = event.pos()
        label_width = self.lbImage.width()
        label_height = self.lbImage.height()

        self.__normalized_mp = (mouse_pos.x() / label_width, mouse_pos.y() / label_height)
        img = self.__image_class.zoom(self.__zoom_factor, self.__normalized_mp[0], self.__normalized_mp[1])

        if isinstance(img, np.ndarray) and img.size > 1:
            label_size = self.lbImage.size()
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            pixmap = QPixmap.fromImage(QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.lbImage.size()))

            # Scale the image to the available space while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio)

            # Update the label with the scaled image
            self.lbImage.setPixmap(scaled_pixmap)
            self.iszoomed = True

        print(f"Relative position within label: ({self.__normalized_mp[0]}, {self.__normalized_mp[1]})")


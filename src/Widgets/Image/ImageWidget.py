from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.Image.ImageView import Ui_Image


class ImageWidget(QWidget, Ui_Image):
    __image_path: str = None

    def __init__(self, *args, obj=None, **kwargs):
        super(ImageWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.lbImage.mousePressEvent = self.get_normalized_position
        self.pbLoad.clicked.connect(self.loadImage)

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
        print(self.__image_path)

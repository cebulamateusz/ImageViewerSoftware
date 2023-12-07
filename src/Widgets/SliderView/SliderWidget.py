from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.SliderView.SliderView import Ui_SliderView


class SliderWidget(QWidget, Ui_SliderView):
    __normalized_mp: tuple = (0.5, 0.5)
    __image_path1: str = None
    __image_path2: str = None

    def __init__(self, *args, obj=None, **kwargs):
        super(SliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.lbImage.mousePressEvent = self.get_normalized_position
        self.pbLoadImg1.clicked.connect(self.loadImage1)
        self.pbLoadImg2.clicked.connect(self.loadImage2)

    def loadImage1(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file", "",
                                                            "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path1 = path

        print(self.__image_path1)

    def loadImage2(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file", "",
                                                            "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path2 = path
        print(self.__image_path2)

    def get_normalized_position(self, event):
        mouse_pos = event.pos()
        label_width = self.lbImage.width()
        label_height = self.lbImage.height()

        self.__normalized_mp = (mouse_pos.x() / label_width, mouse_pos.y() / label_height)
        #todo: pass coordinates to image and refresh it

        print(f"Relative position within label: ({self.__normalized_mp[0]}, {self.__normalized_mp[1]})")



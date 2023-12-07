from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.CheckerboardView.CheckerboardView import Ui_CheckerboardView


class CheckerboardWidget(QWidget, Ui_CheckerboardView):
    __image_path1: str = None
    __image_path2: str = None

    def __init__(self, *args, obj=None, **kwargs):
        super(CheckerboardWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pbLoadImg1.clicked.connect(self.loadImage1)
        self.pbLoadImg2.clicked.connect(self.loadImage2)

    def loadImage1(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path1 = path
        print(self.__image_path1)

    def loadImage2(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select an image file",  "", "PNG (*.png);;JPG (*.jpg);;All Files (*)")
        if path:
            self.__image_path2 = path
        print(self.__image_path2)

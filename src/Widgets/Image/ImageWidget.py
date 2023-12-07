from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.Image.ImageView import Ui_Image


class ImageWidget(QWidget, Ui_Image):

    def __init__(self, *args, obj=None, **kwargs):
        super(ImageWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.SliderView.SliderView import Ui_SliderView


class SliderWidget(QWidget, Ui_SliderView):

    def __init__(self, *args, obj=None, **kwargs):
        super(SliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.CheckerboardView.CheckerboardView import Ui_CheckerboardView


class CheckerboardWidget(QWidget, Ui_CheckerboardView):

    def __init__(self, *args, obj=None, **kwargs):
        super(CheckerboardWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)


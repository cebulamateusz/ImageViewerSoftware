from src.Widgets.CheckerboardView.CheckerboardWidget import CheckerboardWidget
from src.Widgets.MainWindow.MainWindowView import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.Widgets.SliderView.SliderWidget import SliderWidget
from src.Widgets.GridView.GridWidget import GridWidget


class MainWindowWidget(QMainWindow, Ui_MainWindow):
    __sliderWidget: SliderWidget = None
    __gridWidget: GridWidget = None
    __checkerboardWidget: CheckerboardWidget = None

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindowWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)

        self.actionSliderView.triggered.connect(self.__set_slider_widget)
        self.pbSliderView.clicked.connect(self.__set_slider_widget)

        self.actionGridView.triggered.connect(self.__set_grid_widget)
        self.pbGridView.clicked.connect(self.__set_grid_widget)

        self.pbCheckerboardView.clicked.connect(self.__set_checkerboard_widget)
        self.actionCheckerboardView.triggered.connect(self.__set_checkerboard_widget)


    @pyqtSlot()
    def __set_slider_widget(self):
        if self.__checkerboardWidget:
            self.vlView.removeWidget(self.__checkerboardWidget)
            self.__checkerboardWidget.close()
            self.__checkerboardWidget = None
        if self.__gridWidget:
            self.vlView.removeWidget(self.__gridWidget)
            self.__gridWidget.close()
            self.__gridWidget = None
        if not self.__sliderWidget:
            self.__sliderWidget = SliderWidget()
            self.vlView.addWidget(self.__sliderWidget)

    @pyqtSlot()
    def __set_grid_widget(self):
        if self.__checkerboardWidget:
            self.vlView.removeWidget(self.__checkerboardWidget)
            self.__checkerboardWidget.close()
            self.__checkerboardWidget = None
        if self.__sliderWidget:
            self.vlView.removeWidget(self.__sliderWidget)
            self.__sliderWidget.close()
            self.__sliderWidget = None

        if not self.__gridWidget:
            self.__gridWidget = GridWidget()
            self.vlView.addWidget(self.__gridWidget)

    @pyqtSlot()
    def __set_checkerboard_widget(self):
        if self.__gridWidget:
            self.vlView.removeWidget(self.__gridWidget)
            self.__gridWidget.close()
            self.__gridWidget = None
        if self.__sliderWidget:
            self.vlView.removeWidget(self.__sliderWidget)
            self.__sliderWidget.close()
            self.__sliderWidget = None

        if not self.__checkerboardWidget:
            self.__checkerboardWidget = CheckerboardWidget()
            self.vlView.addWidget(self.__checkerboardWidget)

    def close(self):
        if self.__checkerboardWidget:
            self.vlView.removeWidget(self.__checkerboardWidget)
            self.__checkerboardWidget.close()
        if self.__sliderWidget:
            self.vlView.removeWidget(self.__sliderWidget)
            self.__sliderWidget.close()
        if self.__gridWidget:
            self.vlView.removeWidget(self.__gridWidget)
            self.__gridWidget.close()
        super(MainWindowWidget, self).close()

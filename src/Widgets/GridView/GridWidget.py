from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.GridView.GridView import Ui_GridView
from src.Widgets.Image.ImageWidget import ImageWidget
import numpy as np

class GridWidget(QWidget, Ui_GridView):

    imageList: list = None
    imageNum: int = 4
    widgetCount: int = 0
    rowCount: int = 1
    colCount: int = 1

    def __init__(self, *args, obj=None, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.sbNumImages.setMinimum(1)
        self.sbNumImages.setValue(2)
        self.setImagesOnGrid()
        self.pbSetNumImages.clicked.connect(self.setImagesOnGrid)
        self.dsbZoomFactor.valueChanged.connect(self.change_zoom_factors)
        self.doubleclickpos = tuple

    def close(self):
        for i in range(0, self.widgetCount):
            widget = self.imageList[i]
            self.glLayout.removeWidget(widget)
            widget.deleteLater()
        self.widgetCount = self.imageNum
        if self.imageList:
            for el in self.imageList:
                el: ImageWidget
                el.close()
            self.imageList.clear()
            self.imageList = None
        super(GridWidget, self).close()

    def setImagesOnGrid(self):
        self.imageNum = self.sbNumImages.value()
        if self.imageNum < 1:
            self.imageNum = 1
        self.colCount = int(np.ceil(np.sqrt(self.imageNum)))
        self.rowCount = int(np.ceil(self.imageNum/self.colCount))

        for i in range(0, self.widgetCount):
            widget = self.imageList[i]
            self.glLayout.removeWidget(widget)
            widget.deleteLater()
        self.widgetCount = self.imageNum
        if self.imageList:
            for el in self.imageList:
                el: ImageWidget
                el.close()
            self.imageList.clear()
            self.imageList = None
        self.imageList = list()
        for i in range(0, self.imageNum):
            self.imageList.append(ImageWidget())
        for z in self.imageList:
            z: ImageWidget
            z.my_signal.connect(self.zoom_in)
            z.signal_move.connect(self.move_zoomed)
        for i in range(self.rowCount):
            for j in range(self.colCount):
                index = i * self.colCount + j
                if index < self.imageNum:
                    self.glLayout.addWidget(self.imageList[index], i, j)
                else:
                    break

    @pyqtSlot(QEvent)
    def zoom_in(self, event):
        self.doubleclickpos = event.pos()
        for z in self.imageList:
            z: ImageWidget
            z.zoom_in(event)

    @pyqtSlot(QEvent)
    def move_zoomed(self, event):
        for z in self.imageList:
            z: ImageWidget
            z.zoom_in(event, move=True)

    def change_zoom_factors(self):
        for z in self.imageList:
            z: ImageWidget
            z.set_zoom_factor(self.dsbZoomFactor.value())




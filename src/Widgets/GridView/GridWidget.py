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
    image1: ImageWidget = None
    image2: ImageWidget = None
    image3: ImageWidget = None
    image4: ImageWidget = None

    def __init__(self, *args, obj=None, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setImagesOnGrid()
        self.sbNumImages.setMinimum(1)
        self.pbSetNumImages.clicked.connect(self.setImagesOnGrid)
        """
        self.image1 = ImageWidget()
        self.image2 = ImageWidget()
        self.image3 = ImageWidget()
        self.image4 = ImageWidget()
        self.glLayout.addWidget(self.image1, 0, 0)
        self.glLayout.addWidget(self.image2, 0, 1)
        self.glLayout.addWidget(self.image3, 1, 0)
        self.glLayout.addWidget(self.image4, 1, 1)
        """

    def close(self):
        for i in range(0, self.widgetCount):
            widget = self.imageList[i]
            self.glLayout.removeWidget(widget)
            widget.deleteLater()
        self.widgetCount = self.imageNum
        if self.imageList:
            self.imageList.clear()
            self.imageList = None
        self.imageList = list()
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
            self.imageList.clear()
            self.imageList = None
        self.imageList = list()
        for i in range(0, self.imageNum):
            self.imageList.append(ImageWidget())
        for i in range(self.rowCount):
            for j in range(self.colCount):
                index = i * self.colCount + j
                if index < self.imageNum:
                    self.glLayout.addWidget(self.imageList[index], i, j)
                else:
                    break




from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.Widgets.GridView.GridView import Ui_GridView
from src.Widgets.Image.ImageWidget import ImageWidget


class GridWidget(QWidget, Ui_GridView):
    image1: ImageWidget = None
    image2: ImageWidget = None
    image3: ImageWidget = None
    image4: ImageWidget = None

    def __init__(self, *args, obj=None, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.image1 = ImageWidget()
        self.image2 = ImageWidget()
        self.image3 = ImageWidget()
        self.image4 = ImageWidget()
        self.glLayout.addWidget(self.image1, 0, 0)
        self.glLayout.addWidget(self.image2, 0, 1)
        self.glLayout.addWidget(self.image3, 1, 0)
        self.glLayout.addWidget(self.image4, 1, 1)

    def close(self):
        self.glLayout.removeWidget(self.image1)
        self.glLayout.removeWidget(self.image2)
        self.glLayout.removeWidget(self.image3)
        self.glLayout.removeWidget(self.image4)
        self.image1.close()
        self.image2.close()
        self.image3.close()
        self.image4.close()

        super(GridWidget, self).close()

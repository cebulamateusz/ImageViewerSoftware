# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GridView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GridView(object):
    def setupUi(self, GridView):
        GridView.setObjectName("GridView")
        GridView.resize(1062, 838)
        self.gridLayout = QtWidgets.QGridLayout(GridView)
        self.gridLayout.setObjectName("gridLayout")
        self.sbNumImages = QtWidgets.QSpinBox(GridView)
        self.sbNumImages.setObjectName("sbNumImages")
        self.gridLayout.addWidget(self.sbNumImages, 0, 0, 1, 1)
        self.glLayout = QtWidgets.QGridLayout()
        self.glLayout.setObjectName("glLayout")
        self.gridLayout.addLayout(self.glLayout, 1, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.dsbZoomFactor = QtWidgets.QDoubleSpinBox(GridView)
        self.dsbZoomFactor.setMinimum(1.0)
        self.dsbZoomFactor.setSingleStep(0.5)
        self.dsbZoomFactor.setProperty("value", 2.5)
        self.dsbZoomFactor.setObjectName("dsbZoomFactor")
        self.gridLayout.addWidget(self.dsbZoomFactor, 0, 4, 1, 1)
        self.pbSetNumImages = QtWidgets.QPushButton(GridView)
        self.pbSetNumImages.setObjectName("pbSetNumImages")
        self.gridLayout.addWidget(self.pbSetNumImages, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(GridView)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.retranslateUi(GridView)
        QtCore.QMetaObject.connectSlotsByName(GridView)

    def retranslateUi(self, GridView):
        _translate = QtCore.QCoreApplication.translate
        GridView.setWindowTitle(_translate("GridView", "Form"))
        self.pbSetNumImages.setText(_translate("GridView", "Set Number of Images"))
        self.label.setText(_translate("GridView", "Zoom factor: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GridView = QtWidgets.QWidget()
    ui = Ui_GridView()
    ui.setupUi(GridView)
    GridView.show()
    sys.exit(app.exec_())

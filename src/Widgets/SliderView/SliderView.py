# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SliderView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SliderView(object):
    def setupUi(self, SliderView):
        SliderView.setObjectName("SliderView")
        SliderView.resize(1301, 795)
        self.verticalLayout = QtWidgets.QVBoxLayout(SliderView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbImage = QtWidgets.QLabel(SliderView)
        self.lbImage.setObjectName("lbImage")
        self.verticalLayout.addWidget(self.lbImage)
        self.groupBox = QtWidgets.QGroupBox(SliderView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbLoadImg1 = QtWidgets.QPushButton(self.groupBox)
        self.pbLoadImg1.setMinimumSize(QtCore.QSize(0, 50))
        self.pbLoadImg1.setObjectName("pbLoadImg1")
        self.horizontalLayout.addWidget(self.pbLoadImg1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbLoadImg2 = QtWidgets.QPushButton(self.groupBox)
        self.pbLoadImg2.setMinimumSize(QtCore.QSize(0, 50))
        self.pbLoadImg2.setObjectName("pbLoadImg2")
        self.horizontalLayout.addWidget(self.pbLoadImg2)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sbMarkerWidth = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbMarkerWidth.sizePolicy().hasHeightForWidth())
        self.sbMarkerWidth.setSizePolicy(sizePolicy)
        self.sbMarkerWidth.setMinimumSize(QtCore.QSize(82, 0))
        self.sbMarkerWidth.setMaximum(10)
        self.sbMarkerWidth.setProperty("value", 5)
        self.sbMarkerWidth.setObjectName("sbMarkerWidth")
        self.horizontalLayout.addWidget(self.sbMarkerWidth)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(SliderView)
        QtCore.QMetaObject.connectSlotsByName(SliderView)

    def retranslateUi(self, SliderView):
        _translate = QtCore.QCoreApplication.translate
        SliderView.setWindowTitle(_translate("SliderView", "Form"))
        self.lbImage.setText(_translate("SliderView", "Please load images to display"))
        self.pbLoadImg1.setText(_translate("SliderView", "Load Image 1"))
        self.pbLoadImg2.setText(_translate("SliderView", "Load Image 2"))
        self.label.setText(_translate("SliderView", "Marker width:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SliderView = QtWidgets.QWidget()
    ui = Ui_SliderView()
    ui.setupUi(SliderView)
    SliderView.show()
    sys.exit(app.exec_())

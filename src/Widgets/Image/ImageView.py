# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Image(object):
    def setupUi(self, Image):
        Image.setObjectName("Image")
        Image.resize(781, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(Image)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbImage = QtWidgets.QLabel(Image)
        self.lbImage.setObjectName("lbImage")
        self.verticalLayout.addWidget(self.lbImage)
        self.pbLoad = QtWidgets.QPushButton(Image)
        self.pbLoad.setObjectName("pbLoad")
        self.verticalLayout.addWidget(self.pbLoad)

        self.retranslateUi(Image)
        QtCore.QMetaObject.connectSlotsByName(Image)

    def retranslateUi(self, Image):
        _translate = QtCore.QCoreApplication.translate
        Image.setWindowTitle(_translate("Image", "Form"))
        self.lbImage.setText(_translate("Image", "TextLabel"))
        self.pbLoad.setText(_translate("Image", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image = QtWidgets.QWidget()
    ui = Ui_Image()
    ui.setupUi(Image)
    Image.show()
    sys.exit(app.exec_())

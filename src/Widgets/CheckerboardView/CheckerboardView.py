# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckerboardView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckerboardView(object):
    def setupUi(self, CheckerboardView):
        CheckerboardView.setObjectName("CheckerboardView")
        CheckerboardView.resize(1301, 795)
        self.verticalLayout = QtWidgets.QVBoxLayout(CheckerboardView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbImage = QtWidgets.QLabel(CheckerboardView)
        self.lbImage.setObjectName("lbImage")
        self.verticalLayout.addWidget(self.lbImage)
        self.groupBox = QtWidgets.QGroupBox(CheckerboardView)
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
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(CheckerboardView)
        QtCore.QMetaObject.connectSlotsByName(CheckerboardView)

    def retranslateUi(self, CheckerboardView):
        _translate = QtCore.QCoreApplication.translate
        CheckerboardView.setWindowTitle(_translate("CheckerboardView", "Form"))
        self.lbImage.setText(_translate("CheckerboardView", "CheckerBoard"))
        self.pbLoadImg1.setText(_translate("CheckerboardView", "Load Image 1"))
        self.pbLoadImg2.setText(_translate("CheckerboardView", "Load Image 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckerboardView = QtWidgets.QWidget()
    ui = Ui_CheckerboardView()
    ui.setupUi(CheckerboardView)
    CheckerboardView.show()
    sys.exit(app.exec_())
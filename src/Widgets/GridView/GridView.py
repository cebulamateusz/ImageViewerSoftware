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
        self.glLayout = QtWidgets.QGridLayout()
        self.glLayout.setObjectName("glLayout")
        self.gridLayout.addLayout(self.glLayout, 0, 0, 1, 1)

        self.retranslateUi(GridView)
        QtCore.QMetaObject.connectSlotsByName(GridView)

    def retranslateUi(self, GridView):
        _translate = QtCore.QCoreApplication.translate
        GridView.setWindowTitle(_translate("GridView", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GridView = QtWidgets.QWidget()
    ui = Ui_GridView()
    ui.setupUi(GridView)
    GridView.show()
    sys.exit(app.exec_())

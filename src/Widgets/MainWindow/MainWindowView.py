# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbGridView = QtWidgets.QPushButton(self.groupBox)
        self.pbGridView.setMinimumSize(QtCore.QSize(100, 100))
        self.pbGridView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pbGridView.setObjectName("pbGridView")
        self.verticalLayout.addWidget(self.pbGridView)
        self.pbSliderView = QtWidgets.QPushButton(self.groupBox)
        self.pbSliderView.setMinimumSize(QtCore.QSize(100, 100))
        self.pbSliderView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pbSliderView.setObjectName("pbSliderView")
        self.verticalLayout.addWidget(self.pbSliderView)
        self.pbCheckerboardView = QtWidgets.QPushButton(self.groupBox)
        self.pbCheckerboardView.setMinimumSize(QtCore.QSize(100, 100))
        self.pbCheckerboardView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pbCheckerboardView.setObjectName("pbCheckerboardView")
        self.verticalLayout.addWidget(self.pbCheckerboardView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gbView = QtWidgets.QGroupBox(self.centralwidget)
        self.gbView.setTitle("")
        self.gbView.setObjectName("gbView")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vlView = QtWidgets.QVBoxLayout()
        self.vlView.setObjectName("vlView")
        self.verticalLayout_3.addLayout(self.vlView)
        self.horizontalLayout.addWidget(self.gbView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionGridView = QtWidgets.QAction(MainWindow)
        self.actionGridView.setObjectName("actionGridView")
        self.actionCheckerboardView = QtWidgets.QAction(MainWindow)
        self.actionCheckerboardView.setObjectName("actionCheckerboardView")
        self.actionSliderView = QtWidgets.QAction(MainWindow)
        self.actionSliderView.setObjectName("actionSliderView")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbGridView.setText(_translate("MainWindow", "Grid View"))
        self.pbSliderView.setText(_translate("MainWindow", "Slider View"))
        self.pbCheckerboardView.setText(_translate("MainWindow", "Checkerboard \n"
"View"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File"))
        self.actionGridView.setText(_translate("MainWindow", "GridView"))
        self.actionCheckerboardView.setText(_translate("MainWindow", "CheckerboardView"))
        self.actionSliderView.setText(_translate("MainWindow", "SliderView"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

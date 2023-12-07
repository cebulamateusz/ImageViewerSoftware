# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AssignmentsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Assignment(object):
    def setupUi(self, Assignment):
        Assignment.setObjectName("Assignment")
        Assignment.resize(1362, 783)
        self.gridLayout = QtWidgets.QGridLayout(Assignment)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(Assignment)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(Assignment)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.twUsers = QtWidgets.QTableWidget(self.groupBox)
        self.twUsers.setObjectName("twUsers")
        self.twUsers.setColumnCount(0)
        self.twUsers.setRowCount(0)
        self.verticalLayout_4.addWidget(self.twUsers)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Assignment)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.twAssignedVehicles = QtWidgets.QTableWidget(self.groupBox_3)
        self.twAssignedVehicles.setObjectName("twAssignedVehicles")
        self.twAssignedVehicles.setColumnCount(0)
        self.twAssignedVehicles.setRowCount(0)
        self.verticalLayout_5.addWidget(self.twAssignedVehicles)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Assignment)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.twAvailableVehicles = QtWidgets.QTableWidget(self.groupBox_2)
        self.twAvailableVehicles.setObjectName("twAvailableVehicles")
        self.twAvailableVehicles.setColumnCount(0)
        self.twAvailableVehicles.setRowCount(0)
        self.verticalLayout_6.addWidget(self.twAvailableVehicles)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 3, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Assignment)
        self.groupBox_4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.groupBox_4)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout_2.addWidget(self.btnRemove)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(Assignment)
        QtCore.QMetaObject.connectSlotsByName(Assignment)

    def retranslateUi(self, Assignment):
        _translate = QtCore.QCoreApplication.translate
        Assignment.setWindowTitle(_translate("Assignment", "Form"))
        self.btnClose.setText(_translate("Assignment", "Close"))
        self.groupBox.setTitle(_translate("Assignment", "Users"))
        self.groupBox_3.setTitle(_translate("Assignment", "Assigned vehicles"))
        self.groupBox_2.setTitle(_translate("Assignment", "Available vehicles"))
        self.groupBox_4.setTitle(_translate("Assignment", "Operations"))
        self.btnAdd.setText(_translate("Assignment", "<<"))
        self.btnRemove.setText(_translate("Assignment", ">>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Assignment = QtWidgets.QWidget()
    ui = Ui_Assignment()
    ui.setupUi(Assignment)
    Assignment.show()
    sys.exit(app.exec_())

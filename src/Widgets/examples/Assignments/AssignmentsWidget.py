from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Widgets.Assignments.AssignmentsView import Ui_Assignment
from Data import DataProvider
import base64
from Data.Entities import User, Vehicle, UserVehicleAssociation


class AssignmentsWidget(QWidget, Ui_Assignment):

    def __init__(self, *args, obj=None, **kwargs):
        super(AssignmentsWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.__add_assigned_vehicle)
        self.btnRemove.clicked.connect(self.__remove_assigned_vehicle)
        self.btnClose.clicked.connect(self.__close_widget)
        self.init_tw_users()
        self.init_tw_assigned_vehicles()
        self.init_tw_available_vehicles()
        self.fill_users_list()

    @pyqtSlot()
    def __add_assigned_vehicle(self) -> None:
        id_user = self.get_id_of_selected_item(self.twUsers)
        if id_user is None:
            self.__showTestMsgBox("A user must be selected!")
            return
        id_available_vehicle = self.get_id_of_selected_item(self.twAvailableVehicles)
        if id_available_vehicle is None:
            self.__showTestMsgBox("A vehicle must be selected from available vehicles table!")
            return
        user_vehicle = UserVehicleAssociation(id_user, id_available_vehicle)
        DataProvider.insert_user_vehicle_association_table(user_vehicle)
        self.fill_available_vehicles()
        self.fill_assigned_vehicles()
        self.__showTestMsgBox("Vehicle assigned to user successfully!")

    @pyqtSlot()
    def __remove_assigned_vehicle(self) -> None:
        id_user = self.get_id_of_selected_item(self.twUsers)
        if id_user is None:
            self.__showTestMsgBox("A user must be selected!")
            return
        id_assigned_vehicle = self.get_id_of_selected_item(self.twAssignedVehicles)
        if id_assigned_vehicle is None:
            self.__showTestMsgBox("A vehicle must be selected from assigned vehicles table!")
            return
        DataProvider.remove_user_vehicle_association_table(id_user, id_assigned_vehicle)
        self.fill_available_vehicles()
        self.fill_assigned_vehicles()
        self.__showTestMsgBox("Association between selected user and vehicle removed successfully!")

    @pyqtSlot()
    def __close_widget(self) -> None:
        self.close()

    def __showTestMsgBox(self, string: str) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(string)
        msgBox.setWindowTitle("Assignment information")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('Clicked ok.')

    def init_tw_users(self):
        self.twUsers.verticalHeader().setVisible(False)
        self.twUsers.setMinimumWidth(302)
        self.twUsers.setMinimumHeight(200)
        self.twUsers.setColumnCount(4)
        self.twUsers.setColumnWidth(0, 50)
        self.twUsers.setColumnWidth(1, 150)
        self.twUsers.setColumnWidth(2, 150)
        self.twUsers.setColumnWidth(3, 150)
        self.twUsers.setSelectionMode(1)
        self.twUsers.setSelectionBehavior(1)
        header_labels = ["UserID", "UserLogin", "Name", "Surname"]
        self.twUsers.setHorizontalHeaderLabels(header_labels)
        header = self.twUsers.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.twUsers.itemSelectionChanged.connect(self.user_select_changed)

    def fill_users_list(self) -> None:
        self.twUsers.setRowCount(0)
        users = DataProvider.get_all_users()
        for user in users:
            self.add_to_tw_users(user)

    def add_to_tw_users(self, user: User) -> None:
        self.twUsers.insertRow(self.twUsers.rowCount())
        self.twUsers.setItem(self.twUsers.rowCount() - 1, 0, QTableWidgetItem(str(user.id_user)))
        self.twUsers.setItem(self.twUsers.rowCount() - 1, 1, QTableWidgetItem(user.login))
        self.twUsers.setItem(self.twUsers.rowCount() - 1, 2, QTableWidgetItem(user.name))
        self.twUsers.setItem(self.twUsers.rowCount() - 1, 3, QTableWidgetItem(user.surname))

    def init_tw_assigned_vehicles(self):
        self.twAssignedVehicles.verticalHeader().setVisible(False)
        self.twAssignedVehicles.setMinimumWidth(200)
        self.twAssignedVehicles.setMinimumHeight(200)
        self.twAssignedVehicles.setColumnCount(2)
        self.twAssignedVehicles.setColumnWidth(0, 50)
        self.twAssignedVehicles.setColumnWidth(1, 150)
        self.twAssignedVehicles.setSelectionMode(1)
        self.twAssignedVehicles.setSelectionBehavior(1)
        header_labels = ["Vehicle ID", "Vehicle Name"]
        self.twAssignedVehicles.setHorizontalHeaderLabels(header_labels)
        header = self.twAssignedVehicles.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def fill_assigned_vehicles(self):
        self.twAssignedVehicles.setRowCount(0)
        id_user = self.get_id_of_selected_item(self.twUsers)
        if id_user is None:
            return
        user_vehicles = DataProvider.get_user_vehicle_association_by_user_id(id_user)
        for uv in user_vehicles:
            vehicle = DataProvider.get_vehicle_by_id(uv.vehicle_id)
            self.add_to_tw_vehicles(vehicle, self.twAssignedVehicles)

    @staticmethod
    def add_to_tw_vehicles(vehicle: Vehicle, table: QTableWidget) -> None:
        table.insertRow(table.rowCount())
        table.setItem(table.rowCount() - 1, 0, QTableWidgetItem(str(vehicle.id_vehicle)))
        table.setItem(table.rowCount() - 1, 1, QTableWidgetItem(vehicle.name))

    def init_tw_available_vehicles(self):
        self.twAvailableVehicles.verticalHeader().setVisible(False)
        self.twAvailableVehicles.setMinimumWidth(200)
        self.twAvailableVehicles.setMinimumHeight(200)
        self.twAvailableVehicles.setColumnCount(2)
        self.twAvailableVehicles.setColumnWidth(0, 50)
        self.twAvailableVehicles.setColumnWidth(1, 150)
        self.twAvailableVehicles.setSelectionMode(1)
        self.twAvailableVehicles.setSelectionBehavior(1)
        header_labels = ["Vehicle ID", "Vehicle Name"]
        self.twAvailableVehicles.setHorizontalHeaderLabels(header_labels)
        header = self.twAvailableVehicles.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def fill_available_vehicles(self):
        self.twAvailableVehicles.setRowCount(0)
        id_user = self.get_id_of_selected_item(self.twUsers)
        if id_user is None:
            return
        available_vehicles = DataProvider.get_vehicles_not_associated_to_user(id_user)
        for av in available_vehicles:
            self.add_to_tw_vehicles(av, self.twAvailableVehicles)

    @staticmethod
    def get_id_of_selected_item(table: QTableWidget):
        id_item = table.item(table.currentRow(), 0)

        if id_item is None:
            return None
        id_str = id_item.text()
        id_result = int(id_str)
        return id_result

    def user_select_changed(self):
        self.fill_available_vehicles()
        self.fill_assigned_vehicles()

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from Widgets.Vehicles.VehiclesView import Ui_Vehicles
from Data import DataProvider
from Data.Entities import Vehicle, Parameter
from Common import ParameterTypes


class VehiclesWidget(QWidget, Ui_Vehicles):

    def __init__(self, *args, obj=None, **kwargs):
        super(VehiclesWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.__add_vehicle)
        self.btnUpdate.clicked.connect(self.__update_vehicle)
        self.btnClose.clicked.connect(self.__close_widget)
        self.btnDelete.clicked.connect(self.__delete_vehicle)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setMinimumWidth(700)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.setColumnWidth(8, 200)
        self.tableWidget.setSelectionMode(1)
        self.tableWidget.setSelectionBehavior(1)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Name Left",
                                                    "URL Left", "Name Right", "URL Right",
                                                    "Name FE", "URL FE", "URL RESET"])

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.fill_table_widget()

    @pyqtSlot()
    def __add_vehicle(self) -> None:
        name = self.leName.text()
        name_right = self.leNameRight.text()
        name_left = self.leNameLeft.text()
        name_fe = self.leNameFE.text()
        address_right = self.leAddressRight.text()
        address_left = self.leAddressLeft.text()
        address_fe = self.leAddressFE.text()
        address_reset_server = self.leAddressServerReset.text()
        if not name:
            self.__showTestMsgBox("Name field must not be empty!")
            return
        if not name_fe:
            self.__showTestMsgBox("Name FE must not be empty!")
            return
        if not address_fe:
            self.__showTestMsgBox("Address FE must not be empty!")
            return
        if not name_left:
            self.__showTestMsgBox("Name Left must not be empty!")
            return
        if not address_left:
            self.__showTestMsgBox("Address Left must not be empty!")
            return
        if not name_right:
            self.__showTestMsgBox("Name Right must not be empty!")
            return
        if not address_right:
            self.__showTestMsgBox("Address Right must not be empty!")
            return
        if not address_reset_server:
            self.__showTestMsgBox("Address Reset Camera Server field must not be empty!")
        existing_vehicles = DataProvider.get_vehicles_by_name(name)
        if existing_vehicles:
            self.__showTestMsgBox("Vehicle with provided name already exists!")
            return
        vehicle = Vehicle(name)
        parameters = list(
            self.fill_parameters_list(name_left, name_right, name_fe, address_left, address_right, address_fe, address_reset_server))
        vehicle.parameters = parameters
        DataProvider.insert_vehicle(vehicle)

        self.fill_table_widget()
        self.__showTestMsgBox("Vehicle added successfully!")

    @pyqtSlot()
    def __delete_vehicle(self) -> None:
        id_vehicle = self.get_id_of_selected_vehicle()
        if id_vehicle is None:
            self.__showTestMsgBox("Row must be selected to be deleted!")
            return
        DataProvider.remove_parameters_by_vehicle_id(id_vehicle)
        DataProvider.remove_vehicle(id_vehicle)
        self.fill_table_widget()
        self.__showTestMsgBox("Row deleted successfully!")

    @pyqtSlot()
    def __close_widget(self) -> None:
        self.close()

    @pyqtSlot()
    def __update_vehicle(self) -> None:
        id_vehicle = self.get_id_of_selected_vehicle()
        if id_vehicle is None:
            self.__showTestMsgBox("Row must be selected to be updated!")
            return
        vehicle = DataProvider.get_vehicle_by_id(id_vehicle)

        if vehicle is None:
            self.__showTestMsgBox("There is no such vehicle in the database!")
            return
        parameters = DataProvider.get_parameters_by_vehicle_id(vehicle.id_vehicle)
        name = self.leName.text()
        name_right = self.leNameRight.text()
        name_left = self.leNameLeft.text()
        name_fe = self.leNameFE.text()
        address_right = self.leAddressRight.text()
        address_left = self.leAddressLeft.text()
        address_fe = self.leAddressFE.text()
        address_server_reset = self.leAddressServerReset.text()
        if name:
            existing_vehicles = DataProvider.get_vehicles_by_name(name)
            if (name != vehicle.name) and (existing_vehicles is not None):
                self.__showTestMsgBox("Vehicle with provided name already exists!")
                return
            vehicle.set_name(name)
            DataProvider.update_vehicle(vehicle)

        if address_fe:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_fish_eye_url]
            param[0].set_value(address_fe)
            DataProvider.update_parameter(param[0])

        if address_left:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_left_url]
            param[0].set_value(address_left)
            DataProvider.update_parameter(param[0])

        if address_right:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_right_url]
            param[0].set_value(address_right)
            DataProvider.update_parameter(param[0])

        if name_fe:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_fish_eye_name]
            param[0].set_value(name_fe)
            DataProvider.update_parameter(param[0])

        if name_left:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_left_name]
            param[0].set_value(name_left)
            DataProvider.update_parameter(param[0])

        if name_right:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_right_name]
            param[0].set_value(name_right)
            DataProvider.update_parameter(param[0])

        if address_server_reset:
            param = [x for x in parameters if x.parameter_data_type == ParameterTypes.camera_server_restart_url]
            param[0].set_value(address_server_reset)
            DataProvider.update_parameter(param[0])


        self.fill_table_widget()
        self.__showTestMsgBox("Vehicle updated successfully!")

    def __showTestMsgBox(self, string: str) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(string)
        msgBox.setWindowTitle("Vehicle information")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('Clicked ok.')

    def fill_table_widget(self) -> None:
        self.tableWidget.setRowCount(0)
        vehicles = DataProvider.get_all_vehicles()
        for v in vehicles:
            self.add_to_table_widget(v)

    def add_to_table_widget(self, vehicle: Vehicle) -> None:
        params = DataProvider.get_parameters_by_vehicle_id(vehicle.id_vehicle)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(vehicle.id_vehicle)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(vehicle.name)))
        for param in params:
            if param.parameter_data_type == ParameterTypes.camera_left_name:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_left_url:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_right_name:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_right_url:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 5, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_fish_eye_name:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 6, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_fish_eye_url:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 7, QTableWidgetItem(param.value))
            elif param.parameter_data_type == ParameterTypes.camera_server_restart_url:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 8, QTableWidgetItem(param.value))

    def get_id_of_selected_vehicle(self):
        id_item = self.tableWidget.item(self.tableWidget.currentRow(), 0)

        if id_item is None:
            return None
        id_str = id_item.text()
        id_vehicle = int(id_str)
        return id_vehicle

    def fill_parameters_list(self, name_left: str, name_right: str, name_fe: str, url_left: str, url_right: str, url_fe: str, url_serv_reset: str) -> list:
        parameters = []
        parameter = Parameter(ParameterTypes.camera_left_name, name_left)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_right_name, name_right)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_fish_eye_name, name_fe)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_left_url, url_left)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_right_url, url_right)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_fish_eye_url, url_fe)
        parameters.append(parameter)
        parameter = Parameter(ParameterTypes.camera_server_restart_url, url_serv_reset)
        parameters.append(parameter)
        return parameters

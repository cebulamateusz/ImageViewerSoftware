import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from Data import DataProvider
from Shared.Camera import CameraThread
from Data.Entities import Vehicle, Parameter
from Common import ParameterTypes
from Widgets.SingleVehiclePreview.SingleVehiclesPreviewView import Ui_SingleVehiclesPreview
from Widgets.CameraPreview.CameraPreviewWidget import CameraPreviewWidget


class VehicleModel(QAbstractListModel):
    def __init__(self, data, parent=None):
        super(VehicleModel, self).__init__(parent)
        self.data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self.data[index.row()].name)
        return None

    def getObject(self, index):
        return self.data[index]


class SingleVehiclesPreviewWidget(QWidget, Ui_SingleVehiclesPreview):

    __id_logged_user: int
    __associated_vehicle: Vehicle
    __vehicle_params: []
    __all_associated_vehicles: []
    __widgets = []
    close_signal = pyqtSignal()
    __is_init = False
    __detection: str
    __detection_dict: dict

    def __init__(self, vehicle: Vehicle, all_vehicles: [], detection_dict: dict):
        super(SingleVehiclesPreviewWidget, self).__init__()
        self.setupUi(self)
        self.__associated_vehicle = vehicle
        self.__detection_dict = detection_dict

        self.__all_associated_vehicles = all_vehicles
        model = VehicleModel(self.__all_associated_vehicles)
        self.cbVehicleChoice.setModel(model)
        self.cbVehicleChoice.currentIndexChanged.connect(self.on_combobox_selected)
        self.btnMultiVehicle.clicked.connect(self.on_multi_veh_clicked)

        self.__widgets = []

        self.init_widgets()
        self.cbVehicleChoice.setCurrentText(self.__associated_vehicle.name)

    def init_widgets(self):
        if self.__is_init:
            return
        self.__vehicle_params = DataProvider.get_parameters_by_vehicle_id(self.__associated_vehicle.id_vehicle)

        for i in range(1, 4):
            widget: CameraPreviewWidget
            widget = CameraPreviewWidget(self.chooseParameter(i+1).value, self.chooseParameter(i+4).value, self.chooseParameter(ParameterTypes.camera_server_restart_url).value)
            widget.initialized()

            # Set the size policy for each widget
            policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            widget.setSizePolicy(policy)
            widget.setMinimumWidth(300)
            widget.setMinimumHeight(300)

            self.__widgets.append(widget)
        self.__is_init = True
        self.update_widget()

    def update_widget(self):

        if self.__associated_vehicle.id_vehicle in self.__detection_dict:
            self.__detection = self.__detection_dict[self.__associated_vehicle.id_vehicle]
        else:
            self.__detection = "Vehicle id: " + str(self.__associated_vehicle.id_vehicle) + "\nNO DETECTIONS FOUND!"

        self.lblVehicleData.setText(self.__detection)
        i = 0

        for vg in self.__widgets:
            if i == 0:
                self.glCamLeft.addWidget(vg)
            elif i == 1:
                self.glCamRight.addWidget(vg)
            elif i == 2:
                self.glCamFe.addWidget(vg)
            else:
                return
            i = i + 1

    @pyqtSlot()
    def on_multi_veh_clicked(self):
        self.close_signal.emit()
        self.close()

    def on_combobox_selected(self, index):
        selected_object = self.cbVehicleChoice.model().getObject(index)
        self.__associated_vehicle = selected_object

        i = 0
        for vg in self.__widgets:
            if i == 0:
                self.glCamLeft.removeWidget(vg)

            elif i == 1:
                self.glCamRight.removeWidget(vg)
            elif i == 2:
                self.glCamFe.removeWidget(vg)
            else:
                break
            vg.close()
            i = i + 1

        for widget in self.__widgets:
            self.__widgets.remove(widget)

        self.__widgets = []
        self.__is_init = False

        self.init_widgets()

    def chooseParameter(self, paramToChoose: int) -> Parameter:
        for par in self.__vehicle_params:
            if par.parameter_data_type == paramToChoose:
                return par

    def print_detections(self, vehicle_id: int, detection: str):
        if self.__associated_vehicle.id_vehicle == vehicle_id:
            self.lblVehicleData.setText(detection)

    def close(self):
        i = 0
        for vg in self.__widgets:
            if i == 0:
                self.glCamLeft.removeWidget(vg)

            elif i == 1:
                self.glCamRight.removeWidget(vg)
            elif i == 2:
                self.glCamFe.removeWidget(vg)
            else:
                break
            vg.close()
            i = i + 1

        for widget in self.__widgets:
            self.__widgets.remove(widget)

        self.__widgets = []
        self.__is_init = False


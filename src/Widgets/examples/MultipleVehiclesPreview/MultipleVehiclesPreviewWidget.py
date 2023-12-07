import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from Data import DataProvider
from Shared.Camera import CameraThread
from Widgets.MultipleVehiclesPreview.MultipleVehiclesPreviewView import Ui_MultipleVehiclesPreview
from Widgets.VehiclePreview.VehiclePreviewWidget import VehiclePreviewWidget
from Data.Entities import Vehicle


class MultipleVehiclesPreviewWidget(QWidget, Ui_MultipleVehiclesPreview):

    __rows_num = 0
    __columns_num = 4
    __vehicles_num = 0
    __id_logged_user: int
    __associated_vehicles = []
    __cam_thread: CameraThread
    __widgets = []
    vehicle_preview_signal = pyqtSignal(Vehicle)

    def __init__(self):
        super(MultipleVehiclesPreviewWidget, self).__init__()
        self.setupUi(self)
        self.widget_min_width = 300  # Minimum width for each widget
        self.min_columns = 2  # Minimum number of columns
        self.max_columns = 5  # Maximum number of columns
        self.setMinimumWidth(700)

    def init_widgets(self):
        for veh in self.__associated_vehicles:
            widget: VehiclePreviewWidget
            widget = VehiclePreviewWidget(veh)
            widget.initialized()

            # Set the size policy for each widget
            policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            widget.setSizePolicy(policy)
            widget.setMinimumWidth(300)
            widget.setMinimumHeight(300)
            widget.mouse_click_signal.connect(self.handle_mouse_click_signal)

            self.__widgets.append(widget)

        self.update_columns()

    def update_columns(self):
        window_width = self.width()
        column_count = max(self.min_columns, min(window_width // (self.widget_min_width + 25), self.max_columns))
        row_count = (self.__vehicles_num - 1) // column_count + 1

        for i in range(self.__vehicles_num):
            widget = self.__widgets[i]
            self.gridMultipleVehiclesPreview.removeWidget(widget)

        for i, widget in enumerate(self.__widgets):
            row = i // column_count
            col = i % column_count
            self.gridMultipleVehiclesPreview.addWidget(widget, row, col)

            policy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            widget.setSizePolicy(policy)
            widget.setFixedWidth(max(self.widget_min_width, int(self.width() / column_count) - 30))

        self.gridMultipleVehiclesPreview.setRowStretch(row_count, 1)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_columns()

        event.accept()

    def init_2(self, user_id: int) -> None:
        self.__id_logged_user = user_id
        self.__associated_vehicles = []
        __rows_num = 0
        __vehicles_num = 0
        if self.__id_logged_user < 0:
            return
        user_vehicles = DataProvider.get_user_vehicle_association_by_user_id(self.__id_logged_user)
        for uv in user_vehicles:
            vehicle = DataProvider.get_vehicle_by_id(uv.vehicle_id)
            self.__associated_vehicles.append(vehicle)
            self.__vehicles_num = self.__associated_vehicles.__len__()
        self.__rows_num = int((self.__vehicles_num / self.__columns_num)) + 1
        self.__widgets = []

        self.init_widgets()

    def initialize(self, user_id: int) -> None:
        self.__id_logged_user = user_id
        self.__associated_vehicles = []
        __rows_num = 0
        __columns_num = 4
        __vehicles_num = 0

        if self.__id_logged_user < 0:
            return
        user_vehicles = DataProvider.get_user_vehicle_association_by_user_id(self.__id_logged_user)
        self.__columns_num = int(self.width() / 302)
        for uv in user_vehicles:
            vehicle = DataProvider.get_vehicle_by_id(uv.vehicle_id)
            self.__associated_vehicles.append(vehicle)
            self.__vehicles_num = self.__associated_vehicles.__len__()
        self.__rows_num = int((self.__vehicles_num / self.__columns_num)) + 1
        for i in range(self.__rows_num):
            for j in range(self.__columns_num):
                if self.__columns_num*i + j == self.__vehicles_num:
                    return
                widget = VehiclePreviewWidget()
                widget.initialized()
                self.gridMultipleVehiclesPreview.addWidget(widget, i, j)

    def handle_mouse_click_signal(self, selected_vehicle: Vehicle):
        self.vehicle_preview_signal.emit(selected_vehicle)
        self.close()

    def close(self):
        for widget in self.__widgets:
            widget: VehiclePreviewWidget
            widget.close()

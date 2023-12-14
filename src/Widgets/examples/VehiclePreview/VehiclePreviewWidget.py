import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from Shared.Camera import CameraThread
from Widgets.VehiclePreview.VehiclePreviewView import Ui_VehiclePreviewView
from Data.Entities import Vehicle, Parameter
from Data import DataProvider
from Common import ParameterTypes


class VehiclePreviewWidget(QWidget, Ui_VehiclePreviewView):
    mouse_click_signal = pyqtSignal(Vehicle)

    __cam_fe_thread: CameraThread
    __associated_vehicle: Vehicle
    __vehicle_parameters: list
    cam_error = False

    def __init__(self, vehicle: Vehicle):
        super(VehiclePreviewWidget, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(300)
        self.__associated_vehicle = vehicle
        self.__vehicle_parameters = DataProvider.get_parameters_by_vehicle_id(vehicle.id_vehicle)

    def __cam_error(self, is_true: bool):
        if is_true:
            self.lbCameraPreview.clear()
            self.lbCameraPreview.setText("Camera thread error. Check your connection or addressing!")
            self.cam_error = True
        else:
            self.cam_error = False

    def initialized(self) -> None:
        self.lbTextDetails.setMinimumHeight(50)
        self.lbTextDetails.setText("Vehicle name: " + self.__associated_vehicle.name + "\nFE name: "
                                   + self.chooseParameter(ParameterTypes.camera_fish_eye_name).value
                                   + "\nFE address: " + self.chooseParameter(ParameterTypes.camera_fish_eye_url).value)
        self.__cam_fe_thread = CameraThread(self.chooseParameter(ParameterTypes.camera_server_restart_url).value)
        self.__cam_fe_thread.error_signal.connect(self.__cam_error)
        self.__cam_fe_thread.camera_name = self.chooseParameter(ParameterTypes.camera_fish_eye_name).value
        self.__cam_fe_thread.rtsp_url = self.chooseParameter(ParameterTypes.camera_fish_eye_url).value
        self.__cam_fe_thread.new_frame.connect(self.draw_frame)
        self.__cam_fe_thread.start()

    @pyqtSlot(np.ndarray, str)
    def draw_frame(self, frame: np.ndarray, camera_name: str) -> None:
        if self.cam_error:
            return
        qt_format = self.cv2_to_qimage(frame)
        new_img = qt_format.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.lbCameraPreview.setPixmap(QPixmap.fromImage(new_img))

    def cv2_to_qimage(self, frame: np.ndarray) -> QImage:
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return qt_format

    def resizeEvent(self, event):
        super(VehiclePreviewWidget, self).resizeEvent(event)
        event.accept()

    def chooseParameter(self, paramToChoose: int) -> Parameter:
        for par in self.__vehicle_parameters:
            if par.parameter_data_type == paramToChoose:
                return par

    def mouseDoubleClickEvent(self, event):
        self.mouse_click_signal.emit(self.__associated_vehicle)
        self.close()

    def close(self):
        self.__cam_fe_thread.stop()
        self.__cam_fe_thread.wait()


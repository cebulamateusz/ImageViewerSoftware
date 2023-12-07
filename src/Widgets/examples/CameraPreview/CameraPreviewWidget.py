import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from Shared.Camera import CameraThread
from Widgets.CameraPreview.CameraPreviewView import Ui_CameraPreviewView


class CameraPreviewWidget(QWidget, Ui_CameraPreviewView):

    __cam_thread: CameraThread
    __camera_name: str
    __camera_url: str

    __reset_url: str

    cam_error = False

    __wrong_address = False

    def __init__(self, camera_name: str, camera_url: str, reset_url: str):
        super(CameraPreviewWidget, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(300)
        self.__camera_name = camera_name
        self.__camera_url = camera_url
        self.__reset_url = reset_url

    def __cam_error(self, is_true: bool):
        if is_true:
            self.__cam_thread.stop()
            self.lbCameraPreview.clear()
            self.lbCameraPreview.setText("Camera thread error. Check your connection or addressing!")
            self.cam_error = True
        else:
            self.cam_error = False

    def initialized(self) -> None:
        self.lbTextDetails.setMinimumHeight(50)
        self.lbTextDetails.setText("Camera name: " + self.__camera_name
                                   + "\nCamera address: " + self.__camera_url)
        self.__cam_thread = CameraThread(self.__reset_url)
        self.__cam_thread.error_signal.connect(self.__cam_error)
        self.__cam_thread.camera_name = self.__camera_name
        self.__cam_thread.rtsp_url = self.__camera_url
        self.__cam_thread.new_frame.connect(self.draw_frame)
        self.__cam_thread.start()

    @pyqtSlot(np.ndarray, str)
    def draw_frame(self, frame: np.ndarray, camera_name: str) -> None:
        if self.cam_error:
            return
        qt_format = self.cv2_to_qimage(frame)
        or_width = qt_format.width()
        or_height = qt_format.height()
        new_img = qt_format.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.lbCameraPreview.setPixmap(QPixmap.fromImage(new_img))

    def cv2_to_qimage(self, frame: np.ndarray) -> QImage:
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return qt_format

    def resizeEvent(self, event):
        super(CameraPreviewWidget, self).resizeEvent(event)
        event.accept()

    def close(self):
        self.__cam_thread.stop()
        self.__cam_thread.wait()


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Widgets.MainWindow.MainWindowView import Ui_MainWindow
from Widgets.Users.UsersWidget import UsersWidget
from Widgets.Vehicles.VehiclesWidget import VehiclesWidget
from Widgets.Assignments.AssignmentsWidget import AssignmentsWidget
from Widgets.Login.LoginWidget import LoginWidget
from Widgets.MultipleVehiclesPreview.MultipleVehiclesPreviewWidget import MultipleVehiclesPreviewWidget
from Widgets.SingleVehiclePreview.SingleVehiclesPreviewWidget import SingleVehiclesPreviewWidget
from Data.Entities import Vehicle
from Data import DataProvider
from services.grpc.grpc_handler import GrpcHandler


class MainWindowWidget(QMainWindow, Ui_MainWindow):
    __usersWidget: UsersWidget
    __vehiclesWidget: VehiclesWidget
    __assignmentsWidget: AssignmentsWidget
    __multipleVehiclesPreviewWidget: MultipleVehiclesPreviewWidget
    __single_vehicle_preview_widget: SingleVehiclesPreviewWidget
    __loginWidget: LoginWidget
    __is_superuser: bool
    __is_logged_in: bool
    __id_logged_user = -1
    __grpc_handler = None
    __detection_dictionary = dict()

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindowWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.__usersWidget = None
        self.__vehiclesWidget = None
        self.__assignmentsWidget = None
        self.__single_vehicle_preview_widget = None
        self.__multipleVehiclesPreviewWidget = None
        self.__grpc_handler = GrpcHandler()
        self.__grpc_handler.serve_grpc_handler()
        self.__grpc_handler.handler_detection_signal.connect(self.__detection_grpc_signal_execute)
        self.actionUsers.triggered.connect(self.__set_users_widget)
        self.actionUsers.setEnabled(0)
        self.actionVehicles.triggered.connect(self.__set_vehicles_widget)
        self.actionVehicles.setEnabled(0)
        self.actionAssignment.triggered.connect(self.__set_assignment_widget)
        self.actionAssignment.setEnabled(0)
        self.actionLogout.triggered.connect(self.__logout)
        self.actionLogout.setEnabled(0)
        self.actionMultipleCameras.triggered.connect(self.__set_multicam_widget)
        self.actionMultipleCameras.setEnabled(0)
        self.__set_login_widget()

    @pyqtSlot(int, str)
    def __detection_grpc_signal_execute(self, vehicle_id, detection):
        print("CONNECTED")
        self.__detection_dictionary[vehicle_id] = detection

        if self.__single_vehicle_preview_widget is not None:
            self.__single_vehicle_preview_widget.print_detections(vehicle_id, detection)


    @pyqtSlot()
    def __set_users_widget(self):
        self.__usersWidget = UsersWidget()
        self.setCentralWidget(self.__usersWidget)

    @pyqtSlot()
    def __set_vehicles_widget(self):
        self.__vehiclesWidget = VehiclesWidget()
        self.setCentralWidget(self.__vehiclesWidget)

    @pyqtSlot()
    def __set_assignment_widget(self):
        self.__assignmentsWidget = AssignmentsWidget()
        self.setCentralWidget(self.__assignmentsWidget)

    @pyqtSlot()
    def __set_login_widget(self):
        self.__loginWidget = LoginWidget()
        self.__loginWidget.superuser_signal.connect(self.handle_superuser)
        self.setCentralWidget(self.__loginWidget)

    @pyqtSlot()
    def __set_single_vehicle_preview_widget(self, associated_vehicle):
        user_vehicles = DataProvider.get_user_vehicle_association_by_user_id(self.__id_logged_user)
        vehicle_list = []
        for uv in user_vehicles:
            vehicle = DataProvider.get_vehicle_by_id(uv.vehicle_id)
            vehicle_list.append(vehicle)
        self.__single_vehicle_preview_widget = SingleVehiclesPreviewWidget(associated_vehicle, vehicle_list, self.__detection_dictionary)
        self.__single_vehicle_preview_widget.close_signal.connect(self.handle_single_preview_close_signal)
        self.setCentralWidget(self.__single_vehicle_preview_widget)

    @pyqtSlot()
    def __set_multicam_widget(self):
        if self.__multipleVehiclesPreviewWidget:
            self.__multipleVehiclesPreviewWidget.close()
            self.__multipleVehiclesPreviewWidget = None
        self.__multipleVehiclesPreviewWidget = MultipleVehiclesPreviewWidget()
        self.__multipleVehiclesPreviewWidget.init_2(self.__id_logged_user)
        self.__multipleVehiclesPreviewWidget.vehicle_preview_signal.connect(self.handle_vehicle_preview_signal)
        self.setCentralWidget(self.__multipleVehiclesPreviewWidget)

    @pyqtSlot()
    def __logout(self):
        self.handle_superuser(False, False, -1)
        self.__set_login_widget()

    def handle_superuser(self, is_superuser: bool, is_logged_in: bool, user_id: int):
        self.__is_superuser = is_superuser
        self.__is_logged_in = is_logged_in
        self.__id_logged_user = user_id
        self.set_buttons()

    def handle_vehicle_preview_signal(self, vehicle: Vehicle):
        self.__set_single_vehicle_preview_widget(vehicle)

    def handle_single_preview_close_signal(self):
        self.__set_multicam_widget()

    def set_buttons(self):
        self.actionUsers.setEnabled(self.__is_superuser and self.__is_logged_in)
        self.actionVehicles.setEnabled(self.__is_superuser and self.__is_logged_in)
        self.actionAssignment.setEnabled(self.__is_superuser and self.__is_logged_in)
        self.actionMultipleCameras.setEnabled(self.__is_logged_in and (not self.__is_superuser))
        if self.__is_logged_in is False:
            self.actionLogout.setEnabled(False)
        else:
            if self.__is_superuser is False:
                self.__set_multicam_widget()
            self.actionLogout.setEnabled(True)

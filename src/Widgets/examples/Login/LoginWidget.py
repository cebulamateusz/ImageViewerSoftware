from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Widgets.Login.LoginView import Ui_Login
from Common import Globals
from Data import DataProvider
import base64
from Data.Entities import User


class LoginWidget(QWidget, Ui_Login):
    superuser_signal = pyqtSignal(bool, bool, int)

    def __init__(self, *args, obj=None, **kwargs):
        super(LoginWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.__login_user)

    @pyqtSlot()
    def __login_user(self) -> None:
        login = self.leLogin.text()
        password = self.lePassword.text()
        if not login:
            self.__showTestMsgBox("Login cannot be empty!")
            return
        if not password:
            self.__showTestMsgBox("Password cannot be empty!")
            return
        if login == Globals.superadmin_login and password == Globals.superadmin_pass:
            self.superuser_signal.emit(True, True, -2)
            self.close()
            return
        password_encoded = self.encode_password(password)
        user = DataProvider.get_user_by_credentials(login, password_encoded)
        if user is None:
            self.__showTestMsgBox("Login credentials incorrect!")
            return
        self.superuser_signal.emit(False, True, user.id_user)
        self.close()

    @staticmethod
    def encode_password(password_string: str) -> str:
        password_bytes = password_string.encode('ascii')
        base64_bytes = base64.b64encode(password_bytes)
        base64_password = base64_bytes.decode('ascii')
        return base64_password

    def __showTestMsgBox(self, string: str) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(string)
        msgBox.setWindowTitle("Login information")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('Clicked ok.')




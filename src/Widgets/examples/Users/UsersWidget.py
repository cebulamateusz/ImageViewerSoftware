from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Widgets.Users.UsersView import Ui_Users
from Data import DataProvider
import base64
from Data.Entities import User


class UsersWidget(QWidget, Ui_Users):

    def __init__(self, *args, obj=None, **kwargs):
        super(UsersWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.__add_user)
        self.btnDelete.clicked.connect(self.__delete_user)
        self.btnClose.clicked.connect(self.__close_widget)
        self.btnUpdate.clicked.connect(self.__update_user)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setMinimumWidth(502)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setSelectionMode(1)
        self.tableWidget.setSelectionBehavior(1)
        self.tableWidget.setHorizontalHeaderLabels(["UserID", "UserLogin", "Name", "Surname"])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.fill_table_widget()

    @pyqtSlot()
    def __add_user(self) -> None:
        login = self.leLogin.text()
        password = self.lePasswd.text()
        if not login:
            self.__showTestMsgBox("Login field must not be empty!")
            return
        if not password:
            self.__showTestMsgBox("Password field must not be empty!")
            return
        existing_users = DataProvider.get_users_by_login(login)
        if existing_users:
            self.__showTestMsgBox("User with provided login already exists!")
            return
        name = self.leName.text()
        surname = self.leSurname.text()
        password_encoded = self.encode_password(password)
        user = User(login, password_encoded, name, surname)
        DataProvider.insert_user(user)
        self.fill_table_widget()
        self.__showTestMsgBox("User added successfully!")

    @pyqtSlot()
    def __delete_user(self) -> None:
        id_user = self.get_id_of_selected_user()
        if id_user is None:
            self.__showTestMsgBox("Row must be selected to be deleted!")
            return
        DataProvider.remove_user(id_user)
        self.fill_table_widget()
        self.__showTestMsgBox("Row deleted successfully!")

    @pyqtSlot()
    def __close_widget(self) -> None:
        self.close()

    @pyqtSlot()
    def __update_user(self) -> None:
        id_user = self.get_id_of_selected_user()
        if id_user is None:
            self.__showTestMsgBox("Row must be selected to be updated!")
            return
        user = DataProvider.get_user_by_id(id_user)
        if user is None:
            self.__showTestMsgBox("There is no such user in the database!")
            return
        login = self.leLogin.text()
        password = self.lePasswd.text()
        name = self.leName.text()
        surname = self.leSurname.text()
        if login:
            existing_users = DataProvider.get_users_by_login(login)
            if (login != user.login) and (existing_users is not None):
                self.__showTestMsgBox("User with provided login already exists!")
                return
            user.set_login(login)

        if password:
            password_encoded = self.encode_password(password)
            user.set_password(password_encoded)

        if name:
            user.set_name(name)

        if surname:
            user.set_surname(surname)

        DataProvider.update_user(user)
        self.fill_table_widget()
        self.__showTestMsgBox("User updated successfully!")

    def __showTestMsgBox(self, string: str) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(string)
        msgBox.setWindowTitle("User information")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('Clicked ok.')

    def fill_table_widget(self) -> None:
        self.tableWidget.setRowCount(0)
        users = DataProvider.get_all_users()
        for u in users:
            self.add_to_table_widget(u)

    def add_to_table_widget(self, user: User) -> None:
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(user.id_user)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(user.login))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(user.name))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(user.surname))

    @staticmethod
    def encode_password(password_string: str) -> str:
        password_bytes = password_string.encode('ascii')
        base64_bytes = base64.b64encode(password_bytes)
        base64_password = base64_bytes.decode('ascii')
        return base64_password

    def get_id_of_selected_user(self):
        id_item = self.tableWidget.item(self.tableWidget.currentRow(), 0)

        if id_item is None:
            return None
        id_str = id_item.text()
        id_user = int(id_str)
        return id_user

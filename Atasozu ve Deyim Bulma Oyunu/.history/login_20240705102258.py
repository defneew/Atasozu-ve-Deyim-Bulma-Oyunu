from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from loginUI import Ui_MainWindow

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.loginform.first_button.clicked.connect(self.Login)
    def Login(self):
        personName = self.loginform.name_line.text()
        personSurname = self.loginform.surNmae_line.text()
        personMail = self.loginform.mail_line.text()
          

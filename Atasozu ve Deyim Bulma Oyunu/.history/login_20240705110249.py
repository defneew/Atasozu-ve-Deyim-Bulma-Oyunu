from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from loginUI import Ui_MainWindow
import sqlite3

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.loginform.first_button.clicked.connect(self.Login)
    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()
        self.connect.commit()
    def Login(self):
        personName = self.loginform.name_line.text()
        personSurname = self.loginform.surNmae_line.text()
        personMail = self.loginform.mail_line.text()
        self.connection()
        try:
            # print("{} {} {}".format(personName,personSurname,personMail))
            add = "INSERT INTO tbl_person(personName,personSurname,personMail,knownWordsID) values (?,?,?,?,?)"
            self.operation.execute(add,(personName,personSurname,personMail))
            self.connect.commit()
            self.loginform.statusbar.showMessage("Kayıt Eklendi...",10000)
        except:
            self.loginform.statusbar.showMessage("Kayıt Eklenemedi...",10000)    
        finally:
            self.connect.close()
        
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from loginUI import Ui_MainWindow
from category import CategoryPage
import sqlite3

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.categoryopen = CategoryPage()
        self.loginform.first_button.clicked.connect(self.Login)
    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()
    def Login(self):
        personName = self.loginform.name_line.text()
        personSurname = self.loginform.surNmae_line.text()
        personMail = self.loginform.mail_line.text()
        if not personName or not personSurname or not personMail:
            self.loginform.statusbar.showMessage("Lütfen tüm alanları doldurun.", 10000)
            return        
        self.connection()
        try:
            add = "INSERT INTO tbl_person(personName,personSurname,personMail) values (?,?,?)"
            self.operation.execute(add,(personName,personSurname,personMail))
            self.connect.commit()
            self.loginform.statusbar.showMessage("Kayıt Eklendi...",10000)
            self.hide()
            self.categoryopen.show()
        except:
            self.loginform.statusbar.showMessage("Kayıt Eklenemedi...",10000)    
        finally:
            self.connect.close()
        
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from registerUI import Ui_MainWindow
from category import CategoryPage
import sqlite3
import re

class RegisterPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.registerform = Ui_MainWindow()
        self.registerform.setupUi(self)
        self.registerform.kayit_btn.clicked.connect(self.Register)
    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()
    def Register(self):
        personName = self.registerform.name_line.text()
        personSurname = self.registerform.surNmae_line.text()
        personMail = self.registerform.mail_line.text()
        personPassword = self.registerform.sifre_line.text()

        if not personName or not personSurname or not personMail or not personPassword:
            self.registerform.statusbar.showMessage("Lütfen tüm alanları doldurun...", 10000)
            return
        if self.control_email(personMail):
            self.registerform.statusbar.showMessage("Geçerli email adresi giriniz...", 10000)
            return
        self.connection()
        try: 
            add = "INSERT INTO tbl_person(personName,personSurname,personMail,personPassword) values (?,?,?,?)"
            self.operation.execute(add,(personName,personSurname,personMail,personPassword))
            self.connect.commit()
            userID = self.operation.lastrowid
            self.registerform.statusbar.showMessage("Kayıt Eklendi...",10000)
            self.hide()
            self.categoryopen = CategoryPage(userID)
            self.categoryopen.show()
        except sqlite3.Error as e:
            self.registerform.statusbar.showMessage("Kayıt Eklenemedi...",10000)
            print(e)               
        finally:
            self.connect.close()

    def control_email(self,email):
        str_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(str_regex, email) is None        
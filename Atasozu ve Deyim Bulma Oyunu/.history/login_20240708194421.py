from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from loginUI import Ui_MainWindow4
from category import CategoryPage
from register import RegisterPage
import sqlite3

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow4()
        self.loginform.setupUi(self)
        self.loginform.login_btn.clicked.connect(self.Login)
        self.loginform.kayit_btn.clicked.connect(self.Register)
    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()
    def Login(self):
        personMail = self.loginform.mail_line.text()
        personPassword = self.loginform.sifre_line.text()
        if not personMail or not personPassword:
            self.loginform.statusbar.showMessage("Lütfen tüm alanları doldurun.", 10000)
            return        
        self.connection()
        try:
            self.operation.execute("SELECT personID,personPassword FROM tbl_person WHERE personMail = ?",(personMail,))
            checkPassword = self.operation.fetchall()[1]
            userID = self.operation.fetchall()[0]
            if personPassword == checkPassword:
                self.loginform.statusbar.showMessage("Hoşgeldiniz...", 10000)
                self.hide()
                self.categoryopen = CategoryPage(userID)
                self.categoryopen.show()
            else:
                self.loginform.statusbar.showMessage("Yanlış email veya şifre...", 10000)                 
        finally:
            self.connect.close()
    def Register(self):
        self.hide()
        self.registeropen = RegisterPage()
        self.registeropen.show()

            

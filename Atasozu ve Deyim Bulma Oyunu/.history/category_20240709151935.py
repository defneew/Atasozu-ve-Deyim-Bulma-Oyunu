from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from categoryUI import Ui_MainWindow2
from game import GamePage
import sqlite3

class CategoryPage(QMainWindow):
    def __init__(self,userID) -> None:
        super().__init__()
        self.categoryform = Ui_MainWindow2()
        self.categoryform.setupUi(self)
        self.categoryform.pushButton.clicked.connect(self.Category)
        self.userID = userID
    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()        
    def Category(self):
        self.connection()
        category = self.categoryform.category_comboBox.currentText()
        length = self.categoryform.lenght_line.text()
        
        print(category)
        if category == "Kelime":
            self.categoryform.statusbar.showMessage("Bu kategori şu anda kullanılamıyor", 10000) 
        if length:
            take = "SELECT tbl_adw.length FROM tbl_adw INNER JOIN tbl_category ON tbl_adw.categoryID = tbl_category.categoryID WHERE tbl_category.categoryName = ? AND tbl_adw.length = ? AND tbl_adw.adwID NOT IN (SELECT adwID FROM tbl_texts WHERE personID = ?)" 
            self.operation.execute(take, (category,length,self.userID))
            result = self.operation.fetchall()
            if not result:
                self.categoryform.statusbar.showMessage("Bu uzunlukta {} yoktur".format(category), 10000)  
                return      
        self.hide()
        self.gameopen = GamePage(category, length, self.userID)
        self.gameopen.show()
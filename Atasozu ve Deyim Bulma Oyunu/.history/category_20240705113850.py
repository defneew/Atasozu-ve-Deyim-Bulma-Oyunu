from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from categoryUI import Ui_MainWindow2
import sqlite3

class CategoryPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.categoryform = Ui_MainWindow2()
        self.categoryform.setupUi(self)
        self.categoryform.pushButton.clicked.connect(self.Category)
    def Category(self):
        category = self.categoryform.category_comboBox.currentText()
        length = self.categoryform.lenght_line.text()
        

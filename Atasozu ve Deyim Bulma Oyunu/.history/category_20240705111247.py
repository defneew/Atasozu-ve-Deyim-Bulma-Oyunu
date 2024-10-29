from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from categoryUI import Ui_MainWindow2
import sqlite3

class CategoryPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
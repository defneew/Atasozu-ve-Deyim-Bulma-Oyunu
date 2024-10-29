from PyQt5.QtWidgets import QApplication
from login import LoginPage
from category import CategoryPage
from game import GamePage
import sqlite3

app = QApplication([])
window = LoginPage()
window.show()
app.exec_()


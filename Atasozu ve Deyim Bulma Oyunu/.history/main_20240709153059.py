from PyQt5.QtWidgets import QApplication
from login import LoginPage
import sqlite3

app = QApplication([])
window = LoginPage()
window.show()
app.exec_()


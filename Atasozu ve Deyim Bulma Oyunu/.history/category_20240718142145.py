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
        # İndeks oluşturma
        self.operation.execute("CREATE INDEX IF NOT EXISTS idx_length ON tbl_adw(length);")
        self.connect.commit()
    def get_length_range(self, category, target_length):
        self.operation.execute("SELECT MIN(length), MAX(length) FROM tbl_adw INNER JOIN tbl_category ON tbl_adw.categoryID = tbl_category.categoryID WHERE tbl_category.categoryName = ?", (category,))
        min_length, max_length = self.operation.fetchone()

        if min_length is None or max_length is None:
            return None, None

        # Başlangıç aralığı için ikili arama
        start, end = min_length, max_length
        while start < end:
            mid = (start + end) // 2
            self.operation.execute("SELECT COUNT(*) FROM tbl_adw WHERE length <= ? AND categoryID = (SELECT categoryID FROM tbl_category WHERE categoryName = ?)", (mid, category))
            count = self.operation.fetchone()[0]
            if count < target_length:
                start = mid + 1
            else:
                end = mid
        start_length = start

        # Bitiş aralığı için ikili arama
        start, end = min_length, max_length
        while start < end:
            mid = (start + end) // 2
            self.operation.execute("SELECT COUNT(*) FROM tbl_adw WHERE length <= ? AND categoryID = (SELECT categoryID FROM tbl_category WHERE categoryName = ?)", (mid, category))
            count = self.operation.fetchone()[0]
            if count <= target_length:
                start = mid + 1
            else:
                end = mid
        end_length = start - 1

        return start_length, end_length

    def Category(self):
        self.connection()
        category = self.categoryform.category_comboBox.currentText()
        length = self.categoryform.lenght_line.text()

        if category == "Kelime":
            self.categoryform.statusbar.showMessage("Bu kategori şu anda kullanılamıyor", 10000)
            return

        if length:
            length = int(length)
            start_length, end_length = self.get_length_range(category, length)
            if start_length is None or end_length is None:
                self.categoryform.statusbar.showMessage("Bu uzunlukta {} yoktur".format(category), 10000)
                return
            take = "SELECT tbl_adw.text, tbl_adw.adwID, tbl_adw.categoryID, tbl_adw.length FROM tbl_adw INNER JOIN tbl_category ON tbl_adw.categoryID = tbl_category.categoryID WHERE tbl_category.categoryName = ? AND tbl_adw.length BETWEEN ? AND ? AND tbl_adw.adwID NOT IN (SELECT adwID FROM tbl_texts WHERE personID = ?) ORDER BY RANDOM() LIMIT 1"
            self.operation.execute(take, (category, start_length, end_length, self.userID))
        else:
            query = "SELECT tbl_adw.text, tbl_adw.adwID, tbl_adw.categoryID FROM tbl_adw INNER JOIN tbl_category ON tbl_adw.categoryID = tbl_category.categoryID WHERE tbl_category.categoryName = ? AND tbl_adw.adwID NOT IN (SELECT adwID FROM tbl_texts WHERE personID = ?) ORDER BY RANDOM() LIMIT 1"
            self.operation.execute(query, (category, self.userID))

        result = self.operation.fetchone()

        random_sentence = result[0].upper()
        currentTextID = result[1]
        currentTextCategoryID = result[2]

        self.hide()
        self.gameopen = GamePage(category, length, self.userID, random_sentence, currentTextID, currentTextCategoryID)
        self.gameopen.show()

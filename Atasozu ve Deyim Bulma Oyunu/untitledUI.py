# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/defne/OneDrive/Masaüstü/kelime_bulma\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(369, 300)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.verticalLayout.addWidget(self.name_line)
        self.surName = QtWidgets.QLabel(self.centralwidget)
        self.surName.setObjectName("surName")
        self.verticalLayout.addWidget(self.surName)
        self.surNmae_line = QtWidgets.QLineEdit(self.centralwidget)
        self.surNmae_line.setObjectName("surNmae_line")
        self.verticalLayout.addWidget(self.surNmae_line)
        self.mail = QtWidgets.QLabel(self.centralwidget)
        self.mail.setObjectName("mail")
        self.verticalLayout.addWidget(self.mail)
        self.mail_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_line.setObjectName("mail_line")
        self.verticalLayout.addWidget(self.mail_line)
        self.first_button = QtWidgets.QPushButton(self.centralwidget)
        self.first_button.setObjectName("first_button")
        self.verticalLayout.addWidget(self.first_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WORD GAME"))
        self.label.setText(_translate("MainWindow", "WORD GAME"))
        self.name.setText(_translate("MainWindow", "ADINIZ"))
        self.surName.setText(_translate("MainWindow", "SOYADINIZ"))
        self.mail.setText(_translate("MainWindow", "MAİL ADRESİ"))
        self.first_button.setText(_translate("MainWindow", "İLERİ"))
# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QDialog,QWidget,QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from mainWindow import mainWindow
from DBHelper import DBHelper

userInterface = uic.loadUiType("gtk/loginWindow.ui")[0]

class LoginWindow(QDialog, userInterface):
    def __init__(self, parent=None):
        # Initialization main interface from QT to Python
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedWidth(408)
        self.setFixedHeight(280)
        self.pilot = "Admin User"
        self.pushButton_login.clicked.connect(self.Login)
        self.pushButton_reset.clicked.connect(self.reset)

    def Login(self):
        _login = DBHelper()
        res = _login.LoginQuery(self.username_LE.text(), self.password_LE.text())
        if(len(res) > 0):
            if (self.username_LE.text() == str(res[0][1]) and
                self.password_LE.text() == str(res[0][2])):
                QMessageBox.information(QMessageBox(),'Successful','Login Successful')
                self.accept()
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Bad user or password')

    def reset(self):
        self.username_LE.setText("")
        self.password_LE.setText("")

    def GetPilot(self):
        return self.pilot
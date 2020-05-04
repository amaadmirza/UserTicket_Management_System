# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtGui,QtPrintSupport,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from mysql.connector import Error
import sys
import datetime
from About import About
from TicketInfo import TicketInfo
from userPaymentGrid import userPaymentGrid
from ListOfUsers import ListOfUsers

userInterface = uic.loadUiType("gtk/mainWindow.ui")[0]


class mainWindow(QtWidgets.QMainWindow, userInterface):
    def __init__(self, pilot, parent=None):
        # Initialization main interface from QT to Python
        QtWidgets.QMainWindow.__init__(self, parent)
        # Variable
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.About)
        self.actionTicket_info.triggered.connect(self.TicketInfo)
        self.actionUser_Payments_Info.triggered.connect(self.userPaymentGrid)
        self.actionList_Users.triggered.connect(self.ListOfUsers)
        print(pilot)
        self.action_Exit.triggered.connect(self.exit)
        self.update_CurrentDateTime()

    def update_CurrentDateTime(self):
        now = datetime.datetime.now()
        self.label_datetime.setText(now.strftime("%Y-%m-%d %H:%M:%S"))

    def About(self):
        self.about = About(None)
        self.about.exec_()

    def TicketInfo(self):
        self.ticketinfo = TicketInfo(None)
        self.ticketinfo.exec_()

    def userPaymentGrid(self):
        self.userPaymentGrid = userPaymentGrid(None)
        self.userPaymentGrid.show()

    def ListOfUsers(self):
        self.ListOfUsers = ListOfUsers(None)
        self.ListOfUsers.show()

    def exit(self):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message', 
                         quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            print("ignore close")
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import sys

from DBHelper import DBHelper

userInterface = uic.loadUiType("gtk/verify.ui")[0]

class verify(QDialog, userInterface):
    def __init__(self,UID, paymentType,totalCost,totalTickets,parent=None):
        # Initialization help interface from QT to Python
        QWidget.__init__(self, parent)
        self.setupUi(self)
        print(UID)
        self._uid = UID
        self.totalCost = totalCost
        self.totalTickets = totalTickets
        self._paymentType = paymentType
        self.setFixedWidth(305)
        self.setFixedHeight(152)
        self.pushButton_pay.clicked.connect(self.purchaseTicket)

    def purchaseTicket(self):
        if (self.username_LE.text() == "admin" and self.password_LE.text() == "admin"):
            _p = DBHelper()
            _p.InsertPurchaseQuery(self._uid,self._paymentType,self.totalCost, self.totalTickets)
            self.accept()
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Bad user or password')
     
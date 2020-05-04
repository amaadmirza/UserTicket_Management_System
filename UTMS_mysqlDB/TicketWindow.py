from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PaymentWindow import PaymentWindow
from DBHelper import DBHelper

userInterface = uic.loadUiType("gtk/ticketWindow.ui")[0]

class TicketWindow(QDialog, userInterface):
    def __init__(self,userID,FirstName, LastName,  parent=None):
        # Initialization help interface from QT to Python
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.UID = userID
        self.username = LastName+' '+FirstName
        
        self.label_username.setText(format(self.username))
        self.setFixedWidth(471)
        self.setFixedHeight(400)
        self.pushButton_saveTicketInfo.clicked.connect(self.paymentSaveWindow)
        self.pushButton_nextWindow.clicked.connect(self.nextWindow)

    def paymentSaveWindow(self):
        _age = self.comboBox_3.itemText(self.comboBox_3.currentIndex())
        _option = self.comboBox_4.currentIndex()
        self.label_totalTickets.setText(format(self.count_LE.text()))
        self._totaltickets = self.label_totalTickets.text()
        self._price = ""
        if (_option == 0):
            self._price = 50
        elif (_option == 1):
            self._price = 125
        else:
            self._price = 150

        if (_age == "Less than 15"):
            self.totalCost = ((self._price*50)/100)
            self.totalCost = int(self.totalCost)*int(self._totaltickets)
            self.label_totalCost.setText(format(self.totalCost))
        elif (_age == "greater than 20 and less than 40"):
            self.totalCost = self._price
            self.totalCost = int(self.totalCost)*int(self._totaltickets)
            self.label_totalCost.setText(format(self.totalCost))
        else: 
            self.totalCost = ((self._price*75)/100)
            self.totalCost = int(self.totalCost)*int(self._totaltickets)
            self.label_totalCost.setText(format(self.totalCost))
       
    def nextWindow(self):
        _totaltickets = self.label_totalTickets.text()
        _totalCost = self.label_totalCost.text()
        self.PaymentWindow = PaymentWindow(self.UID,self.username, _totaltickets, _totalCost)
        self.PaymentWindow.show()
        self.accept()


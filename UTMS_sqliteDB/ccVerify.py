from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from DBHelper import DBHelper

userInterface = uic.loadUiType("gtk/ccVerify.ui")[0]

class ccVerify(QDialog, userInterface):
    def __init__(self, UID,paymentType, totalCost,totalTickets, parent=None):
        # Initialization help interface from QT to Python
        QWidget.__init__(self, parent)
        self.setupUi(self)
        print(UID)
        self._uid = UID
        self.totalCost = totalCost
        self.totalTickets = totalTickets
        self._paymentType = paymentType
        self.setFixedWidth(400)
        self.setFixedHeight(246)
        self.pushButton_payC.clicked.connect(self.purchaseTicket)

    def purchaseTicket(self):
    	_cNumber = self._cNumber.text()
    	_cDate = self._cDate.text()
    	_cFullName = self._cFullName.text()
    	_cSecNumber = self._cSecNumber.text()
    	_p = DBHelper()
    	_p.InsertPurchaseCCQuery(self._uid, self._paymentType, self.totalCost, self.totalTickets, _cNumber,_cDate,_cFullName,_cSecNumber)


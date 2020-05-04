from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from ccVerify import ccVerify
from verify import verify

userInterface = uic.loadUiType("gtk/paymentWindow.ui")[0]

class PaymentWindow(QDialog, userInterface):
    def __init__(self,UID, UserName,totalCost,totalTickets, parent=None):
        # Initialization help interface from QT to Python
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setFixedWidth(357)
        self.setFixedHeight(221)
        self.label_username.setText(format(UserName))
        self._UID = UID
        self.totalCost = totalCost
        self.totalTickets = totalTickets
        self.pushButton_android.clicked.connect(self.verifyAndroid_Wallet)
        self.pushButton_apple.clicked.connect(self.verifyApple_Wallet)
        self.pushButton_creditCard.clicked.connect(self.creditCard_Wallet)

    def verifyAndroid_Wallet(self):
        self._paymentType = "Android Wallet"
        self.verify = verify(self._UID, self._paymentType,self.totalCost,self.totalTickets)
        self.verify.show()
     
    def verifyApple_Wallet(self):
        self._paymentType = "Apple Wallet"
        self.verify = verify(self._UID, self._paymentType,self.totalCost,self.totalTickets)
        self.verify.show()
    
    def creditCard_Wallet(self):
        self._paymentType = "Credit Card"
        self.ccVerify = ccVerify(self._UID, self._paymentType,self.totalCost,self.totalTickets)
        self.ccVerify.show()

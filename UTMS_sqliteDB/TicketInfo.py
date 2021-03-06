from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

userInterface = uic.loadUiType("gtk/ticketInfo.ui")[0]

class TicketInfo(QDialog, userInterface):
    def __init__(self, parent=None):
        # Initialization help interface from QT to Python
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setFixedWidth(359)
        self.setFixedHeight(317)
        self.pushButton_close.clicked.connect(self.closeWinHelp)

    def closeWinHelp(self):
        self.close()
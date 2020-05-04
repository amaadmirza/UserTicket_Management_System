__author__ = ""
__email__ = ""

import login as _login
import sys
import datetime
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QDialog
import mainWindow

App = QApplication(sys.argv)
# App.setStyle('adwaita')
LoginWindow = _login.LoginWindow(None)
# _mainWindow = mainWindow.mainWindow(None)
LoginWindow.show()

if LoginWindow.exec_() == QDialog.Accepted:
	_mainWindow = mainWindow.mainWindow(LoginWindow.GetPilot())
	_mainWindow.show()
	current_timer = QtCore.QTimer()
	current_timer.timeout.connect(lambda: _mainWindow.update_CurrentDateTime())
	current_timer.start(1000)
sys.exit(App.exec_())

from PyQt5 import QtCore,QtGui,QtPrintSupport,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtGui import *
from DBHelper import DBHelper

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchuser)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Payment ID.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchuser(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            _userpaymentGrid = DBHelper()
            row = _userpaymentGrid.userPaymentSearchQuery(searchrol)
            if(len(row) > 0):
                serachresult = "UserID : "+str(row[0][1])+'\n'+"User Name : "+str(row[0][2])+'\n'+"Payment Method : "+str(row[0][3])+'\n'+"Total Tickets : "+str(row[0][5])+'\n'+"Total Cost : "+str(row[0][4]+"$")
                QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find Record in Table.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find Record in Table.')

class userPaymentGrid(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(userPaymentGrid, self).__init__(*args, **kwargs)

        self.setWindowTitle("User Payments Record")
        self.setMinimumSize(1150, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Payment ID.","User ID.", "User Name", "Payment Method",  "Total Price", "Total Tickets", "Card Number","FullName","Expiry Date","Sec Number","Action"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"),"Refresh",self)   #refresh icon
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  #search icon
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)
        self.loaddata()

    def loaddata(self):
        _userpaymentGrid = DBHelper()
        result = _userpaymentGrid.userPaymentQuery()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
                self.btn_edit = QPushButton('Edit')
                self.btn_edit.clicked.connect(self.handleEditRow)
                self.tableWidget.setCellWidget(row_number,10,self.btn_edit)
                self.tableWidget.item(row_number, 0).setFlags(QtCore.Qt.ItemIsEnabled)

    def handleEditRow(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            item = self.tableWidget.item(index.row(), 0)
            item1 = self.tableWidget.item(index.row(), 4)
            item2 = self.tableWidget.item(index.row(), 5)
            self.item_text = item.text()
            self.item_text1 = item1.text()
            self.item_text2 = item2.text()
            print(self.item_text,self.item_text1,self.item_text2)
            updateRecord = DBHelper()
            updateRecord.updatePaymentQuery(self.item_text,self.item_text1,self.item_text2)

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

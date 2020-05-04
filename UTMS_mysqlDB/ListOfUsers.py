from PyQt5 import QtCore,QtGui,QtPrintSupport,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtGui import *
from TicketWindow import TicketWindow
from DBHelper import DBHelper

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Add User")

        self.setWindowTitle("Add User")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Insert User Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addUser)

        layout = QVBoxLayout()

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First Name")
        layout.addWidget(self.first_name)

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last Name")
        layout.addWidget(self.last_name)

        self.Joined = QLineEdit()
        self.Joined.setPlaceholderText("Date of Joining")
        layout.addWidget(self.Joined)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addUser(self):
        first_name = ""
        last_name = ""
        Joined = ""
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        Joined = self.Joined.text()
        try:
            _userSearch = DBHelper()
            row = _userSearch.addUserQuery(first_name,last_name,Joined)
        except Exception:
            print('')
            
class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchuser)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("User ID.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchuser(self):
        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            _userSearch = DBHelper()
            row = _userSearch.userSearchQuery(searchrol)
            if(len(row) > 0):
                serachresult = "User ID : "+str(row[0][0])+'\n'+"User Name : "+str(row[0][1])+'\n'+"Joined Date : "+str(row[0][2])
                QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find Record in Table.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find Record in Table.')

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deleteuser)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("User ID.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deleteuser(self):
        delrol = ""
        delrol = self.deleteinput.text()
        try:
            _deleteuser = DBHelper()
            row = _deleteuser.deleteUserQuery(delrol)
        except Exception:
            print('')

class ListOfUsers(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ListOfUsers, self).__init__(*args, **kwargs)

        self.setWindowTitle("User Record")
        self.setMinimumSize(700, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("User ID", "First Name", "Last Name", "Joined Date", "Action", "Action"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Add User", self)   #add User icon
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add User")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"),"Refresh",self)   #refresh icon
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  #search icon
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)

        # btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        # btn_ac_delete.triggered.connect(self.delete)
        # btn_ac_delete.setStatusTip("Delete User")
        # toolbar.addAction(btn_ac_delete)

        self.loaddata()

    def loaddata(self):
        _listOfUserQuery = DBHelper()
        result = _listOfUserQuery.listOfUserQuery()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
                self.btn_edit = QPushButton('Edit')
                self.btn_edit.clicked.connect(self.handleEditRow)
                self.tableWidget.setCellWidget(row_number,4,self.btn_edit)
                self.btn_buy = QPushButton('Purchase Ticket')
                self.btn_buy.clicked.connect(self.btn_buyTicket)
                self.tableWidget.setCellWidget(row_number,5,self.btn_buy)
                self.item = self.tableWidget.item(row_number, 0)
                self.item.setFlags(QtCore.Qt.ItemIsEnabled)


    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    # def delete(self):
    #     dlg = DeleteDialog()
    #     dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()


    def handleEditRow(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            item = self.tableWidget.item(index.row(), 0)
            item1 = self.tableWidget.item(index.row(), 1)
            item2 = self.tableWidget.item(index.row(), 2)
            item3 = self.tableWidget.item(index.row(), 3)
            self.item_text = item.text()
            self.item_text1 = item1.text()
            self.item_text2 = item2.text()
            self.item_text3 = item3.text()
            print(self.item_text,self.item_text1,self.item_text2,self.item_text3)
            updateRecord = DBHelper()
            updateRecord.updateUserQuery(self.item_text,self.item_text1,self.item_text2,self.item_text3)
        
    def btn_buyTicket(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            item = self.tableWidget.item(index.row(), 0)
            item1 = self.tableWidget.item(index.row(), 1)
            item2 = self.tableWidget.item(index.row(), 2)
            self.item_text = item.text()
            self.item_text1 = item1.text()
            self.item_text2 = item2.text()
        self.ticketWindow = TicketWindow(self.item_text,self.item_text1,self.item_text2)
        self.ticketWindow.show()
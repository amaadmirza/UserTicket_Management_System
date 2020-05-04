from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QDialog,QWidget, QMessageBox
import mysql.connector
from mysql.connector import Error

class DBHelper():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='127.0.0.1',
                                                 database='userTicketManagement',
                                                 user='adminuser',
                                                 password='ua_soft@1234')
            self.c=self.conn.cursor()
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        
    def LoginQuery(self,name,password):
        try:
            sql_select_Query = """ SELECT * from cPanelUser WHERE name=%s AND password=%s"""
            self.c.execute(sql_select_Query, (name,password))
            recordSet = self.c.fetchall()
            return recordSet
            self.conn.commit()
            self.c.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def userPaymentQuery(self):
        try:
            sql_select_Query = """SELECT p.payment_id, u.user_id, CONCAT(u.last_name,' ',u.first_name) as username,p.Payment_method, 
             p.total_price, p.total_tickets, p.card_number, p.fullname, p.expiry_date, p.sec_number 
            FROM payments as p Inner Join users as u ON u.user_id=p.user_id"""
            self.c.execute(sql_select_Query)
            recordSet = self.c.fetchall()
            return recordSet
            self.conn.commit()
            self.c.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def userPaymentSearchQuery(self,PID):
        try:
            sql_select_Query = "SELECT p.payment_id, u.user_id, CONCAT(u.last_name,' ',u.first_name) as username,p.Payment_method, p.total_price, p.total_tickets, p.card_number, p.fullname, p.expiry_date, p.sec_number FROM payments as p Inner Join users as u ON u.user_id=p.user_id Where p.payment_id="+str(PID)
            self.c.execute(sql_select_Query)
            recordSet = self.c.fetchall()
            return recordSet
            self.conn.commit()
            self.c.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def listOfUserQuery(self):
        try:
            sql_select_Query = """SELECT user_id, first_name,last_name, Joined FROM users"""
            self.c.execute(sql_select_Query)
            recordSet = self.c.fetchall()
            return recordSet
            self.conn.commit()
            self.c.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def userSearchQuery(self,UID):
        try:
            sql_select_Query = "SELECT user_id, CONCAT(last_name,' ',first_name) as username, Joined FROM users Where user_id="+str(UID)
            self.c.execute(sql_select_Query)
            recordSet = self.c.fetchall()
            return recordSet
            self.conn.commit()
            self.c.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def deleteUserQuery(self,UID):
        try:
            sql_select_Query = "SELECT user_id, CONCAT(last_name,' ',first_name) as username, Joined FROM users Where user_id="+str(UID)
            self.c.execute(sql_select_Query)
            recordSet = self.c.fetchall()
            if(len(recordSet) > 0):
                sql_delete_Query = "DELETE from users WHERE user_id="+str(UID)
                self.c.execute(sql_delete_Query)
                self.conn.commit()
                self.c.close()
                QMessageBox.information(QMessageBox(),'Successful','Deleted User From Table Successful')
            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete user from the table User ID doesnot exist')            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def addUserQuery(self,first_name, last_name, Joined):
        try:
            sql_insert_query = "INSERT INTO users (first_name, last_name, Joined) VALUES ('"+str(first_name)+"','"+str(last_name)+"','"+str(Joined)+"')"
            self.c.execute(sql_insert_query)
            self.conn.commit()
            self.c.close()
            QMessageBox.information(QMessageBox(),'Successful','User is added successfully to the table.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def updateUserQuery(self,UID,first_name ,last_name, Joined):
        try:
            sql_update_query = "UPDATE users set first_name='"+first_name+"', last_name='"+last_name+"', Joined='"+Joined+"' WHERE user_id="+str(UID)
            self.c.execute(sql_update_query)
            self.conn.commit()
            self.c.close()
            QMessageBox.information(QMessageBox(),'Successful','User is Updated successfully to the table.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def InsertPurchaseQuery(self,UID,payment_method,totalCost,totalTickets):
        try:
            sql_update_query = "INSERT into payments  (user_id, payment_method, total_price, total_tickets) VALUES ('"+str(UID)+"','"+str(payment_method)+"','"+str(totalCost)+"','"+str(totalTickets)+"')"
            self.c.execute(sql_update_query)
            self.conn.commit()
            self.c.close()
            QMessageBox.information(QMessageBox(),'Successful','Thanks for Purchase..')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def InsertPurchaseCCQuery(self,UID,payment_method,totalCost,totalTickets, _cNumber,_cDate,_cFullName,_cSecNumber):
        try:
            sql_update_query = "INSERT into payments (user_id, payment_method, total_price, total_tickets, card_number, fullname, expiry_date, sec_number) VALUES ('"+str(UID)+"','"+str(payment_method)+"','"+str(totalCost)+"','"+str(totalTickets)+"','"+str(_cNumber)+"','"+str(_cFullName)+"','"+str(_cDate)+"','"+str(_cSecNumber)+"')"
            self.c.execute(sql_update_query)
            self.conn.commit()
            self.c.close()
            QMessageBox.information(QMessageBox(),'Successful','Thanks for Purchase..')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')

    def updatePaymentQuery(self,PID, totalCost, totalTickets):
        print("UPDATE payments set total_price='"+totalCost+"', total_tickets='"+totalTickets+"' WHERE payment_id="+str(PID))
        try:
            sql_update_query = "UPDATE payments set total_price='"+totalCost+"', total_tickets='"+totalTickets+"' WHERE payment_id="+str(PID)
            self.c.execute(sql_update_query)
            self.conn.commit()
            self.c.close()
            QMessageBox.information(QMessageBox(),'Successful','Payment Info is Updated successfully to the table.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not connect to the database.')
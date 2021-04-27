import sys
import platform
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QComboBox,QLineEdit,QLabel,QCheckBox,QMessageBox,QRadioButton,QTimeEdit
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from student_roomNkey import Ui_Form
from student_roomNkey import *
from schedule import Ui_MainWindow
from schedule import *
from time import *
import mysql.connector
from mysql.connector import IntegrityError

class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("student_roomNkey.ui",self)
        self.student_pushButton_room1.clicked.connect(self.gotowindow)
        self.student_pushButton_room2.clicked.connect(self.gotowindow)
        self.student_pushButton_room3.clicked.connect(self.gotowindow)
        self.student_pushButton_room4.clicked.connect(self.gotowindow)
        self.student_pushButton_room5.clicked.connect(self.gotowindow)
        self.student_pushButton_room6.clicked.connect(self.gotowindow)

    def gotowindow(self):
        window=WindowForm()
        widget.addWidget(window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class WindowForm(QMainWindow):
    def __init__(self):
        super(WindowForm, self).__init__()
        loadUi("schedule.ui",self)
        self.time.clicked.connect(self.gototime)
        self.time_2.clicked.connect(self.gototime)
        self.time_3.clicked.connect(self.gototime)
        self.time_4.clicked.connect(self.gototime)
        self.time_5.clicked.connect(self.gototime)
        self.time_6.clicked.connect(self.gototime)
        self.time_7.clicked.connect(self.gototime)
        self.btn_preview.clicked.connect(self.gotologin)

    def gotologin(self):
        loginform=Login()
        widget.addWidget(loginform)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gototime(self):
        time=TimeForm()
        widget.addWidget(time)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class TimeForm(QMainWindow):
    def __init__(self):
        super(TimeForm, self).__init__()
        loadUi("time.ui",self)
        self.btn_preview.clicked.connect(self.gotowindow)
        self.btn_ok.clicked.connect(self.createappointment)

    def gotowindow(self):
        window=WindowForm()
        widget.addWidget(window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createappointment(self):
        try:
            username = self.name.text()
            course_year = self.course.text()
            time = str(self.timeEdit.text())
            no = str(self.room.currentText())

            mydb = mysql.connector.connect(host="localhost",user="root",password="admin",
                                           database="cc15student")

            mycursor = mydb.cursor()

            if no == "----":
                QtWidgets.QMessageBox.critical(self,'Error',"Field Empty")
            elif username == "":
                QtWidgets.QMessageBox.critical(self, 'Error', "Name Field Empty")
            elif course_year == "":
                QtWidgets.QMessageBox.critical(self, 'Error', " Course Field Empty")

            else:
                QtWidgets.QMessageBox.information(self,'Success','Room Reserve Success')
                loginform = Login()
                widget.addWidget(loginform)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                mycursor.execute(
                    """INSERT INTO time (name,courseyear,time,room)
                    VALUES(%s,%s,%s,%s)""",
                    (username,course_year,time,no))
            mydb.commit()
        except IntegrityError:
            QtWidgets.QMessageBox.critical(self,'Error','Duplicate Entry')
            pass





app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(749)
widget.setFixedHeight(620)
widget.show()
app.exec_()


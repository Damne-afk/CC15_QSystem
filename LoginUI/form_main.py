from logging import RootLogger
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QSize, QObject, Qt
from PyQt5.QtWidgets import QDialog,QApplication, QMainWindow, QStackedWidget, QVBoxLayout,QWidget,QComboBox,QLineEdit,QLabel,QCheckBox,QMessageBox,QRadioButton,QShortcut
from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import IntegrityError
import os
import lib
import images

from loginStacked import Ui_MainWindow

## Reusable dictionary used for connecting to the local database
mysqlConfig = { 'host': "localhost",
                'user': "cc15_root",
                'password': "password",
                'database' : "cc15_qsystem" }

class LoginPageHandler(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.handlerPg = Ui_MainWindow()
        self.handlerPg.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        startSize = QSize(1024, 624)
        self.resize(startSize)
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
        
        self.handlerPg.pushButton.clicked.connect(lambda: self.close())
        self.handlerPg.pushButton_2.clicked.connect(lambda: self.showMinimized())

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.handlerPg.loginContainer_top.mouseMoveEvent = moveWindow
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

        # WIDGET TO MOVE
       
        
class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("loginForm.ui",self)

        startSize = QSize(1024, 598)
        self.resize(startSize)
        self.label_5.setHidden(True)

        self.loginbutton.clicked.connect(self.loginUser)
        self.cancelbutton.clicked.connect(lambda: self.close())

    def loginUser(self):
        controlDb = DBControl()
        id=self.id.text()
        password=self.password.text()

        try:
            mydb = mysql.connector.connect(**mysqlConfig)    
            mycursor = mydb.cursor(dictionary=True) #Returns values as dictionaries instead of tuples

            loginFetchedData = controlDb.checkIfUserExists(mycursor,id,password)

            mycursor.close()
            mydb.close()

            if loginFetchedData:
                role = loginFetchedData['role']
                QtWidgets.QMessageBox.information(self,'Success','You are now Logged in')
                self.label_5.setHidden(False)
                clearLineEdits(self)

                ## Some way to show mainwindow

            else:
                self.label_5.setHidden(True)
                clearLineEdits(self)

        except mysql.connector.Error:
            QtWidgets.QMessageBox.critical(self,'Error','Error Connecting to the Database.\nPlease Try Again.')
        

class CreateStudentAcc(QDialog):
    def __init__(self):
        super(CreateStudentAcc, self).__init__()
        loadUi("createStudAcc.ui",self)
        startSize = QSize(1024, 598)
        self.resize(startSize)


        self.submitbutton.clicked.connect(self.createaccfunction)
        self.previousbutton.clicked.connect(lambda: resetChanges(self))
        self.confirmpass.textChanged.connect(lambda: passEq(self.confirmpass.text(),self))

    def createaccfunction(self):

        controlDb = DBControl()

        id = self.id.text()
        firstname = self.firstname.text()
        surname = self.surname.text()
        courseNyear = self.courseNyear.text()
        email = self.email.text()
        password = self.password.text()
        role = 'STUDENT'
        scholar = #something here
        ## Check if scholar or not

        try:
            mydb = mysql.connector.connect(**mysqlConfig)
            mycursor = mydb.cursor()

            validateData = controlDb.validateUser(mycursor,id)

            if validateData:
                user = controlDb.checkIfUserExists(mycursor,id,password)

                if user:
                    QtWidgets.QMessageBox.critical(self,'Error','An account for this user already exists.\nGoing back to the Login page...')
                    self.previousbutton.trigger()
                else:
                    controlDb.insertCredentials(mycursor,id,password,role)

                    mycursor.execute("""INSERT INTO studentusers (id,firstname,surname,courseNyear,email,password,scholar)
                                        VALUES(%s,%s,%s,%s,%s,%s,%s)""",
                                    (id.upper(),firstname.upper(),surname.upper(),courseNyear.upper(),email,password,scholar))
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
            else:
                QtWidgets.QMessageBox.critical(self,'Error','Please enter a valid ID.')


        except mysql.connector.Error:
            QtWidgets.QMessageBox.critical(self,'Error','Error Connecting to the Database.\nPlease Try Again.')

        else:
            QtWidgets.QMessageBox.information(self,'Success','Your account is now registered.\nYou can proceed by logging in your account.')
            self.previousbutton.trigger()


class CreateFacultyAcc(QDialog):
    def __init__(self):
        super(CreateFacultyAcc, self).__init__()
        loadUi("createFactAcc.ui",self)
        startSize = QSize(1024, 598)
        self.resize(startSize)

        self.submitbutton.clicked.connect(self.createaccfunction)
        self.previousbutton.clicked.connect(lambda: resetChanges(self))
        self.confirmpass.textChanged.connect(lambda: passEq(self.confirmpass.text(),self))

    def createaccfunction(self):
        controlDb = DBControl()

        id = self.id.text()
        firstname = self.firstname.text()
        surname = self.surname.text()
        department = self.department.text()
        email = self.email.text()
        password = self.password.text()
        role = 'FACULTY'

        try:
            mydb = mysql.connector.connect(**mysqlConfig)
            mycursor = mydb.cursor()

            validateData = controlDb.validateUser(mycursor,id)

            if validateData:
                user = controlDb.checkIfUserExists(mycursor,id,password)

                if user:
                    QtWidgets.QMessageBox.critical(self,'Error','An account for this user already exists.\nGoing back to the Login page...')
                    self.previousbutton.trigger()
                else:
                    controlDb.insertCredentials(mycursor,id,password,role)

                    mycursor.execute("""INSERT INTO facultyusers (id,firstname,surname,department,email,password)
                                        VALUES(%s,%s,%s,%s,%s,%s)""",
                                    (id.upper(),firstname.upper(),surname.upper(),department.upper(),email,password))
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
            else:
                QtWidgets.QMessageBox.critical(self,'Error','Please enter a valid ID.')


        except mysql.connector.Error:
            QtWidgets.QMessageBox.critical(self,'Error','Error Connecting to the Database.\nPlease Try Again.')

        else:
            QtWidgets.QMessageBox.information(self,'Success','Your account is now registered.\nYou can proceed by logging in your account.')
            self.previousbutton.trigger()


class CreateAdminAcc(QDialog):
    def __init__(self):
        super(CreateAdminAcc, self).__init__()
        loadUi("createAdmnAcc.ui",self)
        startSize = QSize(1024, 598)
        self.resize(startSize)

        self.submitbutton.clicked.connect(self.createaccfunction)
        self.previousbutton.clicked.connect(lambda: resetChanges(self))
        self.confirmpass.textChanged.connect(lambda: passEq(self.confirmpass.text(),self))

    def createaccfunction(self):
        controlDb = DBControl()

        id = self.id.text()
        firstname = self.firstname.text()
        surname = self.surname.text()
        email = self.email.text()
        password = self.password.text()
        role = 'ADMIN'

        try:
            mydb = mysql.connector.connect(**mysqlConfig)
            mycursor = mydb.cursor()

            validateData = controlDb.validateUser(mycursor,id)

            if validateData:
                user = controlDb.checkIfUserExists(mycursor,id,password)

                if user:
                    QtWidgets.QMessageBox.critical(self,'Error','An account for this user already exists.\nGoing back to the Login page...')
                    self.previousbutton.trigger()
                else:
                    controlDb.insertCredentials(mycursor,id,password,role)

                    mycursor.execute("""INSERT INTO adminusers (id,firstname,surname,email,password)
                                        VALUES(%s,%s,%s,%s,%s,%s)""",
                                    (id.upper(),firstname.upper(),surname.upper(),email,password))
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
            else:
                QtWidgets.QMessageBox.critical(self,'Error','Please enter a valid ID.')


        except mysql.connector.Error:
            QtWidgets.QMessageBox.critical(self,'Error','Error Connecting to the Database.\nPlease Try Again.')

        else:
            QtWidgets.QMessageBox.information(self,'Success','Your account is now registered.\nYou can proceed by logging in your account.')
            self.previousbutton.trigger()


class verifyAdmin(QDialog):
    def __init__(self):
        super(verifyAdmin, self).__init__()
        loadUi("verifyAdmn.ui",self)
        startSize = QSize(382, 264)
        self.resize(startSize)

        self.label_2.setHidden(True)
        self.pushButton.clicked.connect(self.whenSubmit)
        self.pushButton_2.clicked.connect(lambda: self.closeEvent())

    def whenSubmit(self):
        controlDb = DBControl()

        id = self.id.text()
        password = self.password.text()

        try:
            mydb = mysql.connector.connect(**mysqlConfig)    
            mycursor = mydb.cursor(dictionary=True) #Returns values as dictionaries instead of tuples

            loginFetchedData = controlDb.checkIfUserExists(mycursor,id,password)

            mycursor.close()
            mydb.close()

            if loginFetchedData:
                self.proceedToCreateAdmin()
                self.closeEvent()
            else:
                self.label_2.setHidden(False)
                
        except mysql.connector.Error:
            QtWidgets.QMessageBox.critical(self,'Error','Error Connecting to the Database.\nPlease Try Again.')

    def closeEvent(self):
        self.label_2.setHidden(True)
        clearLineEdits(self)
        self.close

    ## Definition will be in the runThis()
    def proceedToCreateAdmin(self):
        pass


class DBControl():
    def checkIfUserExists(mycursor1,id,password): 
        mycursor1.execute("""SELECT * FROM credentials WHERE id=%s AND password=%s""",
                            (id,password))
        # Fetches one row of values (i.e. a dictionary)
        loginFetchedData = mycursor1.fetchone() 

        return loginFetchedData

    def validateUser(mycursor2,id):
        mycursor2.execute("""SELECT * FROM recordedusers WHERE id=%s""",id)

        # Fetches one row of values (i.e. a dictionary)
        validateFetchedData = mycursor2.fetchone() 

        return validateFetchedData

    def insertCredentials(mycursor3,id,password,role):
        mycursor3.execute("""INSERT INTO credentials (id,password,role) VALUES (%s,%s,%s)""",
                            (id.upper(),password,role))


def clearLineEdits(widgetObj):
    listofLineEdits = widgetObj.frame.findChildren(QLineEdit)
    for le in listofLineEdits:
        le.clear()

def resetPassStyle(widgetObj):
    widgetObj.confirmpass.setStyleSheet("background: transparent; color:#717072;\n"
                                        "border: none; border-bottom:1px solid #717072;")

def passEq(confirmpassVar,widgetObj):
    if confirmpassVar == widgetObj.password.text():
        widgetObj.confirmpass.setStyleSheet("background: transparent; color:#717072;\n"
                                            "border: 1px solid #35ed69;")
    else:
        widgetObj.confirmpass.setStyleSheet("background: transparent; color:#717072;\n"
                                            "border: 1px solid #f14040;")

def resetChanges(widgetObj):
    resetPassStyle(widgetObj)
    clearLineEdits(widgetObj)

## Acts like the init for the program
def runThis():
    login = Login()
    createStudAcc = CreateStudentAcc()
    createFactAcc = CreateFacultyAcc()
    createAdmnAcc = CreateAdminAcc()
    verifyAdmn = verifyAdmin()

    stackedHandler = LoginPageHandler()

    stackedHandler.handlerPg.login_stackedWidget.addWidget(login)
    stackedHandler.handlerPg.login_stackedWidget.addWidget(createStudAcc)
    stackedHandler.handlerPg.login_stackedWidget.addWidget(createFactAcc)
    stackedHandler.handlerPg.login_stackedWidget.addWidget(createAdmnAcc)

    stackedHandler.handlerPg.login_stackedWidget.setCurrentWidget(login)

    ## NAVIGATION DEFINITIONS
    def gotoLogin():
        stackedHandler.handlerPg.login_stackedWidget.setCurrentWidget(login)

    def gotoCreateStudentAcc():
        stackedHandler.handlerPg.login_stackedWidget.setCurrentWidget(createStudAcc)

    def gotoCreateFacultyAcc():
        stackedHandler.handlerPg.login_stackedWidget.setCurrentWidget(createFactAcc)

    def gotoCreateAdminAcc():
        stackedHandler.handlerPg.login_stackedWidget.setCurrentWidget(createAdmnAcc) 

    stackedHandler.gotoLogin = gotoLogin
    stackedHandler.gotoCreateStudentAcc = gotoCreateStudentAcc
    stackedHandler.gotoCreateFacultyAcc = gotoCreateFacultyAcc
    stackedHandler.gotoCreateAdminAcc = gotoCreateAdminAcc

    ##  WIDGET CONNECTIONS
    """FOR LOGIN PG"""
    login.createStudAcc.clicked.connect(stackedHandler.gotoCreateStudentAcc)
    login.createFacAcc.clicked.connect(stackedHandler.gotoCreateFacultyAcc)

    login.createAdmnAccSC = QShortcut(QKeySequence("Alt+D"),login)
    login.createAdmnAccSC.activated.connect(lambda: verifyAdmn.show())
    

    """FOR CreateSTUDACC PG"""
    createStudAcc.previousbutton.clicked.connect(stackedHandler.gotoLogin)

    """FOR CreateFACTACC PG"""
    createFactAcc.previousbutton.clicked.connect(stackedHandler.gotoLogin)

    """FOR CreateADMNACC PG"""
    createAdmnAcc.previousbutton.clicked.connect(stackedHandler.gotoLogin)

    """FOR VerifyADMN DIALOG PG"""
    verifyAdmn.proceedToCreateAdmin = stackedHandler.gotoCreateAdminAcc

    stackedHandler.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    runThis()
    sys.exit(app.exec_())
################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
from ui_main_Admin import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from ui_main_Admin import Ui_MainWindow
from functions_UI_Admin import *
#from functions_App_Admin import *

## IMPORTS 'ui_main_Admin' in the for_Appmodules MODULE
#uiMain_dImport('ui_main_Admin')

## GIVE 'functions_UI' MODULE THE NAME OF THIS PARTICULAR FILE (i.e 'main_Admin')
#dynamicImport(str(os.path.basename(__file__)).split('.')[0])

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        Admin_UIFunctions.removeTitleBar(True)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        Admin_UIFunctions.labelTitle(self, 'Admin Main Window - Python Base')
        Admin_UIFunctions.labelDescription(self, 'Set text')

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1440, 810)
        self.resize(startSize)
        self.setMinimumSize(1080, 608)

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: Admin_UIFunctions.toggleMenu(self, 240, True))

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        Admin_UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/20x20/icons/20x20/cil-home.png)", True)
        #Admin_UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        Admin_UIFunctions.addNewMenu(self, "APPOINTMENTS", "btn_appointments", "url(:/20x20/icons/20x20/cil-people.png)", True)
        Admin_UIFunctions.addNewMenu(self, "TASKS", "btn_special_services", "url(:/20x20/icons/20x20/cil-task.png)", True)
        Admin_UIFunctions.addNewMenu(self, "ROOM RESERVATION", "btn_roomNkey", "url(:/20x20/icons/20x20/cil-tag.png)", True)
        Admin_UIFunctions.addNewMenu(self, "CUSTOM WIDGETS", "btn_widgets", "url(:/20x20/icons/20x20/cil-equalizer.png)", False)

        # START MENU => SELECTION
        Admin_UIFunctions.selectStandardMenu(self, "btn_home")

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        ## USER ICON ==> SHOW HIDE
        Admin_UIFunctions.userIcon(self, "WM", "", True)
        
        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if Admin_UIFunctions.returnStatus() == 1:
                Admin_UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        ## ==> LOAD DEFINITIONS
        ########################################################################
        Admin_UIFunctions.uiDefinitions(self)

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################
        self.show()


    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            Admin_UIFunctions.resetStyle(self, "btn_home")
            Admin_UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(Admin_UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE APPOINTMENTS
        if btnWidget.objectName() == "btn_appointments":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_appointments)
            Admin_UIFunctions.resetStyle(self, "btn_appointments")
            Admin_UIFunctions.labelPage(self, "Appointments")
            btnWidget.setStyleSheet(Admin_UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SPECIAL SERVICES
        if btnWidget.objectName() == "btn_special_services":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_special_services)
            Admin_UIFunctions.resetStyle(self, "btn_special_services")
            Admin_UIFunctions.labelPage(self, "Special Services")
            btnWidget.setStyleSheet(Admin_UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ROOM RESERVATION
        if btnWidget.objectName() == "btn_roomNkey":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_roomNkey)
            Admin_UIFunctions.resetStyle(self, "btn_roomNkey")
            Admin_UIFunctions.labelPage(self, "Room Reservation")
            btnWidget.setStyleSheet(Admin_UIFunctions.selectMenu(btnWidget.styleSheet()))


        """
        ADDITIONAL PAGES HERE
        """

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            Admin_UIFunctions.resetStyle(self, "btn_widgets")
            Admin_UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(Admin_UIFunctions.selectMenu(btnWidget.styleSheet()))
    ## ==> END ##
 
    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)


    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
    def returnObj(self):
        return self

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
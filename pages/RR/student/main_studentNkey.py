import sys
import platform
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from student_roomNkey import Ui_Form
from student_roomNkey import *
from schedule import Ui_MainWindow
from schedule import *

class Mainwindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        ##Buttons
        self.ui.student_pushButton_room1.clicked.connect(self.openwindow)
        self.ui.student_pushButton_room2.clicked.connect(self.openwindow)
        self.ui.student_pushButton_room3.clicked.connect(self.openwindow)
        self.ui.student_pushButton_room4.clicked.connect(self.openwindow)
        self.ui.student_pushButton_room5.clicked.connect(self.openwindow)
        self.ui.student_pushButton_room6.clicked.connect(self.openwindow)

    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec_())

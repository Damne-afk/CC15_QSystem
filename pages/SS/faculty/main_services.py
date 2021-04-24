import sys
import platform
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


from services import Ui_Dialog
from services import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        ##BUTTONS
        self.ui.btn_task_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_task_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_task_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_task_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.ok_btn.clicked.connect(self.addTaskToList)
        self.ui.ok_btn_2.clicked.connect(self.addTaskToList)
        self.ui.ok_btn_3.clicked.connect(self.addTaskToList)
        self.ui.ok_btn_4.clicked.connect(self.addTaskToList)
        self.show()

        ##ADDT0LIST
    def addTaskToList(self):
        widget = QWidget()
        widget.setObjectName(u"widget")
        #Layout of container  Widget
        layout = QVBoxLayout(widget)
        frame = QFrame()
        inner = QHBoxLayout(frame)
        innerleft = QFrame()
        innerleftframe = QHBoxLayout(innerleft)
        innerright = QFrame()
        innerrightframe = QHBoxLayout(innerright)
        inner.addWidget(innerleft)
        inner.addWidget(innerright)
        sdescription = QTextEdit()
        sdescription.setPlainText(self.ui.tDescription.toPlainText())
        shours = QLabel()
        shours.setText(self.ui.tHours.text())
        sIcon = QPushButton()
        sIcon.setIcon(icon)
        innerleftframe.addWidget(sIcon)
        innerrightframe.addWidget(sdescription)
        innerrightframe.addWidget(shours)

        layout.addWidget(frame)


        self.ui.scrollArea.addWidget(widget)









        ## SHOW ==> MAINWINDOW







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

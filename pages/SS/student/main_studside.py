import sys
import platform
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


from SS_studside import Ui_Form
from SS_studside import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ##BUTTONS
        self.ui.btn_task.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.btn_task_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        self.ui.btn_task_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.ui.btn_task_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))
        ##self.ui.btn_ok.clicked.connect(self.#something)
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

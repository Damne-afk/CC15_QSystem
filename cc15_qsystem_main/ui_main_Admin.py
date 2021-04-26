# -*- coding: utf-8 -*-
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

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 360)
        MainWindow.setMinimumSize(QSize(640, 360))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif

## CENTRAL-STYLE DEFS | START
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
        "QToolTip {\n"
        "	color: #ffffff;\n"
        "	background-color: rgba(27, 29, 35, 160);\n"
        "	border: 1px solid rgb(40, 40, 40);\n"
        "	border-radius: 2px;\n"
        "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
        "color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
        "QLineEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}\n"
        "\n"
        "/* SCROLL BARS */\n"
        "QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "	border-radius: 0px;\n"
        "}\n"
        "QScrollBar::handle:horizontal {\n"
        "    background: rgb(85, 170, 255);\n"
        "    min-width: 25px;\n"
        "	border-radius: 7px\n"
        "}\n"
        "QScrollBar::add-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        "	border-top-right-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "    subcontrol-position: right;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::sub-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        ""
        "	border-top-left-radius: 7px;\n"
        "    border-bottom-left-radius: 7px;\n"
        "    subcontrol-position: left;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        " QScrollBar:vertical {\n"
        "	border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "	border-radius: 0px;\n"
        " }\n"
        " QScrollBar::handle:vertical {	\n"
        "	background: rgb(85, 170, 255);\n"
        "    min-height: 25px;\n"
        "	border-radius: 7px\n"
        " }\n"
        " QScrollBar::add-line:vertical {\n"
        "     border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "     height: 20px;\n"
        "	border-bottom-left-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "     subcontrol-position: bottom;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::sub-line:vertical {\n"
        "	border: none;\n"
        "    background: rgb(55, 63"
                                ", 77);\n"
        "     height: 20px;\n"
        "	border-top-left-radius: 7px;\n"
        "    border-top-right-radius: 7px;\n"
        "     subcontrol-position: top;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        "/* CHECKBOX */\n"
        "QCheckBox::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "	width: 15px;\n"
        "	height: 15px;\n"
        "	border-radius: 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QCheckBox::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QCheckBox::indicator:checked {\n"
        "    background: 3px solid rgb(52, 59, 72);\n"
        "	border: 3px solid rgb(52, 59, 72);	\n"
        "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
        "}\n"
        "\n"
        "/* RADIO BUTTON */\n"
        "QRadioButton::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "	width: 15px;\n"
        "	height: 15px;\n"
        "	border-radius"
                                ": 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QRadioButton::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QRadioButton::indicator:checked {\n"
        "    background: 3px solid rgb(94, 106, 130);\n"
        "	border: 3px solid rgb(52, 59, 72);	\n"
        "}\n"
        "\n"
        "/* COMBOBOX */\n"
        "QComboBox{\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding: 5px;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox::drop-down {\n"
        "	subcontrol-origin: padding;\n"
        "	subcontrol-position: top right;\n"
        "	width: 25px; \n"
        "	border-left-width: 3px;\n"
        "	border-left-color: rgba(39, 44, 54, 150);\n"
        "	border-left-style: solid;\n"
        "	border-top-right-radius: 3px;\n"
        "	border-bottom-right-radius: 3px;	\n"
        "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        " }\n"
        "QComboBox QAbstractItemView {\n"
        "	color: rgb("
                                "85, 170, 255);	\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 10px;\n"
        "	selection-background-color: rgb(39, 44, 54);\n"
        "}\n"
        "\n"
        "/* SLIDERS */\n"
        "QSlider::groove:horizontal {\n"
        "    border-radius: 9px;\n"
        "    height: 18px;\n"
        "	margin: 0px;\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:horizontal:hover {\n"
        "	background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:horizontal {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        "QSlider::groove:vertical {\n"
        "    border-radius: 9px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:vertical:hover {\n"
        "	background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:verti"
                                "cal {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "	border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:vertical:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:vertical:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        "")
## CENTRAL-STYLE DEFS | END

## TOGGLE MENU DEFS | START
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(37, 39, 77);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
        "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-repeat;\n"
        "	border: none;\n"
        "	background-color: rgb(37, 39, 77);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(48, 51, 102);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
## TOGGLE MENU DEFS | END

## TOP FRAME DEFS | START
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(37, 39, 77)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
        "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
        "background-position: center;\n"
        "background-repeat: no-repeat;\n"
        "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
        "")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
        "	border: none;\n"
        "	background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(48, 51, 102);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
        "	border: none;\n"
        "	background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(48, 51, 102);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
        "	border: none;\n"
        "	background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(48, 51, 102);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)
## TOP FRAME DEFS | END

## CENTER FRAME DEFS | START
        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(37, 39, 77);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
        "	border-radius: 30px;\n"
        "	background-color: rgb(44, 49, 60);\n"
        "	border: 5px solid rgb(39, 44, 54);\n"
        "	background-position: center;\n"
        "	background-repeat: no-repeat;\n"
        "}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(70, 72, 102);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
## CENTER FRAME DEFS | END

        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

# HOME_PAGE | ~START~
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(40)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
# HOME_PAGE | ~END~

        self.page_appointments = QWidget()
        self.page_appointments.setObjectName(u"page_appointments")
        self.verticalLayout_10_appt = QVBoxLayout(self.page_appointments)
        self.verticalLayout_10_appt.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10_appt.setSpacing(0)
        self.verticalLayout_10_appt.setObjectName(u"verticalLayout_10_appt")

        self.stackedWidget_appointments = QtWidgets.QStackedWidget(self.page_appointments)
        self.stackedWidget_appointments.setObjectName("stackedWidget_appointments")

        self.page_appointments_changeUserF = QFrame(self.page_appointments)
        self.page_appointments_changeUserF.setObjectName(u"page_appointments_changeUserF")
        self.horizontalLayout_page_appointments_changeUserF = QHBoxLayout(self.page_appointments_changeUserF)
        self.horizontalLayout_page_appointments_changeUserF.setContentsMargins(0,0,0,0)
        self.horizontalLayout_page_appointments_changeUserF.setSpacing(0)
        self.horizontalLayout_page_appointments_changeUserF.setObjectName(u"self.horizontalLayout_page_appointments_changeUserF")

        self.page_appointments_changeUserButton = QPushButton()
        self.page_appointments_changeUserButton.setObjectName(u'page_appointments_changeUserButton')

        self.horizontalLayout_page_appointments_changeUserF.addWidget(self.page_appointments_changeUserButton)

## APPOINTMENTS_PAGE - STUDENT | START
        self.page_student_appnt = QtWidgets.QWidget()
        self.page_student_appnt.setStyleSheet("")
        self.page_student_appnt.setObjectName("page_student_appnt")
        self.verticalLayout_page_student_appnt = QtWidgets.QVBoxLayout(self.page_student_appnt)
        self.verticalLayout_page_student_appnt.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_page_student_appnt.setSpacing(0)
        self.verticalLayout_page_student_appnt.setObjectName("verticalLayout_page_student_appnt")
        self.tabWidget_student_appnt = QtWidgets.QTabWidget(self.page_student_appnt)
        self.tabWidget_student_appnt.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_student_appnt.setTabBarAutoHide(False)
        self.tabWidget_student_appnt.setObjectName("tabWidget_student_appnt")
        self.student_appnt_main = QtWidgets.QWidget()
        self.student_appnt_main.setObjectName("student_appnt_main")
        self.verticalLayout_student_appnt_main = QtWidgets.QVBoxLayout(self.student_appnt_main)
        self.verticalLayout_student_appnt_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_appnt_main.setSpacing(0)
        self.verticalLayout_student_appnt_main.setObjectName("verticalLayout_student_appnt_main")
        self.student_appnt_main_topF = QtWidgets.QFrame(self.student_appnt_main)
        self.student_appnt_main_topF.setStyleSheet("QFrame{\n"
        "border: 0\n"
        "}")
        self.student_appnt_main_topF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_appnt_main_topF.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_appnt_main_topF.setObjectName("student_appnt_main_topF")
        self.horizontalLayout_student_appnt_main_topF = QtWidgets.QHBoxLayout(self.student_appnt_main_topF)
        self.horizontalLayout_student_appnt_main_topF.setContentsMargins(8, 8, 8, 4)
        self.horizontalLayout_student_appnt_main_topF.setSpacing(8)
        self.horizontalLayout_student_appnt_main_topF.setObjectName("horizontalLayout_student_appnt_main_topF")
        self.profile_frame = QtWidgets.QFrame(self.student_appnt_main_topF)
        self.profile_frame.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QWidget{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "}")
        self.profile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame.setObjectName("profile_frame")
        self.verticalLayout_profile_frame = QtWidgets.QVBoxLayout(self.profile_frame)
        self.verticalLayout_profile_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_profile_frame.setSpacing(4)
        self.verticalLayout_profile_frame.setObjectName("verticalLayout_profile_frame")
        self.profile_frame_top = QtWidgets.QFrame(self.profile_frame)
        self.profile_frame_top.setStyleSheet("QFrame{\n"
        "border:0;\n"
        "}")
        self.profile_frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame_top.setObjectName("profile_frame_top")
        self.verticalLayout_profile_frame_top = QtWidgets.QVBoxLayout(self.profile_frame_top)
        self.verticalLayout_profile_frame_top.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_profile_frame_top.setSpacing(6)
        self.verticalLayout_profile_frame_top.setObjectName("verticalLayout_profile_frame_top")
        self.info_frame_top = QtWidgets.QFrame(self.profile_frame_top)
        self.info_frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_top.setObjectName("info_frame_top")
        self.verticalLayout_info_frame_top = QtWidgets.QVBoxLayout(self.info_frame_top)
        self.verticalLayout_info_frame_top.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_info_frame_top.setSpacing(4)
        self.verticalLayout_info_frame_top.setObjectName("verticalLayout_info_frame_top")
        self.info_frame_top_image = QtWidgets.QFrame(self.info_frame_top)
        self.info_frame_top_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_top_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_top_image.setObjectName("info_frame_top_image")
        self.verticalLayout_info_frame_top_image = QtWidgets.QVBoxLayout(self.info_frame_top_image)
        self.verticalLayout_info_frame_top_image.setContentsMargins(30, 4, 30, 4)
        self.verticalLayout_info_frame_top_image.setSpacing(0)
        self.verticalLayout_info_frame_top_image.setObjectName("verticalLayout_info_frame_top_image")
        self.image_faculty_studSide = QtWidgets.QLabel(self.info_frame_top_image)
        self.image_faculty_studSide.setObjectName("image_faculty_studSide")
        self.verticalLayout_info_frame_top_image.addWidget(self.image_faculty_studSide)
        self.verticalLayout_info_frame_top.addWidget(self.info_frame_top_image)
        self.info_frame_top_pickFac = QtWidgets.QFrame(self.info_frame_top)
        self.info_frame_top_pickFac.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_top_pickFac.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_top_pickFac.setObjectName("info_frame_top_pickFac")
        self.horizontalLayout_info_frame_top_pickFac = QtWidgets.QHBoxLayout(self.info_frame_top_pickFac)
        self.horizontalLayout_info_frame_top_pickFac.setSpacing(14)
        self.horizontalLayout_info_frame_top_pickFac.setObjectName("horizontalLayout_info_frame_top_pickFac")
        self.comboBox_pick_facultyDept = QtWidgets.QComboBox(self.info_frame_top_pickFac)
        self.comboBox_pick_facultyDept.setObjectName("comboBox_pick_facultyDept")
        self.horizontalLayout_info_frame_top_pickFac.addWidget(self.comboBox_pick_facultyDept)
        self.pick_faculty_studSide = QtWidgets.QComboBox(self.info_frame_top_pickFac)
        self.pick_faculty_studSide.setObjectName("pick_faculty_studSide")
        self.horizontalLayout_info_frame_top_pickFac.addWidget(self.pick_faculty_studSide)
        self.horizontalLayout_info_frame_top_pickFac.setStretch(0, 2)
        self.horizontalLayout_info_frame_top_pickFac.setStretch(1, 5)
        self.verticalLayout_info_frame_top.addWidget(self.info_frame_top_pickFac)
        self.verticalLayout_info_frame_top.setStretch(0, 3)
        self.verticalLayout_info_frame_top.setStretch(1, 1)
        self.verticalLayout_profile_frame_top.addWidget(self.info_frame_top)
        self.info_frame_bot = QtWidgets.QFrame(self.profile_frame_top)
        self.info_frame_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_bot.setObjectName("info_frame_bot")
        self.verticalLayout_info_frame_bot = QtWidgets.QVBoxLayout(self.info_frame_bot)
        self.verticalLayout_info_frame_bot.setObjectName("verticalLayout_info_frame_bot")
        self.availability_details = QtWidgets.QLabel(self.info_frame_bot)
        self.availability_details.setObjectName("availability_details")
        self.verticalLayout_info_frame_bot.addWidget(self.availability_details)
        self.verticalLayout_profile_frame_top.addWidget(self.info_frame_bot)
        self.verticalLayout_profile_frame_top.setStretch(0, 5)
        self.verticalLayout_profile_frame_top.setStretch(1, 4)
        self.verticalLayout_profile_frame.addWidget(self.profile_frame_top)
        self.profile_frame_bot = QtWidgets.QFrame(self.profile_frame)
        self.profile_frame_bot.setStyleSheet("QFrame{\n"
        "border:0\n"
        "}")
        self.profile_frame_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame_bot.setObjectName("profile_frame_bot")
        self.horizontalLayout_profile_frame_bot = QtWidgets.QHBoxLayout(self.profile_frame_bot)
        self.horizontalLayout_profile_frame_bot.setContentsMargins(70, 2, 70, 7)
        self.horizontalLayout_profile_frame_bot.setSpacing(0)
        self.horizontalLayout_profile_frame_bot.setObjectName("horizontalLayout_profile_frame_bot")
        self.setApp_button = QtWidgets.QPushButton(self.profile_frame_bot)
        self.setApp_button.setMaximumSize(QtCore.QSize(16777215, 24))
        self.setApp_button.setStyleSheet("")
        self.setApp_button.setFlat(False)
        self.setApp_button.setObjectName("setApp_button")
        self.horizontalLayout_profile_frame_bot.addWidget(self.setApp_button)
        self.verticalLayout_profile_frame.addWidget(self.profile_frame_bot)
        self.verticalLayout_profile_frame.setStretch(0, 10)
        self.verticalLayout_profile_frame.setStretch(1, 1)
        self.horizontalLayout_student_appnt_main_topF.addWidget(self.profile_frame)
        self.student_calendar_frame = QtWidgets.QFrame(self.student_appnt_main_topF)
        self.student_calendar_frame.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.student_calendar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_calendar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_calendar_frame.setObjectName("student_calendar_frame")
        self.verticalLayout_calendar_frame = QtWidgets.QVBoxLayout(self.student_calendar_frame)
        self.verticalLayout_calendar_frame.setContentsMargins(18, 18, 18, 18)
        self.verticalLayout_calendar_frame.setSpacing(0)
        self.verticalLayout_calendar_frame.setObjectName("verticalLayout_calendar_frame")
        self.student_calendarWidget_pickdate = QtWidgets.QCalendarWidget(self.student_calendar_frame)
        self.student_calendarWidget_pickdate.setStyleSheet("\n"
        "QCalendarWidget QToolButton {\n"
        "    height: 30px;\n"
        "    width: 55px;\n"
        "    color: white;\n"
        "    font-size: 12px;\n"
        "    icon-size: 30px, 30px;\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        "QCalendarWidget QMenu {\n"
        "    width: 80px;\n"
        "    left: 3px;\n"
        "    color: white;\n"
        "    font-size: 11px;\n"
        "    background-color: rgb(100, 100, 100);\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox { \n"
        "    width: 60px; \n"
        "    font-size:11px; \n"
        "    color: white; \n"
        "    background-color: transparent; \n"
        "    selection-background-color: rgb(136, 136, 136);\n"
        "    selection-color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::up-button { \n"
        "subcontrol-origin: border;  \n"
        "subcontrol-position: top right;  \n"
        "width:25px; \n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::down-button {\n"
        "subcontrol-origin: border; \n"
        "subcontrol-position: bottom right;  \n"
        "width:25px;\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; }\n"
        "\n"
        "QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; }\n"
        "\n"
        "/* header row */\n"
        "QCalendarWidget QWidget { alternate-background-color: transparent; border:0;}\n"
        "\n"
        "/* normal days */\n"
        "QCalendarWidget QAbstractItemView:enabled \n"
        "{\n"
        "    font-size:12px;  \n"
        "    color: white;  \n"
        "    selection-background-color: rgba(242, 242, 242, 40); \n"
        "    selection-color: rgb(0, 255, 0); \n"
        "}\n"
        "\n"
        "/* days in other months */\n"
        "QCalendarWidget QAbstractItemView:disabled { color: rgb(195, 195, 195); }\n"
        "\n"
        "QCalendarWidget::NoVerticalHeader{\n"
        "}")
        self.student_calendarWidget_pickdate.setNavigationBarVisible(True)
        self.student_calendarWidget_pickdate.setObjectName("student_calendarWidget_pickdate")
        self.verticalLayout_calendar_frame.addWidget(self.student_calendarWidget_pickdate)
        self.horizontalLayout_student_appnt_main_topF.addWidget(self.student_calendar_frame)
        self.horizontalLayout_student_appnt_main_topF.setStretch(0, 1)
        self.horizontalLayout_student_appnt_main_topF.setStretch(1, 2)
        self.verticalLayout_student_appnt_main.addWidget(self.student_appnt_main_topF)
        self.student_appnt_main_botF = QtWidgets.QFrame(self.student_appnt_main)
        self.student_appnt_main_botF.setStyleSheet("QFrame{\n"
        "border: 0\n"
        "}")
        self.student_appnt_main_botF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_appnt_main_botF.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_appnt_main_botF.setObjectName("student_appnt_main_botF")
        self.verticalLayout_student_appnt_main_botF = QtWidgets.QVBoxLayout(self.student_appnt_main_botF)
        self.verticalLayout_student_appnt_main_botF.setContentsMargins(8, 4, 8, 8)
        self.verticalLayout_student_appnt_main_botF.setSpacing(0)
        self.verticalLayout_student_appnt_main_botF.setObjectName("verticalLayout_student_appnt_main_botF")
        self.appnt_main_botF_label = QtWidgets.QFrame(self.student_appnt_main_botF)
        self.appnt_main_botF_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appnt_main_botF_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appnt_main_botF_label.setObjectName("appnt_main_botF_label")
        self.horizontalLayout_appnt_main_botF_topFlabels = QtWidgets.QHBoxLayout(self.appnt_main_botF_label)
        self.horizontalLayout_appnt_main_botF_topFlabels.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_appnt_main_botF_topFlabels.setSpacing(0)
        self.horizontalLayout_appnt_main_botF_topFlabels.setObjectName("horizontalLayout_appnt_main_botF_topFlabels")
        self.listofappnt_label = QtWidgets.QLabel(self.appnt_main_botF_label)
        self.listofappnt_label.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 12pt;\n"
        "margin-left: 4px;\n"
        "margin-bottom: 2px;\n"
        "}")
        self.listofappnt_label.setObjectName("listofappnt_label")
        self.horizontalLayout_appnt_main_botF_topFlabels.addWidget(self.listofappnt_label)
        self.verticalLayout_student_appnt_main_botF.addWidget(self.appnt_main_botF_label)
        self.appnt_main_botF_tickets = QtWidgets.QFrame(self.student_appnt_main_botF)
        self.appnt_main_botF_tickets.setStyleSheet("QFrame{\n"
        "border-radius: 10px;\n"
        "border: 1px solid #69cdff;\n"
        "\n"
        "}")
        self.appnt_main_botF_tickets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appnt_main_botF_tickets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appnt_main_botF_tickets.setObjectName("appnt_main_botF_tickets")
        self.horizontalLayout_appnt_main_botF_topFtickets = QtWidgets.QHBoxLayout(self.appnt_main_botF_tickets)
        self.horizontalLayout_appnt_main_botF_topFtickets.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_appnt_main_botF_topFtickets.setSpacing(0)
        self.horizontalLayout_appnt_main_botF_topFtickets.setObjectName("horizontalLayout_appnt_main_botF_topFtickets")
        self.student_scrollArea_tickets = QtWidgets.QScrollArea(self.appnt_main_botF_tickets)
        self.student_scrollArea_tickets.setWidgetResizable(True)
        self.student_scrollArea_tickets.setObjectName("student_scrollArea_tickets")
        self.student_scrollArea_tickets_content = QtWidgets.QWidget()
        self.student_scrollArea_tickets_content.setGeometry(QtCore.QRect(0, 0, 1318, 112))
        self.student_scrollArea_tickets_content.setObjectName("student_scrollArea_tickets_content")
        self.horizontalLayout_student_scrollArea_tickets_content = QtWidgets.QHBoxLayout(self.student_scrollArea_tickets_content)
        self.horizontalLayout_student_scrollArea_tickets_content.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_student_scrollArea_tickets_content.setSpacing(3)
        self.horizontalLayout_student_scrollArea_tickets_content.setObjectName("horizontalLayout_student_scrollArea_tickets_content")
        self.student_scrollArea_tickets.setWidget(self.student_scrollArea_tickets_content)
        self.horizontalLayout_appnt_main_botF_topFtickets.addWidget(self.student_scrollArea_tickets)
        self.verticalLayout_student_appnt_main_botF.addWidget(self.appnt_main_botF_tickets)
        self.verticalLayout_student_appnt_main_botF.setStretch(0, 1)
        self.verticalLayout_student_appnt_main_botF.setStretch(1, 3)
        self.verticalLayout_student_appnt_main.addWidget(self.student_appnt_main_botF)
        self.verticalLayout_student_appnt_main.setStretch(0, 3)
        self.verticalLayout_student_appnt_main.setStretch(1, 1)
        self.tabWidget_student_appnt.addTab(self.student_appnt_main, "")
        self.student_appnt_histofappnts = QtWidgets.QWidget()
        self.student_appnt_histofappnts.setStyleSheet("QWidget{\n"
        "color: white;\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}")
        self.student_appnt_histofappnts.setObjectName("student_appnt_histofappnts")
        self.verticalLayout_student_appnt_histofappnts = QtWidgets.QVBoxLayout(self.student_appnt_histofappnts)
        self.verticalLayout_student_appnt_histofappnts.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_appnt_histofappnts.setSpacing(0)
        self.verticalLayout_student_appnt_histofappnts.setObjectName("verticalLayout_student_appnt_histofappnts")
        self.student_appnt_Fhistofappnts = QtWidgets.QFrame(self.student_appnt_histofappnts)
        self.student_appnt_Fhistofappnts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_appnt_Fhistofappnts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_appnt_Fhistofappnts.setObjectName("student_appnt_Fhistofappnts")
        self.verticalLayout_student_appnt_Fhistofappnts = QtWidgets.QVBoxLayout(self.student_appnt_Fhistofappnts)
        self.verticalLayout_student_appnt_Fhistofappnts.setContentsMargins(8, 4, 8, 8)
        self.verticalLayout_student_appnt_Fhistofappnts.setObjectName("verticalLayout_student_appnt_Fhistofappnts")
        self.student_appnt_Fhistofappnts_Ftop = QtWidgets.QFrame(self.student_appnt_Fhistofappnts)
        self.student_appnt_Fhistofappnts_Ftop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_appnt_Fhistofappnts_Ftop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_appnt_Fhistofappnts_Ftop.setObjectName("student_appnt_Fhistofappnts_Ftop")
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop = QtWidgets.QHBoxLayout(self.student_appnt_Fhistofappnts_Ftop)
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.setSpacing(0)
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.setObjectName("horizontalLayout_student_appnt_Fhistofappnts_Ftop")
        self.student_appnt_Fhistofappnts_Ltop = QtWidgets.QLabel(self.student_appnt_Fhistofappnts_Ftop)
        self.student_appnt_Fhistofappnts_Ltop.setStyleSheet("QLabel{\n"
        "margin-left: 3px;\n"
        "margin-right: 3px;\n"
        "}")
        self.student_appnt_Fhistofappnts_Ltop.setObjectName("student_appnt_Fhistofappnts_Ltop")
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.addWidget(self.student_appnt_Fhistofappnts_Ltop)
        self.student_appnt__Fhistofappnts_Ftop_Fright = QtWidgets.QFrame(self.student_appnt_Fhistofappnts_Ftop)
        self.student_appnt__Fhistofappnts_Ftop_Fright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_appnt__Fhistofappnts_Ftop_Fright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_appnt__Fhistofappnts_Ftop_Fright.setObjectName("student_appnt__Fhistofappnts_Ftop_Fright")
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.addWidget(self.student_appnt__Fhistofappnts_Ftop_Fright)
        self.horizontalLayout_student_appnt_Fhistofappnts_Ftop.setStretch(1, 3)
        self.verticalLayout_student_appnt_Fhistofappnts.addWidget(self.student_appnt_Fhistofappnts_Ftop)
        self.student_scrollArea_histofappnts = QtWidgets.QScrollArea(self.student_appnt_Fhistofappnts)
        self.student_scrollArea_histofappnts.setWidgetResizable(True)
        self.student_scrollArea_histofappnts.setObjectName("student_scrollArea_histofappnts")
        self.student_scrollArea_histofappnts_content = QtWidgets.QWidget()
        self.student_scrollArea_histofappnts_content.setGeometry(QtCore.QRect(0, 0, 85, 54))
        self.student_scrollArea_histofappnts_content.setObjectName("student_scrollArea_histofappnts_content")
        self.verticalLayout_student_scrollArea_histofappnts_content = QtWidgets.QVBoxLayout(self.student_scrollArea_histofappnts_content)
        self.verticalLayout_student_scrollArea_histofappnts_content.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_scrollArea_histofappnts_content.setSpacing(0)
        self.verticalLayout_student_scrollArea_histofappnts_content.setObjectName("verticalLayout_student_scrollArea_histofappnts_content")
        self.student_tableView_histofappnts = QtWidgets.QTableView(self.student_scrollArea_histofappnts_content)
        self.student_tableView_histofappnts.setObjectName("student_tableView_histofappnts")
        self.verticalLayout_student_scrollArea_histofappnts_content.addWidget(self.student_tableView_histofappnts)
        self.student_scrollArea_histofappnts.setWidget(self.student_scrollArea_histofappnts_content)
        self.verticalLayout_student_appnt_Fhistofappnts.addWidget(self.student_scrollArea_histofappnts)
        self.verticalLayout_student_appnt_Fhistofappnts.setStretch(0, 1)
        self.verticalLayout_student_appnt_Fhistofappnts.setStretch(1, 12)
        self.verticalLayout_student_appnt_histofappnts.addWidget(self.student_appnt_Fhistofappnts)
        self.tabWidget_student_appnt.addTab(self.student_appnt_histofappnts, "")
        self.verticalLayout_page_student_appnt.addWidget(self.tabWidget_student_appnt)
        self.stackedWidget_appointments.addWidget(self.page_student_appnt)
## APPOINTMENTS_PAGE - STUDENT | END

## APPOINTMENTS_PAGE - FACULTY | START
        self.page_faculty_appnt = QtWidgets.QWidget()
        self.page_faculty_appnt.setStyleSheet("")
        self.page_faculty_appnt.setObjectName("page_faculty_appnt")
        self.verticalLayout_page_faculty_appnt = QtWidgets.QVBoxLayout(self.page_faculty_appnt)
        self.verticalLayout_page_faculty_appnt.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_page_faculty_appnt.setSpacing(0)
        self.verticalLayout_page_faculty_appnt.setObjectName("verticalLayout_page_faculty_appnt")
        self.tabWidget_faculty_appnt = QtWidgets.QTabWidget(self.page_faculty_appnt)
        self.tabWidget_faculty_appnt.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_faculty_appnt.setObjectName("tabWidget_faculty_appnt")
        self.fac_appnt_main = QtWidgets.QWidget()
        self.fac_appnt_main.setObjectName("fac_appnt_main")
        self.verticalLayout_fac_appnt_main = QtWidgets.QVBoxLayout(self.fac_appnt_main)
        self.verticalLayout_fac_appnt_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_appnt_main.setSpacing(0)
        self.verticalLayout_fac_appnt_main.setObjectName("verticalLayout_fac_appnt_main")
        self.fac_appnt_main_Fcontent = QtWidgets.QFrame(self.fac_appnt_main)
        self.fac_appnt_main_Fcontent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_appnt_main_Fcontent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_appnt_main_Fcontent.setObjectName("fac_appnt_main_Fcontent")
        self.horizontalLayout_fac_appnt_main_Fcontent = QtWidgets.QHBoxLayout(self.fac_appnt_main_Fcontent)
        self.horizontalLayout_fac_appnt_main_Fcontent.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_fac_appnt_main_Fcontent.setSpacing(8)
        self.horizontalLayout_fac_appnt_main_Fcontent.setObjectName("horizontalLayout_fac_appnt_main_Fcontent")
        self.fac_appnt_main_FcontentLeft = QtWidgets.QFrame(self.fac_appnt_main_Fcontent)
        self.fac_appnt_main_FcontentLeft.setStyleSheet("QWidget{\n"
        "color: rgb(255, 255, 255);\n"
        "}")
        self.fac_appnt_main_FcontentLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_appnt_main_FcontentLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_appnt_main_FcontentLeft.setObjectName("fac_appnt_main_FcontentLeft")
        self.verticalLayout_fac_appnt_main_FcontentLeft = QtWidgets.QVBoxLayout(self.fac_appnt_main_FcontentLeft)
        self.verticalLayout_fac_appnt_main_FcontentLeft.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_appnt_main_FcontentLeft.setSpacing(8)
        self.verticalLayout_fac_appnt_main_FcontentLeft.setObjectName("verticalLayout_fac_appnt_main_FcontentLeft")
        self.fac_FcontentLeft_top = QtWidgets.QFrame(self.fac_appnt_main_FcontentLeft)
        self.fac_FcontentLeft_top.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "}")
        self.fac_FcontentLeft_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_FcontentLeft_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_FcontentLeft_top.setObjectName("fac_FcontentLeft_top")
        self.verticalLayout_fac_FcontentLeft_top = QtWidgets.QVBoxLayout(self.fac_FcontentLeft_top)
        self.verticalLayout_fac_FcontentLeft_top.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_FcontentLeft_top.setObjectName("verticalLayout_fac_FcontentLeft_top")
        self.fac_Favl_top = QtWidgets.QFrame(self.fac_FcontentLeft_top)
        self.fac_Favl_top.setStyleSheet("QFrame{\n"
        "border:0;\n"
        "}")
        self.fac_Favl_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_Favl_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_Favl_top.setObjectName("fac_Favl_top")
        self.horizontalLayout_fac_Favl_top = QtWidgets.QHBoxLayout(self.fac_Favl_top)
        self.horizontalLayout_fac_Favl_top.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_fac_Favl_top.setSpacing(0)
        self.horizontalLayout_fac_Favl_top.setObjectName("horizontalLayout_fac_Favl_top")
        self.fac_avl_label = QtWidgets.QLabel(self.fac_Favl_top)
        self.fac_avl_label.setStyleSheet("QWidget{\n"
        "border:0;\n"
        "}\n"
        "\n"
        "QLabel{\n"
        "font-family: Arial;\n"
        "font-size: 11pt;\n"
        "margin-left: 4px;\n"
        "}")
        self.fac_avl_label.setObjectName("fac_avl_label")
        self.horizontalLayout_fac_Favl_top.addWidget(self.fac_avl_label)
        self.fac_avl_addsched = QtWidgets.QFrame(self.fac_Favl_top)
        self.fac_avl_addsched.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_avl_addsched.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_avl_addsched.setObjectName("fac_avl_addsched")
        self.horizontalLayout_fac_avl_addsched = QtWidgets.QHBoxLayout(self.fac_avl_addsched)
        self.horizontalLayout_fac_avl_addsched.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_fac_avl_addsched.setSpacing(3)
        self.horizontalLayout_fac_avl_addsched.setObjectName("horizontalLayout_fac_avl_addsched")
        self.fac_pushButton_addsched = QtWidgets.QPushButton(self.fac_avl_addsched)
        self.fac_pushButton_addsched.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-check-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fac_pushButton_addsched.setIcon(icon)
        self.fac_pushButton_addsched.setIconSize(QtCore.QSize(24, 24))
        self.fac_pushButton_addsched.setObjectName("fac_pushButton_addsched")
        self.horizontalLayout_fac_avl_addsched.addWidget(self.fac_pushButton_addsched)
        self.horizontalLayout_fac_Favl_top.addWidget(self.fac_avl_addsched, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_fac_Favl_top.setStretch(0, 1)
        self.verticalLayout_fac_FcontentLeft_top.addWidget(self.fac_Favl_top)
        self.fac_avl_scrollArea_info = QtWidgets.QScrollArea(self.fac_FcontentLeft_top)
        self.fac_avl_scrollArea_info.setStyleSheet("QWidget{\n"
        "border:0;\n"
        "}")
        self.fac_avl_scrollArea_info.setWidgetResizable(True)
        self.fac_avl_scrollArea_info.setObjectName("fac_avl_scrollArea_info")
        self.fac_avl_scrollArea_contents = QtWidgets.QWidget()
        self.fac_avl_scrollArea_contents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.fac_avl_scrollArea_contents.setObjectName("fac_avl_scrollArea_contents")
        self.verticalLayout_fac_avl_scrollArea_contents = QtWidgets.QVBoxLayout(self.fac_avl_scrollArea_contents)
        self.verticalLayout_fac_avl_scrollArea_contents.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_avl_scrollArea_contents.setSpacing(3)
        self.verticalLayout_fac_avl_scrollArea_contents.setObjectName("verticalLayout_fac_avl_scrollArea_contents")
        self.fac_avl_scrollArea_info.setWidget(self.fac_avl_scrollArea_contents)
        self.verticalLayout_fac_FcontentLeft_top.addWidget(self.fac_avl_scrollArea_info)
        self.verticalLayout_fac_FcontentLeft_top.setStretch(0, 1)
        self.verticalLayout_fac_FcontentLeft_top.setStretch(1, 10)
        self.verticalLayout_fac_appnt_main_FcontentLeft.addWidget(self.fac_FcontentLeft_top)
        self.fac_FcontentLeft_bot = QtWidgets.QFrame(self.fac_appnt_main_FcontentLeft)
        self.fac_FcontentLeft_bot.setStyleSheet("QWidget{\n"
        "border: 1px solid #69cdff;\n"
        "}")
        self.fac_FcontentLeft_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_FcontentLeft_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_FcontentLeft_bot.setObjectName("fac_FcontentLeft_bot")
        self.verticalLayout_fac_FcontentLeft_bot = QtWidgets.QVBoxLayout(self.fac_FcontentLeft_bot)
        self.verticalLayout_fac_FcontentLeft_bot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_FcontentLeft_bot.setSpacing(6)
        self.verticalLayout_fac_FcontentLeft_bot.setObjectName("verticalLayout_fac_FcontentLeft_bot")
        self.label = QtWidgets.QLabel(self.fac_FcontentLeft_bot)
        self.label.setStyleSheet("QLabel{\n"
        "border: 0;\n"
        "}")
        self.label.setObjectName("label")
        self.verticalLayout_fac_FcontentLeft_bot.addWidget(self.label)
        self.verticalLayout_fac_appnt_main_FcontentLeft.addWidget(self.fac_FcontentLeft_bot)
        self.verticalLayout_fac_appnt_main_FcontentLeft.setStretch(0, 5)
        self.verticalLayout_fac_appnt_main_FcontentLeft.setStretch(1, 4)
        self.horizontalLayout_fac_appnt_main_Fcontent.addWidget(self.fac_appnt_main_FcontentLeft)
        self.fac_appnt_main_FcontentRight = QtWidgets.QFrame(self.fac_appnt_main_Fcontent)
        self.fac_appnt_main_FcontentRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_appnt_main_FcontentRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_appnt_main_FcontentRight.setObjectName("fac_appnt_main_FcontentRight")
        self.verticalLayout_fac_appnt_main_FcontentRight = QtWidgets.QVBoxLayout(self.fac_appnt_main_FcontentRight)
        self.verticalLayout_fac_appnt_main_FcontentRight.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_appnt_main_FcontentRight.setSpacing(8)
        self.verticalLayout_fac_appnt_main_FcontentRight.setObjectName("verticalLayout_fac_appnt_main_FcontentRight")
        self.fac_FcontentRight_top = QtWidgets.QFrame(self.fac_appnt_main_FcontentRight)
        self.fac_FcontentRight_top.setStyleSheet("QWidget{\n"
        "border: 1px solid #69cdff;\n"
        "}")
        self.fac_FcontentRight_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_FcontentRight_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_FcontentRight_top.setObjectName("fac_FcontentRight_top")
        self.verticalLayout_fac_FcontentRight_top = QtWidgets.QVBoxLayout(self.fac_FcontentRight_top)
        self.verticalLayout_fac_FcontentRight_top.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_fac_FcontentRight_top.setSpacing(0)
        self.verticalLayout_fac_FcontentRight_top.setObjectName("verticalLayout_fac_FcontentRight_top")
        self.fac_calendarWidget_appnts = QtWidgets.QCalendarWidget(self.fac_FcontentRight_top)
        self.fac_calendarWidget_appnts.setStyleSheet("QWidget{\n"
        "border: 0;\n"
        "}\n"
        "\n"
        "QCalendarWidget QToolButton {\n"
        "    height: 30px;\n"
        "    width: 55px;\n"
        "    color: white;\n"
        "    font-size: 12px;\n"
        "    icon-size: 30px, 30px;\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        "QCalendarWidget QMenu {\n"
        "    width: 80px;\n"
        "    left: 3px;\n"
        "    color: white;\n"
        "    font-size: 11px;\n"
        "    background-color: rgb(100, 100, 100);\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox { \n"
        "    width: 60px; \n"
        "    font-size:11px; \n"
        "    color: white; \n"
        "    background-color: transparent; \n"
        "    selection-background-color: rgb(136, 136, 136);\n"
        "    selection-color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::up-button { \n"
        "subcontrol-origin: border;  \n"
        "subcontrol-position: top right;  \n"
        "width:25px; \n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::down-button {\n"
        "subcontrol-origin: border; \n"
        "subcontrol-position: bottom right;  \n"
        "width:25px;\n"
        "}\n"
        "\n"
        "QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; }\n"
        "\n"
        "QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; }\n"
        "\n"
        "/* header row */\n"
        "QCalendarWidget QWidget { alternate-background-color: transparent; border:0;}\n"
        "\n"
        "/* normal days */\n"
        "QCalendarWidget QAbstractItemView:enabled \n"
        "{\n"
        "    font-size:12px;  \n"
        "    color: white;  \n"
        "    selection-background-color: rgba(242, 242, 242, 40); \n"
        "    selection-color: rgb(0, 255, 0); \n"
        "}\n"
        "\n"
        "/* days in other months */\n"
        "QCalendarWidget QAbstractItemView:disabled { color: rgb(195, 195, 195); }\n"
        "\n"
        "QCalendarWidget::NoVerticalHeader{\n"
        "}")
        self.fac_calendarWidget_appnts.setObjectName("fac_calendarWidget_appnts")
        self.verticalLayout_fac_FcontentRight_top.addWidget(self.fac_calendarWidget_appnts)
        self.verticalLayout_fac_appnt_main_FcontentRight.addWidget(self.fac_FcontentRight_top)
        self.fac_FcontentRight_bot = QtWidgets.QFrame(self.fac_appnt_main_FcontentRight)
        self.fac_FcontentRight_bot.setStyleSheet("QWidget{\n"
        "border: 1px solid #69cdff;\n"
        "}")
        self.fac_FcontentRight_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_FcontentRight_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_FcontentRight_bot.setObjectName("fac_FcontentRight_bot")
        self.verticalLayout_fac_FcontentRight_bot = QtWidgets.QVBoxLayout(self.fac_FcontentRight_bot)
        self.verticalLayout_fac_FcontentRight_bot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_FcontentRight_bot.setObjectName("verticalLayout_fac_FcontentRight_bot")
        self.fac_FcontentRight_bot_Ltop = QtWidgets.QLabel(self.fac_FcontentRight_bot)
        self.fac_FcontentRight_bot_Ltop.setStyleSheet("font-size: 11pt;\n"
        "color: rgb(255, 255, 255);\n"
        "border: 0;\n"
        "margin-left: 4px;")
        self.fac_FcontentRight_bot_Ltop.setObjectName("fac_FcontentRight_bot_Ltop")
        self.verticalLayout_fac_FcontentRight_bot.addWidget(self.fac_FcontentRight_bot_Ltop)
        self.fac_scrollArea_logs = QtWidgets.QScrollArea(self.fac_FcontentRight_bot)
        self.fac_scrollArea_logs.setStyleSheet("QWidget{\n"
        "border: 0;\n"
        "}")
        self.fac_scrollArea_logs.setWidgetResizable(True)
        self.fac_scrollArea_logs.setObjectName("fac_scrollArea_logs")
        self.fac_scrollArea_logs_contents = QtWidgets.QWidget()
        self.fac_scrollArea_logs_contents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.fac_scrollArea_logs_contents.setObjectName("fac_scrollArea_logs_contents")
        self.horizontalLayout_fac_scrollArea_logs_contents = QtWidgets.QHBoxLayout(self.fac_scrollArea_logs_contents)
        self.horizontalLayout_fac_scrollArea_logs_contents.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_fac_scrollArea_logs_contents.setObjectName("horizontalLayout_fac_scrollArea_logs_contents")
        self.fac_scrollArea_logs.setWidget(self.fac_scrollArea_logs_contents)
        self.verticalLayout_fac_FcontentRight_bot.addWidget(self.fac_scrollArea_logs)
        self.verticalLayout_fac_FcontentRight_bot.setStretch(0, 1)
        self.verticalLayout_fac_appnt_main_FcontentRight.addWidget(self.fac_FcontentRight_bot)
        self.verticalLayout_fac_appnt_main_FcontentRight.setStretch(0, 6)
        self.verticalLayout_fac_appnt_main_FcontentRight.setStretch(1, 2)
        self.horizontalLayout_fac_appnt_main_Fcontent.addWidget(self.fac_appnt_main_FcontentRight)
        self.horizontalLayout_fac_appnt_main_Fcontent.setStretch(0, 2)
        self.horizontalLayout_fac_appnt_main_Fcontent.setStretch(1, 3)
        self.verticalLayout_fac_appnt_main.addWidget(self.fac_appnt_main_Fcontent)
        self.tabWidget_faculty_appnt.addTab(self.fac_appnt_main, "")
        self.fac_appnt_histofappnts = QtWidgets.QWidget()
        self.fac_appnt_histofappnts.setStyleSheet("QWidget{\n"
        "color: white;\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}")
        self.fac_appnt_histofappnts.setObjectName("fac_appnt_histofappnts")
        self.verticalLayout_fac_appnt_histofappnts = QtWidgets.QVBoxLayout(self.fac_appnt_histofappnts)
        self.verticalLayout_fac_appnt_histofappnts.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_fac_appnt_histofappnts.setObjectName("verticalLayout_fac_appnt_histofappnts")
        self.fac_appnt_Fhistofappnts_Ftop = QtWidgets.QFrame(self.fac_appnt_histofappnts)
        self.fac_appnt_Fhistofappnts_Ftop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_appnt_Fhistofappnts_Ftop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_appnt_Fhistofappnts_Ftop.setObjectName("fac_appnt_Fhistofappnts_Ftop")
        self.horizontalLayout_fac_appnt_Fhistofappnts_Ftop = QtWidgets.QHBoxLayout(self.fac_appnt_Fhistofappnts_Ftop)
        self.horizontalLayout_fac_appnt_Fhistofappnts_Ftop.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_fac_appnt_Fhistofappnts_Ftop.setObjectName("horizontalLayout_fac_appnt_Fhistofappnts_Ftop")
        self.fac_Fhistofappnts_Ltop = QtWidgets.QLabel(self.fac_appnt_Fhistofappnts_Ftop)
        self.fac_Fhistofappnts_Ltop.setStyleSheet("QWidget{\n"
        "margin-left: 4px;\n"
        "}")
        self.fac_Fhistofappnts_Ltop.setIndent(-1)
        self.fac_Fhistofappnts_Ltop.setObjectName("fac_Fhistofappnts_Ltop")
        self.horizontalLayout_fac_appnt_Fhistofappnts_Ftop.addWidget(self.fac_Fhistofappnts_Ltop)
        self.fac_appnt_histofappnts_Ftop_Fright = QtWidgets.QFrame(self.fac_appnt_Fhistofappnts_Ftop)
        self.fac_appnt_histofappnts_Ftop_Fright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fac_appnt_histofappnts_Ftop_Fright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fac_appnt_histofappnts_Ftop_Fright.setObjectName("fac_appnt_histofappnts_Ftop_Fright")
        self.horizontalLayout_fac_appnt_Fhistofappnts_Ftop.addWidget(self.fac_appnt_histofappnts_Ftop_Fright)
        self.verticalLayout_fac_appnt_histofappnts.addWidget(self.fac_appnt_Fhistofappnts_Ftop)
        self.fac_scrollarea_histofappnts = QtWidgets.QScrollArea(self.fac_appnt_histofappnts)
        self.fac_scrollarea_histofappnts.setWidgetResizable(True)
        self.fac_scrollarea_histofappnts.setObjectName("fac_scrollarea_histofappnts")
        self.fac_scrollAreaWidgetContents_histofappnts = QtWidgets.QWidget()
        self.fac_scrollAreaWidgetContents_histofappnts.setGeometry(QtCore.QRect(0, 0, 73, 54))
        self.fac_scrollAreaWidgetContents_histofappnts.setObjectName("fac_scrollAreaWidgetContents_histofappnts")
        self.verticalLayout_fac_scrollAreaWidgetContents_histofappnts = QtWidgets.QVBoxLayout(self.fac_scrollAreaWidgetContents_histofappnts)
        self.verticalLayout_fac_scrollAreaWidgetContents_histofappnts.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_fac_scrollAreaWidgetContents_histofappnts.setSpacing(0)
        self.verticalLayout_fac_scrollAreaWidgetContents_histofappnts.setObjectName("verticalLayout_fac_scrollAreaWidgetContents_histofappnts")
        self.fac_tableView_histofappnts = QtWidgets.QTableView(self.fac_scrollAreaWidgetContents_histofappnts)
        self.fac_tableView_histofappnts.setObjectName("fac_tableView_histofappnts")
        self.verticalLayout_fac_scrollAreaWidgetContents_histofappnts.addWidget(self.fac_tableView_histofappnts)
        self.fac_scrollarea_histofappnts.setWidget(self.fac_scrollAreaWidgetContents_histofappnts)
        self.verticalLayout_fac_appnt_histofappnts.addWidget(self.fac_scrollarea_histofappnts)
        self.verticalLayout_fac_appnt_histofappnts.setStretch(0, 1)
        self.verticalLayout_fac_appnt_histofappnts.setStretch(1, 11)
        self.tabWidget_faculty_appnt.addTab(self.fac_appnt_histofappnts, "")
        self.verticalLayout_page_faculty_appnt.addWidget(self.tabWidget_faculty_appnt)
        self.stackedWidget_appointments.addWidget(self.page_faculty_appnt)
## APPOINTMENTS_PAGE - FACULTY | END

        self.verticalLayout_10_appt.addWidget(self.stackedWidget_appointments)
        self.verticalLayout_10_appt.addWidget(self.page_appointments_changeUserF, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_10_appt.setStretch(20,1)
        self.stackedWidget.addWidget(self.page_appointments)        

        self.popMenu_appointments = QtWidgets.QMenu()
        self.popMenu_appointments.setObjectName('popMenu_appointments')
        self.studAction_appointments = QtWidgets.QAction("Student")
        self.facAction_appointments = QtWidgets.QAction("Faculty")
        self.popMenu_appointments.addAction(self.studAction_appointments)
        self.popMenu_appointments.addAction(self.facAction_appointments)
        self.studAction_appointments.triggered.connect(lambda: self.stackedWidget_appointments.setCurrentWidget(self.page_student_appnt))
        self.facAction_appointments.triggered.connect(lambda: self.stackedWidget_appointments.setCurrentWidget(self.page_faculty_appnt)) 

        self.page_appointments_changeUserButton.setMenu(self.popMenu_appointments)



        self.page_special_services = QWidget()
        self.page_special_services.setObjectName(u"page_special_services")
        self.verticalLayout_10_specserv = QVBoxLayout(self.page_special_services)
        self.verticalLayout_10_specserv.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10_specserv.setSpacing(0)        
        self.verticalLayout_10_specserv.setObjectName(u"verticalLayout_10_specserv")
        
        self.stackedWidget_special_services = QtWidgets.QStackedWidget(self.page_special_services)
        self.stackedWidget_special_services.setObjectName("stackedWidget_special_services")

        self.page_special_services_changeUserF = QFrame(self.page_special_services)
        self.page_special_services_changeUserF.setObjectName(u"page_special_services_changeUserF")
        self.horizontalLayout_page_special_services_changeUserF = QHBoxLayout(self.page_special_services_changeUserF)
        self.horizontalLayout_page_special_services_changeUserF.setContentsMargins(0,0,0,0)
        self.horizontalLayout_page_special_services_changeUserF.setSpacing(0)
        self.horizontalLayout_page_special_services_changeUserF.setObjectName(u"self.horizontalLayout_page_special_services_changeUserF")

        self.page_special_services_changeUserButton = QPushButton()
        self.page_special_services_changeUserButton.setObjectName(u'page_special_services_changeUserButton')

        self.horizontalLayout_page_special_services_changeUserF.addWidget(self.page_special_services_changeUserButton)

##  SPECIAL SERVICES_PAGE - STUDENT | START
        self.page_student_ss = QtWidgets.QWidget()
        self.page_student_ss.setStyleSheet("")
        self.page_student_ss.setObjectName("page_student_ss")
        self.verticalLayout_page_student_ss = QtWidgets.QVBoxLayout(self.page_student_ss)
        self.verticalLayout_page_student_ss.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_page_student_ss.setSpacing(0)
        self.verticalLayout_page_student_ss.setObjectName("verticalLayout_page_student_ss")
        self.tabWidget_student_ss = QtWidgets.QTabWidget(self.page_student_ss)
        self.tabWidget_student_ss.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_student_ss.setObjectName("tabWidget_student_ss")
        self.student_ss_mainTab = QtWidgets.QWidget()
        self.student_ss_mainTab.setObjectName("student_ss_mainTab")
        self.verticalLayout_student_ss_mainTab = QtWidgets.QVBoxLayout(self.student_ss_mainTab)
        self.verticalLayout_student_ss_mainTab.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_ss_mainTab.setSpacing(0)
        self.verticalLayout_student_ss_mainTab.setObjectName("verticalLayout_student_ss_mainTab")
        self.page_student_Fss = QtWidgets.QFrame(self.student_ss_mainTab)
        self.page_student_Fss.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_student_Fss.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_student_Fss.setObjectName("page_student_Fss")
        self.horizontalLayout_page_student_Fss = QtWidgets.QHBoxLayout(self.page_student_Fss)
        self.horizontalLayout_page_student_Fss.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_page_student_Fss.setSpacing(18)
        self.horizontalLayout_page_student_Fss.setObjectName("horizontalLayout_page_student_Fss")
        self.page_student_ss_Fleft = QtWidgets.QFrame(self.page_student_Fss)
        self.page_student_ss_Fleft.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.page_student_ss_Fleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_student_ss_Fleft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_student_ss_Fleft.setObjectName("page_student_ss_Fleft")
        self.verticalLayout_page_student_ss_Fleft = QtWidgets.QVBoxLayout(self.page_student_ss_Fleft)
        self.verticalLayout_page_student_ss_Fleft.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_page_student_ss_Fleft.setSpacing(6)
        self.verticalLayout_page_student_ss_Fleft.setObjectName("verticalLayout_page_student_ss_Fleft")
        self.student_ss_LavlTasks = QtWidgets.QLabel(self.page_student_ss_Fleft)
        self.student_ss_LavlTasks.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "border: 0;\n"
        "margin-left: 4px;\n"
        "}")
        self.student_ss_LavlTasks.setObjectName("student_ss_LavlTasks")
        self.verticalLayout_page_student_ss_Fleft.addWidget(self.student_ss_LavlTasks)
        self.student_scrollArea_ssLeft = QtWidgets.QScrollArea(self.page_student_ss_Fleft)
        self.student_scrollArea_ssLeft.setStyleSheet("QScrollArea{\n"
        "border: 0;\n"
        "}")
        self.student_scrollArea_ssLeft.setWidgetResizable(True)
        self.student_scrollArea_ssLeft.setObjectName("student_scrollArea_ssLeft")
        self.student_scrollAreaWidgetContents_ssLeft_contents = QtWidgets.QWidget()
        self.student_scrollAreaWidgetContents_ssLeft_contents.setGeometry(QtCore.QRect(0, 0, 641, 603))
        self.student_scrollAreaWidgetContents_ssLeft_contents.setObjectName("student_scrollAreaWidgetContents_ssLeft_contents")
        self.gridLayout_student_scrollAreaWidgetContents_ssLeft_contents = QtWidgets.QGridLayout(self.student_scrollAreaWidgetContents_ssLeft_contents)
        self.gridLayout_student_scrollAreaWidgetContents_ssLeft_contents.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_student_scrollAreaWidgetContents_ssLeft_contents.setHorizontalSpacing(7)
        self.gridLayout_student_scrollAreaWidgetContents_ssLeft_contents.setVerticalSpacing(6)
        self.gridLayout_student_scrollAreaWidgetContents_ssLeft_contents.setObjectName("gridLayout_student_scrollAreaWidgetContents_ssLeft_contents")
        self.student_scrollArea_ssLeft.setWidget(self.student_scrollAreaWidgetContents_ssLeft_contents)
        self.verticalLayout_page_student_ss_Fleft.addWidget(self.student_scrollArea_ssLeft)
        self.verticalLayout_page_student_ss_Fleft.setStretch(0, 1)
        self.verticalLayout_page_student_ss_Fleft.setStretch(1, 20)
        self.horizontalLayout_page_student_Fss.addWidget(self.page_student_ss_Fleft)
        self.page_student_ss_Fright = QtWidgets.QFrame(self.page_student_Fss)
        self.page_student_ss_Fright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_student_ss_Fright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_student_ss_Fright.setObjectName("page_student_ss_Fright")
        self.verticalLayout_page_student_ss_Fright = QtWidgets.QVBoxLayout(self.page_student_ss_Fright)
        self.verticalLayout_page_student_ss_Fright.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_page_student_ss_Fright.setSpacing(18)
        self.verticalLayout_page_student_ss_Fright.setObjectName("verticalLayout_page_student_ss_Fright")
        self.student_ss_taskInfo = QtWidgets.QFrame(self.page_student_ss_Fright)
        self.student_ss_taskInfo.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QLabel{\n"
        "color: white;\n"
        "border: 0;\n"
        "}")
        self.student_ss_taskInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_ss_taskInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_ss_taskInfo.setObjectName("student_ss_taskInfo")
        self.verticalLayout_student_ss_taskInfo = QtWidgets.QVBoxLayout(self.student_ss_taskInfo)
        self.verticalLayout_student_ss_taskInfo.setContentsMargins(10, 10, 10, 8)
        self.verticalLayout_student_ss_taskInfo.setObjectName("verticalLayout_student_ss_taskInfo")
        self.student_ss_taskInfo_mainInf = QtWidgets.QLabel(self.student_ss_taskInfo)
        self.student_ss_taskInfo_mainInf.setStyleSheet("QLabel{\n"
        "font-size: 10pt;\n"
        "}")
        self.student_ss_taskInfo_mainInf.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.student_ss_taskInfo_mainInf.setObjectName("student_ss_taskInfo_mainInf")
        self.verticalLayout_student_ss_taskInfo.addWidget(self.student_ss_taskInfo_mainInf)
        self.student_ss_taskInfo_hoursRend = QtWidgets.QLabel(self.student_ss_taskInfo)
        self.student_ss_taskInfo_hoursRend.setStyleSheet("QLabel{\n"
        "font-size: 11pt;\n"
        "}")
        self.student_ss_taskInfo_hoursRend.setObjectName("student_ss_taskInfo_hoursRend")
        self.verticalLayout_student_ss_taskInfo.addWidget(self.student_ss_taskInfo_hoursRend)
        self.verticalLayout_student_ss_taskInfo.setStretch(0, 3)
        self.verticalLayout_student_ss_taskInfo.setStretch(1, 1)
        self.verticalLayout_page_student_ss_Fright.addWidget(self.student_ss_taskInfo)
        self.student_ss_currentTasks = QtWidgets.QFrame(self.page_student_ss_Fright)
        self.student_ss_currentTasks.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.student_ss_currentTasks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_ss_currentTasks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_ss_currentTasks.setObjectName("student_ss_currentTasks")
        self.verticalLayout_student_ss_currentTasks = QtWidgets.QVBoxLayout(self.student_ss_currentTasks)
        self.verticalLayout_student_ss_currentTasks.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_student_ss_currentTasks.setSpacing(6)
        self.verticalLayout_student_ss_currentTasks.setObjectName("verticalLayout_student_ss_currentTasks")
        self.student_ss_LcurrentTasks = QtWidgets.QLabel(self.student_ss_currentTasks)
        self.student_ss_LcurrentTasks.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "border: 0;\n"
        "margin-left: 4px;\n"
        "}")
        self.student_ss_LcurrentTasks.setObjectName("student_ss_LcurrentTasks")
        self.verticalLayout_student_ss_currentTasks.addWidget(self.student_ss_LcurrentTasks)
        self.student_scrollArea_sscurrentTasks = QtWidgets.QScrollArea(self.student_ss_currentTasks)
        self.student_scrollArea_sscurrentTasks.setStyleSheet("QScrollArea{\n"
        "border: 0;\n"
        "}")
        self.student_scrollArea_sscurrentTasks.setWidgetResizable(True)
        self.student_scrollArea_sscurrentTasks.setObjectName("student_scrollArea_sscurrentTasks")
        self.student_scrollArea_sscurrentTasks_contents = QtWidgets.QWidget()
        self.student_scrollArea_sscurrentTasks_contents.setGeometry(QtCore.QRect(0, 0, 639, 372))
        self.student_scrollArea_sscurrentTasks_contents.setObjectName("student_scrollArea_sscurrentTasks_contents")
        self.gridLayout_student_scrollArea_sscurrentTasks_contents = QtWidgets.QGridLayout(self.student_scrollArea_sscurrentTasks_contents)
        self.gridLayout_student_scrollArea_sscurrentTasks_contents.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_student_scrollArea_sscurrentTasks_contents.setSpacing(6)
        self.gridLayout_student_scrollArea_sscurrentTasks_contents.setObjectName("gridLayout_student_scrollArea_sscurrentTasks_contents")
        self.student_scrollArea_sscurrentTasks.setWidget(self.student_scrollArea_sscurrentTasks_contents)
        self.verticalLayout_student_ss_currentTasks.addWidget(self.student_scrollArea_sscurrentTasks)
        self.verticalLayout_student_ss_currentTasks.setStretch(0, 1)
        self.verticalLayout_student_ss_currentTasks.setStretch(1, 12)
        self.verticalLayout_page_student_ss_Fright.addWidget(self.student_ss_currentTasks)
        self.verticalLayout_page_student_ss_Fright.setStretch(0, 1)
        self.verticalLayout_page_student_ss_Fright.setStretch(1, 2)
        self.horizontalLayout_page_student_Fss.addWidget(self.page_student_ss_Fright)
        self.verticalLayout_student_ss_mainTab.addWidget(self.page_student_Fss)
        self.tabWidget_student_ss.addTab(self.student_ss_mainTab, "")
        self.verticalLayout_page_student_ss.addWidget(self.tabWidget_student_ss)
        self.stackedWidget_special_services.addWidget(self.page_student_ss)
##  SPECIAL SERVICES_PAGE - STUDENT | END

##  SPECIAL SERVICES_PAGE - FACULTY | START
        self.page_faculty_ss = QtWidgets.QWidget()
        self.page_faculty_ss.setStyleSheet("")
        self.page_faculty_ss.setObjectName("page_faculty_ss")
        self.verticalLayout_page_faculty_ss = QtWidgets.QVBoxLayout(self.page_faculty_ss)
        self.verticalLayout_page_faculty_ss.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_page_faculty_ss.setSpacing(0)
        self.verticalLayout_page_faculty_ss.setObjectName("verticalLayout_page_faculty_ss")
        self.tabWidget_faculty_ss = QtWidgets.QTabWidget(self.page_faculty_ss)
        self.tabWidget_faculty_ss.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_faculty_ss.setObjectName("tabWidget_faculty_ss")
        self.faculty_ss_mainTab = QtWidgets.QWidget()
        self.faculty_ss_mainTab.setObjectName("faculty_ss_mainTab")
        self.verticalLayout_faculty_ss_mainTab = QtWidgets.QVBoxLayout(self.faculty_ss_mainTab)
        self.verticalLayout_faculty_ss_mainTab.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_ss_mainTab.setSpacing(0)
        self.verticalLayout_faculty_ss_mainTab.setObjectName("verticalLayout_faculty_ss_mainTab")
        self.page_faculty_Fss = QtWidgets.QFrame(self.faculty_ss_mainTab)
        self.page_faculty_Fss.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_Fss.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_Fss.setObjectName("page_faculty_Fss")
        self.horizontalLayout_page_faculty_Fss = QtWidgets.QHBoxLayout(self.page_faculty_Fss)
        self.horizontalLayout_page_faculty_Fss.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_page_faculty_Fss.setSpacing(18)
        self.horizontalLayout_page_faculty_Fss.setObjectName("horizontalLayout_page_faculty_Fss")
        self.page_faculty_ss_Fleft = QtWidgets.QFrame(self.page_faculty_Fss)
        self.page_faculty_ss_Fleft.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.page_faculty_ss_Fleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_ss_Fleft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_ss_Fleft.setObjectName("page_faculty_ss_Fleft")
        self.verticalLayout_page_faculty_ss_Fleft = QtWidgets.QVBoxLayout(self.page_faculty_ss_Fleft)
        self.verticalLayout_page_faculty_ss_Fleft.setObjectName("verticalLayout_page_faculty_ss_Fleft")
        self.faculty_ss_Fleft_tcreatedLabel = QtWidgets.QLabel(self.page_faculty_ss_Fleft)
        self.faculty_ss_Fleft_tcreatedLabel.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "margin-left: 4px;\n"
        "border:0 ;\n"
        "}")
        self.faculty_ss_Fleft_tcreatedLabel.setObjectName("faculty_ss_Fleft_tcreatedLabel")
        self.verticalLayout_page_faculty_ss_Fleft.addWidget(self.faculty_ss_Fleft_tcreatedLabel)
        self.faculty_scrollArea_tcreated = QtWidgets.QScrollArea(self.page_faculty_ss_Fleft)
        self.faculty_scrollArea_tcreated.setStyleSheet("QScrollArea{\n"
        "border: 0;\n"
        "}")
        self.faculty_scrollArea_tcreated.setWidgetResizable(True)
        self.faculty_scrollArea_tcreated.setObjectName("faculty_scrollArea_tcreated")
        self.faculty_scrollArea_tcreated_contents = QtWidgets.QWidget()
        self.faculty_scrollArea_tcreated_contents.setGeometry(QtCore.QRect(0, 0, 637, 601))
        self.faculty_scrollArea_tcreated_contents.setObjectName("faculty_scrollArea_tcreated_contents")
        self.verticalLayout_faculty_scrollArea_tcreated_contents = QtWidgets.QVBoxLayout(self.faculty_scrollArea_tcreated_contents)
        self.verticalLayout_faculty_scrollArea_tcreated_contents.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_faculty_scrollArea_tcreated_contents.setSpacing(4)
        self.verticalLayout_faculty_scrollArea_tcreated_contents.setObjectName("verticalLayout_faculty_scrollArea_tcreated_contents")
        self.faculty_scrollArea_tcreated.setWidget(self.faculty_scrollArea_tcreated_contents)
        self.verticalLayout_page_faculty_ss_Fleft.addWidget(self.faculty_scrollArea_tcreated)
        self.verticalLayout_page_faculty_ss_Fleft.setStretch(0, 1)
        self.verticalLayout_page_faculty_ss_Fleft.setStretch(1, 20)
        self.horizontalLayout_page_faculty_Fss.addWidget(self.page_faculty_ss_Fleft)
        self.page_faculty_ss_Fright = QtWidgets.QFrame(self.page_faculty_Fss)
        self.page_faculty_ss_Fright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_ss_Fright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_ss_Fright.setObjectName("page_faculty_ss_Fright")
        self.verticalLayout_page_faculty_ss_Fright = QtWidgets.QVBoxLayout(self.page_faculty_ss_Fright)
        self.verticalLayout_page_faculty_ss_Fright.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_page_faculty_ss_Fright.setSpacing(18)
        self.verticalLayout_page_faculty_ss_Fright.setObjectName("verticalLayout_page_faculty_ss_Fright")
        self.page_faculty_ss_right_Ftop = QtWidgets.QFrame(self.page_faculty_ss_Fright)
        self.page_faculty_ss_right_Ftop.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.page_faculty_ss_right_Ftop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_ss_right_Ftop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_ss_right_Ftop.setObjectName("page_faculty_ss_right_Ftop")
        self.verticalLayout_page_faculty_ss_right_Ftop = QtWidgets.QVBoxLayout(self.page_faculty_ss_right_Ftop)
        self.verticalLayout_page_faculty_ss_right_Ftop.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_page_faculty_ss_right_Ftop.setObjectName("verticalLayout_page_faculty_ss_right_Ftop")
        self.faculty_ss_right_Ftop_iconLabel = QtWidgets.QLabel(self.page_faculty_ss_right_Ftop)
        self.faculty_ss_right_Ftop_iconLabel.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "margin-left: 4px;\n"
        "border:0 ;\n"
        "}")
        self.faculty_ss_right_Ftop_iconLabel.setObjectName("faculty_ss_right_Ftop_iconLabel")
        self.verticalLayout_page_faculty_ss_right_Ftop.addWidget(self.faculty_ss_right_Ftop_iconLabel)
        self.page_faculty_ss_right_Ftop_iconContents = QtWidgets.QFrame(self.page_faculty_ss_right_Ftop)
        self.page_faculty_ss_right_Ftop_iconContents.setStyleSheet("QWidget{\n"
        "border: 0;\n"
        "}")
        self.page_faculty_ss_right_Ftop_iconContents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_ss_right_Ftop_iconContents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_ss_right_Ftop_iconContents.setObjectName("page_faculty_ss_right_Ftop_iconContents")
        self.gridLayout_page_faculty_ss_right_Ftop_iconContents = QtWidgets.QGridLayout(self.page_faculty_ss_right_Ftop_iconContents)
        self.gridLayout_page_faculty_ss_right_Ftop_iconContents.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_page_faculty_ss_right_Ftop_iconContents.setSpacing(3)
        self.gridLayout_page_faculty_ss_right_Ftop_iconContents.setObjectName("gridLayout_page_faculty_ss_right_Ftop_iconContents")
        self.verticalLayout_page_faculty_ss_right_Ftop.addWidget(self.page_faculty_ss_right_Ftop_iconContents)
        self.verticalLayout_page_faculty_ss_right_Ftop.setStretch(0, 1)
        self.verticalLayout_page_faculty_ss_right_Ftop.setStretch(1, 10)
        self.verticalLayout_page_faculty_ss_Fright.addWidget(self.page_faculty_ss_right_Ftop)
        self.page_faculty_ss_right_Fbot = QtWidgets.QFrame(self.page_faculty_ss_Fright)
        self.page_faculty_ss_right_Fbot.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 10px;\n"
        "}")
        self.page_faculty_ss_right_Fbot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_ss_right_Fbot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_ss_right_Fbot.setObjectName("page_faculty_ss_right_Fbot")
        self.verticalLayout_page_faculty_ss_right_Fbot = QtWidgets.QVBoxLayout(self.page_faculty_ss_right_Fbot)
        self.verticalLayout_page_faculty_ss_right_Fbot.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_page_faculty_ss_right_Fbot.setSpacing(4)
        self.verticalLayout_page_faculty_ss_right_Fbot.setObjectName("verticalLayout_page_faculty_ss_right_Fbot")
        self.faculty_ss_right_bot_Ftcreation = QtWidgets.QFrame(self.page_faculty_ss_right_Fbot)
        self.faculty_ss_right_bot_Ftcreation.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}")
        self.faculty_ss_right_bot_Ftcreation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_ss_right_bot_Ftcreation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_ss_right_bot_Ftcreation.setObjectName("faculty_ss_right_bot_Ftcreation")
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation = QtWidgets.QHBoxLayout(self.faculty_ss_right_bot_Ftcreation)
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation.setSpacing(0)
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation.setObjectName("horizontalLayout_faculty_ss_right_bot_Ftcreation")
        self.faculty_ss_tcreationLabel = QtWidgets.QLabel(self.faculty_ss_right_bot_Ftcreation)
        self.faculty_ss_tcreationLabel.setStyleSheet("QLabel{\n"
        "color: white;\n"
        "font-size: 11pt;\n"
        "margin-left: 4px;\n"
        "border:0 ;\n"
        "}")
        self.faculty_ss_tcreationLabel.setObjectName("faculty_ss_tcreationLabel")
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation.addWidget(self.faculty_ss_tcreationLabel)
        self.faculty_ss_right_bot_tcreation_Fright = QtWidgets.QFrame(self.faculty_ss_right_bot_Ftcreation)
        self.faculty_ss_right_bot_tcreation_Fright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_ss_right_bot_tcreation_Fright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_ss_right_bot_tcreation_Fright.setObjectName("faculty_ss_right_bot_tcreation_Fright")
        self.horizontalLayout_faculty_ss_right_bot_tcreation_Fright = QtWidgets.QHBoxLayout(self.faculty_ss_right_bot_tcreation_Fright)
        self.horizontalLayout_faculty_ss_right_bot_tcreation_Fright.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_faculty_ss_right_bot_tcreation_Fright.setSpacing(2)
        self.horizontalLayout_faculty_ss_right_bot_tcreation_Fright.setObjectName("horizontalLayout_faculty_ss_right_bot_tcreation_Fright")
        self.faculty_ss_right_top_tcreation_right_okCreationButton = QtWidgets.QPushButton(self.faculty_ss_right_bot_tcreation_Fright)
        self.faculty_ss_right_top_tcreation_right_okCreationButton.setStyleSheet("color: white;")
        self.faculty_ss_right_top_tcreation_right_okCreationButton.setObjectName("faculty_ss_right_top_tcreation_right_okCreationButton")
        self.horizontalLayout_faculty_ss_right_bot_tcreation_Fright.addWidget(self.faculty_ss_right_top_tcreation_right_okCreationButton)
        self.horizontalLayout_faculty_ss_right_bot_Ftcreation.addWidget(self.faculty_ss_right_bot_tcreation_Fright, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_page_faculty_ss_right_Fbot.addWidget(self.faculty_ss_right_bot_Ftcreation)
        self.faculty_scrollArea_tcreation = QtWidgets.QScrollArea(self.page_faculty_ss_right_Fbot)
        self.faculty_scrollArea_tcreation.setStyleSheet("QScrollArea{\n"
        "border: 0;\n"
        "}")
        self.faculty_scrollArea_tcreation.setWidgetResizable(True)
        self.faculty_scrollArea_tcreation.setObjectName("faculty_scrollArea_tcreation")
        self.faculty_scrollArea_tcreation_contents = QtWidgets.QWidget()
        self.faculty_scrollArea_tcreation_contents.setGeometry(QtCore.QRect(0, 0, 639, 346))
        self.faculty_scrollArea_tcreation_contents.setObjectName("faculty_scrollArea_tcreation_contents")
        self.verticalLayout_faculty_scrollArea_tcreation_contents = QtWidgets.QVBoxLayout(self.faculty_scrollArea_tcreation_contents)
        self.verticalLayout_faculty_scrollArea_tcreation_contents.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_faculty_scrollArea_tcreation_contents.setSpacing(0)
        self.verticalLayout_faculty_scrollArea_tcreation_contents.setObjectName("verticalLayout_faculty_scrollArea_tcreation_contents")
        self.faculty_scrollArea_tcreation.setWidget(self.faculty_scrollArea_tcreation_contents)
        self.verticalLayout_page_faculty_ss_right_Fbot.addWidget(self.faculty_scrollArea_tcreation)
        self.verticalLayout_page_faculty_ss_right_Fbot.setStretch(1, 10)
        self.verticalLayout_page_faculty_ss_Fright.addWidget(self.page_faculty_ss_right_Fbot)
        self.verticalLayout_page_faculty_ss_Fright.setStretch(0, 2)
        self.verticalLayout_page_faculty_ss_Fright.setStretch(1, 3)
        self.horizontalLayout_page_faculty_Fss.addWidget(self.page_faculty_ss_Fright)
        self.verticalLayout_faculty_ss_mainTab.addWidget(self.page_faculty_Fss)
        self.tabWidget_faculty_ss.addTab(self.faculty_ss_mainTab, "")
        self.verticalLayout_page_faculty_ss.addWidget(self.tabWidget_faculty_ss)
        self.stackedWidget_special_services.addWidget(self.page_faculty_ss)
##  SPECIAL SERVICES_PAGE - FACULTY | END

        self.verticalLayout_10_specserv.addWidget(self.stackedWidget_special_services)
        self.verticalLayout_10_specserv.addWidget(self.page_special_services_changeUserF, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_10_specserv.setStretch(20,1)
        self.stackedWidget.addWidget(self.page_special_services)

        self.popMenu_special_services = QtWidgets.QMenu()
        self.popMenu_special_services.setObjectName('popMenu_special_services')
        self.studAction_special_services = QtWidgets.QAction("Student")
        self.facAction_special_services = QtWidgets.QAction("Faculty")
        self.popMenu_special_services.addAction(self.studAction_special_services)
        self.popMenu_special_services.addAction(self.facAction_special_services)
        self.studAction_special_services.triggered.connect(lambda: self.stackedWidget_special_services.setCurrentWidget(self.page_student_ss))
        self.facAction_special_services.triggered.connect(lambda: self.stackedWidget_special_services.setCurrentWidget(self.page_faculty_ss))  
 
        self.page_special_services_changeUserButton.setMenu(self.popMenu_special_services)

        self.page_roomNkey = QtWidgets.QWidget()
        self.page_roomNkey.setObjectName("page_roomNkey")
        self.verticalLayout_page_roomNkey = QtWidgets.QVBoxLayout(self.page_roomNkey)
        self.verticalLayout_page_roomNkey.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_page_roomNkey.setSpacing(0)
        self.verticalLayout_page_roomNkey.setObjectName("verticalLayout_page_roomNkey")

        self.page_stackedWidget_roomNkey = QtWidgets.QStackedWidget(self.page_roomNkey)
        self.page_stackedWidget_roomNkey.setObjectName("page_stackedWidget_roomNkey")

        self.page_roomNkey_changeUserF = QFrame(self.page_roomNkey)
        self.page_roomNkey_changeUserF.setObjectName(u"page_roomNkey_changeUserF")
        self.horizontalLayout_page_roomNkey_changeUserF = QHBoxLayout(self.page_roomNkey_changeUserF)
        self.horizontalLayout_page_roomNkey_changeUserF.setContentsMargins(0,0,0,0)
        self.horizontalLayout_page_roomNkey_changeUserF.setSpacing(0)
        self.horizontalLayout_page_roomNkey_changeUserF.setObjectName(u"horizontalLayout_page_roomNkey_changeUserF")

        self.page_roomNkey_changeUserButton = QPushButton()
        self.page_roomNkey_changeUserButton.setObjectName(u'page_roomNkey_changeUserButton')

        self.horizontalLayout_page_roomNkey_changeUserF.addWidget(self.page_roomNkey_changeUserButton)
##  ROOM RESERVATION_PAGE - STUDENT | START
        self.page_student_roomNkey = QtWidgets.QWidget()
        self.page_student_roomNkey.setObjectName("page_student_roomNkey")
        self.verticalLayout_page_student_roomNkey = QtWidgets.QVBoxLayout(self.page_student_roomNkey)
        self.verticalLayout_page_student_roomNkey.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_page_student_roomNkey.setSpacing(0)
        self.verticalLayout_page_student_roomNkey.setObjectName("verticalLayout_page_student_roomNkey")
        self.tabWidget_student_roomNkey = QtWidgets.QTabWidget(self.page_student_roomNkey)
        self.tabWidget_student_roomNkey.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_student_roomNkey.setObjectName("tabWidget_student_roomNkey")
        self.student_roomNkey_mainTab = QtWidgets.QWidget()
        self.student_roomNkey_mainTab.setObjectName("student_roomNkey_mainTab")
        self.verticalLayout_student_roomNkey_mainTab = QtWidgets.QVBoxLayout(self.student_roomNkey_mainTab)
        self.verticalLayout_student_roomNkey_mainTab.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_roomNkey_mainTab.setSpacing(0)
        self.verticalLayout_student_roomNkey_mainTab.setObjectName("verticalLayout_student_roomNkey_mainTab")
        self.page_student_FroomNkey = QtWidgets.QFrame(self.student_roomNkey_mainTab)
        self.page_student_FroomNkey.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}")
        self.page_student_FroomNkey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_student_FroomNkey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_student_FroomNkey.setObjectName("page_student_FroomNkey")
        self.verticalLayout_page_student_FroomNkey = QtWidgets.QVBoxLayout(self.page_student_FroomNkey)
        self.verticalLayout_page_student_FroomNkey.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_page_student_FroomNkey.setSpacing(0)
        self.verticalLayout_page_student_FroomNkey.setObjectName("verticalLayout_page_student_FroomNkey")
        self.page_student_FroomNkey_contents = QtWidgets.QFrame(self.page_student_FroomNkey)
        self.page_student_FroomNkey_contents.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}\n"
        "\n"
        "QLabel{\n"
        "font: 14pt;\n"
        "color: white;\n"
        "margin-left: 4px;\n"
        "}\n"
        "")
        self.page_student_FroomNkey_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_student_FroomNkey_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_student_FroomNkey_contents.setObjectName("page_student_FroomNkey_contents")
        self.gridLayout_page_student_FroomNkey_contents = QtWidgets.QGridLayout(self.page_student_FroomNkey_contents)
        self.gridLayout_page_student_FroomNkey_contents.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_page_student_FroomNkey_contents.setSpacing(10)
        self.gridLayout_page_student_FroomNkey_contents.setObjectName("gridLayout_page_student_FroomNkey_contents")
        self.student_room1 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room1.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room1.setObjectName("student_room1")
        self.verticalLayout_student_room1 = QtWidgets.QVBoxLayout(self.student_room1)
        self.verticalLayout_student_room1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room1.setSpacing(0)
        self.verticalLayout_student_room1.setObjectName("verticalLayout_student_room1")
        self.student_pushButton_room1 = QtWidgets.QPushButton(self.student_room1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room1.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room1.setSizePolicy(sizePolicy)
        self.student_pushButton_room1.setText("")
        self.student_pushButton_room1.setObjectName("student_pushButton_room1")
        self.verticalLayout_student_room1.addWidget(self.student_pushButton_room1)
        self.student_label_room1 = QtWidgets.QLabel(self.student_room1)
        self.student_label_room1.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room1.setObjectName("student_label_room1")
        self.verticalLayout_student_room1.addWidget(self.student_label_room1)
        self.verticalLayout_student_room1.setStretch(0, 7)
        self.verticalLayout_student_room1.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room1, 2, 1, 1, 1)
        self.student_room2 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room2.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room2.setObjectName("student_room2")
        self.verticalLayout_student_room2 = QtWidgets.QVBoxLayout(self.student_room2)
        self.verticalLayout_student_room2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room2.setSpacing(0)
        self.verticalLayout_student_room2.setObjectName("verticalLayout_student_room2")
        self.student_pushButton_room2 = QtWidgets.QPushButton(self.student_room2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room2.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room2.setSizePolicy(sizePolicy)
        self.student_pushButton_room2.setText("")
        self.student_pushButton_room2.setObjectName("student_pushButton_room2")
        self.verticalLayout_student_room2.addWidget(self.student_pushButton_room2)
        self.student_label_room2 = QtWidgets.QLabel(self.student_room2)
        self.student_label_room2.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room2.setObjectName("student_label_room2")
        self.verticalLayout_student_room2.addWidget(self.student_label_room2)
        self.verticalLayout_student_room2.setStretch(0, 7)
        self.verticalLayout_student_room2.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room2, 2, 2, 1, 1)
        self.student_room3 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room3.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room3.setObjectName("student_room3")
        self.verticalLayout_student_room3 = QtWidgets.QVBoxLayout(self.student_room3)
        self.verticalLayout_student_room3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room3.setSpacing(0)
        self.verticalLayout_student_room3.setObjectName("verticalLayout_student_room3")
        self.student_pushButton_room3 = QtWidgets.QPushButton(self.student_room3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room3.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room3.setSizePolicy(sizePolicy)
        self.student_pushButton_room3.setText("")
        self.student_pushButton_room3.setObjectName("student_pushButton_room3")
        self.verticalLayout_student_room3.addWidget(self.student_pushButton_room3)
        self.student_label_room3 = QtWidgets.QLabel(self.student_room3)
        self.student_label_room3.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room3.setObjectName("student_label_room3")
        self.verticalLayout_student_room3.addWidget(self.student_label_room3)
        self.verticalLayout_student_room3.setStretch(0, 7)
        self.verticalLayout_student_room3.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room3, 2, 3, 1, 1)
        self.student_room5 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room5.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room5.setObjectName("student_room5")
        self.verticalLayout_student_room5 = QtWidgets.QVBoxLayout(self.student_room5)
        self.verticalLayout_student_room5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room5.setSpacing(0)
        self.verticalLayout_student_room5.setObjectName("verticalLayout_student_room5")
        self.student_pushButton_room5 = QtWidgets.QPushButton(self.student_room5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room5.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room5.setSizePolicy(sizePolicy)
        self.student_pushButton_room5.setText("")
        self.student_pushButton_room5.setObjectName("student_pushButton_room5")
        self.verticalLayout_student_room5.addWidget(self.student_pushButton_room5)
        self.student_label_room5 = QtWidgets.QLabel(self.student_room5)
        self.student_label_room5.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room5.setObjectName("student_label_room5")
        self.verticalLayout_student_room5.addWidget(self.student_label_room5)
        self.verticalLayout_student_room5.setStretch(0, 7)
        self.verticalLayout_student_room5.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room5, 4, 2, 1, 1)
        self.student_room4 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room4.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room4.setObjectName("student_room4")
        self.verticalLayout_student_room4 = QtWidgets.QVBoxLayout(self.student_room4)
        self.verticalLayout_student_room4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room4.setSpacing(0)
        self.verticalLayout_student_room4.setObjectName("verticalLayout_student_room4")
        self.student_pushButton_room4 = QtWidgets.QPushButton(self.student_room4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room4.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room4.setSizePolicy(sizePolicy)
        self.student_pushButton_room4.setText("")
        self.student_pushButton_room4.setObjectName("student_pushButton_room4")
        self.verticalLayout_student_room4.addWidget(self.student_pushButton_room4)
        self.student_label_room4 = QtWidgets.QLabel(self.student_room4)
        self.student_label_room4.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room4.setObjectName("student_label_room4")
        self.verticalLayout_student_room4.addWidget(self.student_label_room4)
        self.verticalLayout_student_room4.setStretch(0, 7)
        self.verticalLayout_student_room4.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room4, 4, 1, 1, 1)
        self.student_room6 = QtWidgets.QFrame(self.page_student_FroomNkey_contents)
        self.student_room6.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.student_room6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.student_room6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.student_room6.setObjectName("student_room6")
        self.verticalLayout_student_room6 = QtWidgets.QVBoxLayout(self.student_room6)
        self.verticalLayout_student_room6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_student_room6.setSpacing(0)
        self.verticalLayout_student_room6.setObjectName("verticalLayout_student_room6")
        self.student_pushButton_room6 = QtWidgets.QPushButton(self.student_room6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton_room6.sizePolicy().hasHeightForWidth())
        self.student_pushButton_room6.setSizePolicy(sizePolicy)
        self.student_pushButton_room6.setText("")
        self.student_pushButton_room6.setObjectName("student_pushButton_room6")
        self.verticalLayout_student_room6.addWidget(self.student_pushButton_room6)
        self.student_label_room6 = QtWidgets.QLabel(self.student_room6)
        self.student_label_room6.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.student_label_room6.setObjectName("student_label_room6")
        self.verticalLayout_student_room6.addWidget(self.student_label_room6)
        self.verticalLayout_student_room6.setStretch(0, 7)
        self.verticalLayout_student_room6.setStretch(1, 1)
        self.gridLayout_page_student_FroomNkey_contents.addWidget(self.student_room6, 4, 3, 1, 1)
        self.verticalLayout_page_student_FroomNkey.addWidget(self.page_student_FroomNkey_contents)
        self.verticalLayout_student_roomNkey_mainTab.addWidget(self.page_student_FroomNkey)
        self.tabWidget_student_roomNkey.addTab(self.student_roomNkey_mainTab, "")
        self.verticalLayout_page_student_roomNkey.addWidget(self.tabWidget_student_roomNkey)
        self.page_stackedWidget_roomNkey.addWidget(self.page_student_roomNkey)
##  ROOM RESERVATION_PAGE - STUDENT | END


##  ROOM RESERVATION_PAGE - FACULTY | START
        self.page_faculty_roomNkey = QtWidgets.QWidget()
        self.page_faculty_roomNkey.setObjectName("page_faculty_roomNkey")
        self.verticalLayout_page_faculty_roomNkey = QtWidgets.QVBoxLayout(self.page_faculty_roomNkey)
        self.verticalLayout_page_faculty_roomNkey.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_page_faculty_roomNkey.setSpacing(0)
        self.verticalLayout_page_faculty_roomNkey.setObjectName("verticalLayout_page_faculty_roomNkey")
        self.tabWidget_faculty_roomNkey = QtWidgets.QTabWidget(self.page_faculty_roomNkey)
        self.tabWidget_faculty_roomNkey.setStyleSheet("\n"
        "QTabWidget::pane { /* The tab widget frame */\n"
        "border:0\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "left: 15px; /* move to the right by 12px */\n"
        "}\n"
        "\n"
        "\n"
        "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
        "\n"
        "QTabBar{\n"
        "font-size: 12pt;\n"
        "font-family: Helvetica;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "color: white;\n"
        "background-color: transparent;\n"
        "margin-left: 7px;\n"
        "margin-right: 7px;\n"
        "padding-left: 5px;\n"
        "padding-right: 5px;\n"
        "padding-bottom: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "background-color: gray;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "border-top: 0;\n"
        "border-left: 0;\n"
        "border-right: 0;\n"
        "border-bottom: 3px solid #69cdff;\n"
        "}")
        self.tabWidget_faculty_roomNkey.setObjectName("tabWidget_faculty_roomNkey")
        self.faculty_roomNkey_mainTab = QtWidgets.QWidget()
        self.faculty_roomNkey_mainTab.setObjectName("faculty_roomNkey_mainTab")
        self.verticalLayout_faculty_roomNkey_mainTab = QtWidgets.QVBoxLayout(self.faculty_roomNkey_mainTab)
        self.verticalLayout_faculty_roomNkey_mainTab.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_roomNkey_mainTab.setSpacing(0)
        self.verticalLayout_faculty_roomNkey_mainTab.setObjectName("verticalLayout_faculty_roomNkey_mainTab")
        self.page_faculty_FroomNkey = QtWidgets.QFrame(self.faculty_roomNkey_mainTab)
        self.page_faculty_FroomNkey.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}")
        self.page_faculty_FroomNkey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_FroomNkey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_FroomNkey.setObjectName("page_faculty_FroomNkey")
        self.verticalLayout_page_faculty_FroomNkey = QtWidgets.QVBoxLayout(self.page_faculty_FroomNkey)
        self.verticalLayout_page_faculty_FroomNkey.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_page_faculty_FroomNkey.setSpacing(0)
        self.verticalLayout_page_faculty_FroomNkey.setObjectName("verticalLayout_page_faculty_FroomNkey")
        self.page_faculty_FroomNkey_contents = QtWidgets.QFrame(self.page_faculty_FroomNkey)
        self.page_faculty_FroomNkey_contents.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}\n"
        "\n"
        "QLabel{\n"
        "font: 14pt;\n"
        "color:white;\n"
        "}\n"
        "")
        self.page_faculty_FroomNkey_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_faculty_FroomNkey_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_faculty_FroomNkey_contents.setObjectName("page_faculty_FroomNkey_contents")
        self.gridLayout_page_faculty_FroomNkey_contents = QtWidgets.QGridLayout(self.page_faculty_FroomNkey_contents)
        self.gridLayout_page_faculty_FroomNkey_contents.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_page_faculty_FroomNkey_contents.setSpacing(10)
        self.gridLayout_page_faculty_FroomNkey_contents.setObjectName("gridLayout_page_faculty_FroomNkey_contents")
        self.faculty_room1 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room1.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room1.setObjectName("faculty_room1")
        self.verticalLayout_faculty_room1 = QtWidgets.QVBoxLayout(self.faculty_room1)
        self.verticalLayout_faculty_room1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room1.setSpacing(0)
        self.verticalLayout_faculty_room1.setObjectName("verticalLayout_faculty_room1")
        self.faculty_pushButton_room1 = QtWidgets.QPushButton(self.faculty_room1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room1.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room1.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room1.setText("")
        self.faculty_pushButton_room1.setObjectName("faculty_pushButton_room1")
        self.verticalLayout_faculty_room1.addWidget(self.faculty_pushButton_room1)
        self.faculty_label_room1 = QtWidgets.QLabel(self.faculty_room1)
        self.faculty_label_room1.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room1.setObjectName("faculty_label_room1")
        self.verticalLayout_faculty_room1.addWidget(self.faculty_label_room1)
        self.verticalLayout_faculty_room1.setStretch(0, 7)
        self.verticalLayout_faculty_room1.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room1, 2, 1, 1, 1)
        self.faculty_room2 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room2.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room2.setObjectName("faculty_room2")
        self.verticalLayout_faculty_room2 = QtWidgets.QVBoxLayout(self.faculty_room2)
        self.verticalLayout_faculty_room2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room2.setSpacing(0)
        self.verticalLayout_faculty_room2.setObjectName("verticalLayout_faculty_room2")
        self.faculty_pushButton_room2 = QtWidgets.QPushButton(self.faculty_room2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room2.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room2.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room2.setText("")
        self.faculty_pushButton_room2.setObjectName("faculty_pushButton_room2")
        self.verticalLayout_faculty_room2.addWidget(self.faculty_pushButton_room2)
        self.faculty_label_room2 = QtWidgets.QLabel(self.faculty_room2)
        self.faculty_label_room2.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room2.setObjectName("faculty_label_room2")
        self.verticalLayout_faculty_room2.addWidget(self.faculty_label_room2)
        self.verticalLayout_faculty_room2.setStretch(0, 7)
        self.verticalLayout_faculty_room2.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room2, 2, 2, 1, 1)
        self.faculty_room3 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room3.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room3.setObjectName("faculty_room3")
        self.verticalLayout_faculty_room3 = QtWidgets.QVBoxLayout(self.faculty_room3)
        self.verticalLayout_faculty_room3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room3.setSpacing(0)
        self.verticalLayout_faculty_room3.setObjectName("verticalLayout_faculty_room3")
        self.faculty_pushButton_room3 = QtWidgets.QPushButton(self.faculty_room3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room3.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room3.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room3.setText("")
        self.faculty_pushButton_room3.setObjectName("faculty_pushButton_room3")
        self.verticalLayout_faculty_room3.addWidget(self.faculty_pushButton_room3)
        self.faculty_label_room3 = QtWidgets.QLabel(self.faculty_room3)
        self.faculty_label_room3.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room3.setObjectName("faculty_label_room3")
        self.verticalLayout_faculty_room3.addWidget(self.faculty_label_room3)
        self.verticalLayout_faculty_room3.setStretch(0, 7)
        self.verticalLayout_faculty_room3.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room3, 2, 3, 1, 1)
        self.faculty_room5 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room5.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room5.setObjectName("faculty_room5")
        self.verticalLayout_faculty_room5 = QtWidgets.QVBoxLayout(self.faculty_room5)
        self.verticalLayout_faculty_room5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room5.setSpacing(0)
        self.verticalLayout_faculty_room5.setObjectName("verticalLayout_faculty_room5")
        self.faculty_pushButton_room5 = QtWidgets.QPushButton(self.faculty_room5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room5.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room5.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room5.setText("")
        self.faculty_pushButton_room5.setObjectName("faculty_pushButton_room5")
        self.verticalLayout_faculty_room5.addWidget(self.faculty_pushButton_room5)
        self.faculty_label_room5 = QtWidgets.QLabel(self.faculty_room5)
        self.faculty_label_room5.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room5.setObjectName("faculty_label_room5")
        self.verticalLayout_faculty_room5.addWidget(self.faculty_label_room5)
        self.verticalLayout_faculty_room5.setStretch(0, 7)
        self.verticalLayout_faculty_room5.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room5, 4, 2, 1, 1)
        self.faculty_room4 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room4.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room4.setObjectName("faculty_room4")
        self.verticalLayout_faculty_room4 = QtWidgets.QVBoxLayout(self.faculty_room4)
        self.verticalLayout_faculty_room4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room4.setSpacing(0)
        self.verticalLayout_faculty_room4.setObjectName("verticalLayout_faculty_room4")
        self.faculty_pushButton_room4 = QtWidgets.QPushButton(self.faculty_room4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room4.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room4.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room4.setText("")
        self.faculty_pushButton_room4.setObjectName("faculty_pushButton_room4")
        self.verticalLayout_faculty_room4.addWidget(self.faculty_pushButton_room4)
        self.faculty_label_room4 = QtWidgets.QLabel(self.faculty_room4)
        self.faculty_label_room4.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room4.setObjectName("faculty_label_room4")
        self.verticalLayout_faculty_room4.addWidget(self.faculty_label_room4)
        self.verticalLayout_faculty_room4.setStretch(0, 7)
        self.verticalLayout_faculty_room4.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room4, 4, 1, 1, 1)
        self.faculty_room6 = QtWidgets.QFrame(self.page_faculty_FroomNkey_contents)
        self.faculty_room6.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.faculty_room6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_room6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_room6.setObjectName("faculty_room6")
        self.verticalLayout_faculty_room6 = QtWidgets.QVBoxLayout(self.faculty_room6)
        self.verticalLayout_faculty_room6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_faculty_room6.setSpacing(0)
        self.verticalLayout_faculty_room6.setObjectName("verticalLayout_faculty_room6")
        self.faculty_pushButton_room6 = QtWidgets.QPushButton(self.faculty_room6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_pushButton_room6.sizePolicy().hasHeightForWidth())
        self.faculty_pushButton_room6.setSizePolicy(sizePolicy)
        self.faculty_pushButton_room6.setText("")
        self.faculty_pushButton_room6.setObjectName("faculty_pushButton_room6")
        self.verticalLayout_faculty_room6.addWidget(self.faculty_pushButton_room6)
        self.faculty_label_room6 = QtWidgets.QLabel(self.faculty_room6)
        self.faculty_label_room6.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.faculty_label_room6.setObjectName("faculty_label_room6")
        self.verticalLayout_faculty_room6.addWidget(self.faculty_label_room6)
        self.verticalLayout_faculty_room6.setStretch(0, 7)
        self.verticalLayout_faculty_room6.setStretch(1, 1)
        self.gridLayout_page_faculty_FroomNkey_contents.addWidget(self.faculty_room6, 4, 3, 1, 1)
        self.verticalLayout_page_faculty_FroomNkey.addWidget(self.page_faculty_FroomNkey_contents)
        self.verticalLayout_page_faculty_FroomNkey.setStretch(0, 20)
        self.verticalLayout_faculty_roomNkey_mainTab.addWidget(self.page_faculty_FroomNkey)
        self.tabWidget_faculty_roomNkey.addTab(self.faculty_roomNkey_mainTab, "")
        self.verticalLayout_page_faculty_roomNkey.addWidget(self.tabWidget_faculty_roomNkey)
        self.page_stackedWidget_roomNkey.addWidget(self.page_faculty_roomNkey)
##  ROOM RESERVATION_PAGE - FACULTY | END


##  ROOM RESERVATION_PAGE - ADMIN | END
        self.page_admin_roomNkey = QtWidgets.QWidget()
        self.page_admin_roomNkey.setObjectName("page_admin_roomNkey")
        self.verticalLayout_page_admin_roomNkey = QtWidgets.QVBoxLayout(self.page_admin_roomNkey)
        self.verticalLayout_page_admin_roomNkey.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_page_admin_roomNkey.setSpacing(0)
        self.verticalLayout_page_admin_roomNkey.setObjectName("verticalLayout_page_admin_roomNkey")
        self.page_admin_FroomNkey = QtWidgets.QFrame(self.page_admin_roomNkey)
        self.page_admin_FroomNkey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_admin_FroomNkey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_admin_FroomNkey.setObjectName("page_admin_FroomNkey")
        self.horizontalLayout_page_admin_FroomNkey = QtWidgets.QHBoxLayout(self.page_admin_FroomNkey)
        self.horizontalLayout_page_admin_FroomNkey.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_page_admin_FroomNkey.setSpacing(8)
        self.horizontalLayout_page_admin_FroomNkey.setObjectName("horizontalLayout_page_admin_FroomNkey")
        self.page_admin_FroomNkey_ctrl = QtWidgets.QFrame(self.page_admin_FroomNkey)
        self.page_admin_FroomNkey_ctrl.setStyleSheet("QFrame{\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}")
        self.page_admin_FroomNkey_ctrl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_admin_FroomNkey_ctrl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_admin_FroomNkey_ctrl.setObjectName("page_admin_FroomNkey_ctrl")
        self.horizontalLayout_page_admin_FroomNkey_ctrl = QtWidgets.QHBoxLayout(self.page_admin_FroomNkey_ctrl)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.setSpacing(2)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.setObjectName("horizontalLayout_page_admin_FroomNkey_ctrl")
        self.FroomNkey_ctrl_overview = QtWidgets.QFrame(self.page_admin_FroomNkey_ctrl)
        self.FroomNkey_ctrl_overview.setStyleSheet("QFrame{\n"
        "border: 0;\n"
        "}")
        self.FroomNkey_ctrl_overview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_overview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_overview.setObjectName("FroomNkey_ctrl_overview")
        self.verticalLayout_FroomNkey_ctrl_overview = QtWidgets.QVBoxLayout(self.FroomNkey_ctrl_overview)
        self.verticalLayout_FroomNkey_ctrl_overview.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_FroomNkey_ctrl_overview.setSpacing(0)
        self.verticalLayout_FroomNkey_ctrl_overview.setObjectName("verticalLayout_FroomNkey_ctrl_overview")
        self.FroomNkey_ctrl_overview_label = QtWidgets.QLabel(self.FroomNkey_ctrl_overview)
        self.FroomNkey_ctrl_overview_label.setStyleSheet("QLabel{\n"
        "font-size: 13pt;\n"
        "color: white;\n"
        "margin-left: 4px;\n"
        "}")
        self.FroomNkey_ctrl_overview_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.FroomNkey_ctrl_overview_label.setObjectName("FroomNkey_ctrl_overview_label")
        self.verticalLayout_FroomNkey_ctrl_overview.addWidget(self.FroomNkey_ctrl_overview_label)
        self.FroomNkey_ctrl_overview_contents = QtWidgets.QFrame(self.FroomNkey_ctrl_overview)
        self.FroomNkey_ctrl_overview_contents.setStyleSheet("QPushButton:hover{\n"
        "background-color: rgb(50,50,50) ;\n"
        "}\n"
        "\n"
        "QWidget{\n"
        "font-size: 11pt;\n"
        "color: white;\n"
        "}")
        self.FroomNkey_ctrl_overview_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_overview_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_overview_contents.setObjectName("FroomNkey_ctrl_overview_contents")
        self.horizontalLayout_FroomNkey_ctrl_overview_contents = QtWidgets.QHBoxLayout(self.FroomNkey_ctrl_overview_contents)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.setObjectName("horizontalLayout_FroomNkey_ctrl_overview_contents")
        self.FroomNkey_ctrl_overview_Leftcontents = QtWidgets.QFrame(self.FroomNkey_ctrl_overview_contents)
        self.FroomNkey_ctrl_overview_Leftcontents.setStyleSheet("")
        self.FroomNkey_ctrl_overview_Leftcontents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_overview_Leftcontents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_overview_Leftcontents.setObjectName("FroomNkey_ctrl_overview_Leftcontents")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents = QtWidgets.QVBoxLayout(self.FroomNkey_ctrl_overview_Leftcontents)
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.setSpacing(4)
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.setObjectName("verticalLayout_FroomNkey_ctrl_overview_Leftcontents")
        self.FroomNkey_ctrl_pushButton_time1 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time1.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time1.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time1.setStyleSheet("")
        self.FroomNkey_ctrl_pushButton_time1.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time1.setObjectName("FroomNkey_ctrl_pushButton_time1")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time1)
        self.FroomNkey_ctrl_pushButton_time2 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time2.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time2.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time2.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time2.setObjectName("FroomNkey_ctrl_pushButton_time2")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time2)
        self.FroomNkey_ctrl_pushButton_time3 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time3.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time3.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time3.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time3.setObjectName("FroomNkey_ctrl_pushButton_time3")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time3)
        self.FroomNkey_ctrl_pushButton_time4 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time4.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time4.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time4.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time4.setObjectName("FroomNkey_ctrl_pushButton_time4")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time4)
        self.FroomNkey_ctrl_pushButton_time5 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time5.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time5.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time5.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time5.setObjectName("FroomNkey_ctrl_pushButton_time5")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time5)
        self.FroomNkey_ctrl_pushButton_time6 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time6.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time6.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time6.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time6.setObjectName("FroomNkey_ctrl_pushButton_time6")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time6)
        self.FroomNkey_ctrl_pushButton_time7 = QtWidgets.QPushButton(self.FroomNkey_ctrl_overview_Leftcontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FroomNkey_ctrl_pushButton_time7.sizePolicy().hasHeightForWidth())
        self.FroomNkey_ctrl_pushButton_time7.setSizePolicy(sizePolicy)
        self.FroomNkey_ctrl_pushButton_time7.setStyleSheet("")
        self.FroomNkey_ctrl_pushButton_time7.setFlat(True)
        self.FroomNkey_ctrl_pushButton_time7.setObjectName("FroomNkey_ctrl_pushButton_time7")
        self.verticalLayout_FroomNkey_ctrl_overview_Leftcontents.addWidget(self.FroomNkey_ctrl_pushButton_time7)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.addWidget(self.FroomNkey_ctrl_overview_Leftcontents)
        self.FroomNkey_ctrl_overview_Rightcontents = QtWidgets.QFrame(self.FroomNkey_ctrl_overview_contents)
        self.FroomNkey_ctrl_overview_Rightcontents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_overview_Rightcontents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_overview_Rightcontents.setObjectName("FroomNkey_ctrl_overview_Rightcontents")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents = QtWidgets.QVBoxLayout(self.FroomNkey_ctrl_overview_Rightcontents)
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.setObjectName("verticalLayout_FroomNkey_ctrl_overview_Rightcontents")
        self.FroomNkey_ctrl_pushButton_timeSlot1 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot1.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot1.setObjectName("FroomNkey_ctrl_pushButton_timeSlot1")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot1)
        self.FroomNkey_ctrl_pushButton_timeSlot2 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot2.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot2.setObjectName("FroomNkey_ctrl_pushButton_timeSlot2")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot2)
        self.FroomNkey_ctrl_pushButton_timeSlot3 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot3.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot3.setObjectName("FroomNkey_ctrl_pushButton_timeSlot3")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot3)
        self.FroomNkey_ctrl_pushButton_timeSlot4 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot4.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot4.setObjectName("FroomNkey_ctrl_pushButton_timeSlot4")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot4)
        self.FroomNkey_ctrl_pushButton_timeSlot5 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot5.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot5.setObjectName("FroomNkey_ctrl_pushButton_timeSlot5")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot5)
        self.FroomNkey_ctrl_pushButton_timeSlot6 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot6.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot6.setObjectName("FroomNkey_ctrl_pushButton_timeSlot6")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot6)
        self.FroomNkey_ctrl_pushButton_timeSlot7 = QtWidgets.QLabel(self.FroomNkey_ctrl_overview_Rightcontents)
        self.FroomNkey_ctrl_pushButton_timeSlot7.setAlignment(QtCore.Qt.AlignCenter)
        self.FroomNkey_ctrl_pushButton_timeSlot7.setObjectName("FroomNkey_ctrl_pushButton_timeSlot7")
        self.verticalLayout_FroomNkey_ctrl_overview_Rightcontents.addWidget(self.FroomNkey_ctrl_pushButton_timeSlot7)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.addWidget(self.FroomNkey_ctrl_overview_Rightcontents)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.setStretch(0, 1)
        self.horizontalLayout_FroomNkey_ctrl_overview_contents.setStretch(1, 3)
        self.verticalLayout_FroomNkey_ctrl_overview.addWidget(self.FroomNkey_ctrl_overview_contents)
        self.FroomNkey_ctrl_overview_accORdec = QtWidgets.QFrame(self.FroomNkey_ctrl_overview)
        self.FroomNkey_ctrl_overview_accORdec.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_overview_accORdec.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_overview_accORdec.setObjectName("FroomNkey_ctrl_overview_accORdec")
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec = QtWidgets.QHBoxLayout(self.FroomNkey_ctrl_overview_accORdec)
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.setObjectName("horizontalLayout_FroomNkey_ctrl_overview_accORdec")
        self.roomNkey_ctrl_Frequests = QtWidgets.QFrame(self.FroomNkey_ctrl_overview_accORdec)
        self.roomNkey_ctrl_Frequests.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomNkey_ctrl_Frequests.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomNkey_ctrl_Frequests.setObjectName("roomNkey_ctrl_Frequests")
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.addWidget(self.roomNkey_ctrl_Frequests)
        self.roomNkey_ctrl_scrollArea_requests = QtWidgets.QScrollArea(self.FroomNkey_ctrl_overview_accORdec)
        self.roomNkey_ctrl_scrollArea_requests.setWidgetResizable(True)
        self.roomNkey_ctrl_scrollArea_requests.setObjectName("roomNkey_ctrl_scrollArea_requests")
        self.roomNkey_ctrl_scrollArea_requests_contents = QtWidgets.QWidget()
        self.roomNkey_ctrl_scrollArea_requests_contents.setGeometry(QtCore.QRect(0, 0, 445, 111))
        self.roomNkey_ctrl_scrollArea_requests_contents.setObjectName("roomNkey_ctrl_scrollArea_requests_contents")
        self.verticalLayout_roomNkey_ctrl_scrollArea_requests_contents = QtWidgets.QVBoxLayout(self.roomNkey_ctrl_scrollArea_requests_contents)
        self.verticalLayout_roomNkey_ctrl_scrollArea_requests_contents.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_roomNkey_ctrl_scrollArea_requests_contents.setObjectName("verticalLayout_roomNkey_ctrl_scrollArea_requests_contents")
        self.roomNkey_ctrl_scrollArea_requests.setWidget(self.roomNkey_ctrl_scrollArea_requests_contents)
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.addWidget(self.roomNkey_ctrl_scrollArea_requests)
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.setStretch(0, 1)
        self.horizontalLayout_FroomNkey_ctrl_overview_accORdec.setStretch(1, 2)
        self.verticalLayout_FroomNkey_ctrl_overview.addWidget(self.FroomNkey_ctrl_overview_accORdec)
        self.verticalLayout_FroomNkey_ctrl_overview.setStretch(0, 1)
        self.verticalLayout_FroomNkey_ctrl_overview.setStretch(1, 4)
        self.verticalLayout_FroomNkey_ctrl_overview.setStretch(2, 1)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.addWidget(self.FroomNkey_ctrl_overview)
        self.FroomNkey_ctrl_logs = QtWidgets.QFrame(self.page_admin_FroomNkey_ctrl)
        self.FroomNkey_ctrl_logs.setStyleSheet("QWidget{\n"
        "color: white;\n"
        "}\n"
        "\n"
        "QFrame{\n"
        "border:0;\n"
        "}")
        self.FroomNkey_ctrl_logs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FroomNkey_ctrl_logs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FroomNkey_ctrl_logs.setObjectName("FroomNkey_ctrl_logs")
        self.verticalLayout_FroomNkey_ctrl_logs = QtWidgets.QVBoxLayout(self.FroomNkey_ctrl_logs)
        self.verticalLayout_FroomNkey_ctrl_logs.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_FroomNkey_ctrl_logs.setSpacing(4)
        self.verticalLayout_FroomNkey_ctrl_logs.setObjectName("verticalLayout_FroomNkey_ctrl_logs")
        self.roomNkey_logsButton = QtWidgets.QPushButton(self.FroomNkey_ctrl_logs)
        self.roomNkey_logsButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.roomNkey_logsButton.setIcon(icon1)
        self.roomNkey_logsButton.setIconSize(QtCore.QSize(18, 18))
        self.roomNkey_logsButton.setFlat(False)
        self.roomNkey_logsButton.setObjectName("roomNkey_logsButton")
        self.verticalLayout_FroomNkey_ctrl_logs.addWidget(self.roomNkey_logsButton)
        self.roomNkey_accORdecButton = QtWidgets.QPushButton(self.FroomNkey_ctrl_logs)
        self.roomNkey_accORdecButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-chevron-circle-left-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.roomNkey_accORdecButton.setIcon(icon2)
        self.roomNkey_accORdecButton.setIconSize(QtCore.QSize(20, 20))
        self.roomNkey_accORdecButton.setObjectName("roomNkey_accORdecButton")
        self.verticalLayout_FroomNkey_ctrl_logs.addWidget(self.roomNkey_accORdecButton)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.addWidget(self.FroomNkey_ctrl_logs, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.setStretch(0, 14)
        self.horizontalLayout_page_admin_FroomNkey_ctrl.setStretch(1, 1)
        self.horizontalLayout_page_admin_FroomNkey.addWidget(self.page_admin_FroomNkey_ctrl)
        self.page_admin_FroomNkey_rooms = QtWidgets.QFrame(self.page_admin_FroomNkey)
        self.page_admin_FroomNkey_rooms.setStyleSheet("color: white;\n"
        "font: 12pt;")
        self.page_admin_FroomNkey_rooms.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_admin_FroomNkey_rooms.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_admin_FroomNkey_rooms.setObjectName("page_admin_FroomNkey_rooms")
        self.gridLayout_page_admin_FroomNkey_rooms = QtWidgets.QGridLayout(self.page_admin_FroomNkey_rooms)
        self.gridLayout_page_admin_FroomNkey_rooms.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_page_admin_FroomNkey_rooms.setSpacing(8)
        self.gridLayout_page_admin_FroomNkey_rooms.setObjectName("gridLayout_page_admin_FroomNkey_rooms")
        self.admin_room1 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room1.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room1.setObjectName("admin_room1")
        self.verticalLayout_admin_room1 = QtWidgets.QVBoxLayout(self.admin_room1)
        self.verticalLayout_admin_room1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room1.setSpacing(0)
        self.verticalLayout_admin_room1.setObjectName("verticalLayout_admin_room1")
        self.admin_pushButton_room1 = QtWidgets.QPushButton(self.admin_room1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room1.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room1.setSizePolicy(sizePolicy)
        self.admin_pushButton_room1.setText("")
        self.admin_pushButton_room1.setObjectName("admin_pushButton_room1")
        self.verticalLayout_admin_room1.addWidget(self.admin_pushButton_room1)
        self.admin_label_room1 = QtWidgets.QLabel(self.admin_room1)
        self.admin_label_room1.setStyleSheet("border: 0;\n"
        "margin-left: 4px;")
        self.admin_label_room1.setObjectName("admin_label_room1")
        self.verticalLayout_admin_room1.addWidget(self.admin_label_room1)
        self.verticalLayout_admin_room1.setStretch(0, 5)
        self.verticalLayout_admin_room1.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room1, 2, 1, 1, 1)
        self.admin_room2 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room2.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room2.setObjectName("admin_room2")
        self.verticalLayout_admin_room2 = QtWidgets.QVBoxLayout(self.admin_room2)
        self.verticalLayout_admin_room2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room2.setSpacing(0)
        self.verticalLayout_admin_room2.setObjectName("verticalLayout_admin_room2")
        self.admin_pushButton_room2 = QtWidgets.QPushButton(self.admin_room2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room2.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room2.setSizePolicy(sizePolicy)
        self.admin_pushButton_room2.setText("")
        self.admin_pushButton_room2.setObjectName("admin_pushButton_room2")
        self.verticalLayout_admin_room2.addWidget(self.admin_pushButton_room2)
        self.admin_label_room2 = QtWidgets.QLabel(self.admin_room2)
        self.admin_label_room2.setStyleSheet("border:0;\n"
        "margin-left: 4px;")
        self.admin_label_room2.setObjectName("admin_label_room2")
        self.verticalLayout_admin_room2.addWidget(self.admin_label_room2)
        self.verticalLayout_admin_room2.setStretch(0, 5)
        self.verticalLayout_admin_room2.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room2, 2, 2, 1, 1)
        self.admin_room3 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room3.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room3.setObjectName("admin_room3")
        self.verticalLayout_admin_room3 = QtWidgets.QVBoxLayout(self.admin_room3)
        self.verticalLayout_admin_room3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room3.setSpacing(0)
        self.verticalLayout_admin_room3.setObjectName("verticalLayout_admin_room3")
        self.admin_pushButton_room3 = QtWidgets.QPushButton(self.admin_room3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room3.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room3.setSizePolicy(sizePolicy)
        self.admin_pushButton_room3.setText("")
        self.admin_pushButton_room3.setObjectName("admin_pushButton_room3")
        self.verticalLayout_admin_room3.addWidget(self.admin_pushButton_room3)
        self.admin_label_room3 = QtWidgets.QLabel(self.admin_room3)
        self.admin_label_room3.setStyleSheet("border:0;\n"
        "margin-left: 4px;")
        self.admin_label_room3.setObjectName("admin_label_room3")
        self.verticalLayout_admin_room3.addWidget(self.admin_label_room3)
        self.verticalLayout_admin_room3.setStretch(0, 5)
        self.verticalLayout_admin_room3.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room3, 3, 1, 1, 1)
        self.admin_room4 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room4.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room4.setObjectName("admin_room4")
        self.verticalLayout_admin_room4 = QtWidgets.QVBoxLayout(self.admin_room4)
        self.verticalLayout_admin_room4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room4.setSpacing(0)
        self.verticalLayout_admin_room4.setObjectName("verticalLayout_admin_room4")
        self.admin_pushButton_room4 = QtWidgets.QPushButton(self.admin_room4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room4.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room4.setSizePolicy(sizePolicy)
        self.admin_pushButton_room4.setText("")
        self.admin_pushButton_room4.setObjectName("admin_pushButton_room4")
        self.verticalLayout_admin_room4.addWidget(self.admin_pushButton_room4)
        self.admin_label_room4 = QtWidgets.QLabel(self.admin_room4)
        self.admin_label_room4.setStyleSheet("border:0;\n"
        "margin-left: 4px;")
        self.admin_label_room4.setObjectName("admin_label_room4")
        self.verticalLayout_admin_room4.addWidget(self.admin_label_room4)
        self.verticalLayout_admin_room4.setStretch(0, 5)
        self.verticalLayout_admin_room4.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room4, 3, 2, 1, 1)
        self.admin_room5 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room5.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room5.setObjectName("admin_room5")
        self.verticalLayout_admin_room5 = QtWidgets.QVBoxLayout(self.admin_room5)
        self.verticalLayout_admin_room5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room5.setSpacing(0)
        self.verticalLayout_admin_room5.setObjectName("verticalLayout_admin_room5")
        self.admin_pushButton_room5 = QtWidgets.QPushButton(self.admin_room5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room5.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room5.setSizePolicy(sizePolicy)
        self.admin_pushButton_room5.setText("")
        self.admin_pushButton_room5.setObjectName("admin_pushButton_room5")
        self.verticalLayout_admin_room5.addWidget(self.admin_pushButton_room5)
        self.admin_label_room5 = QtWidgets.QLabel(self.admin_room5)
        self.admin_label_room5.setStyleSheet("border:0;\n"
        "margin-left: 4px;")
        self.admin_label_room5.setObjectName("admin_label_room5")
        self.verticalLayout_admin_room5.addWidget(self.admin_label_room5)
        self.verticalLayout_admin_room5.setStretch(0, 5)
        self.verticalLayout_admin_room5.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room5, 4, 1, 1, 1)
        self.admin_room6 = QtWidgets.QFrame(self.page_admin_FroomNkey_rooms)
        self.admin_room6.setStyleSheet("QFrame {\n"
        "border: 1px solid #69cdff;\n"
        "border-radius: 6px;\n"
        "}\n"
        "")
        self.admin_room6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_room6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_room6.setObjectName("admin_room6")
        self.verticalLayout_admin_room6 = QtWidgets.QVBoxLayout(self.admin_room6)
        self.verticalLayout_admin_room6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_admin_room6.setSpacing(0)
        self.verticalLayout_admin_room6.setObjectName("verticalLayout_admin_room6")
        self.admin_pushButton_room6 = QtWidgets.QPushButton(self.admin_room6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_pushButton_room6.sizePolicy().hasHeightForWidth())
        self.admin_pushButton_room6.setSizePolicy(sizePolicy)
        self.admin_pushButton_room6.setText("")
        self.admin_pushButton_room6.setObjectName("admin_pushButton_room6")
        self.verticalLayout_admin_room6.addWidget(self.admin_pushButton_room6)
        self.admin_label_room6 = QtWidgets.QLabel(self.admin_room6)
        self.admin_label_room6.setStyleSheet("border:0;\n"
        "margin-left: 4px;")
        self.admin_label_room6.setObjectName("admin_label_room6")
        self.verticalLayout_admin_room6.addWidget(self.admin_label_room6)
        self.verticalLayout_admin_room6.setStretch(0, 5)
        self.verticalLayout_admin_room6.setStretch(1, 1)
        self.gridLayout_page_admin_FroomNkey_rooms.addWidget(self.admin_room6, 4, 2, 1, 1)
        self.horizontalLayout_page_admin_FroomNkey.addWidget(self.page_admin_FroomNkey_rooms)
        self.horizontalLayout_page_admin_FroomNkey.setStretch(0, 5)
        self.horizontalLayout_page_admin_FroomNkey.setStretch(1, 4)
        self.verticalLayout_page_admin_roomNkey.addWidget(self.page_admin_FroomNkey)
        self.page_stackedWidget_roomNkey.addWidget(self.page_admin_roomNkey)
##  ROOM RESERVATION_PAGE - ADMIN | END

        self.verticalLayout_page_roomNkey.addWidget(self.page_stackedWidget_roomNkey)
        self.verticalLayout_page_roomNkey.addWidget(self.page_roomNkey_changeUserF, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_page_roomNkey.setStretch(20,1)
        self.stackedWidget.addWidget(self.page_roomNkey)

        self.popMenu_roomNkey = QtWidgets.QMenu()
        self.popMenu_roomNkey.setObjectName('popMenu_roomNkey')
        self.studAction_roomNkey = QtWidgets.QAction("Student")
        self.facAction_roomNkey = QtWidgets.QAction("Faculty")
        self.admAction_roomNkey = QtWidgets.QAction("Admin")
        self.popMenu_roomNkey.addAction(self.studAction_roomNkey)
        self.popMenu_roomNkey.addAction(self.facAction_roomNkey)
        self.popMenu_roomNkey.addAction(self.admAction_roomNkey)
        self.studAction_roomNkey.triggered.connect(lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_student_roomNkey))
        self.facAction_roomNkey.triggered.connect(lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_faculty_roomNkey))  
        self.admAction_roomNkey.triggered.connect(lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_admin_roomNkey))  

        self.page_roomNkey_changeUserButton.setMenu(self.popMenu_roomNkey)


        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font8)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_widgets)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)


        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)
         # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
        #if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        #endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        #if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        #endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        #if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        #endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stuff here layouted in card style probs(?)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))

        self.image_faculty_studSide.setText(_translate("MainWindow", "Image here"))
        self.availability_details.setText(_translate("MainWindow", "Availability details"))
        self.setApp_button.setText(_translate("MainWindow", "Set Appointment"))
        self.listofappnt_label.setText(_translate("MainWindow", "List of Appointments"))
        self.tabWidget_student_appnt.setTabText(self.tabWidget_student_appnt.indexOf(self.student_appnt_main), _translate("MainWindow", " Appointments "))
        self.student_appnt_Fhistofappnts_Ltop.setText(_translate("MainWindow", "History of Appointments (tableview form)"))
        self.tabWidget_student_appnt.setTabText(self.tabWidget_student_appnt.indexOf(self.student_appnt_histofappnts), _translate("MainWindow", " History "))
        self.fac_avl_label.setText(_translate("MainWindow", "Availability"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Queue is Empty.</span></p></body></html>"))
        self.fac_FcontentRight_bot_Ltop.setText(_translate("MainWindow", "Logs"))
        self.tabWidget_faculty_appnt.setTabText(self.tabWidget_faculty_appnt.indexOf(self.fac_appnt_main), _translate("MainWindow", " Appointments "))
        self.fac_Fhistofappnts_Ltop.setText(_translate("MainWindow", "History of Appointments (tableview form)"))
        self.tabWidget_faculty_appnt.setTabText(self.tabWidget_faculty_appnt.indexOf(self.fac_appnt_histofappnts), _translate("MainWindow", " History "))
        self.student_ss_LavlTasks.setText(_translate("MainWindow", "Available Tasks"))
        self.student_ss_taskInfo_mainInf.setText(_translate("MainWindow", "Task Info"))
        self.student_ss_taskInfo_hoursRend.setText(_translate("MainWindow", "Hours Rendered: X hours"))
        self.student_ss_LcurrentTasks.setText(_translate("MainWindow", "Current Tasks"))
        self.tabWidget_student_ss.setTabText(self.tabWidget_student_ss.indexOf(self.student_ss_mainTab), _translate("MainWindow", " Tasks "))
        self.faculty_ss_Fleft_tcreatedLabel.setText(_translate("MainWindow", "Tasks Created"))
        self.faculty_ss_right_Ftop_iconLabel.setText(_translate("MainWindow", "Task Icons"))
        self.faculty_ss_tcreationLabel.setText(_translate("MainWindow", "Task Creation"))
        self.faculty_ss_right_top_tcreation_right_okCreationButton.setText(_translate("MainWindow", "TC Done"))
        self.tabWidget_faculty_ss.setTabText(self.tabWidget_faculty_ss.indexOf(self.faculty_ss_mainTab), _translate("MainWindow", " Tasks "))
        self.student_label_room1.setText(_translate("MainWindow", "Room 1"))
        self.student_label_room2.setText(_translate("MainWindow", "Room 2"))
        self.student_label_room3.setText(_translate("MainWindow", "Room 3"))
        self.student_label_room5.setText(_translate("MainWindow", "Room 5"))
        self.student_label_room4.setText(_translate("MainWindow", "Room 4"))
        self.student_label_room6.setText(_translate("MainWindow", "Room 6"))
        self.tabWidget_student_roomNkey.setTabText(self.tabWidget_student_roomNkey.indexOf(self.student_roomNkey_mainTab), _translate("MainWindow", " Room Reservation "))
        self.faculty_label_room1.setText(_translate("MainWindow", "Room 1"))
        self.faculty_label_room2.setText(_translate("MainWindow", "Room 2"))
        self.faculty_label_room3.setText(_translate("MainWindow", "Room 3"))
        self.faculty_label_room5.setText(_translate("MainWindow", "Room 5"))
        self.faculty_label_room4.setText(_translate("MainWindow", "Room 4"))
        self.faculty_label_room6.setText(_translate("MainWindow", "Room 6"))
        self.tabWidget_faculty_roomNkey.setTabText(self.tabWidget_faculty_roomNkey.indexOf(self.faculty_roomNkey_mainTab), _translate("MainWindow", " Room Reservation "))
        self.FroomNkey_ctrl_overview_label.setText(_translate("MainWindow", "(current room. default to first room)"))
        self.FroomNkey_ctrl_pushButton_time1.setText(_translate("MainWindow", "7:30 - 9:00"))
        self.FroomNkey_ctrl_pushButton_time2.setText(_translate("MainWindow", "9:00 - 10:30"))
        self.FroomNkey_ctrl_pushButton_time3.setText(_translate("MainWindow", "10:30 - 12:00"))
        self.FroomNkey_ctrl_pushButton_time4.setText(_translate("MainWindow", "12:00 - 1:30"))
        self.FroomNkey_ctrl_pushButton_time5.setText(_translate("MainWindow", "1:30 - 3:00"))
        self.FroomNkey_ctrl_pushButton_time6.setText(_translate("MainWindow", "3:00 - 4:30"))
        self.FroomNkey_ctrl_pushButton_time7.setText(_translate("MainWindow", "4:30 - 6:00"))
        self.FroomNkey_ctrl_pushButton_timeSlot1.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot2.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot3.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot4.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot5.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot6.setText(_translate("MainWindow", "TextLabel"))
        self.FroomNkey_ctrl_pushButton_timeSlot7.setText(_translate("MainWindow", "TextLabel"))
        self.admin_label_room1.setText(_translate("MainWindow", "Room 1"))
        self.admin_label_room2.setText(_translate("MainWindow", "Room 2"))
        self.admin_label_room3.setText(_translate("MainWindow", "Room 3"))
        self.admin_label_room4.setText(_translate("MainWindow", "Room 4"))
        self.admin_label_room5.setText(_translate("MainWindow", "Room 5"))
        self.admin_label_room6.setText(_translate("MainWindow", "Room 6"))
        self.page_appointments_changeUserButton.setText(_translate("MainWindow", "Change User UI"))
        self.page_special_services_changeUserButton.setText(_translate("MainWindow", "Change User UI"))
        self.page_roomNkey_changeUserButton.setText(_translate("MainWindow", "Change User UI"))

        # retranslateUi

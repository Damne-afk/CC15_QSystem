# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serviceshtHbRi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 857)
        Dialog.setStyleSheet(u"background-color: rgb(82, 82, 122);")
        self.icons = QFrame(Dialog)
        self.icons.setObjectName(u"icons")
        self.icons.setGeometry(QRect(480, 60, 451, 201))
        self.icons.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(74, 74, 74);\n"
"border-radius: 15px\n"
"}")
        self.icons.setFrameShape(QFrame.WinPanel)
        self.icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.icons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_task_1 = QPushButton(self.icons)
        self.btn_task_1.setObjectName(u"btn_task_1")
        self.btn_task_1.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        icon = QIcon()
        icon.addFile(u"documentation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_task_1.setIcon(icon)
        self.btn_task_1.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_task_1)

        self.btn_task_2 = QPushButton(self.icons)
        self.btn_task_2.setObjectName(u"btn_task_2")
        self.btn_task_2.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        icon1 = QIcon()
        icon1.addFile(u"assistant.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_task_2.setIcon(icon1)
        self.btn_task_2.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_task_2)

        self.btn_task_3 = QPushButton(self.icons)
        self.btn_task_3.setObjectName(u"btn_task_3")
        self.btn_task_3.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        icon2 = QIcon()
        icon2.addFile(u"paperwork.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_task_3.setIcon(icon2)
        self.btn_task_3.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_task_3)

        self.btn_task_4 = QPushButton(self.icons)
        self.btn_task_4.setObjectName(u"btn_task_4")
        self.btn_task_4.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        icon3 = QIcon()
        icon3.addFile(u"checking activities.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_task_4.setIcon(icon3)
        self.btn_task_4.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_task_4)

        self.creation = QFrame(Dialog)
        self.creation.setObjectName(u"creation")
        self.creation.setGeometry(QRect(490, 320, 451, 481))
        self.creation.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(74, 74, 74);\n"
"border-radius: 15px\n"
"}")
        self.creation.setFrameShape(QFrame.StyledPanel)
        self.creation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.creation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.creation)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.ok_btn = QPushButton(self.page_1)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(330, 430, 71, 21))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(10)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}")
        self.tIcon = QPushButton(self.page_1)
        self.tIcon.setObjectName(u"tIcon")
        self.tIcon.setGeometry(QRect(30, 20, 61, 61))
        self.tIcon.setIcon(icon)
        self.tIcon.setIconSize(QSize(50, 50))
        self.tType = QLabel(self.page_1)
        self.tType.setObjectName(u"tType")
        self.tType.setGeometry(QRect(110, 40, 151, 16))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(14)
        self.tType.setFont(font1)
        self.tDescription = QTextEdit(self.page_1)
        self.tDescription.setObjectName(u"tDescription")
        self.tDescription.setGeometry(QRect(30, 110, 361, 201))
        self.tHours = QLabel(self.page_1)
        self.tHours.setObjectName(u"tHours")
        self.tHours.setGeometry(QRect(40, 345, 151, 21))
        self.tHours.setFont(font1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.ok_btn_2 = QPushButton(self.page_2)
        self.ok_btn_2.setObjectName(u"ok_btn_2")
        self.ok_btn_2.setGeometry(QRect(330, 430, 71, 21))
        self.ok_btn_2.setFont(font)
        self.ok_btn_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}")
        self.tType_2 = QLabel(self.page_2)
        self.tType_2.setObjectName(u"tType_2")
        self.tType_2.setGeometry(QRect(110, 40, 151, 16))
        self.tType_2.setFont(font1)
        self.tHours_2 = QLabel(self.page_2)
        self.tHours_2.setObjectName(u"tHours_2")
        self.tHours_2.setGeometry(QRect(40, 345, 151, 21))
        self.tHours_2.setFont(font1)
        self.tIcon_2 = QPushButton(self.page_2)
        self.tIcon_2.setObjectName(u"tIcon_2")
        self.tIcon_2.setGeometry(QRect(30, 20, 61, 61))
        self.tIcon_2.setIcon(icon1)
        self.tIcon_2.setIconSize(QSize(50, 50))
        self.tDescription_2 = QTextEdit(self.page_2)
        self.tDescription_2.setObjectName(u"tDescription_2")
        self.tDescription_2.setGeometry(QRect(30, 110, 361, 201))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.ok_btn_3 = QPushButton(self.page_3)
        self.ok_btn_3.setObjectName(u"ok_btn_3")
        self.ok_btn_3.setGeometry(QRect(330, 430, 71, 21))
        self.ok_btn_3.setFont(font)
        self.ok_btn_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}")
        self.tHours_3 = QLabel(self.page_3)
        self.tHours_3.setObjectName(u"tHours_3")
        self.tHours_3.setGeometry(QRect(40, 345, 151, 21))
        self.tHours_3.setFont(font1)
        self.tIcon_3 = QPushButton(self.page_3)
        self.tIcon_3.setObjectName(u"tIcon_3")
        self.tIcon_3.setGeometry(QRect(30, 20, 61, 61))
        self.tIcon_3.setIcon(icon2)
        self.tIcon_3.setIconSize(QSize(50, 50))
        self.tDescription_3 = QTextEdit(self.page_3)
        self.tDescription_3.setObjectName(u"tDescription_3")
        self.tDescription_3.setGeometry(QRect(30, 110, 361, 201))
        self.tType_3 = QLabel(self.page_3)
        self.tType_3.setObjectName(u"tType_3")
        self.tType_3.setGeometry(QRect(110, 40, 151, 16))
        self.tType_3.setFont(font1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.ok_btn_4 = QPushButton(self.page_4)
        self.ok_btn_4.setObjectName(u"ok_btn_4")
        self.ok_btn_4.setGeometry(QRect(330, 430, 71, 21))
        self.ok_btn_4.setFont(font)
        self.ok_btn_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}")
        self.tDescription_4 = QTextEdit(self.page_4)
        self.tDescription_4.setObjectName(u"tDescription_4")
        self.tDescription_4.setGeometry(QRect(30, 110, 361, 201))
        self.tIcon_4 = QPushButton(self.page_4)
        self.tIcon_4.setObjectName(u"tIcon_4")
        self.tIcon_4.setGeometry(QRect(30, 20, 61, 61))
        self.tIcon_4.setIcon(icon3)
        self.tIcon_4.setIconSize(QSize(50, 50))
        self.tType_4 = QLabel(self.page_4)
        self.tType_4.setObjectName(u"tType_4")
        self.tType_4.setGeometry(QRect(110, 35, 181, 31))
        self.tType_4.setFont(font1)
        self.tHours_4 = QLabel(self.page_4)
        self.tHours_4.setObjectName(u"tHours_4")
        self.tHours_4.setGeometry(QRect(40, 345, 151, 21))
        self.tHours_4.setFont(font1)
        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 40, 421, 781))
        self.frame.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(74, 74, 74);\n"
"border-radius: 15px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 403, 763))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_task_1.setText(QCoreApplication.translate("Dialog", u"Documentation", None))
        self.btn_task_2.setText(QCoreApplication.translate("Dialog", u"Assistant", None))
        self.btn_task_3.setText(QCoreApplication.translate("Dialog", u"Paperworks", None))
        self.btn_task_4.setText(QCoreApplication.translate("Dialog", u"Checking Activity", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.tIcon.setText("")
        self.tType.setText(QCoreApplication.translate("Dialog", u"Documentation", None))
        self.tDescription.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">This special service includes working on a computer for making a report, saving documents and exporting them, Student must have a skill on Word, Excel and Powerpoint</span></p></body></html>", None))
        self.tHours.setText(QCoreApplication.translate("Dialog", u"Credits: 5 Hours", None))
        self.ok_btn_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.tType_2.setText(QCoreApplication.translate("Dialog", u"Assistant", None))
        self.tHours_2.setText(QCoreApplication.translate("Dialog", u"Credits: 9 Hours", None))
        self.tIcon_2.setText("")
        self.tDescription_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">This special service includes working and doing chores for the Teacher like Enrollment Assistant or being trusted to take over the table while the Teacher is gone. Student must have the skills on Social and understanding the problem</span></p></body></html>", None))
        self.ok_btn_3.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.tHours_3.setText(QCoreApplication.translate("Dialog", u"Credits: 10 Hours", None))
        self.tIcon_3.setText("")
        self.tDescription_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">This special service focuses mainly on arranging the   papers in a certain order and preparing the exam papers. Student is required to be very patient </span></p></body></html>", None))
        self.tType_3.setText(QCoreApplication.translate("Dialog", u"Paperworks", None))
        self.ok_btn_4.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.tDescription_4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">This special service focuses mainly on checking the papers this includes test papers, review papers and exam papers. Students are required to be patient and have a keen awarness on every small details</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.tIcon_4.setText("")
        self.tType_4.setText(QCoreApplication.translate("Dialog", u"Checking Activity", None))
        self.tHours_4.setText(QCoreApplication.translate("Dialog", u"Credits: 11 Hours", None))
    # retranslateUi


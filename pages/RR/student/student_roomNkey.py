# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_roomNkey.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1318, 673)
        Form.setStyleSheet("background-color: rgb(70, 72, 102);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_student_roomNkey = QtWidgets.QTabWidget(Form)
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
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_student_roomNkey.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget_student_roomNkey)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.student_label_room1.setText(_translate("Form", "Room 1"))
        self.student_label_room2.setText(_translate("Form", "Room 2"))
        self.student_label_room3.setText(_translate("Form", "Room 3"))
        self.student_label_room5.setText(_translate("Form", "Room 5"))
        self.student_label_room4.setText(_translate("Form", "Room 4"))
        self.student_label_room6.setText(_translate("Form", "Room 6"))
        self.tabWidget_student_roomNkey.setTabText(self.tabWidget_student_roomNkey.indexOf(self.student_roomNkey_mainTab), _translate("Form", " Room Reservation "))
        self.tabWidget_student_roomNkey.setTabText(self.tabWidget_student_roomNkey.indexOf(self.tab_4), _translate("Form", "Tab 2"))

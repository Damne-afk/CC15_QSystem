# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 555)
        Dialog.setStyleSheet("background-color: rgb(70, 72, 102);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 691, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 261, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 250, 261, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(370, 90, 271, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.id = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.id.setFont(font)
        self.id.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.id.setObjectName("id")
        self.verticalLayout_3.addWidget(self.id)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(370, 250, 271, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.course = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.course.setFont(font)
        self.course.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.course.setObjectName("course")
        self.verticalLayout_4.addWidget(self.course)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name.setPlaceholderText(_translate("Dialog", "Fullname"))
        self.email.setPlaceholderText(_translate("Dialog", "Email"))
        self.id.setPlaceholderText(_translate("Dialog", "ID"))
        self.course.setPlaceholderText(_translate("Dialog", "Course"))

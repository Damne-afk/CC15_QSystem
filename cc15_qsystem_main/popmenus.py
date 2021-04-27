self.page_appointments_changeUserF = QFrame(self.page_appointments)
        self.page_appointments_changeUserF.setObjectName(u"page_appointments_changeUserF")
        self.horizontalLayout_page_appointments_changeUserF = QHBoxLayout(self.page_appointments_changeUserF)
        self.horizontalLayout_page_appointments_changeUserF.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_page_appointments_changeUserF.setSpacing(0)
        self.horizontalLayout_page_appointments_changeUserF.setObjectName(
            u"self.horizontalLayout_page_appointments_changeUserF")

        self.page_appointments_changeUserButton = QPushButton()

        self.page_appointments_changeUserButton.setObjectName(u'page_appointments_changeUserButton')
        self.page_appointments_changeUserButton.setFixedSize(20, 12)
        self.horizontalLayout_page_appointments_changeUserF.addWidget(self.page_appointments_changeUserButton)

        self.verticalLayout_10_appt.addWidget(self.page_appointments_changeUserF, 0,
                                              QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout_10_appt.setStretch(20, 1)

        self.popMenu_appointments = QtWidgets.QMenu()
        self.popMenu_appointments.setObjectName('popMenu_appointments')
        self.studAction_appointments = QtWidgets.QAction("Student")
        self.facAction_appointments = QtWidgets.QAction("Faculty")
        self.popMenu_appointments.addAction(self.studAction_appointments)
        self.popMenu_appointments.addAction(self.facAction_appointments)
        self.studAction_appointments.triggered.connect(
            lambda: self.stackedWidget_appointments.setCurrentWidget(self.page_student_appnt))
        self.facAction_appointments.triggered.connect(
            lambda: self.stackedWidget_appointments.setCurrentWidget(self.page_faculty_appnt))

        self.page_appointments_changeUserButton.setMenu(self.popMenu_appointments)



        self.page_special_services_changeUserF = QFrame(self.page_special_services)
        self.page_special_services_changeUserF.setObjectName(u"page_special_services_changeUserF")
        self.horizontalLayout_page_special_services_changeUserF = QHBoxLayout(self.page_special_services_changeUserF)
        self.horizontalLayout_page_special_services_changeUserF.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_page_special_services_changeUserF.setSpacing(0)
        self.horizontalLayout_page_special_services_changeUserF.setObjectName(
            u"self.horizontalLayout_page_special_services_changeUserF")

        self.page_special_services_changeUserButton = QPushButton()
        self.page_special_services_changeUserButton.setFixedSize(20, 12)
        self.page_special_services_changeUserButton.setObjectName(u'page_special_services_changeUserButton')

        self.horizontalLayout_page_special_services_changeUserF.addWidget(self.page_special_services_changeUserButton)

        self.verticalLayout_10_specserv.addWidget(self.page_special_services_changeUserF, 0,
                                                  QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout_10_specserv.setStretch(20, 1)

        self.popMenu_special_services = QtWidgets.QMenu()
        self.popMenu_special_services.setObjectName('popMenu_special_services')
        self.studAction_special_services = QtWidgets.QAction("Student")
        self.facAction_special_services = QtWidgets.QAction("Faculty")
        self.popMenu_special_services.addAction(self.studAction_special_services)
        self.popMenu_special_services.addAction(self.facAction_special_services)
        self.studAction_special_services.triggered.connect(
            lambda: self.stackedWidget_special_services.setCurrentWidget(self.page_student_ss))
        self.facAction_special_services.triggered.connect(
            lambda: self.stackedWidget_special_services.setCurrentWidget(self.page_faculty_ss))

        self.page_special_services_changeUserButton.setMenu(self.popMenu_special_services)



        self.page_roomNkey_changeUserF = QFrame(self.page_roomNkey)
        self.page_roomNkey_changeUserF.setObjectName(u"page_roomNkey_changeUserF")
        self.horizontalLayout_page_roomNkey_changeUserF = QHBoxLayout(self.page_roomNkey_changeUserF)
        self.horizontalLayout_page_roomNkey_changeUserF.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_page_roomNkey_changeUserF.setSpacing(0)
        self.horizontalLayout_page_roomNkey_changeUserF.setObjectName(u"horizontalLayout_page_roomNkey_changeUserF")

        self.page_roomNkey_changeUserButton = QPushButton()
        self.page_roomNkey_changeUserButton.setFixedSize(20, 12)
        self.page_roomNkey_changeUserButton.setObjectName(u'page_roomNkey_changeUserButton')

        self.horizontalLayout_page_roomNkey_changeUserF.addWidget(self.page_roomNkey_changeUserButton)

        self.verticalLayout_page_roomNkey.addWidget(self.page_roomNkey_changeUserF, 0,
                                                    QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout_page_roomNkey.setStretch(20, 1)

        self.popMenu_roomNkey = QtWidgets.QMenu()
        self.popMenu_roomNkey.setObjectName('popMenu_roomNkey')
        self.studAction_roomNkey = QtWidgets.QAction("Student")
        self.facAction_roomNkey = QtWidgets.QAction("Faculty")
        self.admAction_roomNkey = QtWidgets.QAction("Admin")
        self.popMenu_roomNkey.addAction(self.studAction_roomNkey)
        self.popMenu_roomNkey.addAction(self.facAction_roomNkey)
        self.popMenu_roomNkey.addAction(self.admAction_roomNkey)
        self.studAction_roomNkey.triggered.connect(
            lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_student_roomNkey))
        self.facAction_roomNkey.triggered.connect(
            lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_faculty_roomNkey))
        self.admAction_roomNkey.triggered.connect(
            lambda: self.page_stackedWidget_roomNkey.setCurrentWidget(self.page_admin_roomNkey))

        self.page_roomNkey_changeUserButton.setMenu(self.popMenu_roomNkey)

        self.page_appointments_changeUserButton.setText(_translate("MainWindow", "Change User UI"))
        self.page_special_services_changeUserButton.setText(_translate("MainWindow", "Change User UI"))
        self.page_roomNkey_changeUserButton.setText(_translate("MainWindow", "Change User UI"))
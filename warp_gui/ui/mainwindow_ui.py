# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowZWvGuY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(249, 305)
        MainWindow.setMinimumSize(QtCore.QSize(249, 305))
        MainWindow.setMaximumSize(QtCore.QSize(249, 305))
        MainWindow.setStyleSheet(u"background:#3d3d3d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.top_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.top_spacer, 0, 0, 1, 1)

        self.account_type = QtWidgets.QLabel(self.centralwidget)
        self.account_type.setObjectName(u"account_type")
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.account_type.setFont(font)
        self.account_type.setStyleSheet(u"color:rgb(247,112,51);")
        self.account_type.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.account_type, 1, 0, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.pushButton_start_end = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_end.setObjectName(u"pushButton_start_end")
        self.pushButton_start_end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_end.setStyleSheet(u"QPushButton{\n"
"    background-color: #fff; /* Green */\n"
"    border: none;\n"
"    color: #000;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 20px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"        background-color:#3bb300;\n"
"        color: #fff;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_start_end, 1, 1, 1, 1)

        self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.label_status_sub_message = QtWidgets.QLabel(self.centralwidget)
        self.label_status_sub_message.setObjectName(u"label_status_sub_message")
        self.label_status_sub_message.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_status_sub_message, 6, 0, 1, 1)

        self.label_status_message = QtWidgets.QLabel(self.centralwidget)
        self.label_status_message.setObjectName(u"label_status_message")

        font1 = QtGui.QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_status_message.setFont(font1)
        self.label_status_message.setStyleSheet(u"color:rgb(255, 80, 57);")
        self.label_status_message.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_status_message, 5, 0, 1, 1)

        self.middle_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.middle_spacer, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"Cloudflare Warp", None))
        self.account_type.setText(QtCore.QCoreApplication.translate("MainWindow", u"WARP", None))
        self.pushButton_start_end.setText(QtCore.QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_status_sub_message.setText(QtCore.QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Your internet is </span><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">not private</span></p></body></html>", None))
        self.label_status_message.setText(QtCore.QCoreApplication.translate("MainWindow", u"DISCONNECTED", None))
    # retranslateUi


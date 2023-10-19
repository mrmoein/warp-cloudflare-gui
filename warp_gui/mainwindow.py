import os
import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon
from qtwidgets import AnimatedToggle

from warp_gui.commend import Commend
from warp_gui.ui.mainwindow_ui import Ui_MainWindow


class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setApplicationName('Cloudflare Warp')
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.closeEvent = self.handleCloseEvent
        self.ui = Ui_MainWindow()
        self.commend = Commend()
        self.ui.setupUi(self.mainWindow)
        self.need_stop = False
        self.last_status = 'First Start'
        self.connected = False
        self.init_tray_icon()
        self.toggle_color = "#f77033"
        self.init_account()
        self.toggle = self.init_toggle(self.toggle_color)
        self.init_signals()
        self.set_icon()
        threading.Thread(target=self.status_thread).start()

    def init_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(QIcon(os.path.dirname(__file__) + '/../icons/offline.png'), self.mainWindow)
        self.menu_tray = QMenu()
        self.__menu_tray_connect = QAction("Connect / Disconnect")
        self.menu_tray.addAction(self.__menu_tray_connect)
        self.__menu_tray_hide = QAction("Hide / Show")
        self.menu_tray.addAction(self.__menu_tray_hide)
        self.__menu_tray_quit = QAction("Quit")
        self.menu_tray.addAction(self.__menu_tray_quit)
        self.tray_icon.setContextMenu(self.menu_tray)
        self.tray_icon.show()

    def set_tray_icon(self, connected):
        if connected:
            self.tray_icon.setIcon(QIcon(os.path.dirname(__file__) + '/../icons/online.png'))
        else:
            self.tray_icon.setIcon(QIcon(os.path.dirname(__file__) + '/../icons/offline.png'))

    def init_account(self):
        account_type = self.commend.account_type()
        if account_type == 'team':
            self.ui.account_type.setText('TEAMS')
            self.ui.account_type.setStyleSheet(u"color:rgb(70, 111, 221);")
            self.toggle_color = "#466fdd"
        elif account_type == 'free':
            pass
        else:
            self.ui.account_type.setText('WARP+')

    def init_toggle(self, color):
        toggle = AnimatedToggle(checked_color=color, pulse_checked_color="#44FFB000")
        if self.connected:
            toggle.setChecked(True)
            self.ui.label_status_message.setStyleSheet(u"color:rgb(123, 199, 171);")
            self.set_tray_icon(True)
        toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        toggle.setMinimumSize(140, 120)
        self.ui.pushButton_start_end.close()
        self.ui.gridLayout.addWidget(toggle, 0, 1, 1, 1)
        return toggle

    def set_icon(self):
        self.mainWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/../icons/logo.png"))

    def init_signals(self):
        self.toggle.clicked.connect(self.connect_button_clicked)
        self.__menu_tray_connect.triggered.connect(self.tray_connect_disconnect_clicked)
        self.__menu_tray_hide.triggered.connect(self.tray_hide_show_clicked)
        self.__menu_tray_quit.triggered.connect(self.app.quit)

    def tray_hide_show_clicked(self):
        if self.mainWindow.isHidden():
            self.mainWindow.show()
        else:
            self.mainWindow.hide()

    def tray_connect_disconnect_clicked(self):
        if not self.commend.is_connected():
            self.commend.connect()
        else:
            self.commend.disconnect()

    def connect_button_clicked(self):
        if self.toggle.isChecked():
            self.commend.connect()
        else:
            self.commend.disconnect()

    def show(self, hide=False):
        if not hide:
            self.mainWindow.show()
        self.app.aboutToQuit.connect(self.end_program)
        sys.exit(self.app.exec_())

    def end_program(self):
        self.need_stop = True

    def status_thread(self):
        while not self.need_stop:
            status = self.commend.status()

            if self.last_status == status:
                time.sleep(1)
                continue

            self.ui.label_status_message.setText(status)

            if status.startswith('Connected'):
                self.toggle.setChecked(True)
                self.ui.label_status_message.setStyleSheet(u"color:rgb(123, 199, 171);")
                self.set_sub_status_message('private')
                self.connected = True
                self.set_tray_icon(True)
            elif status.startswith('Disconnected') or \
                    status.startswith('Unable to connect'):
                self.toggle.setChecked(False)
                self.set_sub_status_message('not private')
                self.ui.label_status_message.setStyleSheet(u"color:rgb(255, 80, 57);")
                self.connected = False
                self.set_tray_icon(False)

            self.last_status = status

    def set_sub_status_message(self, text):
        self.ui.label_status_sub_message.setText(
            "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Your internet is </span><span "
            "style=\" font-size:11pt; font-weight:600; color:#ffffff;\">{text}</span></p></body></html>".format(
                text=text))

    def handleCloseEvent(self, a0):
        self.mainWindow.hide()
        a0.ignore()

from window import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
import time


class StarterGUI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.statement = self.check_warp_statement()
        self.local_statement = self.statement
        self.base_styleSheet = self.ui.pushButton_start_end.styleSheet()
        self.custom_setup()
        # self.change_connect_button_color('#fff', '#ff5c33', '#ff5c33', '#fff')

    def custom_setup(self):
        self.MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        self.ui.pushButton_start_end.clicked.connect(self.connect_button_clicked)
        if self.local_statement == 'on':
            self.change_connect_button_color('#fff', '#ff5c33', '#ff5c33', '#fff')
            self.change_connect_button_text('End')
            self.ui.label_status_message.setText('CONNECTED')
            self.set_sub_status_message('private')
        else:
            self.change_connect_button_color('#000', '#fff', '#fff', '#3bb300')
            self.change_connect_button_text('Start')
            self.ui.label_status_message.setText('DISCONNECTED')
            self.set_sub_status_message('not private')

    def connect_button_clicked(self):
        if self.local_statement == 'off':
            self.connect_to_warp()
        else:
            self.disconnect_to_warp()

    def start(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def set_sub_status_message(self, text):
        self.ui.label_status_sub_message.setText(
            "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">your internet is </span><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">{text}</span></p></body></html>".format(
                text=text))

    def disconnect_to_warp(self):
        """
        Disconnect to warp
        """
        self.change_connect_button_text('Wait...')
        self.ui.pushButton_start_end.setDisabled(True)
        stream = os.popen('warp-cli disconnect')
        output = stream.read()
        stream.close()
        if output == 'Success\n':
            self.statement = self.check_warp_statement()
            if self.statement == 'off':
                self.change_connect_button_color('#000', '#fff', '#fff', '#3bb300')
                self.change_connect_button_text('Start')
                self.ui.label_status_message.setText('DISCONNECTED')
                self.set_sub_status_message('not private')
                self.local_statement = 'off'
            else:
                print('connection failed!')
                self.change_connect_button_text('End')
        else:
            print('error on warp end: {}'.format(output))
            self.change_connect_button_text('End')
        self.ui.pushButton_start_end.setDisabled(False)

    def connect_to_warp(self):
        """
        Connect to warp
        """
        self.change_connect_button_text('Wait...')
        # self.ui.pushButton_start_end.setDisabled(True)
        stream = os.popen('warp-cli connect')
        output = stream.read()
        stream.close()
        time.sleep(2)
        if output == 'Success\n':
            self.statement = self.check_warp_statement()
            if self.statement == 'on':
                self.change_connect_button_color('#fff', '#ff5c33', '#ff5c33', '#fff')
                self.change_connect_button_text('End')
                self.ui.label_status_message.setText('CONNECTED')
                self.set_sub_status_message('private')
                self.local_statement = 'on'
            else:
                print('connection failed!')
                self.change_connect_button_text('Start')
        else:
            print('error on warp start: {}'.format(output))
            self.change_connect_button_text('Start')
        self.ui.pushButton_start_end.setDisabled(False)

    def change_connect_button_text(self, text):
        self.ui.pushButton_start_end.setText(text)

    def change_connect_button_color(self, text_color, bg_color, text_color_hover, bg_color_over):
        my_style = '''
                    QPushButton{
                        background-color: %s;
                        color: %s;
                    }
                    QPushButton:hover{
                        background-color: %s;
                        color: %s;
                    }
                    ''' % (bg_color, text_color, bg_color_over, text_color_hover)
        self.ui.pushButton_start_end.setStyleSheet(self.base_styleSheet + my_style)

    @staticmethod
    def check_warp_statement():
        """
        check status from api
        Return: String => 'on' or 'off'
        """
        try:
            r = requests.get('https://www.cloudflare.com/cdn-cgi/trace/', timeout=4)
            if r.status_code == 200:
                result = r.text.split('\n')[11].split('=')
                if result[0] == 'warp':
                    return result[1]
                else:
                    print('cant find "warp" line in api result')
            else:
                print('error in calling api, status code: {code}'.format(code=r.status_code))
            r.close()
        except Exception as e:
            print('error in calling api, {}'.format(e))


if __name__ == "__main__":
    main_gui = StarterGUI()
    main_gui.start()

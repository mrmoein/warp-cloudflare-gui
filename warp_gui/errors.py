from warp_gui.ui.already_running import *
import sys
import os


def already_running():
    app = QtWidgets.QApplication(sys.argv)
    AlreadyRunning = QtWidgets.QDialog()
    ui = Ui_AlreadyRunning()
    ui.setupUi(AlreadyRunning)
    app.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/../icons/sign-error-icon.png"))
    AlreadyRunning.show()
    sys.exit(app.exec_())

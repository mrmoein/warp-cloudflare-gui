from warp_gui.mainwindow import GUI
import sys
import warp_gui.errors
import socket

try:
    # check program already running or not
    s = socket.socket()
    s.bind(('', 45367))
except:
    warp_gui.errors.already_running()
    sys.exit(-1)

gui = GUI()
if len(sys.argv) == 2 and sys.argv[1] == '--hide':
    # hide mode (only tray icon)
    gui.show(hide=True)
else:
    # normal mode
    gui.show(hide=False)

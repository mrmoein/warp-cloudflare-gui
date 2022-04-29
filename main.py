if __name__ == '__main__':
    from warp_gui.mainwindow import GUI
    import sys

    gui = GUI()
    if len(sys.argv) == 2 and sys.argv[1] == '--hide':
        gui.show(hide=True)
    else:
        gui.show(hide=False)

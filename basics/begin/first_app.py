import sys
from PySide6.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # `QApplication` instance is UNIQUE in per application
    # pass in `sys.argv` to allow command line arguments for the application
    # if no command line arguments are passed, try `QApplication([])`
    app = QApplication(sys.argv)

    # create a Qt widget, which will be the main window
    window = QWidget()
    window.show()

    # start the event loop
    # the application won't reach here until exit and the event loop has stopped
    app.exec()

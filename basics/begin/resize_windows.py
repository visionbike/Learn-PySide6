import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# subclass  `QMainWindow` to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set title for the main window
        self.setWindowTitle('My Application')
        # create `QPushButton` widget
        button = QPushButton('Press Me!')
        # size windows and widgets
        # `setFixedSize` to create a fixed size window with the given size
        self.setFixedSize(QSize(400, 300))
        # `setMaximumSize` to create a window with the given maximum size to stretch
        self.setMaximumSize(QSize(600, 500))
        # `setMinimumSize` to create a window with the given minimum size to corrupt
        self.setMinimumSize(QSize(200, 100))
        # set the central widget of the window
        self.setCentralWidget(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # `QMainWindow` is the pre-made widget with provides standard window features for the application,
    # including menus, menus, a statusbar, dockable widgets and more
    window = MainWindow()
    window.show()

    # start the event loop
    app.exec()
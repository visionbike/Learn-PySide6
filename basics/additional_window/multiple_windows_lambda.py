import sys
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout


class AnotherWindow(QWidget):
    """
    This window is a `QWidget`. If it has no parent, it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()

        self.label = QLabel(f'Another window {randint(0, 100)}')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My application')

        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        layout = QVBoxLayout()

        button1 = QPushButton('Push for window 1')
        button1.clicked.connect(lambda checked: self.toggle_window(self.window1))
        layout.addWidget(button1)

        button2 = QPushButton('Push for window 2')
        button2.clicked.connect(lambda checked: self.toggle_window(self.window2))
        layout.addWidget(button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def toggle_window(self, window: QWidget) -> None:
        """
        The function to show `AnotherWindow` widget.

        Parameters
        -------
        window (QWidget): the `AnotherWindow` widget

        Returns
        -------
        """

        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

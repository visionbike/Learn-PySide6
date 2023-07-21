"""
Create new window at start-up then use `show` function to display it
"""

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

        self.w = AnotherWindow()
        self.button = QPushButton('Push for window')
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self) -> None:
        """
        The function to show `AnotherWindow` widget.

        Returns
        -------
        """

        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

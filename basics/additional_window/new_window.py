"""
Create new window on demand
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

        self.w = None   # initialize variable for the external window
        self.button = QPushButton('Push for window')
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self) -> None:
        """
        The function to show `AnotherWindow` widget.

        Returns
        -------
        """

        if self.w is None:
            # re-create new window when clicking the button then showing it
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()  # close the window
            self.w = None   # discard the reference


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

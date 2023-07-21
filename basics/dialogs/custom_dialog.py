import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QLabel, QPushButton, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('HELLO!')

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        # connect the signals to built-in `accept` and `reject` functions
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Something happened, is that OK?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My application')

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.on_clicked_button)
        self.setCentralWidget(button)

    def on_clicked_button(self, state: bool) -> None:
        """
        The slot to return the `clicked` state in `QPushButton`.

        Parameters
        ----------
        state (bool): the `clicked` state.

        Returns
        -------
        """

        print('clicked', state)

        dialog = CustomDialog()
        if dialog.exec():
            print('success!')
        else:
            print('cancel!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
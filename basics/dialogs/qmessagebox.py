import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My application')

        button = QPushButton('Press me for a dialog!')
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

        dialog = QMessageBox()
        dialog.setWindowTitle('I have question!')
        dialog.setText('This is a simple dialog')
        if dialog.exec() == QMessageBox.StandardButton.Ok:
            print('OK!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

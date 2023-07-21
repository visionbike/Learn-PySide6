import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        # `QDoubleSpinBox` supports floats
        spinbox = QDoubleSpinBox()
        spinbox.setMinimum(-10)
        spinbox.setMaximum(3)
        spinbox.setPrefix('$')
        spinbox.setSuffix('c')
        spinbox.setSingleStep(0.5)
        spinbox.lineEdit().setReadOnly(True)    # prevent changing text on the spin box line edit

        spinbox.valueChanged.connect(self.on_value_changed_spinbox)
        spinbox.textChanged.connect(self.on_text_changed_spinbox)

        self.setCentralWidget(spinbox)

    def on_value_changed_spinbox(self, value: int) -> None:
        """
        The slot to change the current value in `QSpinBox`

        Parameters
        ----------
        value (int): the float value.

        Returns
        -------
        """

        print(value)

    def on_text_changed_spinbox(self, value: str) -> None:
        """
        The slot to change the current value in `QSpinBox`

        Parameters
        ----------
        value (str): the string integer value.

        Returns
        -------
        """

        print(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

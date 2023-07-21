import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        dial = QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)

        dial.valueChanged.connect(self.on_value_changed_dial)
        dial.sliderMoved.connect(self.on_moved_dial)
        dial.sliderPressed.connect(self.on_pressed_dial)
        dial.sliderReleased.connect(self.on_released_dial)

        self.setCentralWidget(dial)

    def on_value_changed_dial(self, value: int) -> None:
        """
        The slot to return changed value in `QDial`.

        Parameters
        ----------
        value (int): the changed value.

        Returns
        -------
        """

        print(value)

    def on_moved_dial(self, pos: int) -> None:
        """
        The slot to return the moving position in `QDial`.

        Parameters
        ----------
        pos (int): the moved position value.

        Returns
        -------
        """

        print(f'position: {pos}')

    def on_pressed_dial(self) -> None:
        """
        The slot to return the `pressed` state in `QDial`.

        Returns
        -------
        """

        print('pressed!')

    def on_released_dial(self) -> None:
        """
        The slot to return the `released` state in `QDial`.

        Returns
        -------
        """

        print('released!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

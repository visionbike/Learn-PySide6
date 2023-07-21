import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        slider = QSlider()
        slider.setMinimum(-10)
        slider.setMaximum(3)
        # or .setRange(-10, 3)
        # slider.setRange(-10, 3)
        slider.setSingleStep(3)

        slider.valueChanged.connect(self.on_value_changed_slider)
        slider.sliderMoved.connect(self.on_moved_slider)
        slider.sliderPressed.connect(self.on_pressed_slider)
        slider.sliderReleased.connect(self.on_released_slider)

        self.setCentralWidget(slider)

    def  on_value_changed_slider(self, value: int) -> None:
        """
        The slot to return changed value in `QSlider`.

        Parameters
        ----------
        value (int): the changed value.

        Returns
        -------
        """

        print(value)

    def on_moved_slider(self, pos: int) -> None:
        """
        The slot to return the moving position in `QSlider`.

        Parameters
        ----------
        pos (int): the moved position value.

        Returns
        -------
        """

        print(f'position: {pos}')

    def on_pressed_slider(self) -> None:
        """
        The slot to return the `pressed` state in `QSlider`.

        Returns
        -------
        """

        print('pressed!')

    def on_released_slider(self) -> None:
        """
        The slot to return the `released` state in `QSlider`.

        Returns
        -------
        """

        print('released!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

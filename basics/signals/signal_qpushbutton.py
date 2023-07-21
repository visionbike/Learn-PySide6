import sys
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Application')
        # variable to store the `toggled` state for the button
        self.is_checked_button = True
        # create `QPushButton` widget
        self.button = QPushButton('Press Me!')
        self.button.setCheckable(True)
        # the `clicked` signal provides some data for events
        self.button.clicked.connect(self.on_clicked_button)
        self.button.clicked.connect(self.on_toggled_button)
        self.button.setChecked(self.is_checked_button)
        # the `released` signal provides some data for events
        self.button.released.connect(self.on_released_button)
        #
        self.windowTitleChanged.connect(self.on_changed_window_title)

        self.setCentralWidget(self.button)

    def on_clicked_button(self) -> None:
        """
        The simple custom slot which accepts the `clicked` signal from the `QPushButton`

        Returns
        -------
        """

        print('clicked!')

        window_title_new = choice(window_titles)
        print(f'setting title: {window_title_new}')
        self.setWindowTitle(window_title_new)

    def on_toggled_button(self, checked: bool) -> None:
        """
        The slot which make the  button checkable and see the effect

        Parameters
        ----------
        checked (bool): the `toggled` state for the button.

        Returns
        -------
        """

        self.is_checked_button = checked
        print('check?', self.is_checked_button)

    def on_released_button(self):
        self.is_checked_button = self.button.isChecked()
        print(self.is_checked_button)

    def on_changed_window_title(self, window_title: str) -> None:
        """
        The slot to change the window title.

        Parameters
        ----------
        window_title (str): the input window title.

        Returns
        -------
        """
        print(f'window title changed: {window_title}')
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

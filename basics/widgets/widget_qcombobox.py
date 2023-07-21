import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        combo_box = QComboBox()
        combo_box.addItems(['One', 'Two', 'Three'])
        # the default signal from `currentIndexChanged` sends the index
        combo_box.currentIndexChanged.connect(self.on_index_changed_combo_box)
        # the default signal from `currentTextChanged` sends a text string
        combo_box.currentTextChanged.connect(self.on_text_changed_combo_box)

        self.setCentralWidget(combo_box)

    def on_index_changed_combo_box(self, index: int) -> None:
        """

        Parameters
        ----------
        index (int): the index of items in `QComboBox`, starting from 0.

        Returns
        -------
        """

        print(index)

    def on_text_changed_combo_box(self, text: str) -> None:
        """

        Parameters
        ----------
        text (str): the input text string to change.

        Returns
        -------
        """

        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        list_widget = QListWidget()
        list_widget.addItems(['one', 'two', 'three'])

        # in `QListWidget` there are separate signals for the item, and the string
        list_widget.currentItemChanged.connect(self.on_index_changed_list_widget)
        list_widget.currentTextChanged.connect(self.on_text_changed_list_widget)

        self.setCentralWidget(list_widget)

    def on_index_changed_list_widget(self, index: QListWidgetItem) -> None:
        """
        The slot for changing `QlistWidgetItem` in the `QListWidget`.

        Parameters
        ----------
        index (QListWidgetItem): the new `QListWidgetItem` value.

        Returns
        -------
        """

        print(index.text())

    def on_text_changed_list_widget(self, text: str) -> None:
        """
        The slot for changing the text in the `QListWidget`
        Parameters
        ----------
        text (syt): the new text value.

        Returns
        -------
        """

        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

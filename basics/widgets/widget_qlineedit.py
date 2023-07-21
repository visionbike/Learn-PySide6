import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(10)
        self.line_edit.setPlaceholderText('enter your text')

        # self.line_edit.setReadOnly(True)    # uncomment this to make read-only
        self.line_edit.returnPressed.connect(self.on_return_pressed_line_edit)
        self.line_edit.selectionChanged.connect(self.on_selection_changed_line_edit)
        self.line_edit.textChanged.connect(self.on_text_changed_line_edit)
        self.line_edit.textEdited.connect(self.on_text_edited_line_edit)
        # the input mask to which characters are supported and where,
        # the below example would allow a series of 3-digit numbers separated with periods as the IPv4 addresses
        # uncomment to see the effect
        # self.line_edit.setInputMask('000.000.000;_')

        self.setCentralWidget(self.line_edit)

    def on_return_pressed_line_edit(self) -> None:
        """
        The slot to return the `return pressed` state in `QLineEdit`.

        Returns
        -------
        """

        print('return pressed!')
        self.line_edit.setText('BOOM!')

    def on_selection_changed_line_edit(self) -> None:
        """
        The slot to return `selection changed` state in `QLineEdit`.

        Returns
        -------
        """

        print('Selection changed')
        print(self.line_edit.selectedText())

    def on_text_changed_line_edit(self, text: str) -> None:
        """
        The slot to the changed text in `QLineEdit`.

        Parameters
        ----------
        text (str): the new text value.

        Returns
        -------
        """

        print('text changed')
        print(text)

    def on_text_edited_line_edit(self, text: str) -> None:
        """
        The slot to the edited text in `QLineEdit`.

        Parameters
        ----------
        text (str): the edited text value.

        Returns
        -------
        """

        print('text edited')
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

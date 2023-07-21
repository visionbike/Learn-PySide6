import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        checkbox = QCheckBox('This is a checkbox')
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.on_checked_state_show)

        self.setCentralWidget(checkbox)

    def on_checked_state_show(self, state: bool) -> None:
        """

        Parameters
        ----------
        state (bool): the `checked` state.

        Returns
        -------
        """

        # Checked States:
        # 0: unchecked
        # 1: partially checked (referred as `tri-state`, which means the widget is either or nor off, the checkbox is commonly shown as greyed-out checkout)
        # 2: checked
        print(f'checked? {state == Qt.CheckState.Checked.value}')
        print(f'state: {state}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



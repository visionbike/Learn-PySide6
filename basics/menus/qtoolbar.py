import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        # set icon size for toolbar butiton
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # add 1st button for toolbar
        button_action = QAction(QIcon('./icons/bug.png'), '&Your button', self)
        button_action.setStatusTip('This is your button')
        # the signal always False since signal passed indicates whether the button is checked
        # the button is not checkable - just checkable - it is always false
        button_action.triggered.connect(self.on_triggered_toolbar_button)
        # make the click to see the toolbar button toggle from `checked` to `unchecked` state.
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        # add 2nd button for toolbar
        button_action2 = QAction(QIcon('./icons/bug.png'), '&Your button2', self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.on_triggered_toolbar_button)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # add 3rd checkbox for toolbar
        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        # add status bar
        # hover mouse over the toolbar button and see the status text in the status bar
        self.setStatusBar(QStatusBar(self))

    def on_triggered_toolbar_button(self, state: bool) -> None:
        """
        The slot to return `triggered` state in `QAction`

        Parameters
        ----------
        state (bool): the `triggered` state.

        Returns
        -------
        """

        print(f'triggered: {state}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QCheckBox, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('./icons/bug.png'), '&Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.on_triggered_toolbar_button)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('./icons/bug.png'), 'Your &button2', self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.on_triggered_toolbar_button)
        button_action2.setCheckable(True)
        # add keyboard shortcut using key name, e.g., Ctrl + p
        button_action2.setShortcut(QKeySequence('Ctrl+p'))
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())
        self.setStatusBar(QStatusBar(self))

        # add menu bar
        menu = self.menuBar()
        # add file menu
        menu_file = menu.addMenu('&File')
        menu_file.addAction(button_action)
        menu_file.addSeparator()
        menu_file.addAction(button_action2)
        # add submenu
        submenu_file = menu_file.addMenu('Submenu')
        submenu_file.addAction(button_action)
        submenu_file.addSeparator()
        submenu_file.addAction(button_action2)


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

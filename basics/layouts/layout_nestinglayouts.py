import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout


class Color(QWidget):
    """
    Color custom widget
    """
    def __init__(self, color: str):
        """

        Parameters
        ----------
        color (str): the color name.
        """
        super().__init__()

        # make the widget to automatically fill its background with window cooler
        self.setAutoFillBackground(True)

        palette = self.palette()
        # change the current `QPalette.ColorRole.Window` - background color
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        # set the spacing around the layouts
        layout1.setContentsMargins(0, 0, 0, 0)
        # set the spacing between elements
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

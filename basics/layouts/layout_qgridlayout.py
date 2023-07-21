import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


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

        layout = QGridLayout()
        # set color, row, column, alignment
        layout.addWidget(Color('red'), 0, 3)
        layout.addWidget(Color('green'), 1, 1)
        layout.addWidget(Color('blue'), 2, 2)
        layout.addWidget(Color('purple'), 3, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

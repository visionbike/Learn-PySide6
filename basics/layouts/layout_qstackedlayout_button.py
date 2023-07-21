import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QPushButton,
)


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

        layout_page = QVBoxLayout()
        layout_button = QHBoxLayout()
        self.layout_stacked = QStackedLayout()

        layout_page.addLayout(layout_button)
        layout_page.addLayout(self.layout_stacked)

        button = QPushButton('red')
        button.pressed.connect(self.on_activate_button_1)
        layout_button.addWidget(button)
        self.layout_stacked.addWidget(Color('red'))

        button = QPushButton('green')
        button.pressed.connect(self.on_activate_button_2)
        layout_button.addWidget(button)
        self.layout_stacked.addWidget(Color('green'))

        button = QPushButton('blue')
        button.pressed.connect(self.on_activate_button_3)
        layout_button.addWidget(button)
        self.layout_stacked.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout_page)
        self.setCentralWidget(widget)

    def on_activate_button_1(self):
        self.layout_stacked.setCurrentIndex(0)

    def on_activate_button_2(self):
        self.layout_stacked.setCurrentIndex(1)

    def on_activate_button_3(self):
        self.layout_stacked.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

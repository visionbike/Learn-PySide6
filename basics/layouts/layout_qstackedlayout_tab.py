import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
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

        tabs = QTabWidget()
        # set tab position
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        # set to make tabs be movable
        tabs.setMovable(True)

        for i, color in enumerate(['red', 'green', 'blue', 'yellow']):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

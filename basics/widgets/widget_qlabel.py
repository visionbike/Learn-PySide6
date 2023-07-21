import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        self.setFixedSize(QSize(400, 300))

        label = QLabel('Hello')
        # get the current font, change its properties and then apply it back,
        # ensuring the font face remains in keeping with the desktop conventions
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        # use `|` to combine the alignment flags together
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # attach the image to `QLabel` - uncomment to see effect
        label.setPixmap(QPixmap('./images/sample.jpg'))
        # scale the image content to fit the window completely
        label.setScaledContents(True)

        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

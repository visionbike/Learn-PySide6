import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        self.label = QLabel()

        self.input = QLineEdit()
        # connect `textCHanged` signal to the `setText` slot on `QLabel`
        # any text changes in the `QLineEdit` the `QLabel` will receive the text to `QLabel`'s `setText` method
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

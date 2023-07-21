import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel('Start')
        btn_danger = QPushButton('DANGER!')
        btn_danger.pressed.connect(self.oh_no)

        btn_question = QPushButton('?')
        btn_question.pressed.connect(self.change_message)

        layout.addWidget(self.label)
        layout.addWidget(btn_danger)
        layout.addWidget(btn_question)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def change_message(self):
        self.message = 'OH NO'


    def oh_no(self):
        self.message = 'pressed'

        for n in range(100):
            time.sleep(0.1)
            self.label.setText(self.message)
            QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

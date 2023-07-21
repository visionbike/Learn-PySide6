import sys
import time
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0

        layout = QVBoxLayout()
        self.label = QLabel('Start')
        btn = QPushButton('DANGER!')
        btn.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(1000)    # 1000ms
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        print('Thread start')
        time.sleep(10)
        print('Thread complete')

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

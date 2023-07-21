import sys
import time
from PySide6.QtCore import QRunnable, QThreadPool, Slot, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel


class Worker(QRunnable):
    """
    The custom `QRunnable` class to define worker thread
    """

    def __init__(self, fn=None, *args, **kwargs):
        """

        Parameters
        ----------
        fn (Callable): the function
        args: arguments to make available for the run code
        kwargs: keyword arguments to make available for the run code
        """

        super().__init__()

        # store the constructor argument
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self) -> None:
        """
        The example method for long-running job
        Returns
        -------
        """

        print('Thread start')
        time.sleep(10)
        # may pass the runner function with passed args, kwargs
        # self.fn(*self.args, **self.kwargs)
        print('Thread complete')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setup thread pool
        self.threadpool = QThreadPool()
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()} threads')

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
        self.timer.setInterval(1000)  # 1000ms
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker()
        # pass the function to execute
        # worker = Worker(self.execute_this_fn)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

import sys
import time
import traceback
from PySide6.QtCore import QObject, Signal, QRunnable, Slot, QThreadPool, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout


class WorkerSignals(QObject):
    """
    Define the signals available from a running worker thread.

    Supported signals includes:
    - finished: no data
    - error: tuple (exctype, value, traceback.format_exc())
    - result: object data returned from the processing, anything
    - progress: int indicates % progress
    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Worker thread which inherits form `QRunnable` to handle worker thread setup, signal and wrap-up.
    """

    def __init__(self, fn, *args, **kwargs):
        super().__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # add the callback to the kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self) -> None:
        # retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))   # return error
        else:
            self.signals.result.emit(result)                                    # return result of the processing
        finally:
            self.signals.finished.emit()                                        # done


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel('Start')
        btn_danger = QPushButton('DANGER!')
        btn_danger.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(btn_danger)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.threadpool = QThreadPool()
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()} threads')

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n) -> None:
        print(f'{n}% done')

    def execute_this_fn(self, progress_callback) -> str:
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(int(n * 100 / 4))
        return 'Done'

    def print_output(self, s) -> None:
        print(s)

    def thread_complete(self) -> None:
        print('THREAD COMPLETE!')

    def oh_no(self) -> None:
        # pass the function to execute
        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        # execute
        self.threadpool.start(worker)

    def recurring_timer(self) -> None:
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

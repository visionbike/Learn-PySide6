import sys
import re
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QPlainTextEdit, QProgressBar, QVBoxLayout


progress_re = re.compile(f'Total complete: (\d+)%')


def simple_percent_parser(output: str):
    """
    Matches lines using the process_re regex, returning the single integer for the % progress.

    Parameters
    ----------
    output

    Returns
    -------
    """

    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('Execute')
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        # create progress bar
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.progress)
        layout.addWidget(self.text)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        """
        Use `QProcess` to execute external application

        Returns
        -------
        """

        self.message('Executing process.')
        self.p = QProcess()                             # keep a reference to the `QProcess` while it's running
        # following two signals are used to notify when data is available in the respective stream
        # getting data from `QProcess`
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.process_finished)  # clean up once complete
        self.p.start('python', ['./dummy_script.py'])

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode('utf8')
        self.message(stdout)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode('utf8')
        # extract progress if it is in the data
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)

    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: 'Not running',
            QProcess.ProcessState.Starting: 'Starting',
            QProcess.ProcessState.Running: 'Running'
        }
        state_name = states[state]
        self.message(f'State changed: {state_name}')

    def process_finished(self):
        self.message('Process finished.')
        self.p = None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

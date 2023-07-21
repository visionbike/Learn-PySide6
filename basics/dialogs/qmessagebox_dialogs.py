import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My application')

        layout = QHBoxLayout()

        button_about = QPushButton('about')
        button_about.clicked.connect(self.on_clicked_button_about)

        button_question = QPushButton('question')
        button_question.clicked.connect(self.on_clicked_button_question)

        button_info = QPushButton('information')
        button_info.clicked.connect(self.on_clicked_button_info)

        button_warn = QPushButton('warning')
        button_warn.clicked.connect(self.on_clicked_button_warn)

        button_critical = QPushButton('critical')
        button_critical.clicked.connect(self.on_clicked_button_critical)

        layout.addWidget(button_about)
        layout.addWidget(button_question)
        layout.addWidget(button_info)
        layout.addWidget(button_critical)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def on_clicked_button_about(self, state: bool) -> None:
        print('clicked', state)

        dialog = QMessageBox.about(self, 'About dialog', 'About message')

    def on_clicked_button_question(self, state: bool) -> None:
        print('clicked', state)

        dialog = QMessageBox.question(self, 'Question dialog', 'Question message', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if dialog == QMessageBox.StandardButton.Yes:
            print('YES!')
        else:
            print('NO!')

    def on_clicked_button_info(self, state: bool) -> None:
        print('clicked', state)

        dialog = QMessageBox.information(self, 'Information dialog', 'Information message', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if dialog == QMessageBox.StandardButton.Yes:
            print('YES!')
        else:
            print('NO!')

    def on_clicked_button_warn(self, state: bool) -> None:
        print('clicked', state)

        dialog = QMessageBox.warning(self, 'Warning dialog', 'Warning message', QMessageBox.StandardButton.Ok)
        if dialog == QMessageBox.StandardButton.Ok:
            print('OK!')

    def on_clicked_button_critical(self, state: bool) -> None:
        print('clicked', state)

        dialog = QMessageBox.critical(self,
                                      'Critical dialog',
                                      'Critical message',
                                      QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
                                      QMessageBox.StandardButton.Discard)
        if dialog == QMessageBox.StandardButton.Discard:
            print('DISCARD!')
        elif dialog == QMessageBox.StandardButton.NoToAll:
            print('NO TO ALL!')
        else:
            print('IGNORED!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

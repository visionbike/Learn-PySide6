import sys
from PySide6.QtGui import QAction, QContextMenuEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        """
        Context menu is the context-sensitive menu which typically appears when right-clicking on a window
        Parameters
        ----------
        event (QContextMenuEvent): context menu event

        Returns
        -------
        """

        context = QMenu(self)
        context.addAction(QAction('test 1', self))
        context.addAction(QAction('test 2', self))
        context.addAction(QAction('test 3', self))
        context.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


import sys
from PySide6.QtCore import Qt, QPoint, QPointF
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.show()

    self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
    self.customContextMenuRequested.connect(self.on_context_menu)

  def on_context_menu(self, pos: QPoint | QPointF) -> None:
    """
    The slot for setting up the context menu at any position in the window

    Parameters
    ----------
    pos (QPoint | QpointF): the position in the window

    Returns
    -------
    """
    context = QMenu(self)
    context.addAction(QAction('test 1', self))
    context.addAction(QAction('test 2', self))
    context.addAction(QAction('test 3', self))
    context.exec(self.mapToGlobal(pos))


if __name__ == '__main__':
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  app.exec()

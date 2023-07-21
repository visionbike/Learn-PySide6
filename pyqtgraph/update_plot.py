import sys
from random import randint
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from pyqtgraph.widgets.PlotWidget import PlotWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget_graph = PlotWidget()
        self.setCentralWidget(self.widget_graph)

        self.x = list(range(100))
        self.y = [randint(0, 100) for _ in range(100)]

        plot_item = pg.PlotItem()
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.data_line = plot_item.plot(self.x, self.y, pen=pen)
        self.widget_graph.setBackground('white')
        self.widget_graph.setCentralWidget(plot_item)

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]             # remove the first element
        self.x.append(self.x[-1] + 1)   # add new value 1 higher value than the last

        self.y = self.y[1:]             # remove the first element
        self.y.append(randint(0, 100))  # add new random value

        self.data_line.setData(self.x, self.y)  # update the data


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

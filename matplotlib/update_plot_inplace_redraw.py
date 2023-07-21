import sys
from random import randint
import matplotlib
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width: int = 5, height: int = 4, dpi: int = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_axes(111)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        num_data = 50
        self.x = list(range(num_data))
        self.y = [randint(0, 10) for _ in range(num_data)]

        # store a reference to the plotted line somewhere,
        # so we can apply the new data to it.
        self.plot_ref = None
        self.update_plot()

        self.show()

        # setup a timer to trigger the redraw by calling `update_plot`
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self) -> None:
        # drop off the first element, append a new once
        self.y = self.y[1:] + [randint(0, 10)]
        # not that we no longer need to clear the axis
        if self.plot_ref is None:
            # plot data if `self.plot_ref` is None
            plot_refs = self.canvas.axes.plot(self.x, self.y, 'red')
            self.plot_ref = plot_refs[0]
        else:
            # just update data if we have a reference
            self.plot_ref.set_ydata(self.y)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    app.exec()

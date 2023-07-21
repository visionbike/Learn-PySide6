import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from pyqtgraph.widgets.PlotWidget import PlotWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget_graph = PlotWidget()
        self.setCentralWidget(self.widget_graph)

        hour = [i for i in range(1, 11)]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        #
        self.plot_item = pg.PlotItem()
        # set title for plot
        self.plot_item.setTitle('Your Title Here', color='black', size='20pt')
        # set style for axis labels
        styles_label = {'color': '#f00', 'font-size': '20px'}
        self.plot_item.setLabel('left', 'Temperature (°C)', **styles_label)
        self.plot_item.setLabel('bottom', 'Hour (H)', **styles_label)
        # add legend
        self.plot_item.addLegend((5, 0))
        # show grid
        self.plot_item.showGrid(x=True, y=True)
        # set axis range
        self.plot_item.setXRange(0, 11, padding=0)
        self.plot_item.setYRange(20, 55, padding=0)
        # plot data
        self.plot(hour, temperature_1, 'sensor 1', 'red')
        self.plot(hour, temperature_2, 'sensor 2', 'blue')

        # set background for widget
        self.widget_graph.setBackground('white')
        # add to `PlotWidget`
        self.widget_graph.setCentralWidget(self.plot_item)

    def plot(self, x, y, plot_name, color):
        pen = pg.mkPen(color=color)
        self.plot_item.plot(x, y, name=plot_name, pen=pen, symbol='+', symbolSize=20, symbolBrush=color)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

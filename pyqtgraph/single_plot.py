import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from pyqtgraph.widgets.PlotWidget import PlotWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget_graph = PlotWidget()
        self.setCentralWidget(self.widget_graph)

        hour = [i for i in range(1, 11)]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # create `PlotItem` instance
        plot_item = pg.PlotItem()
        # set title for plot, it could be HTML tag syntax
        plot_item.setTitle('Your title here', color='black', size='20pt')
        # set style for axis labels, also support HTML tag syntax
        styles_label = {'color': 'red', 'font-size': '20px'}
        plot_item.setLabel('left', 'Temperature (°C)', **styles_label)
        plot_item.setLabel('bottom', 'Hour (H)', **styles_label)
        # style the line drawing
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=Qt.PenStyle.DashLine)
        # add legend
        plot_item.addLegend(offset=(30, 30))
        # show grid
        plot_item.showGrid(x=True, y=True)
        # plot data: x, y values
        plot_item.plot(hour, temperature, name='sensor1', pen=pen, symbol='+', symbolSize=20, symbolBrush='blue')
        # set axis limits
        plot_item.setXRange(0, 11, padding=0)
        plot_item.setYRange(20, 55, padding=0)

        # set background color: can be string, RGB value, or hex notation, `QColor`, `QPalette`
        self.widget_graph.setBackground('white')
        # add plot_item into `PlotWidget`
        self.widget_graph.setCentralWidget(plot_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

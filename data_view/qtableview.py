import sys
from datetime import datetime
from typing import Any
from PySide6.QtCore import (
    Qt,
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex
)
from PySide6.QtGui import (
    QColor,
    QIcon
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView
)


COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']


class TableModel(QAbstractTableModel):
    def __init__(self, data: list):
        super().__init__()
        self._data = data

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            # get the raw value
            value = self._data[index.row()][index.column()]

            # perform per-type checks and render accordingly
            if isinstance(value, datetime):
                # render time to YYYY-MM-DD
                return value.strftime('%Y-%m-%d')

            if isinstance(value, float):
                # render float to 2dp
                return f'{value:.2f}'

            if isinstance(value, str):
                # render strings with quotes
                return f'{value}'
            return value

        if role == Qt.ItemDataRole.DecorationRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, datetime):
                return QIcon('./icons/calendar.png')
            if isinstance(value, bool):
                if value:
                    return QIcon('./icons/tick.png')
                return QIcon('./icons/cross.png')
            # color blocks
            if role == Qt.ItemDataRole.DecorationRole:
                value = self._data[index.row()][index.row()]
                if isinstance(value, int) or isinstance(value, float):
                    value = int(value)
                    # limit to range (-5, ..., +5) then convert to 0, ..., 10
                    value = max(-5, value)  # value < -5 become -5
                    value = min(5, value)   # value > +5 become +5
                    value += 5
                    return QColor(COLORS[value])

        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 2:
                return QColor('blue')

        if role == Qt.ItemDataRole.ForegroundRole:
            if index.column() == 2:
                return QColor('white')

        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

    def rowCount(self, index: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._data)

    def columnCount(self, index: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tableview_data = QTableView()

        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, True, 9],
            [4, 9, False],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.tableview_data.setModel(self.model)

        self.setCentralWidget(self.tableview_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

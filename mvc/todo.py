import sys
from pathlib import Path
from typing import Any
import json
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow_todo import UiMainWindow


tick = QImage('./icons/tick.png')


class TodoModel(QAbstractListModel):
    """
    The custom model to display the result to a `QListView`
    """
    def __init__(self, todos: None | list = None):
        super().__init__()
        # variable to store data
        self.todos = todos or []

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        """
        Core method which handles requests for data from the view and returns appropriate result.
        Parameters
        ----------
        index (QModelIndex, QPersistentModelIndex): the position of data which the view is requesting, accessible by two methods `row` and `column`
        role (int): the flag indicating the type of data that the view is requesting

        Returns
        -------

        """

        # `DisplayRole` (0) indicates that the view is asking to give data for display
        if role == Qt.ItemDataRole.DisplayRole:

            status, text = self.todos[index.row()]
            return text

        # `DecorationRole` (1) indicates that the data to be rendered as a decoration in the form of an icon
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index: QModelIndex | QPersistentModelIndex = ...) -> int:
        """
        Get tje number of rows in the current data

        Parameters
        ----------
        index (QModelIndex, QPersistentModelIndex): the position of data which the view is requesting,

        Returns
        -------
        """

        return len(self.todos)


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = TodoModel(todos=[(False, 'my first todo')])

        # load JSON data
        Path('./data').mkdir(parents=True, exist_ok=True)
        self.load_data()

        self.listview_todo.setModel(self.model)

        # connect to the button
        self.btn_add.pressed.connect(self.add)
        self.btn_delete.pressed.connect(self.delete)
        self.btn_complete.pressed.connect(self.complete)

    def add(self) -> None:
        """
        Add an item to our todo list, getting the text from the `QLineEdit` `todoEdit` and then clearing it.

        Returns
        -------
        """

        text = self.lineedit_todo.text()

        # ensure add non-empty string
        if text:
            # access the list via the model
            self.model.todos.append((False, text))
            # trigger refresh due to the shape of data has been changed
            self.model.layoutChanged.emit()
            # empty the input
            self.lineedit_todo.setText('')
            # save modified data
            self.save_data()

    def delete(self) -> None:
        """
        Remove the item from the todo list

        Returns
        -------
        """

        #  indexes is a list of a single item in single-select mode
        indexes = self.listview_todo.selectedIndexes()

        if indexes:
            index = indexes[0]
            # remove the item and refresh
            del self.model.todos[index.row()]
            # trigger refresh due to the shape of data has been changed
            self.model.layoutChanged.emit()
            # clear the selection (as it is no longer valid)
            self.listview_todo.clearSelection()
            # save modified data
            self.save_data()

    def complete(self) -> None:
        """
        Fetch the item from the model `todos` list and then replace the status with `True`.

        Returns
        -------
        """

        indexes = self.listview_todo.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # `dataChanged` takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # clear the selection (as it is no longer valid)
            self.listview_todo.clearSelection()
            # save modified data
            self.save_data()

    def save_data(self) -> None:
        """
        Save data into JSON

        Returns
        -------
        """
        with open('./data/data.json', 'w') as f:
            json.dump(self.model.todos, f)

    def load_data(self) -> None:
        """
        Load saved JSON data.

        Returns
        -------
        """

        try:
            with open('./data/data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QLineEdit,
    QListView,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget
)


class UiMainWindow:
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName('MainWindow')
        main_window.resize(275, 314)

        self.widget_central = QWidget(main_window)
        self.widget_central.setObjectName('CentralWidget')
        self.layout_vertical = QVBoxLayout(self.widget_central)
        self.layout_vertical.setObjectName('verticalLayout')
        self.listview_todo = QListView(self.widget_central)
        self.listview_todo.setObjectName('todoView')
        self.listview_todo.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.layout_vertical.addWidget(self.listview_todo)

        self.widget = QWidget(self.widget_central)
        self.widget.setObjectName('widget')
        self.layout_horizontal = QHBoxLayout(self.widget)
        self.layout_horizontal.setObjectName('horizontalLayout')
        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName('deleteButton')
        self.layout_horizontal.addWidget(self.btn_delete)

        self.btn_complete = QPushButton(self.widget)
        self.btn_complete.setObjectName('completeButton')
        self.layout_horizontal.addWidget(self.btn_complete)

        self.layout_vertical.addWidget(self.widget)

        self.lineedit_todo = QLineEdit(self.widget_central)
        self.lineedit_todo.setObjectName('todoEdit')
        self.layout_vertical.addWidget(self.lineedit_todo)

        self.btn_add = QPushButton(self.widget_central)
        self.btn_add.setObjectName('addButton')
        self.layout_vertical.addWidget(self.btn_add)

        main_window.setCentralWidget(self.widget_central)

        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName('menubar')
        self.menubar.setGeometry(QRect(0, 0, 275, 22))
        main_window.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName('statusbar')
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate('MainWindow', 'Todo', None))
        self.btn_delete.setText(QCoreApplication.translate('MainWindow', 'Delete', None))
        self.btn_complete.setText(QCoreApplication.translate('MainWindow', 'Complete', None))
        self.btn_add.setText(QCoreApplication.translate('MainWindow', 'Add Todo', None))

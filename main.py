import sys
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget
import random
from PyQt5.QtWidgets import QLabel, QPushButton


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffe')
        model.select()
        self.tableView.setModel(model)
        self.tableView.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())

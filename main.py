import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffe — копия.db')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffeee')
        model.select()
        self.tableView.setModel(model)
        self.tableView.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())

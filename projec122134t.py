import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget
import random
from PyQt5.QtWidgets import QLabel, QPushButton
from qwer import Ui_MainWindow


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.qwe.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        n = random.randint(10,400)
        qp.drawEllipse(50, 50, n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())

import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ellipses')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, e):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def circle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        for i in range(10):
            x = random.randint(20, 400)
            y = random.randint(20, 400)
            z = random.randint(20, 100)
            qp.drawEllipse(x, y, z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
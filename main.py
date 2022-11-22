import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.update)
        self.f = 0
        self.x = 0

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_ellipse(qp)
        # Завершаем рисование
        qp.end()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        self.f = randint(1, 200)
        qp.drawEllipse(self.f // 2, self.f + 45, self.f, self.f)
        self.x = randint(100, 300)
        qp.drawEllipse(self.x, self.x // 2 + 2, self.x, self.x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

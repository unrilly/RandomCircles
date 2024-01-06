from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
from PyQt5 import uic


class Circle:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("UI.ui", self)

        self.setWindowTitle("Желтые окружности")

        self.button.clicked.connect(self.generate_circles)

        self.setCentralWidget(self.centralWidget())
        self.circles = []

    def generate_circles(self):
        for i in range(10):
            x = randint(0, 500)
            y = randint(0, 500)
            diameter = randint(10, 100)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.circles.append(Circle(x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.circles:
            painter.setPen(self.circles[0].color)
        for circle in self.circles:
            painter.setPen(circle.color)
            painter.drawEllipse(circle.x, circle.y, circle.diameter, circle.diameter)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
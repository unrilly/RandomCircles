from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import random


class Circle:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.button = QPushButton("Генерировать окружности")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор окружностей")
        self.ui = Ui()
        self.setCentralWidget(self.ui)
        self.circles = []
        self.ui.button.clicked.connect(self.generate_circles)

    def generate_circles(self):
        for i in range(10):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            diameter = random.randint(10, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.circles.append(Circle(x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setPen(circle.color)
            painter.drawEllipse(circle.x, circle.y, circle.diameter, circle.diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
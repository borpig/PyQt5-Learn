from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1400, 800, 1000, 1000)
        self.setWindowTitle("Jian San's first PyQt GUI")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label1")
        self.label.move(100, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me!")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
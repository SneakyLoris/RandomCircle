import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from Design import Ui_Form

x, y = randint(300, 800), randint(300, 1000)


class Program(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 500, 500)
        self.entercode = 0
        self.x = 0
        self.y = 0
        self.pushButton.clicked.connect(self.pushbtn)

    def paintEvent(self, event):
        pass

    def pushbtn(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec())

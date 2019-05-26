import sys
import time
import PyQt5.QtWidgets
from PyQt5.QtCore import pyqtSlot

n = 0

class  MP(PyQt5.QtWidgets.QWidget) :

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(300,200)
        self.setWindowTitle('название')

        self.hegb = PyQt5.QtWidgets.QPushButton("Причесать ежа", self)
        self.hegb.move(50,25)
        self.hegb.clicked.connect(self.hedgehog)

        self.infb = PyQt5.QtWidgets.QPushButton("Кликер", self)
        self.infb.move(50,75)
        self.infb.clicked.connect(self.click)

        self.divb = PyQt5.QtWidgets.QPushButton("Поделить на ноль", self)
        self.divb.move(50,125)
        self.divb.clicked.connect(self.division)

        self.disp = PyQt5.QtWidgets.QLCDNumber(self)
        self.disp.move(200, 50)


    @pyqtSlot()
    def hedgehog(self):
        print("А вы знали,что невозможно причесать свернувшегося клубком ежа так, чтобы у него не торчала ни одна иголка?"
        "Читайте тут https://en.wikipedia.org/wiki/Hairy_ball_theorem ")

    @pyqtSlot()
    def click(self):
        global n
        n += 1

        self.disp.display(n)

    @pyqtSlot()
    def division(self):
        time.sleep(13)
        raise ZeroDivisionError




if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    a = MP()
    a.show()
    sys.exit(app.exec_())





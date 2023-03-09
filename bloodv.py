import random, sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

if os.path.exists("config.ini") == False:
    f=open("config.ini", "w")
    f.write("[RGB]\n")
    f.write("[R]\n")
    f.write("255\n")
    f.write("[G]\n")
    f.write("0\n")
    f.write("[B]\n")
    f.write("0\n")
    f.write("\n[Other]\n")
    f.write("[Crosshair Type]\n")
    f.write("1\n")
    f.close()

# Config
f=open("config.ini", "r")
n = f.readline()
n = f.readline()
R = f.readline()
n = f.readline()
G = f.readline()
n = f.readline()
B = f.readline()
n = f.readline()
n = f.readline()
n = f.readline()
ctype = f.readline()

R = int(R)
G = int(G)
B = int(B)
ctype = int(ctype)

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor(R, G, B))
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))

    def paintEvent(self, event):
        if ctype == 1:
            d = 10
        elif ctype == 2:
            d = 4
        else:
            d = 10
        ws = self.ws
        res = int(ws/2)
        red = int(ws/d)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(res, 0, res, res - red)
        painter.drawLine(res, res + red+1, res, ws)
        painter.drawLine(0, res, res - red, res)
        painter.drawLine(res + red, res, int(ws - 0.5), res)

app = QtWidgets.QApplication(sys.argv)
widget = Crosshair(windowSize=16, penWidth=2)
widget.show()
sys.exit(app.exec_())
#input("")
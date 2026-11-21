import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

from PyQt5.QtWebEngineWidgets import *

class MainWinow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName("Sand Browser")
window = MainWindow()
app.exec_()

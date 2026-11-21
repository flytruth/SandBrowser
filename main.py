from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import * 

class SandBrowser(QMainWindow):

    def __init__ (self, *args, **kwargs):
        super(SandBrowser, self).__init__(*args, **kwargs)

         self.window = QWidget()
         self.window.setWindowTitle("Sand Browser")

         self.layout = QVBoxLayout()
         self.horizontal = QHBoxLayout()

         self.url_bar = QTextEdit()
         self.url_bar.setMaximumHeight(30)

         self.go_btn = QPushButton("Go")
         self.go_btn.setMaximumHeight(30)

         self.back_btn = QPushButton("<")
         self.back_btn.setMinimumHeight(30)

         self.forward_btn = QPushButton(">")
         self.forward_btn.setMinimumHeight(30)

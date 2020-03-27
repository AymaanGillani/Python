import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow,QWidget

class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(50,50,300,300)
        self.setWindowTitle("Test")
        self.setWindowIcon(QIcon("pic.png"))
        self.home()

    def home(self):
        button=QPushButton("Quit",self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(100,100)
        button.move(50,50)
        self.show() 

def run():
    app=QApplication(sys.argv)
    Gui=window()
    sys.exit(app.exec_())

run()
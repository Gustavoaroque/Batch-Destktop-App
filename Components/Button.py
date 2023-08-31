
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self,text,width,height,color):
        super().__init__(text)
        self.width = width
        self.height = height
        self.color = color
        styles = "background-color:#"+ str(self.color)+ ";color:#FFF;"
        self.setFixedSize(self.width,self.height)
        self.setStyleSheet(styles)
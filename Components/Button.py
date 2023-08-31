
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from .Font import MyFonts

class Button(QPushButton):
    def __init__(self,text,width,height,color,font_name,point_size):
        super().__init__(text)
        self.width = width
        self.height = height
        self.color = color

        styles = "background-color:#"+ str(self.color)+ ";color:#FFF;"
        self.setFixedSize(self.width,self.height)

        font = MyFonts(point_size,font_name)
        self.setFont(font.get_Font())           

        self.setStyleSheet(styles)
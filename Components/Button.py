
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from .Font import MyFonts

class Button(QPushButton):
    def __init__(self,text,width,height,color,font_name,point_size):
        super().__init__(text)
        self.width = width
        self.height = height
        self.color = color
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        styles = '''
                QPushButton{
                background-color:#31317B;
                border-radius:20px;
                color:#FFF;
                }
                QPushButton:hover {
                    background-color:#1F1F59;
                }
                QPushButton:disable {
                    background-color: lightgray;
                }
                QPushButton:enable {
                    background-color: #323297;
                }
                '''

        font = MyFonts(point_size,font_name)
        self.setFont(font.get_Font())           

        self.setStyleSheet(styles)
        


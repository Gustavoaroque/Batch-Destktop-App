
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from .Font import MyFonts

class Button(QPushButton):
    def __init__(self,text,width,height,color,font_name,point_size,click_function):
        super().__init__(text)
        self.width = width
        self.height = height
        self.color = color
        self.click_function = click_function
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        # self.setFixedSize(self.width,self.height)
        styles = "background-color:#"+ str(self.color)+ ";color:#FFF; border-radius:20px"
        styles = '''
                QPushButton{
                background-color:#31317B;
                border-radius:20px;
                color:#FFF;
                }
                QPushButton:hover {
                    background-color:#1F1F59;
                }
                '''

        font = MyFonts(point_size,font_name)
        self.setFont(font.get_Font())           

        self.setStyleSheet(styles)
        self.clicked.connect(self.click_function)


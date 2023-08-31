import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QWidget,QPushButton
)

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QFont, QFontDatabase,QPixmap


class Button(QPushButton):
    def __init__(self,text,width,height,color):
        super().__init__(text)
        self.width = width
        self.height = height
        self.color = color
        styles = "background-color:#"+ str(self.color)+ ";color:#FFF;"
        self.setFixedSize(self.width,self.height)
        self.setStyleSheet(styles)
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QLabel,QLineEdit,QVBoxLayout,QGridLayout,QHBoxLayout,QMainWindow
)

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QFont, QFontDatabase,QPixmap

class MyFonts():
    def __init__(self,size,font_name):
        self.size = size
        self.dir = os.path.dirname(os.path.realpath(__file__)) + "\\Statics\\fonts\\" + font_name + ".ttf"

    def get_Font(self):
        font = QFont()
        font.setPointSize(self.size)
        font_id = QFontDatabase.addApplicationFont(self.dir)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font.setFamily(font_family)
        return font
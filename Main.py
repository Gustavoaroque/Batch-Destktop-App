import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QPushButton,QGroupBox,QLabel,QLineEdit,QVBoxLayout,QGridLayout,QHBoxLayout,QMainWindow
)

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QFont, QFontDatabase,QPixmap

from Components.Button import Button
from Components.Font import MyFonts


class mainApp(QWidget):
    def __init__(self):
        super().__init__()
        btn = Button("Log",240,80,323297)
        text = QLabel("Test")
        font = MyFonts(20,"Montserrat-Medium")
        text.setFont(font.get_Font())
        layout = QVBoxLayout()

        layout.addWidget(btn)
        layout.addWidget(text)


        self.setLayout(layout)

app=QApplication(sys.argv)

window = mainApp()
window.showFullScreen()
app.exec()

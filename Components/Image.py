import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QPushButton,QGroupBox,QLabel,QLineEdit,QVBoxLayout,QGridLayout,QHBoxLayout,QMainWindow
)

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QFont, QFontDatabase,QPixmap


class Image(QLabel):
        def __init__(self):
            super().__init__()
            pixmap = QPixmap("C:\\Users\\Programador_4\\Documents\\Programs\\PyQt\\first_test\\azocar_logo.png")  # Replace with your image path
            resize_image = pixmap.scaledToHeight(150)
            self.setPixmap(resize_image)
            self.setAlignment(Qt.AlignLeft)
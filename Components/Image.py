import os
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QPushButton,QGroupBox,QLabel,QLineEdit,QVBoxLayout,QGridLayout,QHBoxLayout,QMainWindow
)

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap


class Image(QLabel):
        def __init__(self,img_name,height):
            super().__init__()
            self.dir = "C:\\Users\\Programador_4\\Documents\\Programs\\PyQt\\DemoDesign\\dist\\Main\\Components\\img\\" + img_name 
            pixmap = QPixmap(self.dir)  # Replace with your image path
            resize_image = pixmap.scaledToHeight(height)
            self.setPixmap(resize_image)
            self.setAlignment(Qt.AlignLeft)
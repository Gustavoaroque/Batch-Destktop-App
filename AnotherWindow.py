import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel
)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        self.label = QLabel("New Window")
        lay.addWidget(self.label)
        self.setLayout(lay)

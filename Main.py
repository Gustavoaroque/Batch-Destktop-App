import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout
)

from Head import HeadSection
from OptionSection import WeightCap
from SendCommand import SendCommand
from Connection import *


class mainApp(QWidget):
    def __init__(self):
        super().__init__()

        nav = HeadSection(self.close)

        sect1 = WeightCap(Connect,Close)
        command = SendCommand(Connect,Close)

        layout = QVBoxLayout()



        layout.addWidget(nav)
        layout.addWidget(sect1)
        layout.addWidget(command)


        self.setLayout(layout)

app=QApplication(sys.argv)

window = mainApp()
window.showFullScreen()
app.exec()

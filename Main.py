import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QHBoxLayout
)

from Head import HeadSection
from OptionSection import WeightCap
from SendCommand import SendCommand
from Connection import *

from LocalDB import LocadlDbSection


class mainApp(QWidget):
    def __init__(self):
        super().__init__()

        nav = HeadSection(self.close)

        sect1 = WeightCap(Connect,Close)
        command = SendCommand(Connect,Close)
        DBSection = LocadlDbSection()

        FirstRow = QHBoxLayout()
        layout = QVBoxLayout()

        FirstRow.addWidget(sect1)
        FirstRow.addStretch(1)
        FirstRow.addWidget(DBSection)

        layout.addWidget(nav)
        layout.addLayout(FirstRow)
        layout.addWidget(command)

        self.setStyleSheet("background-color:#FFF;")
        self.setLayout(layout)

app=QApplication(sys.argv)

window = mainApp()
window.showFullScreen()
app.exec()

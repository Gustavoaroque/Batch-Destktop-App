import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QHBoxLayout
)
from PyQt5.QtGui import QIcon
from Head import HeadSection
from OptionSection import WeightCap
from SendCommand import SendCommand
from Connection import *
import os
from LocalDB import LocadlDbSection
from Login import Login


class mainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Azocar")
        r = os.path.dirname(os.path.realpath(__file__)) + "\\Components\\Statics\\img\\azocar_logo.png"
        print(r)
        self.setWindowIcon(QIcon(r))
        nav = HeadSection(self.close)

        sect1 = WeightCap()
        command = SendCommand()
        DBSection = LocadlDbSection()

        FirstRow = QHBoxLayout()
        layout = QVBoxLayout()

        FirstRow.addWidget(sect1)
        FirstRow.addStretch(1)
        FirstRow.addWidget(DBSection)

        layout.addWidget(nav)
        layout.addLayout(FirstRow)
        layout.addWidget(command)

        self.setStyleSheet("background-color:#FFF")
        self.setLayout(layout)

app=QApplication(sys.argv)

window = Login()
window.showFullScreen()
app.exec()

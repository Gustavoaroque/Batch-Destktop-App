import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QGridLayout
)

from Head import HeadSection
from OptionSection import OptionSection

class mainApp(QWidget):
    def __init__(self):
        super().__init__()

        nav = HeadSection()
        sect = OptionSection()

        layout = QVBoxLayout()
        layout.addWidget(nav)
        layout.addWidget(sect)


        self.setLayout(layout)

app=QApplication(sys.argv)

window = mainApp()
window.showFullScreen()
app.exec()

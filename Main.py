import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QGridLayout
)

from Head import HeadSection

class mainApp(QWidget):
    def __init__(self):
        super().__init__()

        nav = HeadSection()


        layout = QVBoxLayout()
        layout.addWidget(nav)


        self.setLayout(layout)

app=QApplication(sys.argv)

window = mainApp()
window.showFullScreen()
app.exec()

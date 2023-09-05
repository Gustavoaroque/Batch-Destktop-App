
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
QWidget,QGroupBox,QHBoxLayout,QMainWindow
)

from PyQt5.QtCore import Qt 
from Components.Button import Button
from Components.Image import Image

class HeadSection(QWidget):
    def __init__(self, fn):
        super().__init__()
        HeadSectionLayout = QHBoxLayout()
        HeadSectionGroup = QGroupBox()
        HeadSectionGroup.setFixedHeight(150)
        Layout = QHBoxLayout()
        self.fn = fn

        #The image can be subclassed
        image = Image("azocar_logo.png",150)
        logOut_btn = Button("Log Out",250,80,323297,"Montserrat-SemiBold",20)
        logOut_btn.clicked.connect(self.closeSesion)

        HeadSectionLayout.addWidget(image)
        HeadSectionLayout.addStretch(1)
        HeadSectionLayout.addWidget(logOut_btn, alignment=Qt.AlignCenter| Qt.AlignRight)

        HeadSectionGroup.setLayout(HeadSectionLayout)
        HeadSectionGroup.setStyleSheet("border:none")
        Layout.addWidget(HeadSectionGroup)
        self.setLayout(Layout)

    def closeSesion(self):
        self.fn()

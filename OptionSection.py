
import typing
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout

from Components.Font import MyFonts
from Components.Button import Button

class OptionSection(QWidget):
    def __init__(self):
        super().__init__()
        SectionLayout = QVBoxLayout()
        SectionGroup = QGroupBox()
        BtnLayout = QHBoxLayout()
        SectionGroup.setFixedHeight(300)
        SectionGroup.setFixedWidth(800)

        Layout = QVBoxLayout()

        main_text = QLabel("Estado de Comunicacion")
        font_text = MyFonts(20,"Montserrat-Medium")
        main_text.setFont(font_text.get_Font())

        Start = Button("Iniciar",250,80,323297,"Montserrat-SemiBold",24)
        close = Button("Iniciar",250,80,323297,"Montserrat-SemiBold",24)

        BtnLayout.addStretch(1)
        BtnLayout.addWidget(Start)
        BtnLayout.addStretch(1)
        BtnLayout.addWidget(close)
        BtnLayout.addStretch(1)

        SectionLayout.addStretch(1)
        SectionLayout.addWidget(main_text,alignment=Qt.AlignHCenter |Qt.AlignTop )
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(BtnLayout)
        SectionLayout.addStretch(1)

        SectionGroup.setStyleSheet("QGroupBox { border: 3px solid #04047B; border-radius:20px;}")
        SectionGroup.setLayout(SectionLayout)
        Layout.addWidget(SectionGroup)
        self.setLayout(Layout)



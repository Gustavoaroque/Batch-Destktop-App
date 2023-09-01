
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout,QLineEdit
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from Components.Font import MyFonts
from Components.Button import Button

class LocadlDbSection(QWidget):
    def __init__(self):
        super().__init__()

        TitleTextLayout = QHBoxLayout()
        InputTextLayout = QHBoxLayout()
        ButtonLayout = QHBoxLayout()
        SectionLayout = QVBoxLayout()

        title_font = MyFonts(20,"Montserrat-Medium")
        inputs_font = MyFonts(20,"Montserrat-Regular")
        inputs_t_font = MyFonts(20,"Montserrat-Medium")
        


        Layout = QVBoxLayout()

        DBGroup = QGroupBox()

        DBGroup.setFixedSize(900,450)

        titleText = QLabel("Base de Datos")
        titleText.setFont(title_font.get_Font())

        inputText = QLabel("Nombre de Tabla: ")
        inputText.setFont(inputs_t_font.get_Font())

        inputLine = QLineEdit()
        inputLine.setMaxLength(20)
        inputLine.setFixedHeight(50)
        inputLine.setFixedWidth(300)
        inputLine.setStyleSheet("border: 3px solid #04047B; border-radius:10px;")
        inputLine.setFont(inputs_font.get_Font())
        consult = Button("Ver Registros",290,80,323297,"Montserrat-Medium",20,self.Habilitar)
        
        TitleTextLayout.addWidget(titleText,alignment=Qt.AlignCenter)
        
        InputTextLayout.addStretch(1)
        InputTextLayout.addWidget(inputText)
        InputTextLayout.addWidget(inputLine)
        InputTextLayout.addStretch(1)

        ButtonLayout.addWidget(consult,alignment=Qt.AlignCenter)

        SectionLayout.addStretch(1)
        SectionLayout.addLayout(TitleTextLayout)
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(InputTextLayout)
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(ButtonLayout)
        SectionLayout.addStretch(1)

        DBGroup.setStyleSheet("QGroupBox { border: 4px solid #04047B; border-radius:20px; }")
        DBGroup.setLayout(SectionLayout)

        Layout.addWidget(DBGroup)

        self.setLayout(Layout)



    def Habilitar():
        print("Hola")


        



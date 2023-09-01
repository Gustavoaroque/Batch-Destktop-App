from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout,QLineEdit
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from Components.Font import MyFonts
from Components.Button import Button
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from Components.Image import Image


class Login(QWidget):
    def __init__(self):
        super().__init__()

        Layout = QVBoxLayout()

        VericalLayout = QVBoxLayout()
        Horizontal = QHBoxLayout()

        ButtonLayout = QHBoxLayout()
        TitleLayout = QVBoxLayout()
        FormLayout = QVBoxLayout()

        LoginGroup = QGroupBox()


        TitleFont = MyFonts(30,"Montserrat-SemiBold")
        TitleText = QLabel("Login")
        TitleText.setFont(TitleFont.get_Font())

        LabelsForm = MyFonts(20,"Montserrat-Medium")
        LabelUsername = QLabel("Username")
        LabelPassword = QLabel("Password")
        LabelUsername.setFont(LabelsForm.get_Font())
        LabelPassword.setFont(LabelsForm.get_Font())

        InputUsername = QLineEdit()
        InputPassword = QLineEdit()
        InputPassword.setFixedSize(500,50)
        InputUsername.setFixedSize(500,50)

        Logo = Image("azocar_logo.png",200)

        btn = Button("Iniciar Sesion", 400,60,323297,"Montserrat-SemiBold",20,self.Hello)

        TitleLayout.addWidget(TitleText)

        FormLayout.addWidget(LabelUsername)
        FormLayout.addWidget(InputUsername)

        FormLayout.addWidget(LabelPassword)
        FormLayout.addWidget(InputPassword)

        ButtonLayout.addWidget(btn)

        VericalLayout.addLayout(TitleLayout)
        VericalLayout.addLayout(FormLayout)
        VericalLayout.addLayout(ButtonLayout)

        Horizontal.addWidget(Logo)
        Horizontal.addLayout(VericalLayout)

        LoginGroup.setFixedSize(1600,600)
        LoginGroup.setLayout(Horizontal)
        # FormLayout.addWidget(LabelUsername)
        Layout.addWidget(LoginGroup)

    def Hello():
        print("Hello")


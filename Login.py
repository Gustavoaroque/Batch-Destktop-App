from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout,QLineEdit
from Components.Font import MyFonts
from Components.Button import Button
from Components.Image import Image
from Connection import check_user
from Main import mainApp
from PyQt5.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QHBoxLayout
)
# from AnotherWindow import DBTabel
import sys


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

        self.errorText = QLabel("")
        TitleFont = MyFonts(30,"Montserrat-SemiBold")
        InputFont = MyFonts(15,"Montserrat-Regular")
        ErrorFont = MyFonts(12,"Montserrat-Regular")

        self.errorText.setFont(ErrorFont.get_Font())
        self.errorText.setStyleSheet("color:#CD0606")


        TitleText = QLabel("Login")
        TitleText.setFont(TitleFont.get_Font())

        LabelsForm = MyFonts(20,"Montserrat-Medium")
        LabelUsername = QLabel("Username")
        LabelPassword = QLabel("Password")
        LabelUsername.setFont(LabelsForm.get_Font())
        LabelPassword.setFont(LabelsForm.get_Font())

        self.InputUsername = QLineEdit()
        self.InputPassword = QLineEdit()

        self.InputUsername.setStyleSheet("border-radius:15px;border:2px solid #04047B; background-color:none;padding-left:10px;")
        self.InputPassword.setStyleSheet("border-radius:15px;border:2px solid #04047B; background-color:none;padding-left:10px;")
        
        self.InputPassword.setFont(InputFont.get_Font())
        self.InputUsername.setFont(InputFont.get_Font())
        self.InputPassword.setFixedSize(500,50)
        self.InputUsername.setFixedSize(500,50)
        self.InputPassword.setEchoMode(QLineEdit.Password)

        Logo = Image("azocar_logo.png",270)

        btn = Button("Iniciar Sesion", 400,60,323297,"Montserrat-SemiBold",20)
        btn.clicked.connect(self.Hello)
        TitleLayout.addWidget(TitleText, alignment=Qt.AlignCenter)

        FormLayout.addWidget(LabelUsername, alignment=Qt.AlignLeft)
        FormLayout.addWidget(self.InputUsername)

        FormLayout.addWidget(LabelPassword)
        FormLayout.addWidget(self.InputPassword)

        ButtonLayout.addWidget(btn)

        VericalLayout.addStretch(1)
        VericalLayout.addLayout(TitleLayout)
        VericalLayout.addStretch(1)
        VericalLayout.addLayout(FormLayout)
        VericalLayout.addWidget(self.errorText)
        VericalLayout.addStretch(1)
        # VericalLayout.addStretch(1)
        VericalLayout.addLayout(ButtonLayout)
        VericalLayout.addStretch(1)
        VericalLayout.setContentsMargins(0,20,100,0)
        Horizontal.addWidget(Logo, alignment=Qt.AlignVCenter)
        Horizontal.addLayout(VericalLayout)

        LoginGroup.setFixedSize(1600,800)
        LoginGroup.setStyleSheet("QGroupBox { border: 4px solid #04047B; border-radius:20px; }")

        LoginGroup.setLayout(Horizontal)

        Layout.addWidget(LoginGroup, alignment=Qt.AlignCenter)
        self.setLayout(Layout)

    def Hello(self):
        username = self.InputUsername.text()
        password = self.InputPassword.text()
        rcv = check_user(username,password)
        if rcv == 'admin':
            print('Usuario es admin')
            self.start_app = mainApp()
            self.start_app.showFullScreen()
            self.close()
        elif rcv =='user':
            print('User')
        else:
            self.errorText.setText("Usuario no encontrado")
            print('No se ha encontrado el usuario')
        


app=QApplication(sys.argv)

window = Login()
window.showFullScreen()
sys.exit(app.exec())
app.quit()


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from Components.Font import MyFonts
from Components.Button import Button
import threading
import _thread
from PyQt5.QtNetwork import QTcpSocket, QHostAddress


class SendCommand(QWidget):
    def __init__(self):
        super().__init__()
        SectionLayout = QVBoxLayout()
        SectionGroup = QGroupBox()
        BtnLayout = QHBoxLayout()
        TextLayout = QHBoxLayout()

        self.tcp_client = None

        SectionGroup.setFixedHeight(350)
        SectionGroup.setFixedWidth(1870)

        Layout = QVBoxLayout()

        main_text = QLabel("Datos del Indicador")
        self.state_text = QLabel("Desconectado")
        font_text = MyFonts(20,"Montserrat-Medium")
        font_info = MyFonts(10,"Montserrat-Thin")
        main_text.setFont(font_text.get_Font())
        self.state_text.setFont(font_text.get_Font())

        self.info_text = QLabel("Info")
        self.info_text.setFont(font_text.get_Font())

        BackUp = Button("Conectar",250,80,323297,"Montserrat-Medium",24)
        Delete = Button("Enviar",250,80,323297,"Montserrat-Medium",24)

        BtnLayout.addStretch(1)
        BtnLayout.addWidget(BackUp)
        BtnLayout.addStretch(1)
        BtnLayout.addWidget(Delete)
        BtnLayout.addStretch(1)

        TextLayout.addStretch(1)
        TextLayout.addWidget(main_text)
        TextLayout.addWidget(self.state_text)
        TextLayout.addStretch(1)

        SectionLayout.addStretch(1)
        SectionLayout.addLayout(TextLayout )
        SectionLayout.addStretch(1)
        SectionLayout.addWidget(self.info_text,alignment=Qt.AlignCenter)
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(BtnLayout)
        SectionLayout.addStretch(1)

        SectionGroup.setStyleSheet("QGroupBox { border: 4px solid #04047B; border-radius:20px;}")
        SectionGroup.setLayout(SectionLayout)
        Layout.addWidget(SectionGroup)
        self.setLayout(Layout)

        BackUp.clicked.connect(self.Habilitar)
        Delete.clicked.connect(self.Send)

    def Habilitar(self):
        if self.tcp_client is None:
            self.tcp_client =QTcpSocket()
            self.tcp_client.connected.connect(self.on_connected)
            self.tcp_client.disconnected.connect(self.on_disconnected)
            self.tcp_client.error.connect(self.on_error)
            self.tcp_client.readyRead.connect(self.on_ready_read)

            self.tcp_client.connectToHost("192.168.1.86",10001)

    def Send(self):
        command = "db.data#1\r\n"
        self.tcp_client.write(command.encode())
        
        # print("Sent command to server:", command)

    def on_connected(self):
        self.state_text.setStyleSheet("color:#06CD4A")
        self.state_text.setText("Conectado")
        
    def on_disconnected(self):
        self.state_text.setStyleSheet("color:#CD0606")
        self.state_text.setText("Desconectado") 
        self.info_text.setText("Sin Conexion")
    
    def on_error(self):
        self.state_text.setText("Error")
    
    def on_ready_read(self):
        data = self.tcp_client.readAll().data().decode()
        self.info_text.setText("Received Data: " + data)
        # data = data.splitlines()
        # data1 = '1,2,3,4'.split(',')
        # data = data.split('\r\n')
        print(len(data))



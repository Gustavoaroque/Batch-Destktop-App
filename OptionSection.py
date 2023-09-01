

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,QGroupBox,QLabel,QHBoxLayout
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from Components.Font import MyFonts
from Components.Button import Button
import threading
import _thread
from PyQt5.QtNetwork import QTcpSocket, QHostAddress


class WeightCap(QWidget):
    def __init__(self,fn_start, fn_close):
        super().__init__()
        SectionLayout = QVBoxLayout()
        SectionGroup = QGroupBox()
        BtnLayout = QHBoxLayout()
        TextLayout = QHBoxLayout()
        TextResultLayout = QHBoxLayout()
        self.fn_start = fn_start
        self.fn_start = fn_start

        self.tcp_client = None
        # if self.tcp_client is not None:
        # self.socket = QTcpSocket()
        # self.socket.connected.connect(self.Habilitar)

        SectionGroup.setFixedHeight(450)
        SectionGroup.setFixedWidth(900)

        Layout = QVBoxLayout()

        main_text = QLabel("Estado de Comunicacion")
        self.state_text = QLabel("Desconectado")
        self.info_text = QLabel("Start")

        font_text = MyFonts(20,"Montserrat-Medium")
        font_info = MyFonts(20,"Montserrat-Bold")
        result_text = MyFonts(22,"Montserrat-SemiBold")

        main_text.setFont(font_text.get_Font())
        self.state_text.setFont(font_info.get_Font())
        result_text = self.info_text.setFont(result_text.get_Font())

        self.info_text.setFont(font_text.get_Font())

        self.Start = Button("Iniciar",300,120,323297,"Montserrat-Medium",24,self.Habilitar)
        close = Button("Cerrar",300,120,323297,"Montserrat-Medium",24,self.Desconectar)

        BtnLayout.addStretch(1)
        BtnLayout.addWidget(self.Start)
        BtnLayout.addStretch(1)
        BtnLayout.addWidget(close)
        BtnLayout.addStretch(1)

        TextLayout.addStretch(1)
        TextLayout.addWidget(main_text)
        TextLayout.addStretch(1)
        TextLayout.addWidget(self.state_text)
        TextLayout.addStretch(1)

        TextResultLayout.addWidget(self.info_text,alignment=Qt.AlignCenter)

        SectionLayout.addStretch(1)
        SectionLayout.addLayout(TextLayout )
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(TextResultLayout)
        SectionLayout.addStretch(1)
        SectionLayout.addLayout(BtnLayout)
        SectionLayout.addStretch(1)

        SectionGroup.setStyleSheet("QGroupBox { border: 4px solid #04047B; border-radius:30px;}")
        SectionGroup.setLayout(SectionLayout)
        Layout.addWidget(SectionGroup)
        self.setLayout(Layout)

    def Habilitar(self):
        if self.tcp_client is None:
            self.tcp_client =QTcpSocket()
            self.tcp_client.connected.connect(self.on_connected)
            self.tcp_client.disconnected.connect(self.on_disconnected)
            self.tcp_client.error.connect(self.on_error)
            self.tcp_client.readyRead.connect(self.on_ready_read)

            self.tcp_client.connectToHost("192.168.1.86",20001)

    def Desconectar(self):
        if self.tcp_client is not None:
            self.tcp_client.disconnectFromHost()
            self.tcp_client =None

    def on_connected(self):
        self.state_text.setStyleSheet("color:#06CD4A")
        self.Start.setEnabled(False)
        self.state_text.setText("Conectado")
        
    def on_disconnected(self):
        self.state_text.setStyleSheet("color:#CD0606")
        self.state_text.setText("Desconectado") 
        self.info_text.setText("Sin Conexion")
        self.Start.setEnabled(True)
    
    def on_error(self):
        self.state_text.setText("Error")
    
    def on_ready_read(self):
        # print("Leyendo")
        data = self.tcp_client.readAll().data().decode("utf-8")
        self.info_text.setText("Received Data: " + data)



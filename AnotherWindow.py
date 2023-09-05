import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QTableView,QVBoxLayout,QHBoxLayout, QGroupBox, QLabel
from Components.Button import Button
from Head import HeadSection

basedir = os.path.dirname(__file__)

db = QSqlDatabase.addDatabase("QPSQL7")

class DBTabel(QWidget):

    def __init__(self,table_name):
        super().__init__()
        db.setHostName("localhost")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setUserName("postgres")
        db.setPassword("Admin4")


        filterLabel = QLabel("Filtrar: ")
        #Navbar section
        nav = HeadSection(self)

        LeftLayout = QVBoxLayout()
        RightLayout = QVBoxLayout()

        FilterSeccion = QHBoxLayout()
        TableGroup = QGroupBox()

        TableGroup.setFixedSize(1200,900)

        Layout = QVBoxLayout()

        FilterSeccion.addWidget(filterLabel,alignment=Qt.AlignCenter)
        
        # db.open()
        self.table = QTableView()
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)
        if db.open():
            # print('Todo Ok')
            quer = "SELECT * FROM " + table_name + ";"
            q = QSqlQuery(quer,db=db)
            self.model.setQuery(q)
            # self.model.select()
            # self.setMinimumSize(QSize(1024, 600))
            db.close()
        else:
            print('Error')
        # # self.StartCom()
        # self.setCentralWidget(self.table)
        LeftLayout.addLayout(FilterSeccion)
        LeftLayout.addWidget(self.table)
        TableGroup.setLayout(LeftLayout)


        Layout.addWidget(TableGroup)
        self.setLayout(Layout)

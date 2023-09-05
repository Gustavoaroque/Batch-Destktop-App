import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableView,QVBoxLayout
# from QWid
# Initialize the Qt application


# Initialize the Qt database driver for PostgreSQL

# Rest of your code
basedir = os.path.dirname(__file__)


class DBTabel(QWidget):

    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        db = QSqlDatabase.addDatabase("QPSQL7")
        # db = QSqlDatabase.database()
        db.setHostName("localhost")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setUserName("postgres")
        db.setPassword("Admin4")
        # db.open()
        self.table = QTableView()
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)
        if db.open():
            # print('Todo Ok')
            quer = "SELECT * FROM public.plu;"
            q = QSqlQuery(quer,db=db)
            self.model.setQuery(q)
            # self.model.select()
            # self.setMinimumSize(QSize(1024, 600))
        else:
            print('Error')
        # # self.StartCom()
        # self.setCentralWidget(self.table)
        lay.addWidget(self.table)
        self.setLayout(lay)

import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
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
        db.open()
        # if db.open():
        #     print('Todo Ok')
        # else:
        #     print('Error')
        # # self.StartCom()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        self.model.setTable("public.plu")
        self.model.select()
        self.setMinimumSize(QSize(1024, 600))
        # self.setCentralWidget(self.table)
        lay.addWidget(self.table)
        self.setLayout(lay)

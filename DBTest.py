import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)

# Load the PostgreSQL driver before creating a QSqlDatabase instance
QSqlDatabase.addDatabase("QPSQL7")

db = QSqlDatabase.database()
db.setHostName("localhost")
db.setPort(5432)
db.setDatabaseName("postgres")
db.setUserName("postgres")
db.setPassword("Admin4")
db.open()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        self.model.setTable("public.plu")
        self.model.select()
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)

window = MainWindow()
window.show()
app.exec_()

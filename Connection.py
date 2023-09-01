from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
import psycopg2

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self.data = data
        self.header = header

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self.data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self.header[section])
        return None

app = QApplication([])

# Establish a PostgreSQL connection and retrieve data
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin4"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM plu")  # Replace with your table name
data = cursor.fetchall()
print(type(data))
header = [desc[0] for desc in cursor.description]
print(header)

model = CustomTableModel(data, header)

# Create a QTableView
view = QTableView()
view.setModel(model)

window = QMainWindow()
window.setCentralWidget(view)
window.show()

app.exec_()

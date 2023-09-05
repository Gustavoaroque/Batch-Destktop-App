# from PyQt5.QtCore import Qt, QAbstractTableModel
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
import psycopg2

# class CustomTableModel(QAbstractTableModel):
#     def __init__(self, data, header, parent=None):
#         super().__init__(parent)
#         self.data = data
#         self.header = header

#     def rowCount(self, parent):
#         return len(self.data)

#     def columnCount(self, parent):
#         return len(self.data[0])

#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             return str(self.data[index.row()][index.column()])
#         return None

#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return str(self.header[section])
#         return None

# app = QApplication([])

# Establish a PostgreSQL connection and retrieve data
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Admin4"
)
def check_user(username,password):
    query = "SELECT role FROM Users WHERE username = '" + username + "' and passwrd = '" + password + "';"
    cursor = connection.cursor()
    cursor.execute(query)  # Replace with your table name
    data = cursor.fetchall()
    if data:
        # print('Usuario encontrado')
        list1 = data[0]
        print(list1[0])
        cursor.close()
        return list1[0]
    else :
        return None
    

    
    

# check_user("Gustavoaroque","Admin4")

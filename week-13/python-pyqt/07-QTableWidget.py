import sys

from PyQt5.QtWidgets import (
  QApplication, QMainWindow, QTableWidget, 
  QTableWidgetItem, QVBoxLayout, QHeaderView)


table_data = {
       "No.": ["1", "2", "3"],
       "NIM": ["101010101", "101010105", "101020201"],
      "Nama": ["Andi Fulan", "Wulandari Saifah", "Nirmala Suhadah"],
    "Alamat": ["Jln. Sungai Wein", "Jln. Daun Borneo", "Jln. Kacang Tanah"],
  "No. Telp": ["087867556464", "087867556461", "087581225321"]
}

def printItem(row, column):
  print(row, column)
  if (table.item(row, column) != None):
    print(table.item(row, column).text())

def setData(tableObj, tableData):
  horizontalHeaders = []
  for n, key in enumerate(tableData.keys()):
    horizontalHeaders.append(key)
    for m, item in enumerate(tableData[key]):
      newItem = QTableWidgetItem(item)
      tableObj.setItem(m, n, newItem)
    
  tableObj.setHorizontalHeaderLabels(horizontalHeaders)
  tableObj.resizeColumnsToContents()
  # tableObj.resizeRowsToContents()
  tableObj.show()


app = QApplication([])

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Hello World!")
mainWindow.setGeometry(200, 200, 700, 500)

table = QTableWidget(10, 5)
setData(table, table_data)
table.horizontalHeader().setStretchLastSection(True)
table.horizontalHeader().setSectionResizeMode(
  QHeaderView.Stretch)

table.cellClicked.connect(printItem)

# -- after everything is set put table object into mainWindow
mainWindow.setCentralWidget(table)
mainWindow.show()
sys.exit(app.exec_())

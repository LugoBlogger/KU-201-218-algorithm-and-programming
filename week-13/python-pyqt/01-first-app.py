import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Hello World!")
mainWindow.setGeometry(200, 200, 700, 500)

mainWindow.show()
sys.exit(app.exec_())
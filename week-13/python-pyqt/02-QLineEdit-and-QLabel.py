import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, \
  QLineEdit

app = QApplication([])

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Hello World!")
mainWindow.setGeometry(200, 200, 700, 500)

def textEditEnter():
  text = textEdit.text()   # get the text (string)
  textLabel.setText(text)
  textLabel.adjustSize()



textLabel = QLabel("Empty text", parent=mainWindow)
textEdit = QLineEdit("", parent=mainWindow)
textEdit.resize(500, 50)
textEdit.move(0, 50)

textEdit.returnPressed.connect(textEditEnter)


mainWindow.show()
sys.exit(app.exec_())

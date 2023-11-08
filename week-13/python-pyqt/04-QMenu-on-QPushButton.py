import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import \
  (QApplication, 
   QMainWindow, 
   QLabel, 
   QLineEdit, 
   QPushButton, 
   QMenu)

app = QApplication([])

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Hello World!")
mainWindow.setGeometry(200, 200, 700, 500)

def textEditEnter():
  text = textEdit.text()   # get the text (string)
  textLabel.setText(text)
  textLabel.adjustSize()

## -- Label and TextEdit
textLabel = QLabel("Empty text", parent=mainWindow)
textEdit = QLineEdit("", parent=mainWindow)
textEdit.resize(500, 50)
textEdit.move(0, 50)

textEdit.returnPressed.connect(textEditEnter)

## -- Button for submission
submitBtn = QPushButton("Submit", parent=mainWindow)
submitBtn.move(510, 50)
submitBtn.setFixedSize(150, 50)

fontBtn = QFont()
fontBtn.setBold(True)
fontBtn.setPointSize(14)
submitBtn.setFont(fontBtn)

submitBtn.clicked.connect(textEditEnter)

## -- Add some drop-down list in `submitBtn`
menu = QMenu()
menu.addAction("Aksi 1", textEditEnter)
menu.addAction("Aksi 2", textEditEnter)
menu.addAction("Aksi 3", textEditEnter)
submitBtn.setMenu(menu)


mainWindow.show()
sys.exit(app.exec_())



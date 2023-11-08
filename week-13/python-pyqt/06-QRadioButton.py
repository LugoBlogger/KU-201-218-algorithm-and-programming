import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import \
  (QApplication, 
   QMainWindow, 
   QLabel, 
   QLineEdit, 
   QPushButton, 
   QMenu,
   QCheckBox, 
   QRadioButton)

app = QApplication([])

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Hello World!")
mainWindow.setGeometry(200, 200, 700, 500)

## -- Function declarations
def textEditEnter():
  text = textEdit.text()   # get the text (string)
  textLabel.setText(text)
  textLabel.adjustSize()

def updateLabel():
  text = ""
  if (option1CheckBox.isChecked()):
    text += "Option 1; "
  
  if (option2CheckBox.isChecked()):
    text += "Option 2; "

  if (option3CheckBox.isChecked()):
    text += "Option 3; "

  textLabel.setText(text)
  textLabel.adjustSize()

def updateLabelRadioButton():
  text = ""
  if (option1RadioButton.isChecked()):
    text = option1RadioButton.text()
  
  if (option2RadioButton.isChecked()):
    text = option2RadioButton.text() 

  if (option3CheckBox.isChecked()):
    text = option3RadioButton.text()

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

## -- Add list of checkbox
option1CheckBox = QCheckBox("Option 1", parent=mainWindow)
option2CheckBox = QCheckBox("Option 2", parent=mainWindow)
option3CheckBox = QCheckBox("Option 3", parent=mainWindow)
option1CheckBox.move(10, 110)
option2CheckBox.move(10, 140)
option3CheckBox.move(10, 170)
option1CheckBox.stateChanged.connect(updateLabel)
option2CheckBox.stateChanged.connect(updateLabel)
option3CheckBox.stateChanged.connect(updateLabel)

## -- Add radio button on the right of list of checkbox
option1RadioButton = QRadioButton("A", parent=mainWindow)
option2RadioButton = QRadioButton("B", parent=mainWindow)
option3RadioButton = QRadioButton("C", parent=mainWindow)
option1RadioButton.move(150, 110)
option2RadioButton.move(150, 140)
option3RadioButton.move(150, 170)
option1RadioButton.toggled.connect(updateLabelRadioButton)
option2RadioButton.toggled.connect(updateLabelRadioButton)
option3RadioButton.toggled.connect(updateLabelRadioButton)


mainWindow.show()
sys.exit(app.exec_())





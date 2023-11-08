import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit

app = QApplication([])

main_window = QMainWindow()
main_window.setGeometry(200, 200, 700, 500)
main_window.setWindowTitle("Hello World!")

text_label = QLabel("Teks Kosong", parent=main_window)

text_edit_label = QLineEdit("Silahkan ketik", parent=main_window)
text_edit_label.move(50, 50)

# Semua widgets


main_window.show()
sys.exit(app.exec_())


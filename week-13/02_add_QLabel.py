import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication([])

main_window = QMainWindow()
main_window.setGeometry(200, 200, 700, 500)
main_window.setWindowTitle("Hello World!")

text_label = QLabel("Teks Kosong", parent=main_window)


# Semua widgets


main_window.show()
sys.exit(app.exec_())

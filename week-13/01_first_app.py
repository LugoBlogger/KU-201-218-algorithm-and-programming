import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])

main_window = QMainWindow()
main_window.setGeometry(200.5, 200, 700, 500)
main_window.setWindowTitle("Hello World!")


# Semua widgets


main_window.show()
sys.exit(app.exec_())
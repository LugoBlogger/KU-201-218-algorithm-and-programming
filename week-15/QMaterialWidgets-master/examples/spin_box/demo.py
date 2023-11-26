# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from qmaterialwidgets import SpinBox, DoubleSpinBox, DateTimeEdit, DateEdit, TimeEdit, setTheme, Theme, palette


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet('Demo{background:'+palette.surface.name()+'}')

        self.vBoxLayout = QVBoxLayout(self)

        self.spinBox = SpinBox(self)
        self.timeEdit = TimeEdit(self)
        self.dateEdit = DateEdit(self)
        self.dateTimeEdit = DateTimeEdit(self)
        self.doubleSpinBox = DoubleSpinBox(self)

        self.spinBox.setLabel('Label')
        self.timeEdit.setLabel('Time')
        self.dateEdit.setLabel('Date')
        self.doubleSpinBox.setLabel('Double'*2)
        self.dateTimeEdit.setLabel('Date time')

        self.resize(500, 500)

        self.vBoxLayout.setContentsMargins(100, 50, 100, 50)
        self.vBoxLayout.addWidget(self.spinBox)
        self.vBoxLayout.addWidget(self.doubleSpinBox)
        self.vBoxLayout.addWidget(self.timeEdit)
        self.vBoxLayout.addWidget(self.dateEdit)
        self.vBoxLayout.addWidget(self.dateTimeEdit)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()

# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSpinBox
from qmaterialwidgets import ProgressRing, setTheme, Theme, IndeterminateProgressRing, setFont


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        # self.setStyleSheet('Demo{background: rgb(32, 32, 32)}')

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.spinner = IndeterminateProgressRing(self)
        self.progressRing = ProgressRing(self)
        self.spinBox = QSpinBox(self)

        self.progressRing.setValue(50)
        self.progressRing.setTextVisible(True)
        self.progressRing.setFixedSize(80, 80)

        # self.spinner.setFixedSize(50, 50)

        # change background color
        # self.progressRing.setCustomBackgroundColor(Qt.transparent, Qt.transparent)

        # change font
        # setFont(self.progressRing, fontSize=15)

        # change size
        # self.spinner.setFixedSize(50, 50)

        # change thickness
        # self.progressRing.setStrokeWidth(4)
        # self.spinner.setStrokeWidth(4)

        self.spinBox.setRange(0, 100)
        self.spinBox.setValue(50)
        self.spinBox.valueChanged.connect(self.progressRing.setValue)

        self.hBoxLayout.addWidget(self.progressRing, 0, Qt.AlignHCenter)
        self.hBoxLayout.addWidget(self.spinBox, 0, Qt.AlignHCenter)

        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.spinner, 0, Qt.AlignHCenter)
        self.resize(400, 400)



if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
# coding:utf-8
import sys
from PyQt5.QtCore import QEvent, QPoint, Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from qmaterialwidgets import ToolTip, ToolTipFilter, setTheme, Theme, OutlinedPushButton, ToolTipPosition


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # use dark theme
        # setTheme(Theme.DARK)
        # self.setStyleSheet('Demo {background: rgb(20, 18, 24)}')

        self.hBox = QHBoxLayout(self)
        self.button1 = OutlinedPushButton('キラキラ', self)
        self.button2 = OutlinedPushButton('食べた愛', self)
        self.button3 = OutlinedPushButton('シアワセ', self)

        self.button1.setToolTip('aiko - キラキラ ✨')
        self.button2.setToolTip('aiko - 食べた愛 🥰')
        self.button3.setToolTip('aiko - シアワセ 😊')
        self.button1.setToolTipDuration(1000)
        # self.button2.setToolTipDuration(-1)  # won't disappear

        self.button1.installEventFilter(ToolTipFilter(self.button1, 200, ToolTipPosition.TOP))
        self.button2.installEventFilter(ToolTipFilter(self.button2, 0, ToolTipPosition.BOTTOM))
        self.button3.installEventFilter(ToolTipFilter(self.button3, 300, ToolTipPosition.RIGHT))

        self.button1.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=S0bXDRY1DGM&list=RDMM&index=1')))
        self.button2.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=CZLs8GuCq2U&list=RDMM&index=4')))
        self.button3.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=fp-yJUB7sS8&list=RDMM&index=3')))

        self.hBox.setContentsMargins(24, 24, 24, 24)
        self.hBox.setSpacing(16)
        self.hBox.addWidget(self.button1)
        self.hBox.addWidget(self.button2)
        self.hBox.addWidget(self.button3)

        self.resize(480, 240)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()

# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout

from qmaterialwidgets import (TeachingTip, TeachingTipTailPosition, InfoBarIcon, setTheme, Theme,
                            TeachingTipView, FlyoutViewBase, BodyLabel, OutlinedPushButton,
                            PopupTeachingTip, FilledPushButton, palette, TonalPushButton)


class CustomFlyoutView(FlyoutViewBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = BodyLabel(
            '这是一场「试炼」，我认为这就是一场为了战胜过去的「试炼」，\n只有战胜了那些幼稚的过去，人才能有所成长。')
        self.button = OutlinedPushButton('Action')

        self.button.setFixedWidth(140)
        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.button)

    def paintEvent(self, e):
        pass


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet("Demo{background:"+palette.surface.name()+'}')

        self.hBoxLayout = QHBoxLayout(self)
        self.button1 = OutlinedPushButton('Top', self)
        self.button2 = OutlinedPushButton('Bottom', self)
        self.button3 = OutlinedPushButton('Custom', self)

        self.resize(700, 500)
        self.button1.setFixedWidth(150)
        self.button2.setFixedWidth(150)
        self.button3.setFixedWidth(150)
        self.hBoxLayout.addWidget(self.button2, 0, Qt.AlignHCenter)
        self.hBoxLayout.addWidget(self.button1, 0, Qt.AlignHCenter)
        self.hBoxLayout.addWidget(self.button3, 0, Qt.AlignHCenter)
        self.button1.clicked.connect(self.showTopTip)
        self.button2.clicked.connect(self.showBottomTip)
        self.button3.clicked.connect(self.showCustomTip)

    def showTopTip(self):
        position = TeachingTipTailPosition.BOTTOM
        view = TeachingTipView(
            icon=None,
            title='Lesson 5',
            content="最短的捷径就是绕远路，绕远路才是我的最短捷径。",
            image='resource/Gyro.jpg',
            # image='resource/boqi.gif',
            isClosable=True,
            tailPosition=position,
        )

        # add widget to view
        button = FilledPushButton('Action')
        button.setFixedWidth(120)
        view.addWidget(button, align=Qt.AlignRight)

        w = TeachingTip.make(
            target=self.button1,
            view=view,
            duration=-1,
            tailPosition=position,
            parent=self
        )
        view.closed.connect(w.close)

    def showBottomTip(self):
        TeachingTip.create(
            target=self.button2,
            icon=InfoBarIcon.SUCCESS,
            title='Lesson 4',
            content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
            isClosable=True,
            tailPosition=TeachingTipTailPosition.TOP,
            duration=2000,
            parent=self
        )

    def showCustomTip(self):
        # TeachingTip.make(
        PopupTeachingTip.make(
            target=self.button3,
            view=CustomFlyoutView(),
            tailPosition=TeachingTipTailPosition.RIGHT,
            duration=2000,
            parent=self
        )


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()

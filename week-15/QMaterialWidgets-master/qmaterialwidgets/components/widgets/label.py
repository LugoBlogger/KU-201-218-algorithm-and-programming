# coding:utf-8

from typing import List, Union

from PyQt5.QtCore import Qt, pyqtProperty, QPoint, pyqtSignal, QSize
from PyQt5.QtGui import (QPainter, QPixmap, QPalette, QColor, QFont, QImage, QPainterPath,
                         QImageReader, QBrush, QMovie)
from PyQt5.QtWidgets import QLabel, QWidget

from ...common.overload import singledispatchmethod
from ...common.font import setFont, getFont
from ...common.config import qconfig, isDarkTheme


class MaterialLabelBase(QLabel):
    """ Material label base class """

    @singledispatchmethod
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._init()

    @__init__.register
    def _(self, text: str, parent: QWidget = None):
        self.__init__(parent)
        self.setText(text)

    def _init(self):
        self.setFont(self.getFont())
        self.setTextColor()
        qconfig.themeChanged.connect(
            lambda: self.setTextColor(self.lightColor, self.darkColor))
        return self

    def getFont(self):
        raise NotImplementedError

    def setTextColor(self, light=QColor(0, 0, 0), dark=QColor(255, 255, 255)):
        """ set the text color of label

        Parameters
        ----------
        light, dark: QColor | Qt.GlobalColor | str
            text color in light/dark mode
        """
        self._lightColor = QColor(light)
        self._darkColor = QColor(dark)

        palette = self.palette()
        color = self.darkColor if isDarkTheme() else self.lightColor
        palette.setColor(QPalette.ColorRole.WindowText, color)
        self.setPalette(palette)

    @pyqtProperty(QColor)
    def lightColor(self):
        return self._lightColor

    @lightColor.setter
    def lightColor(self, color: QColor):
        self.setTextColor(color, self.darkColor)

    @pyqtProperty(QColor)
    def darkColor(self):
        return self._darkColor

    @darkColor.setter
    def darkColor(self, color: QColor):
        self.setTextColor(self.lightColor, color)

    @pyqtProperty(int)
    def pixelFontSize(self):
        return self.font().pixelSize()

    @pixelFontSize.setter
    def pixelFontSize(self, size: int):
        font = self.font()
        font.setPixelSize(size)
        self.setFont(font)

    @pyqtProperty(bool)
    def strikeOut(self):
        return self.font().strikeOut()

    @strikeOut.setter
    def strikeOut(self, isStrikeOut: bool):
        font = self.font()
        font.setStrikeOut(isStrikeOut)
        self.setFont(font)

    @pyqtProperty(bool)
    def underline(self):
        return self.font().underline()

    @underline.setter
    def underline(self, isUnderline: bool):
        font = self.font()
        font.setStyle()
        font.setUnderline(isUnderline)
        self.setFont(font)


class CaptionLabel(MaterialLabelBase):
    """ Caption text label """

    def getFont(self):
        return getFont(12)


class BodyLabel(MaterialLabelBase):
    """ Body text label """

    def getFont(self):
        return getFont(14)


class StrongBodyLabel(MaterialLabelBase):
    """ Strong body text label """

    def getFont(self):
        return getFont(14, QFont.Weight.DemiBold)


class SubtitleLabel(MaterialLabelBase):
    """ Sub title text label """

    def getFont(self):
        return getFont(20, QFont.Weight.DemiBold)


class TitleLabel(MaterialLabelBase):
    """ Sub title text label """

    def getFont(self):
        return getFont(28, QFont.Weight.DemiBold)


class LargeTitleLabel(MaterialLabelBase):
    """ Large title text label """

    def getFont(self):
        return getFont(40, QFont.Weight.DemiBold)


class DisplayLabel(MaterialLabelBase):
    """ Display text label """

    def getFont(self):
        return getFont(68, QFont.Weight.DemiBold)


class ImageLabel(QLabel):
    """ Image label """

    clicked = pyqtSignal()

    @singledispatchmethod
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.image = QImage()
        self.setBorderRadius(0, 0, 0, 0)

    @__init__.register
    def _(self, image: str, parent=None):
        self.__init__(parent)
        self.setImage(image)

    @__init__.register
    def _(self, image: QImage, parent=None):
        self.__init__(parent)
        self.setImage(image)

    @__init__.register
    def _(self, image: QPixmap, parent=None):
        self.__init__(parent)
        self.setImage(image)

    def _onFrameChanged(self, index: int):
        self.image = self.movie().currentImage()
        self.update()

    def setBorderRadius(self, topLeft: int, topRight: int, bottomLeft: int, bottomRight: int):
        """ set the border radius of image """
        self._topLeftRadius = topLeft
        self._topRightRadius = topRight
        self._bottomLeftRadius = bottomLeft
        self._bottomRightRadius = bottomRight
        self.update()

    def setImage(self, image: Union[str, QPixmap, QImage] = None):
        """ set the image of label """
        self.image = image or QImage()

        if isinstance(image, str):
            reader = QImageReader(image)
            if reader.supportsAnimation():
                self.setMovie(QMovie(image))
            else:
                self.image = reader.read()
        elif isinstance(image, QPixmap):
            self.image = image.toImage()

        self.setFixedSize(self.image.size())
        self.update()

    def scaledToWidth(self, width: int):
        if self.isNull():
            return

        h = int(width / self.image.width() * self.image.height())
        self.setFixedSize(width, h)

        if self.movie():
            self.movie().setScaledSize(QSize(width, h))

    def scaledToHeight(self, height: int):
        if self.isNull():
            return

        w = int(height / self.image.height() * self.image.width())
        self.setFixedSize(w, height)

        if self.movie():
            self.movie().setScaledSize(QSize(w, height))

    def isNull(self):
        return self.image.isNull()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    def setPixmap(self, pixmap: QPixmap):
        self.setImage(pixmap)

    def pixmap(self) -> QPixmap:
        return QPixmap.fromImage(self.image)

    def setMovie(self, movie: QMovie):
        super().setMovie(movie)
        self.movie().start()
        self.image = self.movie().currentImage()
        self.movie().frameChanged.connect(self._onFrameChanged)

    def paintEvent(self, e):
        if self.isNull():
            return

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        path = QPainterPath()
        w, h = self.width(), self.height()

        # top line
        path.moveTo(self.topLeftRadius, 0)
        path.lineTo(w - self.topRightRadius, 0)

        # top right arc
        d = self.topRightRadius * 2
        path.arcTo(w - d, 0, d, d, 90, -90)

        # right line
        path.lineTo(w, h - self.bottomRightRadius)

        # bottom right arc
        d = self.bottomRightRadius * 2
        path.arcTo(w - d, h - d, d, d, 0, -90)

        # bottom line
        path.lineTo(self.bottomLeftRadius, h)

        # bottom left arc
        d = self.bottomLeftRadius * 2
        path.arcTo(0, h - d, d, d, -90, -90)

        # left line
        path.lineTo(0, self.topLeftRadius)

        # top left arc
        d = self.topLeftRadius * 2
        path.arcTo(0, 0, d, d, -180, -90)

        # draw image
        image = self.image.scaled(
            self.size()*self.devicePixelRatioF(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setClipPath(path)
        painter.drawImage(self.rect(), image)

    @pyqtProperty(int)
    def topLeftRadius(self):
        return self._topLeftRadius

    @topLeftRadius.setter
    def topLeftRadius(self, radius: int):
        self.setBorderRadius(radius, self.topRightRadius, self.bottomLeftRadius, self.bottomRightRadius)

    @pyqtProperty(int)
    def topRightRadius(self):
        return self._topRightRadius

    @topRightRadius.setter
    def topRightRadius(self, radius: int):
        self.setBorderRadius(self.topLeftRadius, radius, self.bottomLeftRadius, self.bottomRightRadius)

    @pyqtProperty(int)
    def bottomLeftRadius(self):
        return self._bottomLeftRadius

    @bottomLeftRadius.setter
    def bottomLeftRadius(self, radius: int):
        self.setBorderRadius(self.topLeftRadius, self.topRightRadius, radius, self.bottomRightRadius)

    @pyqtProperty(int)
    def bottomRightRadius(self):
        return self._bottomRightRadius

    @bottomRightRadius.setter
    def bottomRightRadius(self, radius: int):
        self.setBorderRadius(self.topLeftRadius, self.topRightRadius, self.bottomLeftRadius, radius)

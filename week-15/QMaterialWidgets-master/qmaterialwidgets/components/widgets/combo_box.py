# coding:utf-8
from typing import Union, List, Iterable

from PyQt5.QtCore import Qt, pyqtSignal, QRectF, QPoint, QObject, QEvent, pyqtProperty
from PyQt5.QtGui import QPainter, QCursor, QIcon
from PyQt5.QtWidgets import QApplication, QAction

from .menu import RoundMenu, MenuAnimationType, IndicatorMenuItemDelegate
from .line_edit import LineEdit, LineEditButton, FilledLineEdit, LineEditIcon
from ...common.animation import TranslateYAnimation
from ...common.icon import MaterialIconBase, isDarkTheme, Action
from ...common.icon import FluentIcon as FIF
from ...common.font import setFont
from ...common.style_sheet import MaterialStyleSheet


class ComboItem:
    """ Combo box item """

    def __init__(self, text: str, icon: Union[str, QIcon, MaterialIconBase] = None, userData=None):
        """ add item

        Parameters
        ----------
        text: str
            the text of item

        icon: str | QIcon | MaterialIconBase
            the icon of item

        userData: Any
            user data
        """
        self.text = text
        self.userData = userData
        self.icon = icon

    @property
    def icon(self):
        if isinstance(self._icon, QIcon):
            return self._icon

        return self._icon.icon()

    @icon.setter
    def icon(self, ico: Union[str, QIcon, MaterialIconBase]):
        if ico:
            self._icon = QIcon(ico) if isinstance(ico, str) else ico
        else:
            self._icon = QIcon()


class ComboBoxBase:
    """ Combo box base """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.isHover = False
        self.isPressed = False
        self.items = []     # type: List[ComboItem]
        self._currentIndex = -1
        self._maxVisibleItems = -1
        self.dropMenu = None

        #MaterialStyleSheet.COMBO_BOX.apply(self)
        self.installEventFilter(self)

    def addItem(self, text, icon: Union[str, QIcon, MaterialIconBase] = None, userData=None):
        """ add item

        Parameters
        ----------
        text: str
            the text of item

        icon: str | QIcon | MaterialIconBase
        """
        item = ComboItem(text, icon, userData)
        self.items.append(item)
        if len(self.items) == 1:
            self.setCurrentIndex(0)

    def addItems(self, texts: Iterable[str]):
        """ add items

        Parameters
        ----------
        text: Iterable[str]
            the text of item
        """
        for text in texts:
            self.addItem(text)

    def removeItem(self, index: int):
        """ Removes the item at the given index from the combobox.
        This will update the current index if the index is removed.
        """
        if not 0 <= index < len(self.items):
            return

        self.items.pop(index)

        if index < self.currentIndex():
            self._onItemClicked(self._currentIndex - 1)
        elif index == self.currentIndex():
            if index > 0:
                self._onItemClicked(self._currentIndex - 1)
            else:
                self.setCurrentIndex(0)
                self.currentTextChanged.emit(self.currentText())
                self.currentIndexChanged.emit(0)

    def setMaxVisibleItems(self, num: int):
        self._maxVisibleItems = num

    def maxVisibleItems(self):
        return self._maxVisibleItems

    def currentIndex(self):
        return self._currentIndex

    def setCurrentIndex(self, index: int):
        """ set current index

        Parameters
        ----------
        index: int
            current index
        """
        if not 0 <= index < len(self.items):
            return

        self._currentIndex = index
        self.setText(self.items[index].text)

    def setText(self, text: str):
        super().setText(text)
        self.adjustSize()

    def currentText(self):
        if not 0 <= self.currentIndex() < len(self.items):
            return ''

        return self.items[self.currentIndex()].text

    def currentData(self):
        if not 0 <= self.currentIndex() < len(self.items):
            return None

        return self.items[self.currentIndex()].userData

    def setCurrentText(self, text):
        """ set the current text displayed in combo box,
        text should be in the item list

        Parameters
        ----------
        text: str
            text displayed in combo box
        """
        if text == self.currentText():
            return

        index = self.findText(text)
        if index >= 0:
            self.setCurrentIndex(index)

    def setItemText(self, index: int, text: str):
        """ set the text of item

        Parameters
        ----------
        index: int
            the index of item

        text: str
            new text of item
        """
        if not 0 <= index < len(self.items):
            return

        self.items[index].text = text
        if self.currentIndex() == index:
            self.setText(text)

    def itemData(self, index: int):
        """ Returns the data in the given index """
        if not 0 <= index < len(self.items):
            return None

        return self.items[index].userData

    def itemText(self, index: int):
        """ Returns the text in the given index """
        if not 0 <= index < len(self.items):
            return ''

        return self.items[index].text

    def itemIcon(self, index: int):
        """ Returns the icon in the given index """
        if not 0 <= index < len(self.items):
            return QIcon()

        return self.items[index].icon

    def setItemData(self, index: int, value):
        """ Sets the data role for the item on the given index """
        if 0 <= index < len(self.items):
            self.items[index].userData = value

    def setItemIcon(self, index: int, icon: Union[str, QIcon, MaterialIconBase]):
        """ Sets the data role for the item on the given index """
        if 0 <= index < len(self.items):
            self.items[index].icon = icon

    def findData(self, data):
        """ Returns the index of the item containing the given data, otherwise returns -1 """
        for i, item in enumerate(self.items):
            if item.userData == data:
                return i

        return -1

    def findText(self, text: str):
        """ Returns the index of the item containing the given text; otherwise returns -1. """
        for i, item in enumerate(self.items):
            if item.text == text:
                return i

        return -1

    def clear(self):
        """ Clears the combobox, removing all items. """
        if self.currentIndex() >= 0:
            self.setText('')

        self.items.clear()
        self._currentIndex = -1

    def count(self):
        """ Returns the number of items in the combobox """
        return len(self.items)

    def insertItem(self, index: int, text: str, icon: Union[str, QIcon, MaterialIconBase] = None, userData=None):
        """ Inserts item into the combobox at the given index. """
        item = ComboItem(text, icon, userData)
        self.items.insert(index, item)

        if index <= self.currentIndex():
            self._onItemClicked(self.currentIndex() + 1)

    def insertItems(self, index: int, texts: Iterable[str]):
        """ Inserts items into the combobox, starting at the index specified. """
        pos = index
        for text in texts:
            item = ComboItem(text)
            self.items.insert(pos, item)
            pos += 1

        if index <= self.currentIndex():
            self._onItemClicked(self.currentIndex() + pos - index)

    def _closeComboMenu(self):
        if not self.dropMenu:
            return

        self.dropMenu.close()
        self.dropMenu = None

    def _onDropMenuClosed(self):
        pos = self.mapFromGlobal(QCursor.pos())
        if not self.rect().contains(pos):
            self.dropMenu = None

    def _showComboMenu(self):
        if not self.items:
            return

        menu = ComboBoxMenu(self)
        for i, item in enumerate(self.items):
            menu.addAction(
                QAction(item.icon, item.text, triggered=lambda x=i: self._onItemClicked(x)))

        if menu.view.width() < self.width():
            menu.view.setMinimumWidth(self.width())
            menu.adjustSize()

        menu.setMaxVisibleItems(self.maxVisibleItems())
        menu.closed.connect(self._onDropMenuClosed)
        self.dropMenu = menu

        # set the selected item
        if self.currentIndex() >= 0 and self.items:
            menu.setDefaultAction(menu.menuActions()[self.currentIndex()])

        # show menu
        x = -menu.width()//2 + menu.layout().contentsMargins().left() + self.width()//2
        y = self.height()
        pos = self.mapToGlobal(QPoint(x, y))

        aniType = MenuAnimationType.DROP_DOWN
        menu.view.adjustSize(pos, aniType)

        if menu.view.height() < 120 and menu.view.itemsHeight() > menu.view.height():
            aniType = MenuAnimationType.PULL_UP
            pos = self.mapToGlobal(QPoint(x, self._menuPullUpY()))
            menu.view.adjustSize(pos, aniType)

        menu.exec(pos, aniType=aniType)

    def _toggleComboMenu(self):
        if self.dropMenu:
            self._closeComboMenu()
        else:
            self._showComboMenu()

    def _onItemClicked(self, index):
        if index == self.currentIndex():
            return

        self.setCurrentIndex(index)
        self.currentTextChanged.emit(self.currentText())
        self.currentIndexChanged.emit(index)

    def _menuPullUpY(self):
        return 10


class EditableComboBoxBase(ComboBoxBase):
    """ Editable combo box base class """

    currentIndexChanged = pyqtSignal(int)
    currentTextChanged = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropButton = self.setTrailingAction(Action(LineEditIcon.ARROW_DROP_DOWN, ''))
        self.setClearButtonEnabled(False)

        self.dropButton.clicked.connect(self._toggleComboMenu)
        self.textEdited.connect(self._onTextEdited)
        self.returnPressed.connect(self._onReturnPressed)

        MaterialStyleSheet.LINE_EDIT.apply(self)
        self.setAttribute(Qt.WidgetAttribute.WA_MacShowFocusRect, False)

    def currentText(self):
        return self.text()

    def clear(self):
        ComboBoxBase.clear(self)

    def _onReturnPressed(self):
        if not self.text():
            return

        index = self.findText(self.text())
        if index >= 0 and index != self.currentIndex():
            self._currentIndex = index
            self.currentIndexChanged.emit(index)
        elif index == -1:
            self.addItem(self.text())
            self.setCurrentIndex(self.count() - 1)

    def eventFilter(self, obj, e: QEvent):
        if obj is self:
            if e.type() == QEvent.Type.MouseButtonPress:
                self.isPressed = True
            elif e.type() == QEvent.Type.MouseButtonRelease:
                self.isPressed = False
            elif e.type() == QEvent.Type.Enter:
                self.isHover = True
            elif e.type() == QEvent.Type.Leave:
                self.isHover = False

        return super().eventFilter(obj, e)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        if not self.isEditable():
            self._showComboMenu()

    def _onTextEdited(self, text: str):
        self._currentIndex = -1
        self.currentTextChanged.emit(text)

        for i, item in enumerate(self.items):
            if item.text == text:
                self._currentIndex = i
                self.currentIndexChanged.emit(i)
                return

    def _onDropMenuClosed(self):
        self.dropMenu = None


class ComboBox(EditableComboBoxBase, LineEdit):
    """ Combo box """

    currentIndexChanged = pyqtSignal(int)
    currentTextChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setEditable(False)

    def _menuPullUpY(self):
        return 16

    def setEditable(self, isEditable: bool):
        self.setReadOnly(not isEditable)
        if not isEditable:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        else:
            QApplication.restoreOverrideCursor()

    def isEditable(self):
        return not self.isReadOnly()

    editable = pyqtProperty(bool, isEditable, setEditable)


class FilledComboBox(EditableComboBoxBase, FilledLineEdit):
    """ Filled combo box """

    currentIndexChanged = pyqtSignal(int)
    currentTextChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setEditable(False)

    def setEditable(self, isEditable: bool):
        self.setReadOnly(not isEditable)
        if not isEditable:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        else:
            QApplication.restoreOverrideCursor()

    def isEditable(self):
        return not self.isReadOnly()

    editable = pyqtProperty(bool, isEditable, setEditable)


class ComboBoxMenu(RoundMenu):
    """ Combo box menu """

    def __init__(self, parent=None):
        super().__init__(title="", parent=parent)

        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view.setItemDelegate(IndicatorMenuItemDelegate())
        self.view.setObjectName('comboListWidget')

        self.setItemHeight(33)

    def exec(self, pos, ani=True, aniType=MenuAnimationType.DROP_DOWN):
        self.view.adjustSize(pos, aniType)
        self.adjustSize()
        return super().exec(pos, ani, aniType)
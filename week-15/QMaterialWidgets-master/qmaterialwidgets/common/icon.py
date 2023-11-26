# coding:utf-8
from enum import Enum
from typing import Union

from PyQt5.QtXml import QDomDocument
from PyQt5.QtCore import QRectF, Qt, QFile, QObject, QRect
from PyQt5.QtGui import QIcon, QIconEngine, QColor, QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QAction
from PyQt5.QtSvg import QSvgRenderer

from qmaterialwidgets.common.config import Theme

from .config import isDarkTheme, Theme
from .overload import singledispatchmethod


class MaterialIconEngine(QIconEngine):

    def __init__(self, icon):
        super().__init__()
        self.icon = icon

    def paint(self, painter, rect, mode, state):
        painter.save()

        if mode == QIcon.Mode.Disabled:
            painter.setOpacity(0.5)
        elif mode == QIcon.Mode.Selected:
            painter.setOpacity(0.7)

        # change icon color according to the theme
        icon = self.icon
        if isinstance(self.icon, Icon):
            icon = self.icon.materialIcon.icon()

        if rect.x() == 19:
            rect = rect.adjusted(-1, 0, 0, 0)

        icon.paint(painter, rect, Qt.AlignmentFlag.AlignCenter, QIcon.Mode.Normal, state)
        painter.restore()


class SvgIconEngine(QIconEngine):
    """ Svg icon engine """

    def __init__(self, svg: str):
        super().__init__()
        self.svg = svg

    def paint(self, painter, rect, mode, state):
        drawSvgIcon(self.svg.encode(), painter, rect)

    def clone(self) -> QIconEngine:
        return SvgIconEngine(self.svg)

    def pixmap(self, size, mode, state):
        image = QImage(size, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.transparent)
        pixmap = QPixmap.fromImage(image, Qt.ImageConversionFlag.NoFormatConversion)

        painter = QPainter(pixmap)
        rect = QRect(0, 0, size.width(), size.height())
        self.paint(painter, rect, mode, state)
        return pixmap


def getIconColor(theme=Theme.AUTO, reverse=False):
    """ get the color of icon based on theme """
    if not reverse:
        lc, dc = "black", "white"
    else:
        lc, dc = "white", "black"

    if theme == Theme.AUTO:
        color = dc if isDarkTheme() else lc
    else:
        color = dc if theme == Theme.DARK else lc

    return color


def drawSvgIcon(icon, painter, rect):
    """ draw svg icon

    Parameters
    ----------
    icon: str | bytes | QByteArray
        the path or code of svg icon

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon
    """
    renderer = QSvgRenderer(icon)
    renderer.render(painter, QRectF(rect))


def writeSvg(iconPath: str, indexes=None, **attributes):
    """ write svg with specified attributes

    Parameters
    ----------
    iconPath: str
        svg icon path

    indexes: List[int]
        the path to be filled

    **attributes:
        the attributes of path

    Returns
    -------
    svg: str
        svg code
    """
    if not iconPath.lower().endswith('.svg'):
        return ""

    f = QFile(iconPath)
    f.open(QFile.OpenModeFlag.ReadOnly)

    dom = QDomDocument()
    dom.setContent(f.readAll())

    f.close()

    # change the color of each path
    pathNodes = dom.elementsByTagName('path')
    indexes = range(pathNodes.length()) if not indexes else indexes
    for i in indexes:
        element = pathNodes.at(i).toElement()

        for k, v in attributes.items():
            element.setAttribute(k, v)

    return dom.toString()


def drawIcon(icon, painter, rect, state=QIcon.State.Off, **attributes):
    """ draw icon

    Parameters
    ----------
    icon: str | QIcon | MaterialIconBaseBase
        the icon to be drawn

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon

    state: QIcon.State
        icon state

    **attribute:
        the attribute of svg icon
    """
    if isinstance(icon, MaterialIconBase):
        icon.render(painter, rect, **attributes)
    elif isinstance(icon, Icon):
        icon.materialIcon.render(painter, rect, **attributes)
    else:
        icon = QIcon(icon)
        icon.paint(painter, QRectF(rect).toRect(), Qt.AlignmentFlag.AlignCenter, state=state)


class MaterialIconBase:
    """ Fluent icon base class """

    def path(self, theme=Theme.AUTO) -> str:
        """ get the path of icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        raise NotImplementedError

    def icon(self, theme=Theme.AUTO, color: QColor = None):
        """ create an fluent icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`

        color: QColor | Qt.GlobalColor | str
            icon color, only applicable to svg icon
        """
        path = self.path(theme)

        if not (path.endswith('.svg') and color):
            return QIcon(self.path(theme))

        color = QColor(color).name()
        return QIcon(SvgIconEngine(writeSvg(path, fill=color)))

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        """ draw svg icon

        Parameters
        ----------
        painter: QPainter
            painter

        rect: QRect | QRectF
            the rect to render icon

        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`

        indexes: List[int]
            the svg path to be modified

        **attributes:
            the attributes of modified path
        """
        icon = self.path(theme)

        if icon.endswith('.svg'):
            if attributes:
                icon = writeSvg(icon, indexes, **attributes).encode()

            drawSvgIcon(icon, painter, rect)
        else:
            icon = QIcon(icon)
            rect = QRectF(rect).toRect()
            painter.drawPixmap(rect, icon.pixmap(QRectF(rect).toRect().size()))


class MaterialIcon(MaterialIconBase, Enum):
    """ Material icon """

    SEARCH = "Search"
    SCHEDULE = "Schedule"

    def path(self, theme=Theme.AUTO) -> str:
        return f':/qmaterialwidgets/images/material_icons/{self.value}_{getIconColor(theme)}.svg'


class FluentIcon(MaterialIconBase, Enum):
    """ Fluent icon """

    UP = "Up"
    ADD = "Add"
    BUS = "Bus"
    CAR = "Car"
    CUT = "Cut"
    IOT = "IOT"
    PIN = "Pin"
    TAG = "Tag"
    VPN = "VPN"
    CAFE = "Cafe"
    CHAT = "Chat"
    COPY = "Copy"
    CODE = "Code"
    DOWN = "Down"
    EDIT = "Edit"
    FLAG = "Flag"
    FONT = "Font"
    GAME = "Game"
    HELP = "Help"
    HIDE = "Hide"
    HOME = "Home"
    INFO = "Info"
    LEAF = "Leaf"
    LINK = "Link"
    MAIL = "Mail"
    MENU = "Menu"
    MORE = "More"
    MOVE = "Move"
    SAVE = "Save"
    SEND = "Send"
    SYNC = "Sync"
    UNIT = "Unit"
    VIEW = "View"
    WIFI = "Wifi"
    ZOOM = "Zoom"
    ALBUM = "Album"
    BRUSH = "Brush"
    BROOM = "Broom"
    CLOSE = "Close"
    CLOUD = "Cloud"
    EMBED = "Embed"
    GLOBE = "Globe"
    HEART = "Heart"
    LABEL = "Label"
    MEDIA = "Media"
    MOVIE = "Movie"
    MUSIC = "Music"
    ROBOT = "Robot"
    PASTE = "Paste"
    PHOTO = "Photo"
    PHONE = "Phone"
    PRINT = "Print"
    SHARE = "Share"
    TILES = "Tiles"
    UNPIN = "Unpin"
    VIDEO = "Video"
    TRAIN = "Train"
    ADD_TO  ="AddTo"
    ACCEPT = "Accept"
    CAMERA = "Camera"
    CANCEL = "Cancel"
    DELETE = "Delete"
    FOLDER = "Folder"
    FILTER = "Filter"
    MARKET = "Market"
    SCROLL = "Scroll"
    LAYOUT = "Layout"
    GITHUB = "GitHub"
    UPDATE = "Update"
    RETURN = "Return"
    PEOPLE = "People"
    QRCODE = "QRCode"
    RINGER = "Ringer"
    ROTATE = "Rotate"
    SEARCH = "Search"
    FRIGID  = "Frigid"
    SAVE_AS = "SaveAs"
    ZOOM_IN = "ZoomIn"
    CONNECT  ="Connect"
    HISTORY = "History"
    SETTING = "Setting"
    PALETTE = "Palette"
    MESSAGE = "Message"
    FIT_PAGE = "FitPage"
    ZOOM_OUT = "ZoomOut"
    AIRPLANE = "Airplane"
    ASTERISK = "Asterisk"
    CALORIES = "Calories"
    CALENDAR = "Calendar"
    FEEDBACK = "Feedback"
    LIBRARY = "BookShelf"
    MINIMIZE = "Minimize"
    CHECKBOX = "CheckBox"
    DOCUMENT = "Document"
    LANGUAGE = "Language"
    DOWNLOAD = "Download"
    QUESTION = "Question"
    SPEAKERS = "Speakers"
    DATE_TIME = "DateTime"
    FONT_SIZE = "FontSize"
    HOME_FILL = "HomeFill"
    PAGE_LEFT = "PageLeft"
    SAVE_COPY = "SaveCopy"
    SEND_FILL = "SendFill"
    SPEED_OFF = "SpeedOff"
    ALIGNMENT = "Alignment"
    BLUETOOTH = "Bluetooth"
    COMPLETED = "Completed"
    CONSTRACT = "Constract"
    HEADPHONE = "Headphone"
    MEGAPHONE = "Megaphone"
    PROJECTOR = "Projector"
    EDUCATION = "Education"
    ERASE_TOOL = "EraseTool"
    PAGE_RIGHT = "PageRight"
    BOOK_SHELF = "BookShelf"
    HIGHTLIGHT = "Highlight"
    FOLDER_ADD = "FolderAdd"
    PENCIL_INK = "PencilInk"
    PIE_SINGLE = "PieSingle"
    QUICK_NOTE = "QuickNote"
    SPEED_HIGH = "SpeedHigh"
    STOP_WATCH = "StopWatch"
    ZIP_FOLDER = "ZipFolder"
    BASKETBALL = "Basketball"
    BRIGHTNESS = "Brightness"
    DICTIONARY = "Dictionary"
    MICROPHONE = "Microphone"
    ARROW_DOWN = "ChevronDown"
    FULL_SCREEN = "FullScreen"
    MIX_VOLUMES = "MixVolumes"
    REMOVE_FROM = "RemoveFrom"
    QUIET_HOURS  ="QuietHours"
    FINGERPRINT = "Fingerprint"
    APPLICATION = "Application"
    CERTIFICATE = "Certificate"
    TRANSPARENT = "Transparent"
    IMAGE_EXPORT = "ImageExport"
    SPEED_MEDIUM = "SpeedMedium"
    LIBRARY_FILL = "LibraryFill"
    MUSIC_FOLDER = "MusicFolder"
    POWER_BUTTON = "PowerButton"
    CARE_UP_SOLID = "CareUpSolid"
    ACCEPT_MEDIUM = "AcceptMedium"
    CANCEL_MEDIUM = "CancelMedium"
    CHEVRON_RIGHT = "ChevronRight"
    CLIPPING_TOOL = "ClippingTool"
    SHOPPING_CART = "ShoppingCart"
    FONT_INCREASE = "FontIncrease"
    BACK_TO_WINDOW = "BackToWindow"
    COMMAND_PROMPT = "CommandPrompt"
    CLOUD_DOWNLOAD = "CloudDownload"
    DICTIONARY_ADD = "DictionaryAdd"
    CARE_DOWN_SOLID = "CareDownSolid"
    CARE_LEFT_SOLID = "CareLeftSolid"
    CLEAR_SELECTION = "ClearSelection"
    DEVELOPER_TOOLS = "DeveloperTools"
    BACKGROUND_FILL = "BackgroundColor"
    CARE_RIGHT_SOLID = "CareRightSolid"
    EMOJI_TAB_SYMBOLS = "EmojiTabSymbols"
    EXPRESSIVE_INPUT_ENTRY = "ExpressiveInputEntry"

    def path(self, theme=Theme.AUTO):
        return f':/qmaterialwidgets/images/icons/{self.value}_{getIconColor(theme)}.svg'


class Icon(QIcon):

    def __init__(self, icon: MaterialIconBase):
        super().__init__(icon.path())
        self.materialIcon = icon


def toQIcon(icon: Union[QIcon, MaterialIconBase, str]) -> QIcon:
    """ convet `icon` to `QIcon` """
    if isinstance(icon, str):
        return QIcon(icon)

    if isinstance(icon, MaterialIconBase):
        return icon.icon()

    return icon


class Action(QAction):
    """ Fluent action """

    @singledispatchmethod
    def __init__(self, parent: QObject = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.materialIcon = None

    @__init__.register
    def _(self, text: str, parent: QObject = None, **kwargs):
        super().__init__(text, parent, **kwargs)
        self.materialIcon = None

    @__init__.register
    def _(self, icon: QIcon, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon, text, parent, **kwargs)
        self.materialIcon = None

    @__init__.register
    def _(self, icon: MaterialIconBase, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon.icon(), text, parent, **kwargs)
        self.materialIcon = icon

    def icon(self) -> QIcon:
        if self.materialIcon:
            return Icon(self.materialIcon)

        return super().icon()

    def setIcon(self, icon: Union[MaterialIconBase, QIcon]):
        if isinstance(icon, MaterialIconBase):
            self.materialIcon = icon
            icon = icon.icon()

        super().setIcon(icon)

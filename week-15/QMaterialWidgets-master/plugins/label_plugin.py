# coding: utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin

from qmaterialwidgets import (BodyLabel, CaptionLabel, StrongBodyLabel, SubtitleLabel, TitleLabel, LargeTitleLabel,
                            DisplayLabel, ImageLabel)

from plugin_base import PluginBase


class LabelPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Label)'

    def domXml(self):
        return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="text">
                <string>{self.toolTip()}</string>
            </property>
        </widget>
        """


class CaptionLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Caption label plugin """

    def createWidget(self, parent):
        return CaptionLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "CaptionLabel"


class BodyLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Body label plugin """

    def createWidget(self, parent):
        return BodyLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "BodyLabel"


class StrongBodyLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Strong body label plugin """

    def createWidget(self, parent):
        return StrongBodyLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "StrongBodyLabel"


class SubtitleLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Subtitle label plugin """

    def createWidget(self, parent):
        return SubtitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "SubtitleLabel"


class TitleLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Title label plugin """

    def createWidget(self, parent):
        return TitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "TitleLabel"


class LargeTitleLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Title label plugin """

    def createWidget(self, parent):
        return LargeTitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "LargeTitleLabel"


class DisplayLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Display label plugin """

    def createWidget(self, parent):
        return DisplayLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "DisplayLabel"


class ImageLabelPlugin(LabelPlugin, QPyDesignerCustomWidgetPlugin):
    """ Image label plugin """

    def createWidget(self, parent):
        return ImageLabel(self.icon().pixmap(72, 72), parent)

    def icon(self):
        return super().icon("Image")

    def name(self):
        return "ImageLabel"

    def domXml(self):
        return f"""<widget class="{self.name()}" name="{self.name()}"></widget>"""

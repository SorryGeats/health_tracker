import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QListWidgetItem, QPushButton

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme
from .group_interface_ui import Ui_GroupInterface

from ..config import *
from ...tracker import User

class GroupInterface(QWidget, Ui_GroupInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.groupThemeButton.setIcon(FIF.CONSTRACT)
        self.groupThemeButton.setToolTip("Change Theme")
        self.groupThemeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        groups = [
            "👥 Group 1",
            "👥 Group 2",
            "👥 Group 3",
            "👥 Group 4"
        ]
        for group in groups:
            item = QListWidgetItem(group)
            self.listWidget.addItem(item)
        
        self.listWidget.currentItemChanged.connect(self.on_current_item_changed)
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)

    def on_current_item_changed(self, current):
        index = self.listWidget.row(current)
        self.stackedWidget.setCurrentIndex(index)

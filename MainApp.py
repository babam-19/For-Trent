import sys  # helps to hand the app's termination and exit status
import os
import time
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, 
    QFormLayout, 
    QLineEdit, 
    QWidget,
    QPushButton,
    QLabel,
    QGridLayout)


class MainAppPage(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.resize(800, 600)
        self.windowTitle("Innate Domain: Physics Labyrinth")
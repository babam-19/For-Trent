import sys
import typing
from PyQt6 import QtCore # helps to hand the app's termination and exit status
from PyQt6.QtWidgets import (
    QApplication, 
    QFormLayout, 
    QLineEdit, 
    QWidget,
    QVBoxLayout,
    QDialog,
    QDialogButtonBox,
    QPushButton,
    QLabel,
    QGridLayout)

# note that the LandingWindow class inherits from the parent QDialog Class
class LandingWindow(QWidget):
    def __init__(self):
        super().__init__(parent=None) # helps with multiple inheritance.. I have to look into this to learn more
        layout = QGridLayout()
        self.setLayout(layout)

        title = QLabel("Welcome Mr. Foster - Time to log in")
        layout.addWidget(title, 0, 1)

        user = QLabel("Username:")
        layout.addWidget(user, 1, 0, )

        pwd = QLabel("Password:")
        layout.addWidget(pwd, 2, 0)

        usernameInput = QLineEdit(placeholderText = "Enter one of ur many nicknames")
        layout.addWidget(usernameInput, 1, 1)

        pwdInput = QLineEdit(placeholderText = "Our anniversary (ex: 10/27/2020)") # that example date was the first time I texted trent (I said "it's brianna")
        layout.addWidget(pwdInput, 2, 1)

        

if __name__ == "__main__":
    app = QApplication([])
    window = LandingWindow()
    window.setWindowTitle('Landing Page')

    window.show()
    sys.exit(app.exec())

    print("hello world")
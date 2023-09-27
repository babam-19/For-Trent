import sys  # helps to hand the app's termination and exit status
import typing
import time
from MainApp import MainAppPage
from PyQt6 import QtCore, QtGui
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
    QGridLayout,
    QStatusBar,
    QMessageBox)

# note that the LandingWindow class inherits from the parent QDialog Class
class LandingWindow(QWidget): # was qwidget
    def __init__(self):
        super().__init__(parent=None) # helps with multiple inheritance.. I have to look into this to learn more
        
        # Creating a title for the window and setting window size
        self.setWindowTitle("'Domain Expansion... Physics Labyrinth'")
        self.window_width, self.window_height = 300, 150
        self.setFixedSize(self.window_width, self.window_height)

        # Creating the window layout
        layout = QGridLayout()
        self.setLayout(layout)

        title = QLabel("Welcome Mr. Foster - Time to log in")
        layout.addWidget(title, 0, 0, 1, 3, QtCore.Qt.AlignmentFlag.AlignCenter)

        user = QLabel("Username:")
        layout.addWidget(user, 1, 0)

        pwd = QLabel("Password:")
        layout.addWidget(pwd, 2, 0)

        self.usernameInput = QLineEdit(placeholderText = "Enter one of ur many nicknames")
        layout.addWidget(self.usernameInput, 1, 1, 1, 2)

        self.pwdInput = QLineEdit(placeholderText = "Our anniversary (ex: 10/27/2020)") # that example date was the first time I texted trent (I said "it's brianna")
        self.pwdInput.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pwdInput, 2, 1, 1, 2)

        submitButton = QPushButton("Submit")
        submitButton.clicked.connect(self.login)
        layout.addWidget(submitButton, 3, 1)

        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        layout.addWidget(cancelButton, 3, 2)

        


    def login(self):
        acceptableUsernames = ['baby', 'trentonious', 'bubs', 'bubski', 'stinky', 'stinkiest butt', 'Mr. Foster', 'Noel', 'lovey', 'my love']
        acceptablePassword = ['04/07/2023', '1'] # using the "1" for testing purposes
        if self.usernameInput.text() in acceptableUsernames:
            if self.pwdInput.text() in acceptablePassword:
                msg = QMessageBox()
                msg.setText("Entering Innate Domain :")
                msg.setIconPixmap(QtGui.QPixmap("Photos\M_EntryImage.jpg").scaled(300, 200)) 
                msg.addButton("Allow", QMessageBox.ButtonRole.AcceptRole)
                msg.setStyleSheet("font-family: Fantasy; color:white; background-color:black")
                
                time.sleep(1) # delay window launch by 2 sec
                msg.exec()
                self.mainApp = MainAppPage()
                self.mainApp.show() # open the main app window
                self.close()
            else:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.Critical)
                msg.setText("*EEEEEEEEEEEEEE* Wrong")
                msg.setInformativeText('Not you forgetting our anniversary...')
                msg.setWindowTitle("Wrong Password")
                msg.exec()
                
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Critical)
            # msg.setStyleSheet()
            msg.setText("Womp Woooooomp")
            msg.setInformativeText("You have many nicknames, try another one lol")
            msg.setWindowTitle("Wrong Username")
            msg.exec()
            # self.statusBar().showMessage("You have many nicknames, try another one lol")
            # self.setStatusTip("You have many nicknames, try another one lol")
            # self.showStatusbar()



        

if __name__ == "__main__":
    app = QApplication([])
    window = LandingWindow()

    window.show()
    sys.exit(app.exec())

    print("hello world")
import sys  # helps to hand the app's termination and exit status
import time
from MainApp import MainAppPage
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication, 
    QLineEdit, 
    QWidget,
    QPushButton,
    QLabel,
    QGridLayout,
    QMessageBox)



# note that the LandingWindow class inherits from the parent QDialog Class
class LandingWindow(QWidget): 
    def __init__(self):
        super().__init__(parent=None) # helps with multiple inheritance.. I have to look into this to learn more

        # Creating a QLabel for the background image
        physicsBuilding = QLabel(self)
        pixmapPhysicsBuilding = QtGui.QPixmap("Photos/physicsBuilding.jpg").scaled(550, 500)  # Replace with the path to your background image
        if not pixmapPhysicsBuilding.isNull():
            physicsBuilding.setPixmap(pixmapPhysicsBuilding)
            physicsBuilding.setGeometry(0, 0, self.width(), self.height())

        # Creating a title for the window and setting window size
        self.setWindowTitle("'Domain Expansion... Physics Labyrinth'")
        self.window_width, self.window_height = 550, 350
        self.setFixedSize(self.window_width, self.window_height)

        # Creating the window layout
        layout = QGridLayout()
        self.setLayout(layout)

        # Title Label
        title = QLabel("- Welcome Mr. Foster -\n        Time to log in")
        title.setStyleSheet("font-family: Arial; font-size: 20pt; color:black; background-color:purple")
        layout.addWidget(title, 0, 0, 1, 5, QtCore.Qt.AlignmentFlag.AlignCenter) # layout.addWidget(title, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        # Inserting image of the Player
        trentImage = QLabel()
        pixmap = QtGui.QPixmap('Photos/trent.png').scaled(200, 200)
        if not pixmap.isNull():
            trentImage.setPixmap(pixmap)
            layout.addWidget(trentImage, 1, 3, 3, 2)
        else:
            print("Image file not found. Please check the file path.")

        # Username Label
        user = QLabel("Username:")
        user.setStyleSheet("font-family: Arial; font-size: 14pt; color:black; background-color:purple")
        user.setFixedHeight(30)
        layout.addWidget(user, 1, 0)

        # Password label
        pwd = QLabel("Password:")
        pwd.setStyleSheet("font-family: Arial; font-size: 14pt; color:black; background-color:purple")
        pwd.setFixedHeight(30)
        layout.addWidget(pwd, 2, 0)

        # Username Input
        self.usernameInput = QLineEdit(placeholderText = "Enter one of ur many nicknames")
        layout.addWidget(self.usernameInput, 1, 1, 1, 2)

        # Password Input
        self.pwdInput = QLineEdit(placeholderText = "Our anniversary (ex: 10/27/2020)") # that example date was the first time I texted trent (I said "it's brianna")
        self.pwdInput.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pwdInput, 2, 1, 1, 2)

        # Submit button that takes you into the login method
        self.submitButton = QPushButton("Submit")
        self.submitButton.setAutoDefault(True)
        self.submitButton.setDefault(True)
        self.submitButton.clicked.connect(self.login)
        layout.addWidget(self.submitButton, 3, 1)

        # Cancel button that quits the application
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        layout.addWidget(cancelButton, 3, 2)

    
    def login(self):
        '''
        This function checks if the login that the user typed into the username and password inputs (QlineEdit) are the desired input.
        If the user inputs the wrong information, a message box appears and tells the user what more is needed from them
        for a successful login. 
        If the correct information is entered, a message box alerts the user to let them know they are entering the game. 
        Once the user clicks the Allow button, the main page of the game appears  
        '''
        acceptableUsernames = ['baby', 'trentonious', 'bubs', 'bubski', 'stinky', 'stinkiest butt', 'Mr. Foster', 'Noel', 'lovey', 'my love']
        acceptablePassword = ['04/07/2023', '1'] # using the "1" for testing purposes

        input_username = self.usernameInput.text()
        input_password = self.pwdInput.text()

        if self.usernameInput.text() not in acceptableUsernames and self.pwdInput.text() not in acceptablePassword:
            msg = QMessageBox()
            msg.setText("Way off mate..........")
            msg.addButton("Try again", QMessageBox.ButtonRole.AcceptRole)
            msg.setWindowTitle("Wrong Username and Password")
            msg.setStyleSheet("font-family: Arial; color:black; background-color:red")
            msg.exec()

        else:
            if input_username in acceptableUsernames:
                if input_password in acceptablePassword:
                    msg = QMessageBox()
                    msg.setText("Trent,\nYou are now\nentering the Innate Domain :")
                    msg.setIconPixmap(QtGui.QPixmap("Photos\M_EntryImage.jpg").scaled(300, 200)) 
                    msg.addButton("Allow", QMessageBox.ButtonRole.AcceptRole)
                    msg.setStyleSheet("font-family: Fantasy; color:white; background-color:black")
                    
                    time.sleep(1) # delay window launch by 1 sec
                    
                    msg.exec()
                    self.mainApp = MainAppPage()
                    self.mainApp.show() # open the main app window
                    self.close()
                else:
                    msg = QMessageBox()
                    msg.setText("*EEEEEEEEEEEEEE* Wrong")
                    msg.setInformativeText('Not you forgetting our anniversary...')
                    msg.setWindowTitle("Wrong Password")
                    msg.exec()
                    
            else:
                msg = QMessageBox()
                msg.setText("Womp Woooooomp")
                msg.setInformativeText("You have many nicknames, try another one lol")
                msg.setWindowTitle("Wrong Username")
                msg.exec()
        

if __name__ == "__main__":
    app = QApplication([])
    window = LandingWindow()

    window.show()
    sys.exit(app.exec())

    
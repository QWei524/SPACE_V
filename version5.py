
#This code will be deleted in the future, this is just a temporary code to run the GUI


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout, QLineEdit
from PyQt5.QtGui import QPixmap,QMovie, QIcon
from PyQt5.QtCore import Qt
from SGA_functions.py import *
from html_PyQt_code/database/user_database.db import *
import sys

class Gif_bg(QWidget):
    def __init__(self, gif_path, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 900)

        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 500, 900)
        self.bg_label.setAlignment(Qt.AlignCenter)

        self.bg_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.movie = QMovie(gif_path)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setScaledSize(self.bg_label.size())
        self.bg_label.setMovie(self.movie)
        self.movie.start()

class SkyGuideApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("-- SPACE VISION --")
        self.setFixedSize(500, 900)
        self.db = ()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background: transparent;")  

        self.bg = Gif_bg("SGA_loginWindow_images/bg_video_0.01s.gif", parent=central_widget)
        self.bg.setGeometry(0, 0, 500, 900)
        
        self.page_container = QWidget(central_widget)
        self.page_container.setGeometry(0, 0, 500, 900)
        self.page_container.setStyleSheet("background: transparent;")
        self.page_container.setAttribute(Qt.WA_StyledBackground, True)
        
        self.stackedLayout = QStackedLayout(self.page_container)
        
        self.main_page = QWidget()
        self.main_page.setStyleSheet("background: transparent;") 
        #login and signup pages
        self.login_page = login_page(self.open_main_page)
        self.signup_page = SignUp_page(self.open_main_page, self.db)

        self.stackedLayout.addWidget(self.main_page)
        self.stackedLayout.addWidget(self.login_page)
        self.stackedLayout.addWidget(self.signup_page)

        container = QWidget(self.main_page)
        container.setGeometry(0, 0, 500, 900)
        container.setStyleSheet("background: transparent;") 
        
        self.title_sub = TitleSubtitlePart(container)
        self.logo = LogoPart(container)
        self.login_btn = LoginPart(container, self.open_login_page)
        self.signup_btn = SignUpPart(container, self.open_SignUp_page)
        self.help_info = HelpInfoPart(container)
        self.copyr_info = CopyrInfoPart(container)

    def open_login_page(self):
        self.stackedLayout.setCurrentWidget(self.login_page)

    def open_SignUp_page(self):
        self.stackedLayout.setCurrentWidget(self.signup_page)

    def open_main_page(self):
        self.stackedLayout.setCurrentWidget(self.main_page)    

class TitleSubtitlePart:
    def __init__(self, parent):
        title = QLabel("WELCOME TO\nSPACE VISION", parent)
        title.setGeometry(110, 120, 300, 80)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 39px; font-family:Horizon; font-weight: bold; color: #FFFFFF; }")

        subtitle = QLabel("Explore the Universe", parent)
        subtitle.setGeometry(100, 200, 300, 40)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("QLabel { font-size: 20px; color: #BBE6FF; font-style: italic; }")

class LogoPart:
    def __init__(self, parent):
        lbl = QLabel(parent)
        lbl.setGeometry(155, 268, 185, 185)
        pix = QPixmap("SGA_LoginWindow_images/Ras-logo.png").scaled(185, 185, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        lbl.setPixmap(pix)
        lbl.setAlignment(Qt.AlignCenter)

class LoginPart:
    def __init__(self, parent, callback):
        btn = QPushButton("LOG IN", parent)
        btn.setGeometry(150, 460, 200, 40)
        btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px;
                          border-radius:10px; border: 1px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        if callback:
            btn.clicked.connect(callback)

class login_page(QWidget):
    def __init__(self, back_callback):
        super().__init__()
        self.setFixedSize(500, 900)

        container = QWidget(self)
        container.setGeometry(0, 0, 500, 900)

        label = QLabel("Nice To See You Again!", container)
        label.setGeometry(100, 100, 300, 40)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")

        user_label = QLabel("Username:", container)
        user_label.setGeometry(100, 170, 100, 30)
        user_label.setStyleSheet("color: white; font-size: 16px;")

        self.user_input = QLineEdit(container)
        self.user_input.setGeometry(100, 210, 300, 40)
        self.user_input.setPlaceholderText("Enter username")

        pass_label = QLabel("Password:", container)
        pass_label.setGeometry(100, 270, 100, 30)
        pass_label.setStyleSheet("color: white; font-size: 16px;")

        self.pass_input = QLineEdit(container)
        self.pass_input.setGeometry(100, 310, 300, 40)
        self.pass_input.setPlaceholderText("Enter password")
        self.pass_input.setEchoMode(QLineEdit.Password)

        submit_btn = QPushButton("Submit", container)
        submit_btn.setGeometry(150, 380, 200, 40)
        submit_btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px;
                          border-radius:10px; border: 1px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)

        back_btn = QPushButton("Back To Main Page", container)
        back_btn.setGeometry(150, 500, 200, 40)
        back_btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px;
                          border-radius:10px; border: 1px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        back_btn.clicked.connect(back_callback)

class SignUpPart:
    def __init__(self, parent, callback):
        btn = QPushButton("SIGN UP", parent)
        btn.setGeometry(150, 520, 200, 40)
        btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px; border-radius: 10px;
                          border: 2px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        if callback:
            btn.clicked.connect(callback)

class SignUp_page(QWidget):
    def __init__(self, back_callback,db):
        super().__init__()
        self.db = db
        self.setFixedSize(500, 900)
        container = QWidget(self)
        container.setGeometry(0, 0, 500, 900)

        label = QLabel("It's Nice To See Some New Faces Here!", container)
        label.setGeometry(0, 100, 500, 40)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")

        user_label = QLabel("Username:", container)
        user_label.setGeometry(100, 170, 100, 30)
        user_label.setStyleSheet("color: white; font-size: 16px;")

        self.user_input = QLineEdit(container)
        self.user_input.setGeometry(100, 210, 300, 40)
        self.user_input.setPlaceholderText("Enter username")

        pass_label = QLabel("Password:", container)
        pass_label.setGeometry(100, 270, 100, 30)
        pass_label.setStyleSheet("color: white; font-size: 16px;")

        self.pass_input = QLineEdit(container)
        self.pass_input.setGeometry(100, 310, 300, 40)
        self.pass_input.setPlaceholderText("Enter password")
        self.pass_input.setEchoMode(QLineEdit.Password)

        submit_btn = QPushButton("Submit", container)
        submit_btn.setGeometry(150, 380, 200, 40)
        submit_btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px;
                          border-radius:10px; border: 1px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        submit_btn.clicked.connect(self.register_user)
        back_btn = QPushButton("Back To Main Page", container)
        back_btn.setGeometry(150, 500, 200, 40)
        back_btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px;
                          border-radius:10px; border: 1px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        back_btn.clicked.connect(back_callback)
    def register_user(self):
        username = self.user_input.text()
        password = self.pass_input.text()
        


class GuestPart:
    def __init__(self, parent, callback):
        btn = QPushButton("CONTINUE AS GUEST", parent)
        btn.setGeometry(150, 580, 200, 40)
        btn.setStyleSheet("""
            QPushButton { background: transparent; color: white;
                          font-weight: bold; font-size: 20px; border-radius: 10px;
                          border: 2px solid transparent; }
            QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }
            QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }
        """)
        if callback:
            btn.clicked.connect(callback)

       
class HelpInfoPart:
    def __init__(self, parent):
        lbl = QLabel("Need some help? Click here ! support@spacevision.net", parent)
        lbl.setGeometry(80, 660, 350, 20)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("QLabel { color: #BBE6FF; font-size: 12px; }")

class CopyrInfoPart:
    def __init__(self, parent):
        lbl = QLabel("© 2025 Space Vision", parent)
        lbl.setGeometry(350, 740, 130, 20)
        lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        lbl.setStyleSheet("QLabel { color: #7FB3D5; font-size: 10px; }")

if __name__ == "__main__":
    app     = QApplication([])
    appicon = QIcon("SGA_LoginWindow_images/Ras-logo.png")
    app.setWindowIcon(appicon)
    window  = SkyGuideApp()
    window.show()
    app.exec_()

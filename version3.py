from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SkyGuideApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("-- SPACE VISION --")
        self.setFixedSize(500, 900)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        background = QLabel()
        background.setPixmap(QPixmap("SGA_LoginWindow_images/backgroundimage.jpg").scaled(500, 900))
        background.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(background)
        container = QWidget(background)
        container.setGeometry(0, 0, 500, 900)
        self.title_subtitle = TitleSubtitlePart(container)
        self.logo = LogoPart(container)
        self.login_button = LoginPart(container)
        self.signup_button = SigninPart(container)
        self.cag_button = CAGPart(container)  # Continue as Guest
        self.help = HelpInformationPart(container)
        self.information = InformationPart(container)


  
class TitleSubtitlePart:
    def __init__(self, parent):
        self.title = QLabel("SPACE VISION", parent)
        self.title.setGeometry(100, 120, 300, 80)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 36px;
                font-weight: bold;
                color: #FFFFFF;
                text-shadow: 0 0 10px rgba(0, 200, 255, 0.7);
            }
        """)

        self.subtitle = QLabel("Explore the Universe", parent)
        self.subtitle.setGeometry(100, 200, 300, 40)
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("""
            QLabel {
                font-size: 20px;
                color: #BBE6FF;
                font-style: italic;
            }
        """)


class LogoPart:
    def __init__(self, parent):
        self.logo = QLabel(parent)
        self.logo.setGeometry(155, 268, 185, 185)
        pixmap = QPixmap("SGA_LoginWindow_images/Ras-logo.png").scaled(185, 185,  Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignCenter)


class LoginPart:
    def __init__(self, parent):
        btn = QPushButton("LOG IN", parent)
        btn.setGeometry(150, 460, 200, 40)
        btn.setStyleSheet("QPushButton { background: transparent; color: white;"
                          "font-weight: bold; font-size: 20px; "
                          "border-radius:10px ;border: 1px solid transparent; }"
                          "QPushButton:hover { background-color: rgba(255, 255, 255,0.05); }"
                           "QPushButton:pressed { background-color: rgba(255, 255, 255,0.2); }" )


class SigninPart:
    def __init__(self, parent):
        self.button = QPushButton("SIGN UP", parent)
        self.button.setGeometry(150, 520, 200, 40)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #5A9BC6;
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                border: 2px solid #3A7CA5;
            }
            QPushButton:hover {
                background-color: #3A7CA5;
            }
            QPushButton:pressed {
                background-color: #2C5C7F;
            }
        """)


class CAGPart:
    def __init__(self, parent):
        self.button = QPushButton("CONTINUE AS GUEST", parent)
        self.button.setGeometry(150, 580, 200, 40)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #5A9BC6;
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                border: 2px solid #3A7CA5;
            }
            QPushButton:hover {
                background-color: #3A7CA5;
            }
            QPushButton:pressed {
                background-color: #2C5C7F;
            }
        """)


class HelpInformationPart:
    def __init__(self, parent):
        self.help = QLabel("Need help? Contact support@spacevision.com", parent)
        self.help.setGeometry(80, 660, 350, 15)
        self.help.setAlignment(Qt.AlignCenter)
        self.help.setStyleSheet("""
            QLabel {
                color: #BBE6FF;
                font-size: 12px;
            }
        """)


class InformationPart:
    def __init__(self, parent):
        self.info = QLabel("© 2025 Space Vision", parent)
        self.info.setGeometry(350, 740, 130, 10)
        self.info.setStyleSheet("""
            QLabel {
                color: #7FB3D5;
                font-size: 10px;
            }
        """)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    window = SkyGuideApp()
    window.show()
    app.exec_()
        

#您好 我感到无上的荣幸 您在您尊贵的电脑上装载敝程序 
#您好 我感到無上的榮幸 您在您尊貴的電腦上裝載敝程序
#貴殿の尊き御パソコンに拙作をお載せいただき、無上の光栄に存じます
#尊貴하신 컴퓨터에 拙프로그램을 設置해 주신 것을 無上의 榮光으로 생각합니다.
#J’estime comme un privilège inestimable que mon humble programme ait trouvé place sur votre illustre machine
#I deem it the highest of honors that my humble program should find its place upon your venerable machine.
#Ritengo un onore sommo che il mio umile programma abbia trovato dimora nella Vostra nobile macchina
#Для меня является величайшей честью, что моё скромное творение обретает место на Вашей досточтимой машине
#إنه لشرفٌ عظيمٌ لي أن يجد برنامجي المتواضع مكانه على حاسوبكم الجليل
#Considero un honor supremo que mi humilde programa haya hallado su lugar en su ilustre máquina





from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton,
QVBoxLayout, QHBoxLayout, QStackedLayout, QLineEdit, QSizePolicy, QFrame, QTextBrowser)
from PyQt6.QtGui import QMovie, QIcon, QPainter
from PyQt6.QtCore import Qt, QUrl, QTimer, QCoreApplication
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineScript
from datetime import datetime
from zoneinfo import ZoneInfo
from PyQt6.QtGui import QDesktopServices
import os, sys
BUTTON_STYLE = """
                QPushButton {background: transparent;color: 
                white;font-weight: 
                bold;font-size: 20px;
                border-radius: 10px;
                border: 1px solid transparent;}
                QPushButton:hover {background-color: rgba(255, 255, 255, 0.05);}
                QPushButton:pressed {background-color: rgba(255, 255, 255, 0.2);}"""

INFO_BADGE_STYLE = """QFrame { background: rgba(0,0,0,0.35); border: 2px solid rgba(255,255,255,0.35);
 border-radius: 8px;}QLabel { color: white; }"""

NASA_HOSTS = {"bilibili.com"}

def apply_layout_settings(layout, margin=40, spacing=12):
    layout.setContentsMargins(margin, margin, margin, margin)
    layout.setSpacing(spacing)

def get_tz(tz_name: str):
    try:
        tz = ZoneInfo(tz_name)
        label = tz_name
    except Exception:
        local_tz = datetime.now().astimezone().tzinfo
        label = getattr(local_tz, "key", str(local_tz)) or "Local"
        tz = local_tz
    return tz, label

class Gif_bg(QWidget):
    def __init__(self, gif_path: str, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.movie = QMovie(gif_path)
        self.movie.setCacheMode(QMovie.CacheMode.CacheAll)
        self.movie.frameChanged.connect(self.update)
        self.movie.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        pix = self.movie.currentPixmap()
        if not pix.isNull():
            painter.drawPixmap(self.rect(), pix) 

class InfoWidget(QWidget):
    def __init__(self, html_path: str = None, parent=None):
        super().__init__(parent)
        self._html_path = html_path

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        head = QHBoxLayout()
        title = QLabel("Information")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
        refresh = QPushButton("Refresh")
        refresh.setFixedHeight(30)
        refresh.setStyleSheet("QPushButton{color:#BBE6FF;font-size:12px;border:1px solid rgba(255,255,255,0.25);border-radius:6px;} QPushButton:hover{background:rgba(255,255,255,0.06)}")
        refresh.clicked.connect(lambda: self.load_html(self._html_path))
        head.addWidget(title)
        head.addStretch(1)
        head.addWidget(refresh)
        layout.addLayout(head)

        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(True)
        self.browser.setStyleSheet("QTextBrowser { background: rgba(255,255,255,0.05);  color: #E6F0FF; border: none; padding:8px; }")
        layout.addWidget(self.browser, 1)

        self.load_html(self._html_path)

    def load_html(self, path: str | None):
        if not path:
            self.browser.setHtml("<h3 style='color:#BBE6FF'> Space Vision</h3><p>Explore the Universe</p>")
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.browser.setHtml(f.read())
        except Exception as e:
            self.browser.setHtml(f"<p style='color:red'>fail: {e}</p>")

class SkyGuideApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("-- SPACE VISION --")
        self.resize(1024, 640)
        self.setMinimumSize(900, 560)

        self.db = ()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        root = QVBoxLayout(central_widget)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        overlay = QStackedLayout()
        overlay.setStackingMode(QStackedLayout.StackingMode.StackAll)
        root.addLayout(overlay)

        self.bg = Gif_bg("SPACEVISION_T/assets/bg_video_0.01s.gif", parent=central_widget)
        self.bg.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        overlay.addWidget(self.bg)

        self.page_container = QWidget(central_widget)
        self.page_container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.page_container.setStyleSheet("background: transparent;")
        self.page_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.page_container.setMinimumSize(1, 1)
        overlay.addWidget(self.page_container)

        overlay.setCurrentWidget(self.page_container)
        self.bg.lower()
        self.page_container.raise_()

        self.stackedLayout = QStackedLayout(self.page_container)

        self.main_page = QWidget()
        self.main_page.setStyleSheet("background: transparent;")
        self.main_page.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.login_page = login_page(back_callback=self.open_main_page,
                                     submit_callback=self.open_home_page)
        self.signup_page = SignUp_page(self.open_main_page, self.db)
        self.home_page = HomePage()

        self.stackedLayout.addWidget(self.main_page)   
        self.stackedLayout.addWidget(self.login_page)
        self.stackedLayout.addWidget(self.signup_page)
        self.stackedLayout.addWidget(self.home_page)   

        main_v = QVBoxLayout(self.main_page)
        main_v.setContentsMargins(24, 24, 24, 24)
        main_v.setSpacing(16)
        main_v.addWidget(TopInfoBar("UTC 15", "Auckland, New Zealand")) 
        main_v.addStretch(1)

        title_sub = TitleSubtitlePart()
        main_v.addLayout(title_sub.layout)

        logo = LogoPart()
        main_v.addLayout(logo.layout)

        btn_group = QVBoxLayout()
        LoginPart(btn_group, self.open_login_page)
        SignUpPart(btn_group, self.open_SignUp_page)
        GuestPart(btn_group, self.open_home_page)
        btn_group.setSpacing(10)
        main_v.addLayout(btn_group)

        help_info = HelpInfoPart()
        main_v.addLayout(help_info.layout)

        copyr = CopyrInfoPart()
        main_v.addLayout(copyr.layout)

        main_v.addStretch(2)

        self.stackedLayout.setCurrentWidget(self.main_page)

    def open_login_page(self):
        self.stackedLayout.setCurrentWidget(self.login_page)

    def open_SignUp_page(self):
        self.stackedLayout.setCurrentWidget(self.signup_page)

    def open_main_page(self):
        self.stackedLayout.setCurrentWidget(self.main_page)

    def open_home_page(self):
        self.stackedLayout.setCurrentWidget(self.home_page)

class WebSitePage(QWebEnginePage):
    def createWindow(self, _type):
        temp = QWebEnginePage(self.profile())
        temp.urlChanged.connect(lambda url: self.view().setUrl(url))
        return temp
    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        host = url.host().lower()
        if host and host not in NASA_HOSTS:
            QDesktopServices.openUrl(url)
            return False
        return True

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(24, 24, 24, 24)
        outer.setSpacing(16)

        outer.addWidget(TopInfoBar("Wellington Time", "Auckland, New Zealand"))

        main_content = QHBoxLayout()
        main_content.setSpacing(16)
        outer.addLayout(main_content)

        self.left_content = _outlined_frame(radius=8)
        self.left_content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        left_lay = self.left_content.layout()
        self.nasa = QWebEngineView(self.left_content)
        self.nasa.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
       


        poly = QWebEngineScript()
        poly.setName("polyfill_Object_hasOwn")
        poly.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentCreation)
        poly.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
        s = self.nasa.settings()
        s.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        s.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True)
        poly.setRunsOnSubFrames(True)
        poly.setSourceCode("""(function(){if (!Object.hasOwn) {Object.hasOwn = function(obj, prop){
                             return Object.prototype.hasOwnProperty.call(obj, prop);};}})();""")
        self.nasa.page().scripts().insert(poly)
        self.nasa.setUrl(QUrl("https://eyes.nasa.gov/apps/solar-system/#/home?featured=false&detailPanel=false&logo=false&search=false&shareButton=false&menu=false&collapseSettingsOptions=true&hideExternalLinks=true&surfaceMapTiling=true&hd=true&lighting=natural&showOrbits=false&showLabels=false&showStars=false&showConstellations=false&showEcliptic=false&showEquator=false&showGrid=false&camera=0&position=0,0,5,0,0,0,0"))
        self.nasa.page().fullScreenRequested.connect(lambda r: r.accept())
        left_lay.addWidget(self.nasa)
        

        self.right_content = _outlined_frame(radius=8)
        self.right_content.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.right_content.setMinimumWidth(260)
        right_lay = self.right_content.layout()

        self.info = InfoWidget("SPACEVISION_T/assets/article.html", self.right_content)
        right_lay.addWidget(self.info)

        main_content.addWidget(self.left_content, 4)
        main_content.addWidget(self.right_content, 1)

class TopInfoBar(QFrame):
    def __init__(self, tz_name: str = "Wellington Time", location_text: str = "Auckland, New Zealand"):
        super().__init__()
        self.setFixedHeight(56)
        self.setStyleSheet(INFO_BADGE_STYLE)

        self._tz, self._tz_label = get_tz(tz_name)
        self._location = location_text

        lay = QHBoxLayout(self)
        lay.setContentsMargins(12, 8, 12, 8)
        lay.setSpacing(16)

        self.lbl_time = QLabel()
        self.lbl_time.setStyleSheet("QLabel{font-size:16px;font-weight:bold}")

        self.lbl_tz = QLabel()
        self.lbl_tz.setStyleSheet("QLabel{font-size:13px;opacity:0.9}")

        self.lbl_loc = QLabel(self._location)
        self.lbl_loc.setStyleSheet("QLabel{font-size:13px;opacity:0.9}")

        lay.addWidget(self.lbl_time)
        lay.addStretch(1)
        lay.addWidget(self.lbl_tz)
        lay.addWidget(self.lbl_loc)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(1000)
        self._tick()

    def set_location(self, text: str):
        self._location = text
        self.lbl_loc.setText(text)

    def set_timezone(self, tz_name: str):
        self._tz, self._tz_label = get_tz(tz_name)
        self._tick()

    def _tick(self):
        now = datetime.now(self._tz)
        self.lbl_time.setText(now.strftime("%Y-%m-%d %H:%M:%S"))
        offset = now.utcoffset() or 0
        total_sec = int(offset.total_seconds())
        sign = '+' if total_sec >= 0 else '-'
        total_sec = abs(total_sec)
        hh = total_sec // 3600
        mm = (total_sec % 3600) // 60
        abbr = now.tzname() or "Local"
        self.lbl_tz.setText(f"{self._tz_label} (UTC{sign}{hh:02d}:{mm:02d} / {abbr})")


def _outlined_frame(height: int = 0, radius: int = 8) -> QFrame:
    f = QFrame()
    if height > 0:
        f.setFixedHeight(height)
    f.setStyleSheet(f"""
        QFrame {{ background: transparent;
                    border: 2px solid rgba(255,255,255,0.35);
                    border-radius: {radius}px;}}""")
    lay = QVBoxLayout(f)
    lay.setContentsMargins(12, 12, 12, 12)
    lay.setSpacing(8)
    return f

class TitleSubtitlePart:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(6)

        title = QLabel("WELCOME TO\nSPACE VISION")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 39px; font-family:Horizon; font-weight: bold; color: #FFFFFF; }")

        subtitle = QLabel("Explore the Universe")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("QLabel { font-size: 20px; color: #BBE6FF; font-style: italic; }")

        self.layout.addWidget(title)
        self.layout.addWidget(subtitle)

class LogoPart:
    def __init__(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.logo = QSvgWidget("SPACEVISION_T/assets/Untitled-2.svg")
        self.logo.setStyleSheet("background: transparent;")
        self.logo.setMinimumSize(120, 120)
        self.logo.setMaximumSize(260, 260)

        self.layout.addStretch(1)
        self.layout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignCenter)
        self.layout.addStretch(1)

class LoginPart:
    def __init__(self, parent_layout: QVBoxLayout, callback):
        btn = QPushButton("LOG IN")
        btn.setFixedHeight(45)
        btn.setStyleSheet(BUTTON_STYLE)
        if callback:
            btn.clicked.connect(callback)
        parent_layout.addWidget(btn, 0, Qt.AlignmentFlag.AlignHCenter)

class SignUpPart:
    def __init__(self, parent_layout: QVBoxLayout, callback):
        btn = QPushButton("SIGN UP")
        btn.setFixedHeight(45)
        btn.setStyleSheet(BUTTON_STYLE)
        if callback:
            btn.clicked.connect(callback)
        parent_layout.addWidget(btn, 0, Qt.AlignmentFlag.AlignHCenter)

class GuestPart:
    def __init__(self, parent_layout: QVBoxLayout, callback):
        btn = QPushButton("CONTINUE AS GUEST")
        btn.setFixedHeight(45)
        btn.setStyleSheet(BUTTON_STYLE)
        if callback:
            btn.clicked.connect(callback)
        parent_layout.addWidget(btn, 0, Qt.AlignmentFlag.AlignHCenter)

class HelpInfoPart:
    def __init__(self):
        self.layout = QHBoxLayout()
        lbl = QLabel("Need some help? Click here ! support@spacevision.net")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet("QLabel { color: #BBE6FF; font-size: 12px; }")
        self.layout.addStretch(1)
        self.layout.addWidget(lbl)
        self.layout.addStretch(1)

class CopyrInfoPart:
    def __init__(self):
        self.layout = QHBoxLayout()
        lbl = QLabel("© 2025 Space Vision")
        lbl.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        lbl.setStyleSheet("QLabel { color: #7FB3D5; font-size: 10px; }")
        self.layout.addStretch(1)
        self.layout.addWidget(lbl)

class login_page(QWidget):
    def __init__(self, back_callback, submit_callback):
        super().__init__()
        self._submit_callback = submit_callback

        outer = QVBoxLayout(self)
        apply_layout_settings(outer)

        outer.addStretch(1)

        label = QLabel("Nice To See You Again!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        outer.addWidget(label)

        outer.addSpacing(8)

        user_label = QLabel("Username:")
        user_label.setStyleSheet("color: white; font-size: 16px;")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Enter username")

        pass_label = QLabel("Password:")
        pass_label.setStyleSheet("color: white; font-size: 16px;")
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Enter password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        for w in (user_label, self.user_input, pass_label, self.pass_input):
            outer.addWidget(w)

        submit_btn = QPushButton("Submit")
        submit_btn.setFixedHeight(45)
        submit_btn.setStyleSheet(BUTTON_STYLE)
        submit_btn.clicked.connect(self._on_submit_clicked)
        outer.addWidget(submit_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        outer.addStretch(2)

        back_btn = QPushButton("Back To Main Page")
        back_btn.setFixedHeight(40)
        back_btn.setStyleSheet(BUTTON_STYLE)
        back_btn.clicked.connect(back_callback)
        outer.addWidget(back_btn, 0, Qt.AlignmentFlag.AlignHCenter)

    def _on_submit_clicked(self):
        if callable(self._submit_callback):
            self._submit_callback()

class SignUp_page(QWidget):
    def __init__(self, back_callback, db):
        super().__init__()
        self.db = db

        outer = QVBoxLayout(self)
        apply_layout_settings(outer)

        outer.addStretch(1)

        label = QLabel("It's Nice To See Some New Faces Here!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        outer.addWidget(label)

        outer.addSpacing(8)

        user_label = QLabel("Username:")
        user_label.setStyleSheet("color: white; font-size: 16px;")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Enter username")

        pass_label = QLabel("Password:")
        pass_label.setStyleSheet("color: white; font-size: 16px;")
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Enter password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        for w in (user_label, self.user_input, pass_label, self.pass_input):
            outer.addWidget(w)

        submit_btn = QPushButton("Submit")
        submit_btn.setFixedHeight(45)
        submit_btn.setStyleSheet(BUTTON_STYLE)
        submit_btn.clicked.connect(self.register_user)
        outer.addWidget(submit_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        outer.addStretch(2)

        back_btn = QPushButton("Back To Main Page")
        back_btn.setFixedHeight(40)
        back_btn.setStyleSheet(BUTTON_STYLE)
        back_btn.clicked.connect(back_callback)
        outer.addWidget(back_btn, 0, Qt.AlignmentFlag.AlignHCenter)

    def register_user(self):
        username = self.user_input.text()
        password = self.pass_input.text()
        print("Register:", username, password)



def set_render_mode(mode: str):
    proxy = (os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
             or os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy"))
    flag_proxy = f"--proxy-server={proxy}" if proxy else "--proxy-auto-detect"

    def _use_software():
        os.environ["QT_OPENGL"] = "software"
        QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL, True)

    def _use_hw():
        os.environ.pop("QT_OPENGL", None)

    flags = ["--disable-features=Vulkan", "--ignore-gpu-blocklist", "--enable-webgl"]
    flags.append("--remote-debugging-port=9222")

    mode = (mode or "").lower()
    if mode == "auto":
        if sys.platform.startswith("win"):
            mode = "d3d11"
        elif sys.platform == "darwin":
            mode = "metal"
        else:
            mode = "opengl"

    if mode == "software":
        _use_software()
        flags += ["--disable-gpu", "--disable-gpu-compositing",
                  "--use-gl=swiftshader", "--use-angle=swiftshader"]
    elif mode == "d3d11":
        _use_hw()
        flags += ["--use-gl=angle", "--use-angle=d3d11"]
    elif mode == "d3d9":
        _use_hw()
        QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES, True)
        flags += ["--use-gl=angle", "--use-angle=d3d9"]
    elif mode == "metal":
        _use_hw()
        flags += ["--use-gl=angle", "--use-angle=metal"]
    elif mode == "opengl":
        _use_hw()
        flags += ["--use-gl=angle", "--use-angle=opengl"]
    else:
        if sys.platform.startswith("win"):
            _use_hw()
            flags += ["--use-gl=angle", "--use-angle=d3d11"]
        elif sys.platform == "darwin":
            _use_hw()
            flags += ["--use-gl=angle", "--use-angle=metal"]
       
    existing = os.environ.get("QTWEBENGINE_CHROMIUM_FLAGS", "")
    merged = " ".join(x for x in [existing, flag_proxy] + flags if x).strip()
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = merged


if __name__ == "__main__":
    set_render_mode("auto")
    app = QApplication(sys.argv)
    appicon = QIcon("SPACEVISION_T/assets/Untitled-2.svg")
    app.setWindowIcon(appicon)
    window = SkyGuideApp()
    window.show()
    sys.exit(app.exec())

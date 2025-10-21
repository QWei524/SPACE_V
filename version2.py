
# main.py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (500, 900)

KV = '''
#:import Color kivy.graphics.Color
#:import Rectangle kivy.graphics.Rectangle
#:import RoundedRectangle kivy.graphics.RoundedRectangle

<LoginScreen>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.3
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'SGA_loginWindow_images/backgroundimage.jpg'
        allow_stretch: True
        keep_ratio: False
        size: root.size
        pos: root.pos

    Image:
        source: 'SGA_loginWindow_images/Ras-logo.png'
        size_hint: None, None
        size: 185, 185
        pos: (157.5, 900 - 268 - 185)

    Label:
        text: 'Welcome to\\nSPACE VISION'
        font_size: '39sp'
        bold: True
        color: 1, 1, 1, 1
        halign: 'center'
        valign: 'middle'
        size_hint: None, None
        size: 300, 100
        pos: (100, 900 - 200 - 100)

    Label:
        text: 'Explore the Universe'
        font_size: '20sp'
        italic: True
        color: 0.733, 0.9, 1, 1
        size_hint: None, None
        size: 300, 40
        pos: (100, 900 - 250 - 40)

    Button:
        text: 'LOG IN'
        size_hint: None, None
        size: 200, 40
        pos: (150, 900 - 460 - 40)
        background_normal: ''
        background_color: 1, 1, 1, 0
        color: 1, 1, 1, 1
        canvas.before:
            Color:
                rgba: (1, 1, 1, 0.05) if self.state == 'down' else (1, 1, 1, 0)
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [10]

    Button:
        text: 'SIGN UP'
        size_hint: None, None
        size: 200, 40
        pos: (150, 900 - 520 - 40)
        background_normal: ''
        background_color: 1, 1, 1, 0
        color: 1, 1, 1, 1
        canvas.before:
            Color:
                rgba: (1, 1, 1, 0.05) if self.state == 'down' else (1, 1, 1, 0)
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [10]

    Button:
        text: 'CONTINUE AS GUEST'
        font_size: '14sp'
        size_hint: None, None
        size: 200, 40
        pos: (150, 900 - 580 - 40)
        background_normal: ''
        background_color: 1, 1, 1, 0
        color: 0.353, 0.612, 0.776, 1
        canvas.before:
            Color:
                rgba: (1, 1, 1, 0.05) if self.state == 'down' else (1, 1, 1, 0)
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [10]

    Label:
        text: 'Need some help? support@spacevision.com'
        font_size: '12sp'
        color: 0.733, 0.9, 1, 1
        size_hint: None, None
        size: 350, 20
        pos: (75, 900 - 660 - 20)

    Label:
        text: '© 2025 Space Vision'
        font_size: '10sp'
        color: 0.498, 0.702, 0.835, 1
        size_hint: None, None
        size: 130, 20
        pos: (350, 900 - 740 - 20)
'''

class LoginScreen(FloatLayout):
    pass

class SkyVisionApp(App):
    def build(self):
        Builder.load_string(KV)
        return LoginScreen()

if __name__ == '__main__':
    SkyVisionApp().run()

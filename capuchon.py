from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('capuchon.kv')
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1080/3,1920/3)

class Capuchon(Screen):

    pass

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file('anillo.kv')

class Anillo(Screen):
    pass
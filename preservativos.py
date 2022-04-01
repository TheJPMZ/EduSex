from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

Builder.load_file('preservativos.kv')

lista = ["Condones Masculinos", "Condones Femeninos", "DIU", "Pastilla", "Vasectonmia"]
preservativos = []

class RoundedButton(Button):
    pass


class Preservativo(BoxLayout):
    pass


class ListaPreservativos(BoxLayout):
    pass


class Preservativos(Screen):
    pass

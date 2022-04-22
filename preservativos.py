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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'horizontal'
        self.spacing= 5
        self.size_hint = (1, None)
        self.height = 100

    def crear(self,x):
        print(x)
        b = RoundedButton(text=x)
        p = self.add_widget(b)
        preservativos.append(p)


class ListaPreservativos(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for x in preservativos:
            print(x)
            self.add_widget(self,x)


class Preservativos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for x in lista:
            x = Preservativo(x)
    pass

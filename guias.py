from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

Builder.load_file('guias.kv')

dicGuias = {
    "Guia1": 25,
    "Guia2": 25,
    "Guia3": 25,
    "Guia4": 100,
    "Guia5": 100,
    "Guia6": 100,
}


class RoundedButton(Button):
    pass


class Tile(RoundedButton):
    pass


class InnerStack(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for x, y in dicGuias.items():
            b = Tile(text=x,
                     size_hint=(.2, .2)
                     )
            self.add_widget(b)
    


class Guias(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


 

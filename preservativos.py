from cgitb import text
from turtle import heading

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from numpy import size

Builder.load_file('preservativos.kv')

lista = {"Anillo": ["images\sal.png","Memes"],
         "Capuchon": ["images\sal.png","Memes"],
         "Condon Femenino" : ["images\sal.png","Memes"],
         "Condon Masculino": ["images\sal.png","Memes"],
         "Diafragma": ["images\sal.png","Memes"],
         "Espermicida": ["images\sal.png","Memes"],
         "Esponja": ["images\sal.png","Memes"],
         "Inyeccion": ["images\sal.png","Memes"],
         "Parche": ["images\sal.png","Memes"]
         }

class RoundedButton(Button):
    pass

class Preservativos(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)

        box = BoxLayout(
            orientation="vertical",
        )

        box.add_widget(Label(
            text="Preservativos",
            font_size = 50,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        ))

        scroll = ScrollView()

        ListaPreservativos = BoxLayout(
            orientation = 'vertical',
            spacing = 10,
            padding = (20, 10, 20, 20),
            size_hint_y = None,
            height = (len(lista)*110+10)
        )
        
        for x,y in lista.items():
            b = BoxLayout(
                orientation= 'horizontal',
                spacing= 5,
                size_hint= (1, None),
                height= 100
            )
            b.add_widget(Image(
                source = "images\sal.png",

                size = (100, 100)
            ))
            b.add_widget(RoundedButton(
                text= x,
                size_hint = (2, 1),

            ))
            ListaPreservativos.add_widget(b)
                
        scroll.add_widget(ListaPreservativos)
        
        box.add_widget(scroll)
        
        self.add_widget(box)
        
    pass
from cgitb import text
from pydoc import describe
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
from kivy.core.window import Window
from math import ceil

Builder.load_file('carrito.kv')
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1080/3,1920/3)

lista = {"Anillo": ["""images/anillo.png""","anillo"],
         "Capuchon": ["images/capuchon.png","capuchon"],
         "Condon Femenino" : ["images/cinterno.png","cinterno"],
         "Condon Masculino": ["images/condon.png","condones"],
         "Diafragma": ["images/diafragma.png","diafragma"],
         "Espermicida": ["images/espermicida.png","espermicida"],
         "Esponja": ["images/esponja.png","esponja"],
         "Inyeccion": ["images/inyeccion.png","inyeccion"],
         "Parche": ["images/parche.png","parche"]
         }

meme = ""
memes = []

class RoundedButton(Button):
    pass

class Tile(RoundedButton):
    pass

class BackgroundLabel(Label):
    pass

class Carrito(Screen):

    def __init__(self, **kw):
        super(Carrito,self).__init__(**kw)

        scroll = ScrollView(
         
            padding=( 50, 20, 50, 20)
        )

        box = BoxLayout(
            orientation="vertical",
            padding=(50,200,50,0)
        )

        box.add_widget(Label(
            text="",
            font_size = 50,
            padding=(50,50),
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        ))

        ListaPreservativos = BoxLayout(
            orientation = 'vertical',
            spacing = 10,
            padding = (20, 200, 20, 20),
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
                source = y[0],

                size = (100, 100)
            ))

            def meme (x):
                global meme
                meme = x
                self.goanillo(x)

            description = BackgroundLabel(
                text= x,
                size_hint = (2, 1),
                on_press = meme

            )

            boton = RoundedButton(
                text= "Eliminar",
                size_hint = (1, 1),
                on_press = meme

            )
            b.add_widget(description)
            b.add_widget(boton)
            memes.append(boton)
            ListaPreservativos.add_widget(b)

        scroll.add_widget(ListaPreservativos)

        box.add_widget(scroll)

        self.add_widget(box)

    def goanillo(self, *args):
        global meme
        print(args)
        print("Meme>",meme)
        print(memes.index(meme))

        self.manager.current = list(lista.pop.values())[memes.index(meme)][1]
    pass

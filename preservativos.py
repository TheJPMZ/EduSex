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

lista = {"Anillo": [r"""images\anillo.png""","anillo"],
         "Capuchon": ["images\capuchon.png","capuchon"],
         "Condon Femenino" : ["images\cinterno.png","cinterno"],
         "Condon Masculino": ["images\condon.png","condones"],
         "Diafragma": ["images\diafragma.png","diafragma"],
         "Espermicida": ["images\espermicida.png","espermicida"],
         "Esponja": ["images\esponja.png","esponja"],
         "Inyeccion": ["images\inyeccion.png","inyeccion"],
         "Parche": ["images\parche.png","parche"],
         "Pastillas":["images\pastillas.png","pastillas"]
         }

meme = ""
memes = []

class RoundedButton(Button):
    pass

class Preservativos(Screen):




    def __init__(self, **kw):
        super(Preservativos,self).__init__(**kw)

        scroll = ScrollView()

        box = BoxLayout(
            orientation="vertical",
        )

        box.add_widget(Label(
            text="Preservativos",
            font_size = 50,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        ))

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
                source = y[0],

                size = (100, 100)
            ))

            def meme (x):
                global meme
                meme = x
                self.goanillo(x)

            boton = RoundedButton(
                text= x,
                size_hint = (2, 1),
                on_press = meme

            )


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


        self.manager.current = list(lista.values())[memes.index(meme)][1]


    pass

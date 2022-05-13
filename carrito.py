from cgitb import text
from curses import color_content
from pydoc import describe
from tkinter import Variable
from turtle import heading
from typing import Tuple

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
import json
import anillo
import capuchon

Builder.load_file('carrito.kv')

numero = 0

with open('productos.json', 'r', encoding="utf_8") as f:
    productos = json.load(f)
    

class RoundedButton(Button):
    pass

class Carrito(Screen):

    def set_list(self):
        def addToCart(name):
            self.ids.product.add_widget(
                Label(
                    size_hint=(1, None),
                    size_y=100,
                    text=name,
                    text_size=(300, None),
                    color = (0,0,0)
                )
            )
        self.ids.product.clear_widgets()

        addToCart(productos["Anillo Vaginal"])
        addToCart(productos["Precio Anillo Vaginal"])

    def agregar (self):
        while numero < 5:
            self.ids.contador.add_widget(
                Label(
                    size_hint=(1, None),
                    size_y=100,
                    text_size=(300, None),
                    color = (0,0,0)
                )
            )
        numero += 1
    
    def quitar (self):
        while self.numero < 5:
            self.ids.contador.add_widget(
                Label(
                    size_hint=(1, None),
                    size_y=100,
                    text_size=(300, None),
                    color = (0,0,0)
                )
            )
            numero -= 1
     

    def __init__(self, **kw):
        super().__init__(**kw)

        self.set_list()

    pass
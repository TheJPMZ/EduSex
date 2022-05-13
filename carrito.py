from cgitb import text
from pydoc import describe
from tkinter import Variable
from turtle import heading
from typing import Tuple

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
from kivy.uix.checkbox import CheckBox
import json

Builder.load_file('carrito.kv')

productos = {}

with open('productos.json', 'r', encoding="utf_8") as f:
    productos = json.load(f)

class RoundedButton(Button):
    pass

global numero

class Carrito(Screen):

    def set_list(self, text="", search=False):
        def add_item(name):
            self.ids.product.add_widget(
                Button(
                    size_hint=(1, None),
                    size_y=100,
                    text=name,
                    text_size=(300, None),
                    background_normal = "",
                    background_color= (.97, .79, .89),
                    color = (0,0,0)

                )
            )

        self.ids.product.clear_widgets()
        for pregunta in productos.keys():
            if search:
                if text in pregunta:
                    add_item(pregunta)
                    continue
                for y in productos[pregunta].get("tags"):
                    if text in y:
                        add_item(pregunta)
                        continue
            else:
                add_item(pregunta)

    def __init__(self, **kw):
        super().__init__(**kw)

        self.set_list()

    pass
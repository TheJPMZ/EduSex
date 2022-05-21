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

Builder.load_file('filtrar.kv')

numero = 0

with open('productos.json', 'r', encoding="utf_8") as f:
    productos = json.load(f)
    

class RoundedButton(Button):
    pass

class Filtrar(Screen):

    pass
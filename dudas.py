from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelLabel
from kivymd.uix.boxlayout import MDBoxLayout
import json

informacion = {}

with open('informacion.json', 'r', encoding="utf_8") as f:
    informacion = json.load(f)




Builder.load_file('dudas.kv')






class Dudas(Screen):

    def set_list(self, text="", search=False):
        def add_item(name):
            self.ids.meme.add_widget(
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

        self.ids.meme.clear_widgets()
        for pregunta in informacion.keys():
            if search:
                if text in pregunta:
                    add_item(pregunta)
                    continue
                for y in informacion[pregunta].get("tags"):
                    if text in y:
                        add_item(pregunta)
                        continue
            else:
                add_item(pregunta)




    def __init__(self, **kw):
        super().__init__(**kw)

        self.set_list()

    
    pass
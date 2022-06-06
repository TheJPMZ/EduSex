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

lista = [{"Tags": "Masturbacion",
         "Tags": "Femenino",
         "Tags": "Fertilidad"
        }]

class Dudas(Screen):

    def choose_info(self,title):
        print(title)
        new_dicc = {
            "title": title,
            "info": informacion.get(title).get("info"),
        }

        image = informacion.get(title).get("image")
        if image:
            new_dicc["image"] = image

        with open('innerlog.json', 'w', encoding="utf_8") as f:
            f.write(json.dumps(new_dicc))

        self.manager.current = "showdudas"

    def set_list(self, text="", search=False):
        def add_item(name):
            self.ids.meme.add_widget(
                Button(
                    size_hint=(1, None),
                    text=name,
                    text_size=(300, None),
                    background_normal = "",
                    background_color= (.51, .21, .25),
                    color = (1,1,1),
                    on_press = lambda x: self.choose_info(name)
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

    def tags (self):
        for tag in informacion.keys():
            for x in informacion[tag].get("tags"):
                if not x in lista:
                    b = Button(text=x,
                            background_color= (.51, .21, .25),
                            font_size= 15,
                            size_hint=(0.33, 0.10),
                            on_press = lambda a: self.set_list(x, True)
                        )
                    lista.append(x)
                    self.ids.sexo.add_widget(b)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.set_list()
        self.tags()

    pass
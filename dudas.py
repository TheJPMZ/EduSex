from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from math import ceil
from kivymd.uix.button import MDIconButton

import json

from numpy import size

dicGuias = {
    "Guia6": 100,
    "Guia7": 100,
    "Guia8": 100,
    "Guia9": 100,
    "Guia0": 100,
    "Guia11": 100,
}

meme = ""
memes = []

informacion = {}

with open('informacion.json', 'r', encoding="utf_8") as f:
    informacion = json.load(f)

Builder.load_file('dudas.kv')

class RoundedButton(Button):
    pass

class Tile(RoundedButton):
    pass

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
                    size_y=100,
                    text=name,
                    text_size=(300, None),
                    background_normal = "",
                    background_color= (.97, .79, .89),
                    color = (0,0,0),
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

    def __init__(self, **kw):
        super().__init__(**kw)

        box = BoxLayout(
            orientation="vertical",
        )

        box.add_widget(Label(
            text="",
            font_size = 70,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
        ))

        scroll = ScrollView()

        InnerStack = StackLayout(
            orientation='lr-tb',
            padding= (25,10,25,10),
            size_hint=(1, 1),
            spacing=5,
        )

        print(len(dicGuias))

        self.set_list()

        def meme(x):
            global meme
            meme = x
            self.recor(x)

        for tag in informacion.keys():
            for x in informacion[tag].get("tags"):
                if x not in memes:
                    b = Tile(text=x,
                            on_press=meme,
                            font_size=25,
                            size_hint=(0.3, 0.05)
                        )
                    memes.append(b)
                    InnerStack.add_widget(b)
                    
        scroll.add_widget(InnerStack)

        box.add_widget(scroll)

        self.add_widget(box)

    def recor(self, *args):
        global meme
        print(args)
        print("Meme>",meme)
        print(memes.index(meme))


        self.manager.current = list(dicGuias.values())[memes.index(meme)][1]

    
    pass
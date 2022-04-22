
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from math import ceil

Builder.load_file('guias.kv')

dicGuias = {
    "Consentimiento": [25,"info_con"],
    "Preservativos": [25,"info_pre"],
    "Planificacion": [25,"info_planf"],
    "Menstruacion":  [25,"info_mens"],
    "ITS":  [25,"info_its"],
    "Guia6": 100,
    "Guia7": 100,
    "Guia8": 100,
    "Guia9": 100,
    "Guia0": 100,
    "Guia11": 100,
}

meme = ""
memes = []


class RoundedButton(Button):
    pass


class Tile(RoundedButton):
    pass


class Guias(Screen):

    """Layout Guide:
    Guias{
        box:BoxLayout{
            Label{}
            scroll:ScrollView{
                InnerStack:StackLayout{
                    Tile{} * len(dicGuias)
                }
            }
        }
    }
    """


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        scroll = ScrollView()

        box = BoxLayout(
            orientation="vertical",
        )

        box.add_widget(Label(
            text="Guias",
            font_size = 70,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        ))

        InnerStack = StackLayout(
            orientation='lr-tb',
            padding= (25,10,10,10),
            spacing=10,
            size_hint=(1, None),
            height= ceil(len(dicGuias)/2)*160+15,
            
            )

        print(len(dicGuias))

        def meme(x):
            global meme
            meme = x
            self.goanillo(x)

        for x, y in dicGuias.items():
            b = Tile(text=x,
                     on_press=meme
                     )
            InnerStack.add_widget(b)
            memes.append(b)
        scroll.add_widget(InnerStack)

        box.add_widget(scroll)

        self.add_widget(box)

    def goanillo(self, *args):
        global meme
        print(args)
        print("Meme>",meme)
        print(memes.index(meme))


        self.manager.current = list(dicGuias.values())[memes.index(meme)][1]


    pass

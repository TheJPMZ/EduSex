
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
    "Guia1": 25,
    "Guia2": 25,
    "Guia3": 25,
    "Guia4": 100,
    "Guia5": 100,
    "Guia6": 100,
    "Guia7": 100,
    "Guia8": 100,
    "Guia9": 100,
    "Guia0": 100,
    "Guia11": 100,
}


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

        box = BoxLayout(
            orientation="vertical",
        )

        box.add_widget(Label(
            text="Guias",
            font_size = 70,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        ))

        scroll = ScrollView()

        InnerStack = StackLayout(
            orientation='lr-tb',
            padding= (25,10,10,10),
            spacing=10,
            size_hint=(1, None),
            height= ceil(len(dicGuias)/2)*160+15,
            
            )

        print(len(dicGuias))


        for x, y in dicGuias.items():
            b = Tile(text=x,
                     )
            InnerStack.add_widget(b)
        scroll.add_widget(InnerStack)

        box.add_widget(scroll)

        self.add_widget(box)

    pass

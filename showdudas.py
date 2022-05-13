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
from kivymd.uix.label import MDLabel
import json

Builder.load_file('showdudas.kv')

class ShowDudas(Screen):
    """LayoutGuide
    ShowDudas {
        MDBoxLayout{
            MDIconButton{}
            MDBoxLayout#infolayout{
                h1title:MDLabel{}
                scroll:ScrollView{
                    answerbox:MDBoxLayout{
                        answerlabel:MDLabel{}
                        answerimage:Image{} ?
                    }
                }
            }
        }
    }
    """

    def recharge(self):
        global title, answer, image

        with open("innerlog.json", "r", encoding="utf_8") as f:
            info = json.load(f)

        title = info.get("title")
        answer = info.get("info")
        image = info.get("image")

        if not info.get("image"):
            image = ""

        print(info)
        return title, answer, image

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):

        title, answer, image = self.recharge()

        self.ids.infolayout.clear_widgets()

        h1title = MDLabel(
            size_hint=(1, .3),
            font_style="H4",
            halign="center",
            text=title
        )
        h1title.size = h1title.texture_size

        self.ids.infolayout.add_widget(h1title)

        answerbox = MDBoxLayout(
            orientation = "vertical",
            padding = (40,0,40,0),
        )

        answerlabel = MDLabel(
            halign = "center",
            valign = "middle",
            font_style = "Body1",
            text = answer,
            text_size = (1,None)
        )


        answerbox.add_widget(answerlabel)

        if image:
            answerimage = Image(
                source = image
            )
            answerbox.add_widget(answerimage)


        self.ids.infolayout.add_widget(answerbox)






    pass
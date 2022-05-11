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

Builder.load_file('dudas.kv')

class Dudas(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)

        for x in range(10):
            self.ids.meme.add_widget(
                Button(
                    size_hint= (1, None),
                    size_y= 100,
                    text= "memes"
                )

            )
    
    pass
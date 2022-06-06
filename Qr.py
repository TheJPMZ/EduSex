from cgitb import text
from turtle import heading, onclick




from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle
from numpy import source, spacing



class RoundedButton(Button):
    pass

class Generator(Screen):
    

    def __init__(self, **kw):
        super(Generator,self).__init__(**kw)


        box = BoxLayout(
            orientation="vertical",
            spacing = 15
        )
        
        
        
        lab1 = Label(
            text="Código QR",
            font_size = 30,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        )
        
        box.add_widget(lab1)
        
        #Tarjeta de credito o débito

        b1 = BoxLayout(
            orientation= 'vertical',
        )

        try:
            b1.add_widget(
                Image(
                    source="images/compra.png",
                    size = (100,100)
                )
            )
        except:
           lab2 = Label(
            text="Código QR",
            font_size = 30,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2)
            )
           b1.add_widget(lab2)
        
        box.add_widget(b1)
        self.add_widget(box)
        
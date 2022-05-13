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

Builder.load_file('MetodosPago.kv')

lista = {"Anillo": ["""images\anillo.png""","anillo"],
         "Capuchon": ["images\capuchon.png","capuchon"],
         "Condon Femenino" : ["images\cinterno.png","cinterno"],
         "Condon Masculino": ["images\condon.png","condones"],
         "Diafragma": ["images\diafragma.png","diafragma"],
         "Espermicida": ["images\espermicida.png","espermicida"],
         "Esponja": ["images\esponja.png","esponja"],
         "Inyeccion": ["images\inyeccion.png","inyeccion"],
         "Parche": ["images\parche.png","parche"]
         }

meme = ""
memes = []

class RoundedButton(Button):
    pass

class Pago(Screen):
    

    def __init__(self, **kw):
        super(Pago,self).__init__(**kw)


        box = BoxLayout(
            orientation="vertical",
            spacing = 15
        )
        
        
        
        lab1 = Label(
            text="Métodos de pago",
            font_size = 30,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        )
        
        #Tarjeta de credito o débito

        
        b1 = BoxLayout(
            orientation= 'horizontal',
            spacing= 5,
            size_hint= (0.95, None),
            height= 100
        )
        b1.add_widget(
            Image(
                source="images/debito.png",
                size = (100,100)
            )
        )
        
        but1 = RoundedButton(
            text= "Tarjeta de crédito",
            size_hint = (2, 1),
            font_size = 20,
            on_press = self.imprimir1
            
        )
        
        b1.add_widget(but1)
        
        
        #cash

        b2 = BoxLayout(
            orientation= 'horizontal',
            spacing= 5,
            size_hint= (0.95, None),
            height= 100
        )
        b2.add_widget(
            Image(
                source="images/dinero.png",
                size = (100,100)
            )
        )
        
        but2 = RoundedButton(
            text= "Efectivo",
            size_hint = (2, 1),
            font_size = 20,
            on_press = self.imprimir2
            
        )
        
        espacio = BoxLayout(
            size = (self.width, self.height/10)
        )
        
        with lab1.canvas:
            Color(rgb = (248, 202, 226))
            Rectangle(size= lab1.size, pos= lab1.pos)
        
        b2.add_widget(but2)

        box.add_widget(lab1)
        box.add_widget(b1)
        box.add_widget(b2)
        box.add_widget(espacio)
        self.add_widget(box)

    def imprimir1(self, *args):
        print("Se eligió pagar con tarjeta de crédito")
    
    def imprimir2(self, *args):
        print("Se eligió pagar con efectivo")
    pass

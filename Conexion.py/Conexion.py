from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random
import requests
import json 

class Conexion(App):
    url_firebase ="https://base-de-datos-edusex-default-rtdb.firebaseio.com/"

    def conectar(self):
        boxlayout = BoxLayout()
        button = Button(text= "Pagar")
        boxlayout.add_widget(button)
        return  boxlayout


if __name__ == '__main__':
    Conexion().run()

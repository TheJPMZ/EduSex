from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json
import random 
import uuid



class Conexion (App):
    firebase = "https://base-de-datos-edusex-default-rtdb.firebaseio.com/.json"
    def build(self):
        boxLayout = BoxLayout()
        button = Button (text = 'create Patch')
        button.bind(on_press = self.write)
        boxLayout.add_widget(button)
        return boxLayout

    def write (self , *args):
        id= uuid.uuid1()
        id_producto= id.hex
        no_compa = random.randint(1,10000000002121)
        no_compa = random.randint(1,10000)
        print("Button clicked")
        json_data = '{"Numero de compra": "123","id_producto":"dsdwqwerqcsv","total":"Q 20.00"}'
        dato = requests.patch(url= self.firebase,json=json.loads(json_data))
        print(dato)



if __name__ == '__main__':
    Conexion().run()
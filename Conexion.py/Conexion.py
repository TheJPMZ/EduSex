from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json 


class Conexion (App):
    firebase = "https://base-de-datos-edusex-default-rtdb.firebaseio.com/"
    def build(self):
        boxLayout = BoxLayout()
        button = Button (text = 'create Patch')
        button.bind(on_press = self.write)
        boxLayout.add_widget(button)
        return boxLayout

    def write (self , *args):
        print("Button clicked")
        json_data = '{"url":"nada.com","hora":"hoooy"}'
        dato = requests.patch(url= self.firebase,json=json.loads(json_data))
        print(dato)



if __name__ == '__main__':
    Conexion().run()
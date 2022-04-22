from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('genero.kv')

def store_data(data):
    with open('data.txt', 'w') as f:
        f.write(data)



class Genero(Screen):
    genero = ""
    def save_gender(self, gender):
        self.genero = gender
        store_data(self.genero)
        self.manager.current = "menu"

    pass

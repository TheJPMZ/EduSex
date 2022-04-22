from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('genero.kv')


class Genero(Screen):
    genero = ""
    def save_gender(self, gender):
        self.genero = gender
        print(self.genero)
        self.genero
        self.manager.current = "PlantillaPre"

        pass

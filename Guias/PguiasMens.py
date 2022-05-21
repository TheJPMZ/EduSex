from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('Guias/PguiasMens.kv')

class PlantillaMens(Screen):
    index = ""
    def save_gender(self, ind):
        self.index= ind
        print(self.index)
        self.index
    
    pass
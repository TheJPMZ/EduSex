from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('PinfoCon.kv')




class InfoCon(Screen):
    def cambiar(self):
        self.manager.current = "PlantillaCon"

        
        pass
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('info_its.kv')




class InfoITS(Screen):
    def cambiar(self):
        self.manager.current = "PlantillaCon"

        
        pass
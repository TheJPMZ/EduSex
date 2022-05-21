from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('Info/info_mens.kv')




class InfoMens(Screen):
    def cambiar(self):
        self.manager.current = "Plantilla"

        
        pass
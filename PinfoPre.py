from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('PinfoPre.kv')




class InfoP(Screen):
    def cambiar(self):
        self.manager.current = "Plantilla"
        
        pass
    def regresar(self):
        self.manager.current = "Guias "
        pass
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('PinfoCon.kv')




class InfoCon(Screen):
    def cambiar(self,index):
        print(index)
        self.manager.current = "Plantilla"

        
        pass
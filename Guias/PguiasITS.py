from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from puntos import ganar

Builder.load_file('Guias/PguiasITS.kv')

class PlantillaITS(Screen):
    buenas = 0
    res = ['V', 'V', 'F', 'V', 'F']
    comp = []
    def save_gender(self, respuesta, index):
        try:
            self.comp[index] = respuesta
        except:
            self.comp.append(respuesta)
        print(self.comp)
    def Evaluate(self):
        if self.buenas == 0:
            for i in range(5):
                if self.res[i] == self.comp[i]:
                    self.buenas += 1
        ganar(self.buenas, 'ITS')
        pass

    
    pass
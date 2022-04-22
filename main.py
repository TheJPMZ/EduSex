from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window


import menu
import settings
import genero
import guias
import PguiasPre
import PinfoPre
import PinfoCon
import PguiasCon
##import preservativos

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1080/3,1920/3)

class EduSexApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        sm.add_widget(guias.Guias(name="guias"))
        ##sm.add_widget(preservativos.Preservativos(name="preservativos"))
        sm.add_widget(PguiasPre.PlantillaPre(name ="PlantillaPre"))
        sm.add_widget(PinfoPre.InfoP(name ="InfoP"))
        sm.add_widget(PinfoCon.InfoCon(name ="InfoCon"))
        sm.add_widget(PguiasCon.PlantillaCon(name ="PlantillaCon"))
        return sm


if __name__ == '__main__':
    EduSexApp().run()

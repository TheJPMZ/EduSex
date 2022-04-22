from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window


import menu
import settings
import genero
import guias
import preservativos
import pguias

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1080/3,1920/3)

#Check if there is a file named data.txt with a string, return the string
def get_data():
    try:
        with open('data.txt', 'r') as f:
            if f.read() != '':
                return True
            else:
                return False
    except FileNotFoundError:
        return False

class EduSexApp(App):
    def build(self):
        sm = ScreenManager()
        if not get_data():
            sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        sm.add_widget(guias.Guias(name="guias"))
        sm.add_widget(preservativos.Preservativos(name="preservativos"))
        # sm.add_widget(pguias.Plantilla(name ="plantilla"))
        return sm


if __name__ == '__main__':
    EduSexApp().run()

import imp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window

import menu
import settings
import genero
import guias
import pastillas
import condones
import diafragma
import inyeccion
import anillo
import parche
import condonI
import esponja
import capuchon
import espermicida

#import preservativos

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1080/3,1920/3)

class EduSexApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        sm.add_widget(guias.Guias(name="guias"))
        sm.add_widget(espermicida.Espermicida(name="espermicida"))
        #sm.add_widget(preservativos.Preservativos(name="preservativos"))
        return sm


if __name__ == '__main__':
    EduSexApp().run()

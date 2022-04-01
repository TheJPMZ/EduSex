from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window

import menu
import settings
import genero
import guias


Window.clearcolor = (1, 1, 1, 1)

class EduSexApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        sm.add_widget(guias.Guias(name="guias"))
        return sm


if __name__ == '__main__':
    EduSexApp().run()

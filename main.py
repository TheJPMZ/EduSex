from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget

import menu
import settings
import genero


class EduSexApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        return sm


if __name__ == '__main__':
    EduSexApp().run()

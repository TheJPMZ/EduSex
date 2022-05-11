from kivymd.app import MDApp
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
import preservativos
import dudas

import PguiasCon
import PguiasPre
import PinfoCon
import PinfoPre
import planFInfo
import planF

#import carrito
import carrito

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

class EduSexApp(MDApp):
    def build(self):
        sm = ScreenManager()
        if not get_data():
            sm.add_widget(genero.Genero(name="genero"))
        sm.add_widget(menu.MainMenu(name="menu"))
        sm.add_widget(settings.Settings(name="settings"))
        sm.add_widget(guias.Guias(name="guias"))
        sm.add_widget(preservativos.Preservativos(name="preservativos"))
        # sm.add_widget(dudas.Dudas(name ="dudas"))

        #Preservativos
        sm.add_widget(anillo.Anillo(name="anillo"))
        sm.add_widget(capuchon.Capuchon(name="capuchon"))
        sm.add_widget(condonI.CondonI(name="cinterno"))
        sm.add_widget(condones.Condones(name="condones"))
        sm.add_widget(diafragma.Diafragma(name="diafragma"))
        sm.add_widget(espermicida.Espermicida(name="espermicida"))
        sm.add_widget(esponja.Esponja(name="esponja"))
        sm.add_widget(inyeccion.Inyeccion(name="inyeccion"))
        sm.add_widget(parche.Parche(name="parche"))

        #Guias
        sm.add_widget(PguiasCon.PlantillaCon(name="guia_con"))
        sm.add_widget(PguiasPre.PlantillaPre(name="guia_pre"))
        sm.add_widget(planF.PlanF(name="guia_planf"))

        # Informacion
        sm.add_widget(PinfoCon.InfoCon(name="info_con"))
        sm.add_widget(PinfoPre.InfoP(name="info_pre"))
        sm.add_widget(planFInfo.PlanFInfo(name="info_planf"))

        # Carrito
        sm.add_widget(carrito.Carrito(name="carrito"))

        return sm

if __name__ == '__main__':
    EduSexApp().run()

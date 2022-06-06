from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window


import menu
import genero
import guias

from Preservativos import pastillas
from Preservativos import condones
from Preservativos import diafragma
from Preservativos import inyeccion
from Preservativos import anillo
from Preservativos import parche
from Preservativos import condonI
from Preservativos import esponja
from Preservativos import capuchon
from Preservativos import espermicida

import preservativos
import dudas
import showdudas


from Guias import PguiasCon
from Guias import PguiasPre
from Guias import PguiasMens
from Guias import PguiasITS
from Guias import planF

from Info import PinfoCon
from Info import PinfoPre
from Info import planFInfo
from Info import info_its
from Info import info_mens

import carrito

import MetodosPago
import Conexion



Window.clearcolor = (.87, .95, 1, 1)
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

        sm.add_widget(guias.Guias(name="guias"))
        sm.add_widget(preservativos.Preservativos(name="preservativos"))
        sm.add_widget(dudas.Dudas(name ="dudas"))

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
        sm.add_widget(pastillas.Pastillas(name="pastillas"))

        #Guias
        sm.add_widget(PguiasCon.PlantillaCon(name="guia_con"))
        sm.add_widget(PguiasPre.PlantillaPre(name="guia_pre"))
        sm.add_widget(planF.PlanF(name="guia_planf"))
        sm.add_widget(PguiasMens.PlantillaMens(name="PlantillaMens"))
        sm.add_widget(PguiasITS.PlantillaITS(name="PlantillaITS"))


        # Informacion
        sm.add_widget(PinfoCon.InfoCon(name="info_con"))
        sm.add_widget(PinfoPre.InfoP(name="info_pre"))
        sm.add_widget(planFInfo.PlanFInfo(name="info_planf"))
        sm.add_widget(info_its.InfoITS(name="info_its"))
        sm.add_widget(info_mens.InfoMens(name="info_mens"))
        



        sm.add_widget(showdudas.ShowDudas(name = "showdudas"))

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

        sm.add_widget(MetodosPago.Pago(name="metodospago"))

        return sm

if __name__ == '__main__':
    EduSexApp().run()

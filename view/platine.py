from gpiozero import DistanceSensor, Button
from view.ADCDevice import *
from view.view import View
from model.model import Modele

class Platine:
    
    def __init__(self):
        self.bouton_demarrer = Button(13, bounce_time=0.1)
        self.bouton_fermer = Button(6, bounce_time=0.1)
        self.ouvert = False
        
        self.afficher = View()
        
        self.modele = Modele()

        self.capteur = DistanceSensor(echo = 12, trigger = 17, max_distance = 3)

        self.adc = ADCDevice()

        if(self.adc.detectI2C(0x4b)):
            self.adc = ADS7830()

    def mesurer_distance(self):
        
        
        self.cm = self.capteur.distance * 100
        self.cm = round(self.cm, 2)
        self.afficher.afficher_lcd(self.cm)
        return self.cm
        
        
    def potentionmetre(self):
        
            
        self.valeurADC = self.adc.analogRead(0)
        self.voltage = self.valeurADC / 255.0 * 3.3
        self.voltage = round(self.voltage, 2)
        self.afficher.afficher_console(self.valeurADC, self.voltage)
        
        return self.valeurADC, self.voltage
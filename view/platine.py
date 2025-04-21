from gpiozero import DistanceSensor, Button
from time import sleep
from view.ADCDevice import *
from view.LCD1602 import CharLCD1602
from view.view import View
import threading
from model.mesure import Mesure
from datetime import datetime
from model.model import Modele

class Platine:
    
    def __init__(self):
        self.bouton_demarrer = Button(13, bounce_time=0.1)
        self.bouton_fermer = Button(6, bounce_time=0.1)
        self.ouvert = False
        
        self.bouton_fermer.when_pressed = self.fermer_programme
        
        self.afficher = View()
        
        self.modele = Modele()

    def mesurer_distance(self):
        self.capteur = DistanceSensor(echo = 12, trigger = 17, max_distance = 3)
        while self.ouvert:
            self.cm = self.capteur.distance * 100
            self.cm = round(self.cm, 2)
            self.afficher.afficher_lcd(self.cm)
            sleep(1)
        
        
    def potentionmetre(self):
        self.adc = ADCDevice()

        if(self.adc.detectI2C(0x4b)):
            self.adc = ADS7830()
            
        while self.ouvert:
            self.valeurADC = self.adc.analogRead(0)
            self.voltage = self.valeurADC / 255.0 * 3.3
            self.voltage = round(self.voltage, 2)
            self.afficher.afficher_console(self.valeurADC, self.voltage)
            sleep(0.03)
        
    def fermer_programme(self):
        self.ouvert = False
        self.mesure = Mesure(str(datetime.now()), self.valeurADC, self.voltage, self.cm)
        self.modele.enregistremant(self.mesure)
    
    def ouvrir_programme(self):
        self.ouvert = True
    
    def demarrer(self):
        self.ouvrir_programme()
        self.un_thread = threading.Thread(target = self.potentionmetre)
        self.un_thread.start()
        self.mesurer_distance()
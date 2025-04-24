from view.platine import Platine
from model.model import Modele
from model.mesure import Mesure
from datetime import datetime
from time import sleep

class Controleur():
    
    def __init__(self):
        self.platine = Platine()
        self.modele = Modele()

        self.platine.bouton_fermer.when_pressed = self.fermer_programme
        
    def commencer(self):
        self.platine.bouton_demarrer.wait_for_press()
        self.ouvrir_programme()
        while self.ouvert:
            self.donner_potentio = self.platine.potentionmetre()
            self.donner_distance = self.platine.mesurer_distance()
            self.mesure = Mesure(str(datetime.now()), self.donner_potentio[0], self.donner_potentio[1], self.donner_distance)
            self.modele.enregistremant(self.mesure)
            sleep(5)

    def enregistrer_modele(self, mesure):
        self.modele.enregistremant(mesure)

    def fermer_programme(self):
        self.ouvert = False
    
    def ouvrir_programme(self):
        self.ouvert = True
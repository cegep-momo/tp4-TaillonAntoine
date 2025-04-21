from view.platine import Platine

class Controleur():
    
    def __init__(self):
        self.platine = Platine()
        
    def commencer(self):
        self.platine.bouton_demarrer.wait_for_press()
        self.platine.demarrer()
from gpiozero import Button

class Platine_bouton():

    def __init__(self, pin_bouton):
        self.bouton_demarrer = Button(pin_bouton)
        self.bouton_demarrer.wait_for_press
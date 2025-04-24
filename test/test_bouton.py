import unittest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from platine_bouton import Platine_bouton

Device.pin_factory = MockFactory()

class Test_bouton(unittest.TestCase):
    
    def setUp(self):
        self.platine = Platine_bouton(13)
        
    def test_bouton_presser(self):
        self.platine.bouton_demarrer.pin.drive_low()
        self.assertTrue(self.platine.bouton_demarrer.is_active)
        
if __name__ == "__maine__":
    unittest.main()
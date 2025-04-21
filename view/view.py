from view.LCD1602 import CharLCD1602

class View():
    
    def __init__(self):
        self.ecran_lcd = CharLCD1602()
        self.ecran_lcd.init_lcd(0x27, 1)
    
    def afficher_lcd(self, cm):
        self.ecran_lcd.write(0, 0, "Distance :")
        self.ecran_lcd.write(0, 1, f"{str(cm)} cm")
        
    def afficher_console(self, adc, voltage):
        print(f"Valeur ADC : {adc}, Voltage :{voltage}")
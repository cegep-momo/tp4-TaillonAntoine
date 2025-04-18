from gpiozero import DistanceSensor
from time import sleep
from ADCDevice import *

capteur = DistanceSensor(echo = 12, trigger = 17, max_distance = 3)

# adc = ADCDevice()

# if(adc.detectI2C(0x4b)):
#     adc = ADS7830()

while True:
    cm = capteur.distance * 100
    print(f"Distance : {str(cm)} cm")
    sleep(1)

# while True:
#     valeurADC = adc.analogRead(0)
#     voltage = valeurADC / 255.0 * 3.3
#     print(f"Valeur ADC : {valeurADC}, Voltage :{voltage:.2}")
#     sleep(0.03)
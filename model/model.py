import json
import codecs

class Modele():
    
    def __init__(self):
        try:
            with open("resultat.json", "r") as json_fichier:
                self.donnes_existant = json.load(json_fichier)
        except FileNotFoundError:
            self.donnes_existant = {"resultat": []}
    
    def enregistremant(self, donner):
        self.donnes_existant["resultat"].append(self.convertir_json(donner))
        with codecs.open("resultat.json", "w", encoding="utf-8") as json_fichier:
            json.dump(self.donnes_existant, json_fichier, ensure_ascii=False, indent=4, sort_keys=False)
            
    def convertir_json(self, donner):
        # resultat = {"date": donner.date,
        #             "adc": donner.adc,
        #             "voltage": donner.voltage,
        #             "cm": donner.cm}
        
        resultat = {"date": donner.date,
                    "adc": donner.adc,
                    "voltage": donner.voltage,
                    "cm": donner.cm}
        return resultat
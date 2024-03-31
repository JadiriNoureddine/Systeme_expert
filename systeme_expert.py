# systeme_expert.py
import json

class SystemeExpert:
    def __init__(self):
        self.regles = {}
        self.load_rules()

    def ajouter_regle(self, symptomes, panne):
        self.regles[tuple(symptomes)] = panne
        self.save_rules()

    def supprimer_regle(self, symptomes):
        if tuple(symptomes) in self.regles:
            del self.regles[tuple(symptomes)]
            self.save_rules()

    def modifier_regle(self, symptomes, nouvelle_panne):
        if tuple(symptomes) in self.regles:
            self.regles[tuple(symptomes)] = nouvelle_panne
            self.save_rules()

    def diagnostiquer_panne(self, symptomes):
        pannes_possibles = []
        for symptomes_regle, panne in self.regles.items():
            if all(symptome in symptomes_regle for symptome in symptomes):
                pannes_possibles.append(panne)
        if pannes_possibles:
            return ", ".join(pannes_possibles)
        else:
            return "Panne inconnue"

    def save_rules(self):
        with open('rules.json', 'w') as f:
            json.dump(list(self.regles.items()), f)

    def load_rules(self):
        try:
            with open('rules.json', 'r') as f:
                rule_list = json.load(f)
                self.regles = {tuple(symptomes): panne for symptomes, panne in rule_list}
        except FileNotFoundError:
            pass

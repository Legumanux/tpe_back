import json


class Item:

    def __init__(self, nom, prix, cat): # Notre méthode constructeur
        self.nom = nom
        self.prix = prix
        self.stock = None
        self.isformule = False
        self.categorie = cat

tab = []
tab.append(Item("Poulet basquaise", 15, "plat"))
tab.append(Item("Steak haché", 7, "plat"))
tab.append(Item("Mousse au caca", 2.5, "dessert"))

with open('data.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in tab], outfile)
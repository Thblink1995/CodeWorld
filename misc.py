import os
import random
def clear():
    os.system('clear')

def import_file(filename: str) -> dict:
    raise NotImplementedError

def export_file(nom_fichier: str, data) -> None:
    raise NotImplementedError

def separateur(delimiteur: str, valeur: str) -> list:
    rep = valeur.split(delimiteur)
    return rep

def replique_pnj():
    with open("replique.csv", mode='r', newline='') as replique:
        repliques = list(replique)
        print("\n" + random.choice(repliques))
# -*- coding: utf-8 -*-
from misc import *
from landing_menu import ecran_accueil
from game import GameState

#définition des classes de personnages-------------#
guerrier = {
    "force": 10,
    "defense": 20,
    "HP": 100,
    "objet": ["coutelas", "tunique de cuir"]
}
mage = {
    "force": 5,
    "defense": 40,
    "HP": 80,
    "objet": ["bâtonnet magique", "robe déchirée"]
}
dic_classes = {"mage":mage,"guerrier":guerrier}
classesdico = {"guerrier": guerrier, "mage": mage}
classes_values = list(classesdico.values())
classes_key = list(classesdico.keys())

map = {"/PC": {"/overworld": {"/batch": ["/auberge_CodeX", "/village"]}}}



def main():
    save_key = ecran_accueil()
    game_state = GameState("Debug§") #TODO remplacer par save_key

    #classep = dic_save[save_key]["classe"]
    #auberge_1()
    #fichierq1(save_key)
    #exporter("save", dic_save) #point de sauvegarde
    #auberge_foret(save_key, classep)

main()

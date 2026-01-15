# -*- coding: utf-8 -*-
from misc import *
from landing_menu import ecran_accueil
from game import GameState
from worldmanager import WorldManager
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
    if not save_key:
        return
    game_state = GameState("Debug§")
    manager = WorldManager(game_state)
    manager.load_world("data/regions/test_world.json")
    manager.enter_location("LOBBY_01")


main()

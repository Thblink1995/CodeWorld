#bibliothèques-------------------------------------#
import csv
import random
import os
import time
import colorama
from colorama import Fore, Back, Style
import misc as m
import fight
import landing_menu as lm






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
dic_save = m.import_file("save")
dic_item = m.import_file("items")
dic_mobs = m.import_file("mobs")
classesdico = {"guerrier": guerrier, "mage": mage}
classes_values = list(classesdico.values())
classes_key = list(classesdico.keys())

map = {"/PC": {"/overworld": {"/batch": ["/auberge_CodeX", "/village"]}}}

#SETUP TERMINAL--------------------------------------------------------------

#---------------------------------------------------------------------------

#random des répliques des pnj------------------------#



def ecran_accueil():
    print(27 * '-+' + "\n{" + 20 * ' ' + "Bienvenue sur" + 19 * " " + "}" +
          "\n{" + 52 * ' ' + "}" + "\n{" + 21 * ' ' + "Code World" + 21 * " " +
          "}\n" + 27 * '+-' + "\n")
    print(19 * ' ' + "1/ \"New Game\"\n" + 19 * ' ' + "2/ \"Continue\"\n" +
          19 * ' ' + "3/ \"Credits\"\n")
    rep = str(input("entrez votre choix : "))
    while rep != "1" and rep != "2" and rep != "3":
        rep = str(input("entrez votre choix : "))
    if rep == "1":
        m.clear()
        save_key = lm.start("1")
    if rep == "2":
        m.clear()
        save_key = lm.start("2")
    if rep == "3":
        m.clear()
        print("\n" + 28 * ' ' + "Crédits :\n" + "\n" + 13 * ' ' +
              "directeur projet/développeur/scénariste :\n" + 28 * ' ' +
              "Paul-Evan\n\n" + 15 * ' ' +
              "sous directeur projet/développeur :\n" + 28 * ' ' +
              "Théobald\n")
        save_key = ecran_accueil()
    return save_key











def main():
    save_key = ecran_accueil()
    #il faudra reprendre directement là où le joueur s'était arrêté s'il avait déjà une save
    classep = dic_save[save_key]["classe"]
    #auberge_1()
    #fichierq1(save_key)
    #exporter("save", dic_save) #point de sauvegarde
    #auberge_foret(save_key, classep)




#combat('tkt', 'mage', 1, 2, 0)

#Terminal("tkt")
#sortie_tuto("tkt")
main()

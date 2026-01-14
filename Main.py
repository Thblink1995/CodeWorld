# -*- coding: utf-8 -*-
import misc as m
import landing_menu

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



def main():
    save_key = landing_menu.ecran_accueil()
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

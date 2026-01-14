# -*- coding: utf-8 -*-
import csv
import os
import random
import json

#----------données globales :
player_save_filepath = "player_save.json"
repliques_pnj_filepath = "repliques_pnj.json"
mob_data_filepath = "mob_data.json"
items_data_filepath = "items_data.json"
#----------------------------


def clear():
    os.system('clear')

def import_file(filename: str) -> dict:
    with open("data/" + filename, "r", encoding="utf-8") as f:
        donnees_chargees = json.load(f)
    return donnees_chargees

def export_file(filename: str, data) -> None:
    with open("data/" + filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def separateur(delimiteur: str, valeur: str) -> list:
    rep = valeur.split(delimiteur)
    return rep

def replique_pnj():
    with open("data/replique.csv", mode='r', newline='') as replique:
        repliques = list(replique)
        print("\n" + random.choice(repliques))


data = {
    "exemple": {
        "arme":"épée",
        "classe":"guerrier",
        "progression": {
            "forest":"1-1",
            "auberge":"2"
        },
        "inventaire":[
            "épée-1",
            "bouclier-1"
            "potion-1"
        ],
        "location":"/PC/overworld/batch/auberge_CodeX"
    }
}
#export_file(player_save_file, data)
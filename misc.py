# -*- coding: utf-8 -*-
import io
import os
import random
import json
import sys

from rich.prompt import Prompt

version = "v0.0.1-alpha"

#----------données globales :
player_save_filepath = "data/player_save.json"
repliques_pnj_filepath = "data/dialogues/repliques_pnj.json"
mob_data_filepath = "data/mob_data.json"
items_data_filepath = "data/items_data.json"
characters_data_filepath = "data/characters_data.json"
scenes_dir_path = "data/scenes/"
#----------------------------

def clear():
    os.system('clear')

def import_file(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        donnees_chargees = json.load(f)
    return donnees_chargees

def export_file(filename: str, data) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def parse_script(txt_path):
    dialogues = {}
    current_key = None

    base_path = os.path.splitext(txt_path)[0]  # Enlève l'extension .txt
    json_path = base_path + ".json"

    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"): continue  # Ignore vide et commentaires

            if line.startswith("=="):
                current_key = line.replace("==", "").strip()
                dialogues[current_key] = []
            elif "|" in line and current_key:
                speaker, text = line.split("|", 1)
                dialogues[current_key].append({
                    "speaker": speaker.strip(),
                    "text": text.strip()
                })

    export_file(json_path, dialogues)

class NoColonPrompt(Prompt):
    prompt_suffix = " "

class Stack:
    def __init__(self):
        self.list = []
        self.top_element = self.list[-1]

    def pop(self):
        return self.list.pop()

    def push(self, element):
        self.list.append(element)

    def is_empty(self):
        return len(self.list) == 0

    def len(self):
        return len(self.list)

    def debug_print(self):
        print(self.list)


#parse_script("data/dialogues/intro.txt")
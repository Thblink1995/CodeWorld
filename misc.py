# -*- coding: utf-8 -*-
import os
import json
from rich.prompt import Prompt

version = "v0.0.1-alpha"

#----------données globales :
player_save_filepath = "data/player_save.json"
repliques_pnj_filepath = "data/repliques_pnj.json"
mob_data_filepath = "data/mob_data.json"
items_data_filepath = "data/items_data.json"
characters_data_filepath = "data/characters_data.json"
scenes_dir_path = "data/scenes/"
#----------------------------

def clear():
    os.system('clear')

def list_files_by_extension(directory, extension):
    rep = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                #print(os.path.join(root, file))
                rep.append(os.path.join(root, file))
    return rep


def import_file(filename: str) -> dict:
    #print(f"importing {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        donnees_chargees = json.load(f)
    return donnees_chargees

def export_file(filename: str, data) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


import json


def txt_to_dialogue_scene_json(file_path):
    """
    Transforme un fichier texte structuré en JSON pour le système de dialogue.
    """
    result = {
        "id": "",
        "name": "",
        "description": "",
        "type": "dialogue",
        "data": {
            "lines": [],
            "next_scene": "null_scene"
        }
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Séparation entre les métadonnées et les répliques (séparateur ---)
    parts = content.split('---')
    header = parts[0].strip().split('\n')
    body = parts[1].strip().split('\n') if len(parts) > 1 else []

    # Parsing du Header (id, name, description, etc.)
    for line in header:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()

            if key in ["id", "name", "description", "type"]:
                result[key] = value
            elif key == "next_scene":
                result["data"]["next_scene"] = value

    # Parsing du Corps (Dialogue)
    for line in body:
        line = line.strip()
        if not line: continue  # Sauter les lignes vides

        if ':' in line:
            speaker, text = line.split(':', 1)
            result["data"]["lines"].append({
                "speaker": speaker.strip(),
                "text": text.strip()
            })
    new_file_path = file_path.replace('.txt', '.json')
    export_file(new_file_path, result)
    return result


class NoColonPrompt(Prompt):
    prompt_suffix = " "

class Stack:
    def __init__(self):
        self.list = []
        self.len = 0

    @property
    def top_element(self):
        if self.len > 0:
            return self.list[self.len-1]
        raise ValueError("L'inventaire est vide")

    def pop(self):
        self.len -= 1
        return self.list.pop()

    def push(self, element):
        self.len += 1
        self.list.append(element)

    def is_empty(self):
        return len(self.list) == 0

    def debug_print(self):
        print(self.list)


#parse_script("data/dialogues/intro.txt")
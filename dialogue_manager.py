# -*- coding: utf-8 -*-
import random
import time
import json
from rich.console import Console
from rich.live import Live
from rich.text import Text
from game import GameState

class DialogueEngine:
    def __init__(self, data_path):
        with open(data_path, 'r', encoding='latin-1') as f:
            data = json.load(f)
            self.dialogues = data['sequences']
            self.chars = data['characters']
            # TODO ajouter
            #  f"{player_name}": {"color": "bold red", "prefix": f"[!] {player_name}: "}
            #  dans self.chars

        self.console = Console(force_terminal=True, color_system="truecolor")


    def typewriter_effect_temp(self, speaker, message, state):
        char_info = self.chars.get(speaker, {"text_color": "white", "prefix": "", "prefix_color": "bold white"})
        prefix = char_info['prefix']
        text_color = char_info['text_color']
        prefix_color = char_info['prefix_color']

        # On pré-formate le message avec le GameState
        full_message = message.format(s=state)

        current_text = ""


        with Live(None, console=self.console, auto_refresh=True) as live:
            for char in full_message:
                current_text += char

                styled_output = Text()
                styled_output.append(prefix, style=prefix_color)
                styled_output.append(current_text, style=text_color)

                live.update(styled_output)

                time.sleep(random.uniform(0.01, 0.04))


    def typewriter_effect(self, speaker, message, state):
        char_info = self.chars.get(speaker, {"text_color": "white", "prefix": "", "prefix_color": "bold white"})

        # 1. On prépare le préfixe
        prefix_text = Text(char_info['prefix'], style=char_info['prefix_color'])
        self.console.print(prefix_text, end="")

        # 2. On prépare le message (injection des variables)
        try:
            full_message = message.format(s=state)
        except Exception:
            full_message = message

        # 3. Affichage caractère par caractère
        for char in full_message:
            # On affiche le caractère sans saut de ligne
            # highlight=False empêche Rich de ralentir en cherchant des patterns à chaque lettre
            self.console.print(char, style=char_info['text_color'], end="", highlight=False)

            # On force la sortie immédiate (indispensable pour la fluidité)
            #self.console.file.flush() #est parfois nécessaire sur certains systèmes

            time.sleep(0.02)

        # 4. Une fois la phrase finie, on passe à la ligne
        self.console.print()

    def play_sequence(self, key, state):
        """
        state: l'instance de ta classe GameState
        """
        if key not in self.dialogues:
            return

        for line in self.dialogues[key]:
            # On injecte l'objet 'state' sous le nom 's' (ou ce que tu veux)
            try:
                processed_text = line['text'].format(s=state)
            except AttributeError as e:
                processed_text = f"[Code Error: {e}]"

            self.typewriter_effect(line['speaker'], processed_text, state)
            self.console.print()



temp = DialogueEngine("data/dialogues.json")
temp.play_sequence("welcome_logic", GameState())
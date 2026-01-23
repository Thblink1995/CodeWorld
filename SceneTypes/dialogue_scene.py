# -*- coding: utf-8 -*-
from .base_scene import Scene
import time
import random
from misc import *


#TODO à implémenter
class DialogueScene(Scene):
    def __init__(self, scene_data: dict, state):
        super().__init__(scene_data, state)
        self.dialogues = scene_data["data"]["lines"]
        self.next_scene = scene_data["data"]["next_scene"]
        self.chars = import_file(characters_data_filepath)

    def render(self):
        self.play_diag()

    def handle_input(self) -> tuple[str, any]:
        return "SCENE", self.next_scene

    def typewriter_effect(self, speaker:str, message:str):

        char_info = self.chars.get(speaker, {
            "text_color": "white",
            "prefix": f"{speaker} > ",
            "prefix_color": "white"
        })

        if speaker == "player":
            # On remplace le préfixe générique par le nom du joueur
            char_info['prefix'] = f"{self.state.player_name} > "
        # Si le personnage n'existe pas, on met un style par défaut

        # Affichage du préfixe
        self.console.print(char_info['prefix'], style=char_info['prefix_color'], end="")

        try:
            full_message = message.format(s=self.state)
        except:
            full_message = message

        for char in full_message:
            self.console.print(char, style=char_info['text_color'], end="", highlight=False)
            # Petit sys.stdout.flush() si besoin pour la fluidité sur Mac

            #TODO résoudre le problème de fluidité
            time.sleep(random.choice([0.02, 0.03, 0.04]))


    def play_sequence(self, line:dict, delay_time:float=0.4):
        # On injecte l'objet 'state' sous le nom 's'
        try:
            processed_text = line['text'].format(s=self.state)
        except AttributeError as e:
            processed_text = f"[Code Error: {e}]"
        self.typewriter_effect(line['speaker'], processed_text)
        time.sleep(random.choice([delay_time, delay_time+0.1, delay_time-0.1]))


    def play_diag(self):
        self.console.clear()
        self.console.print(f"[dim]— LOGS DE SESSION :  —[/]\n") #{self.name.upper()}
        last_speaker = None
        for line in self.dialogues:
            current_speaker = line.get('speaker')
            if last_speaker is not None and current_speaker != last_speaker:
                self.console.print()  # Add a blank line if speaker changes
            self.play_sequence(line)
            self.console.print()
            last_speaker = current_speaker
        self.console.print()
        NoColonPrompt.ask("\n[blink white]Continuer...[/]")




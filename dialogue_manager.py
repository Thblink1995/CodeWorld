# -*- coding: utf-8 -*-
from game import GameState
from misc import *
from rich.console import Console

class DialogueEngine:
    def __init__(self, diag_path:str, state:GameState):
        self.console = Console()
        self.state = state
        self.chars = import_file(characters_data_filepath)
        self.dialogues = import_file(diag_path)

        # TODO ajouter
        #  f"{player_name}": {"color": "bold red", "prefix": f"[!] {player_name}: "}
        #  dans self.chars

        self.console = Console(force_terminal=True, color_system="truecolor")

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
            #time.sleep(0.2)

        self.console.print()



    def play_sequence(self, sequence_id:str):
        """
        state: l'instance de ta classe GameState
        """
        if sequence_id not in self.dialogues:
            return

        for line in self.dialogues[sequence_id]:
            # On injecte l'objet 'state' sous le nom 's'
            try:
                processed_text = line['text'].format(s=self.state)
            except AttributeError as e:
                processed_text = f"[Code Error: {e}]"

            self.typewriter_effect(line['speaker'], processed_text)
        NoColonPrompt.ask("\n[blink white]continuer...[/]")

        self.console.print()


    def play_diag(self):
        for i in self.dialogues:
            self.play_sequence(i, self.state)
            self.console.print()





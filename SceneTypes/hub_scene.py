# -*- coding: utf-8 -*-
from rich.console import Group
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text
import datetime
import random
from .base_scene import *


class HubScene(Scene):
    def __init__(self, scene_data: dict, state):
        super().__init__(scene_data, state)
        self.scene_raw_data = scene_data
        self.id = scene_data['id']
        self.name = scene_data['name']
        self.description = scene_data['description']
        self.type = scene_data['type']
        self.options = [Option(**opt) for opt in self.scene_raw_data['data']]
        self.state = state
        self.timecode = TimeCode()
        #self.coords = scene_data.get('location', "UNKN_LOC")

    def render(self):
        #TODO à améliorer
        print(self.name)
        print(self.description)
        for i in self.options:
            print(i.label)

    def render(self):
        """Affiche la scène Hub avec la DA CodeWorld."""

        # 1. En-tête avec TimeCode et Coordonnées
        header_text = Text.assemble(
            (self.timecode.__rich__()),  # On appelle notre classe stylisée
            #(f" SYNC_LOC: {self.coords}", "dim yellow")
        )

        # 2. Corps narratif (La description)
        # On ajoute une marge pour aérer le texte
        narrative = Text.from_markup(f"\n{self.description}\n", style="white")

        # 3. Menu d'options (Les vecteurs d'entrée)
        menu_elements = [Rule(title="[bold cyan]VECTEURS DE CONNEXION[/]", style="dim cyan"), ""]

        for i, opt in enumerate(self.options, 1):
            # Style : [1] > NOM DE L'OPTION
            choice_line = Text.assemble(
                (f" [{i}] ", "bold cyan"),
                (f" > {opt.label.upper()}", "bold white")
            )
            menu_elements.append(choice_line)
            # On pourrait ajouter ici le type d'action en discret
            # menu_elements.append(Text(f"     TYPE: {opt.option_type}", style="dim italic blue"))
            menu_elements.append("")

            # 4. Assemblage final dans un Panel unique
        # On place l'en-tête tout en haut
        display_group = Group(
            header_text,
            Rule(style="dim white"),
            narrative,
            *menu_elements
        )

        self.console.print(Panel(
            display_group,
            title=f"[bold gold1]— {self.name.upper()} —[/]",
            subtitle="[blink red]CONNECTED_TO_NODE[/]",
            border_style="bright_blue",
            padding=(1, 2)
        ))

    def handle_input(self)-> tuple[str, any]:
        """Transforme l'input en une instruction (action_type, action_data)"""
        choices = [str(i) for i in range(1, len(self.options) + 1)]
        choix = Prompt.ask("Votre choix :", choices=choices)

        try:
            index = int(choix) - 1
            action_choisie = self.options[index]

            return "SCENE", action_choisie.data
        except (ValueError, IndexError):
            print("Choix invalide.")

    def render(self):
        """Affiche la scène dans le style CodeWorld (Cyber-Sunless)."""

        # 1. Corps narratif
        narrative = Text.from_markup(f"\n{self.description}\n", style="white")

        # 2. Construction du menu d'options
        menu_elements = [Rule(style="dim cyan"), ""]

        for i, opt in enumerate(self.options, 1):
            # Style : [1] > NOM DE L'OPTION
            choice_line = Text.assemble(
                (f" [{i}] ", "bold cyan"),
                (f" > {opt.label.upper()}", "bold white")
            )
            menu_elements.append(choice_line)
            menu_elements.append("")  # Espacement pour la lisibilité

        # 3. Rendu final dans un Panel
        display_group = Group(narrative, *menu_elements)

        self.console.print(Panel(
            display_group,
            title=f"[bold gold1]— {self.name.upper()} —[/]",
            subtitle="[blink red]AWAITING_INPUT[/]",
            border_style="bright_blue",
            padding=(1, 2)
        ))


    def handle_input(self) -> tuple[str, any]:
        """Récupère l'input avec le préfixe du joueur."""
        choices = [str(i) for i in range(1, len(self.options) + 1)]

        # On utilise le style de préfixe discuté plus tôt
        prompt_label = Text.assemble(
            (f"{self.state.player_name}", "bold green"),
            ("@codeworld", "bold blue"),
            (":~$ ", "white")
        )

        choix = Prompt.ask(prompt_label, choices=choices, show_choices=False)

        try:
            index = int(choix) - 1
            action_choisie = self.options[index]

            # On retourne le type et la donnée (ex: 'SCENE', 'id_destination')
            return "SCENE", action_choisie.data
        except (ValueError, IndexError):
            self.console.print("[bold red]ERREUR : Entrée corrompue. Réessayez.[/]")
            return self.handle_input()

class Option:
    def __init__(self, label: str, type: str, data):
        self.label = label
        self.option_type = type
        self.data = data  # ID de la scène ou de l'événement cible

    def debug_print_option(self):
        print(self.label, self.option_type, self.data)


class TimeCode:
    """Génère un marquage temporel stylisé pour les logs de CodeWorld."""

    def __init__(self):
        # On peut imaginer une date de départ fixe pour le lore
        self.base_date = "2026-01-24"

    def __rich__(self):
        now = datetime.datetime.now()
        # On crée une adresse mémoire fictive pour le look hacker
        mem_addr = f"0x{random.randint(0x1000, 0xFFFF):X}"

        return Text.assemble(
            ("[", "white"),
            (f"{now.strftime('%H:%M:%S')}", "bold cyan"),
            ("] [", "white"),
            (f"{mem_addr}", "dim green"),
            ("] ", "white")
        )
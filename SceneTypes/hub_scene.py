# -*- coding: utf-8 -*-
from rich.console import Group
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

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

    def render(self):
        #TODO à améliorer
        print(self.name)
        print(self.description)
        for i in self.options:
            print(i.label)

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
# -*- coding: utf-8 -*-
from misc import *
from rich.console import Console, Group
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

class SceneManager:
    def __init__(self): #, world_data):
        self.console = Console()
        #self.world_data = world_data
        self.history = []  # Pile pour gérer les menus et sous-menus (back)
        self.current_scene = None

    def load_scene(self, scene_id: str) -> None:
        """Récupère les données d'une scène spécifique."""
        self.current_scene = Scene(import_file(scene_id), self.console)
        self.current_scene.display()
        

    def switch_to(self, scene_id: str):
        """Charge une nouvelle scène et l'ajoute à l'historique."""
        pass

    def go_back(self):
        """Revient à la scène précédente (utile pour les sous-menus)."""
        pass

    def handle_choice(self, index: int):
        """Récupère l'option choisie et déclenche l'action associée."""
        # Si option.type == 'scene' -> switch_to(target_id)
        # Si option.type == 'evenement' -> event_manager.trigger(target_id)
        pass




# Instance globale pour la classe



class Scene:
    def __init__(self, scene_data: dict, console: Console):
        self.name = scene_data['name']
        self.description = scene_data['description']
        self.console = console
        # On s'assure que les options sont bien initialisées
        self.options = [Option(**opt) for opt in scene_data.get('options', [])]

    def display(self):
        """Affiche la scène dans un style narratif Cyber-Sunless."""

        # 1. Le corps narratif
        # On utilise Text pour supporter les couleurs et le style
        narrative = Text.from_markup(f"\n{self.description}\n", style="white")

        # 2. Construction de la zone de choix (Le sous-menu)
        menu_elements = [Rule(style="dim cyan"), ""]  # Ligne de séparation cyber

        for i, opt in enumerate(self.options, 1):
            # Formatage : [ID] NOM DE L'OPTION
            choice_line = Text.assemble(
                (f" [{i}] ", "bold cyan"),
                (f" > {opt.label.upper()}", "bold white")
            )
            menu_elements.append(choice_line)

            # Note : Tu pourrais ajouter ici un 'subtext' si tu l'ajoutes à ta classe Option
            # menu_elements.append(Text(f"     Type: {opt.action_type}", style="dim italic"))

            menu_elements.append("")  # Espacement

        # 3. Assemblage dans le Panel "Code World"
        # On utilise Group pour empiler le texte et les règles
        display_group = Group(narrative, *menu_elements)

        self.console.print(Panel(
            display_group,
            title=f"[bold gold1]— {self.name.upper()} —[/]",
            subtitle="[blink red]AWAITING_INPUT[/]",
            border_style="bright_blue",
            padding=(1, 2)
        ))


class Option:
    def __init__(self, label: str, type: str, id: str):
        self.label = label
        self.type = type  # 'scene', 'evenement', 'retour'
        self.id = id  # ID de la scène ou de l'événement cible
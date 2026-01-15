# -*- coding: utf-8 -*-
import json
from rich.panel import Panel
from rich.console import Console
from dialogue_manager import DialogueEngine
from game import GameState
from misc import *

class WorldManager:
    def __init__(self, game_state:GameState):
        self.console = Console()
        self.state = game_state
        self.world_data = {}

        # Le dictionnaire modulaire des types d'événements
        self.event_handlers = {
            "dialogue": self._handle_dialogue,
            "move": self._handle_move,
            "status_effect": self._handle_status_effect
        }

    def load_world(self, filepath):
        """Charge les données du monde (JSON)."""
        self.world_data = import_file(filepath)

    def register_event_type(self, event_name, func):
        """Permet d'ajouter dynamiquement un nouveau type d'événement (Combat, Hack, etc.)."""
        self.event_handlers[event_name] = func

    def enter_location(self, loc_id):
        """Action de pénétrer dans une nouvelle zone."""
        if loc_id not in self.world_data:
            self.console.print(f"[bold red]ERREUR : Localisation {loc_id} introuvable.[/]")
            return

        location = self.world_data[loc_id]
        self.state.current_location = loc_id

        # 1. Affichage de la zone
        self.console.print(Panel(
            location['description'],
            title=f"[bold cyan]{location['name']}[/]",
            border_style="blue"
        ))

        # 2. Exécution des événements automatiques (on_enter)
        if "on_enter" in location:
            for event in location['on_enter']:
                self.trigger_event(event)

    def trigger_event(self, event_data):
        """Déclenche un événement basé sur son type."""
        event_type = event_data.get("type")
        handler = self.event_handlers.get(event_type)

        if handler:
            handler(event_data)
        else:
            self.console.print(f"[dim red]Type d'événement inconnu : {event_type}[/]")

    # --- HANDLERS PAR DÉFAUT ---

    def _handle_dialogue(self, data):
        """Lance une séquence de dialogue."""
        diag = DialogueEngine(data['diag_path'], self.state)
        sequence_id = data['sequence_id']
        if sequence_id:
            diag.play_sequence(data['sequence_id'])
        else :
            diag.play_diag()

    def _handle_move(self, data):
        """Déplace le joueur vers une autre node."""
        self.enter_location(data['target_id'])

    def _handle_status_effect(self, data):
        """Modifie les stats du joueur (ex: PV, RAM)."""
        attr = data['stat']
        value = data['value']
        # Utilise setattr pour modifier dynamiquement GameState
        current = getattr(self.state, attr)
        setattr(self.state, attr, current + value)
        self.console.print(f"[italic]Statistique {attr} modifiée de {value}.[/]")

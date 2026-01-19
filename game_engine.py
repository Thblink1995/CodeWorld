# -*- coding: utf-8 -*-
from event_manager import EventManager
from playerstate import PlayerState
from parser import Parser
from scene_manager import SceneManager
from misc import *

class GameEngine:
    def __init__(self, player:PlayerState):#, world):
        self.player = player
        self.parser = Parser()
        self.scene_manager = SceneManager()
        self.event_manager = EventManager()
        self.is_running = True
        self.current_scene = None
        self.history_id_stack: Stack = Stack()

    def debug_print_scene_stack(self):
        self.history_id_stack.debug_print()

    def switch_to(self, scene_id: str):
        """Charge une nouvelle scène et l'ajoute à l'historique."""
        self.history_id_stack.push(scene_id)
        self.scene_manager.get_scene(scene_id)

    def go_back(self):
        """Revient à la scène précédente (utile pour les sous-menus)."""
        if self.history_id_stack.len() > 1:
            self.history_id_stack.pop()
            self.current_scene = self.history_id_stack.top_element

    def run(self) -> None:
        """Lance la boucle de jeu (Game Loop) principale."""
        self.switch_to(self.player.start_location)
        while self.is_running:
            player_input = NoColonPrompt("[dim cyan]0x{s.player_id}[/] [bold white]>[/]")


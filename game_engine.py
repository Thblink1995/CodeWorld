# -*- coding: utf-8 -*-
from event_manager import EventManager
from playerstate import PlayerState
from parser import Parser
from scene_manager import SceneManager
from misc import *

class GameEngine:
    def __init__(self, player:PlayerState):#, world):
        self.player_state = player
        self.parser = Parser()
        self.scene_manager = SceneManager()
        self.event_manager = EventManager
        self.is_running = True

    def play_scene(self, filepath):
        """Charge les données du monde (JSON)."""
        self.scene_manager.load_scene(filepath)

    def run(self) -> None:
        """Lance la boucle de jeu (Game Loop) principale."""
        self.scene_manager.switch_to(self.player.start_location)
        while self.is_running:
            player_input = NoColonPrompt("[dim cyan]0x{s.player_id}[/] [bold white]>[/]")

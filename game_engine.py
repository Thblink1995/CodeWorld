# -*- coding: utf-8 -*-
from action_registry import ActionRegistry
from playerstate import PlayerState
from scene_manager import SceneManager
from misc import *
from SceneTypes.scene_registry import *

class GameEngine:
    def __init__(self, player:PlayerState):
        self.player = player
        self.scene_manager = SceneManager()
        self.is_running = True
        self.current_scene: Scene = NullScene()
        self.history_id_stack: Stack = Stack()
        self.action_registry = ActionRegistry(self)

    def debug_print_scene_stack(self):
        self.history_id_stack.debug_print()

    def switch_to(self, scene_id: str):
        """Charge une nouvelle scène et l'ajoute à l'historique."""
        self.history_id_stack.push(scene_id)
        self.current_scene = self.scene_manager.get_scene(scene_id)

    def go_back(self):
        """Revient à la scène précédente (utile pour les sous-menus)."""
        if self.history_id_stack.len > 1:
            self.history_id_stack.pop()
            self.current_scene = self.history_id_stack.top_element

    def run(self) -> None:
        """Lance la boucle de jeu (Game Loop) principale."""
        print(self.player.start_location)
        self.switch_to(self.player.start_location)
        while self.is_running:
            self.current_scene = self.history_id_stack.top_element
            self.current_scene.render()
            self.current_scene.handle_input()

            #player_input = NoColonPrompt("[dim cyan]0x{s.player_id}[/] [bold white]>[/]")
            #launch according to input


# -*- coding: utf-8 -*-
from action_registry import ActionRegistry
from playerstate import PlayerState
from parser import Parser
from scene_manager import SceneManager, Scene, NullScene
from misc import *

class GameEngine:
    def __init__(self, player:PlayerState):#, world):
        self.player = player
        self.parser = Parser()
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
        if self.history_id_stack.len() > 1:
            self.history_id_stack.pop()
            self.current_scene = self.history_id_stack.top_element

    def handle_input(self):
        # 1. On récupère les options de la scène actuelle
        options = self.current_scene.options  # Liste d'objets Action

        # 2. On demande un choix
        choices = [str(i) for i in range(1, len(options) + 1)]
        choix = Prompt.ask("Votre choix :", choices=choices)

        try:
            index = int(choix) - 1
            action_choisie = options[index]

            # 3. On envoie l'action au registre pour exécution
            self.action_registry.execute(action_choisie.type, action_choisie.data)
        except (ValueError, IndexError):
            print("Choix invalide.")

    def run(self) -> None:
        """Lance la boucle de jeu (Game Loop) principale."""
        print(self.player.start_location)
        self.switch_to(self.player.start_location)
        while self.is_running:
            #self.current_scene = self.history_id_stack.top_element
            #display scene
            print(self.current_scene.name)
            print(self.current_scene.description)
            for i in self.current_scene.options:
                print(i.label, i.type, i.data)
            self.handle_input()

            #player_input = NoColonPrompt("[dim cyan]0x{s.player_id}[/] [bold white]>[/]")
            #launch according to input


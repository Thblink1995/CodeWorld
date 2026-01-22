# -*- coding: utf-8 -*-
from rich.prompt import Prompt
from rich.console import Console
class Scene:
    def __init__(self, scene_data, state):
        self.scene_raw_data = scene_data
        self.id = scene_data['id']
        self.type = scene_data['type']
        self.console = Console(force_terminal=True, color_system="truecolor")
        self.state = state

    def render(self):
        """Affiche la scène"""
        raise NotImplementedError

    def handle_input(self) -> tuple[str, any]:
        """Transforme l'input en une instruction (action_type, action_data)"""
        raise NotImplementedError

    def debug_print_scene_raw_data(self):
        print(self.scene_raw_data)





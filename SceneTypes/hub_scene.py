# -*- coding: utf-8 -*-
from .base_scene import *
class HubScene(Scene):
    def __init__(self, scene_data: dict):
        super().__init__(scene_data, {})
        self.scene_raw_data = scene_data
        self.id = scene_data['id']
        self.name = scene_data['name']
        self.description = scene_data['description']
        self.type = scene_data['type']
        self.options = [Option(**opt) for opt in self.scene_raw_data['data']]

    def render(self):
        #TODO à améliorer
        print(self.name)
        print(self.description)
        for i in self.options:
            print(i.label, i.type, i.data)

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

class Option:
    def __init__(self, label: str, type: str, data):
        self.label = label
        self.type = type
        self.data = data  # ID de la scène ou de l'événement cible

    def debug_print_option(self):
        print(self.label, self.option_type, self.data)
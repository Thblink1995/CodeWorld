# -*- coding: utf-8 -*-
from .base_scene import Scene
from dialogue_manager import DialogueEngine
#TODO à implémenter
class DialogueScene(Scene):
    def __init__(self, scene_data: dict):
        super().__init__(scene_data)
        self.dialogue_engine = DialogueEngine()
        self.debug_print_scene_raw_data()
        self.next_scene = scene_data["data"]["next_scene"]

    def render(self):
        raise NotImplementedError

    def handle_input(self) -> tuple[str, any]:
        return "SCENE", self.next_scene



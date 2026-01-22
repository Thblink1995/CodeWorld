# -*- coding: utf-8 -*-
from .base_scene import *
class NullScene(Scene):
    def __init__(self, scene_data: dict, state):
        super().__init__(scene_data, {})
        self.id = "NullScene"
        self.name = "NullScene"
        self.description = "Placeholder Scene"
        self.type = "hub"
        self.options = []

    def render(self):
        print(self.name)

    def handle_input(self, user_input) -> tuple[str, any]:
        return None, None
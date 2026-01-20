# -*- coding: utf-8 -*-
from .base_scene import Scene

#TODO à implémenter
class DialogueScene(Scene):
    def __init__(self, scene_data: dict):
        super().__init__(scene_data)

    def render(self):
        raise NotImplementedError



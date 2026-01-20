# -*- coding: utf-8 -*-
from os.path import isfile
from misc import *

class Scene:
    def __init__(self, scene_data: dict):
        self.scene_raw_data = scene_data
        self.id = scene_data['id']
        self.name = scene_data['name']
        self.description = scene_data['description']
        self.type = scene_data['type']
        self.options = [Option(**opt) for opt in scene_data.get('options', [])]

    def debug_print_scene_raw_data(self):
        print(self.scene_raw_data)

class NullScene(Scene):
    def __init__(self):
        self.id = "NullScene"
        self.name = "NullScene"
        self.description = "Placeholder Scene"
        self.type = "hub"
        self.options = []

class Option:
    def __init__(self, label: str, type: str, data):
        self.label = label
        self.type = type
        self.data = data  # ID de la scène ou de l'événement cible
    def debug_print_option(self):
        print(self.label, self.id)


class SceneManager:
    def __init__(self):
        self.scenes_dict: dict = {}
        self.index_scenes()

    def index_scenes(self):
        scenes_paths = list_files_by_extension("data/scenes/", ".json")
        if scenes_paths is None:
            raise Exception
        for i in scenes_paths :
            if isfile(i):
                temp = import_file(i)
                self.scenes_dict[temp["id"]] = i

    def debug_print_scenes_dic(self):
        print(self.scenes_dict)

    def get_scene(self, scene_id: str) -> Scene:
        """charge une scène en mémoire à l'aide de son id"""
        scene = Scene(import_file(self.scenes_dict[scene_id]))
        return scene
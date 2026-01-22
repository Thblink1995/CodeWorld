# -*- coding: utf-8 -*-
from os.path import isfile
from misc import *
from SceneTypes.scene_registry import get_scene_class
from SceneTypes.base_scene import Scene


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

    def get_scene(self, scene_id: str, state) -> Scene:
        """charge une scène en mémoire à l'aide de son id"""
        data = import_file(self.scenes_dict[scene_id])
        klass: Scene = get_scene_class(data['type'])
        return klass(data, state)
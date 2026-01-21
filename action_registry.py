# -*- coding: utf-8 -*-

class ActionRegistry:
    def __init__(self, engine):
        self.engine = engine
        # Le dictionnaire de correspondance
        self.actions = {
            "SCENE": self.change_scene,
        }

    @property
    def state(self):
        return self.engine.player

    def execute(self, action_type, data):
        # On récupère la fonction et on l'exécute avec les données
        func = self.actions.get(action_type)
        if func:
            func(data)
        else:
            print(f"Action {action_type} non reconnue.")

    def change_scene(self, scene_id):
        self.engine.switch_to(scene_id)  # 'data' est l'ID de la scène

    def trigger_event(self, data):
        print(f"Événement déclenché : {data}")


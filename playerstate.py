# -*- coding: utf-8 -*-
from misc import *
class PlayerState:
    def __init__(self, save_key):
        save_data = import_file(player_save_filepath)
        player_data = save_data[save_key]
        self.player_name = save_key
        self.max_health = player_data["max_health"]
        self.current_health = player_data["current_health"]
        self.inventory = player_data["inventory"]
        self.location = player_data["location"]
        self.start_location = None

    def get_inventory(self):
        raise NotImplementedError

    def save(self):
        data = {
            "max_health": self.max_health,
            "current_health": self.current_health,
            "inventory": self.inventory,
            "location": self.location
        }

        global_data = import_file(player_save_filepath)
        global_data[self.player_name] = data
        export_file(player_save_filepath, global_data)







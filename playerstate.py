# -*- coding: utf-8 -*-
from misc import *
class PlayerState:
    def __init__(self, save_key):
        save_data = import_file(player_save_filepath)
        self.player_raw_data = save_data[save_key]
        self.player_name = save_key
        self.max_health = self.player_raw_data["max_health"]
        self.current_health = self.player_raw_data["current_health"]
        self.inventory = self.player_raw_data["inventory"]
        self.location = self.player_raw_data["location"]
        self.start_location = self.player_raw_data["start_location"]

    def get_inventory(self):
        raise NotImplementedError

    def save(self):
        data = {
            "max_health": self.max_health,
            "current_health": self.current_health,
            "inventory": self.inventory,
            "location": self.location,
            "start_location": self.start_location,
        }

        global_data = import_file(player_save_filepath)
        global_data[self.player_name] = data
        export_file(player_save_filepath, global_data)

    def debug_print_player_data(self):
        print(self.player_raw_data)







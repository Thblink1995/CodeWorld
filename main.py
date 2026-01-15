# -*- coding: utf-8 -*-
from misc import *
from landing_menu import ecran_accueil, boot_sequence
from game import GameState
from worldmanager import WorldManager


def main():
    boot_sequence()
    save_key = ecran_accueil()
    if not save_key:
        return
    game_state = GameState("Debug§")
    manager = WorldManager(game_state)
    manager.load_world("data/regions/test_world.json")
    manager.enter_location("LOBBY_01")
    game_state.save()


main()

# -*- coding: utf-8 -*-
from landing_menu import ecran_accueil, boot_sequence
from playerstate import PlayerState
from game_engine import GameEngine


def main():
    #boot_sequence()
    #save_key = ecran_accueil()
    #if not save_key:
    #    return
    player_state = PlayerState("Debug§")
    manager = GameEngine(player_state)
    manager.play_scene("regions/sunless_skies/port_avalon.json")
    player_state.save()


main()

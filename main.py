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
    engine = GameEngine(player_state)
    engine.player.debug_print_player_data()
    engine.run()
    engine.scene_manager.debug_print_scenes_dic()
    player_state.save()


main()

# -*- coding: utf-8 -*-
class EventManager:
    def __init__(self, engine):
        self.engine = engine
        # Registre des types d'événements
        self.handlers = {

            #évènements de scène
            "dialogue": self._handle_dialogue,
            "combat": self._handle_combat,
            "evenement_unique": self._handle_unique,

            #évènements de commandes

        }

    def trigger_events(self, event_list: list):
        """Parcourt et lance chaque événement d'une scène."""
        pass

    def _handle_dialogue(self, data: dict):
        """Lance la logique de dialogue."""
        pass

    def _handle_combat(self, data: dict):
        """Lance l'entrée en mode combat."""
        pass

    def _handle_unique(self, data: dict):
        """Cherche et exécute un script spécifique via data['script_id']."""
        pass
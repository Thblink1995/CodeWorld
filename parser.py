# -*- coding: utf-8 -*-
class Parser:
    def __init__(self):
        # Liste des verbes et synonymes (ex: "aller", "marcher", "go")
        pass

    def parse(self, raw_input: str) -> dict:
        """Nettoie l'entrée et retourne un dictionnaire d'intention."""
        pass

    def _tokenize(self, text: str) -> list[str]:
        """Découpe la chaîne et retire les mots inutiles (le, la, un)."""
        pass

    def _extract_intent(self, tokens: list[str]) -> dict:
        """Identifie l'action et l'objet (ex: {'action': 'take', 'target': 'sword'})."""
        pass
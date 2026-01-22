# -*- coding: utf-8 -*-
from .hub_scene import HubScene
from .null_scene import NullScene

from .base_scene import Scene # Ta classe de base
from .dialogue_scene import DialogueScene

# Le dictionnaire de mapping
SCENE_CLASSES = {
    "hub": HubScene,
    "null": NullScene,
    "dialogue": DialogueScene,
    "null_scene": NullScene
}

def get_scene_class(scene_type: str):
    """Retourne la classe correspondante ou la classe de base par défaut."""
    return SCENE_CLASSES.get(scene_type, Scene)
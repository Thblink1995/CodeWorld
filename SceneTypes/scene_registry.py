# -*- coding: utf-8 -*-
from .hub_scene import HubScene
from .null_scene import NullScene

from .base_scene import Scene # Ta classe de base
from .dialogue_scene import DialogueScene
from .cemetery_scene import CemeteryScene
from .tunnel_scene import TunnelScene
from .market_scene import MarketScene
from .guardian_scene import GuardianScene
from .kernel_scene import KernelScene

# Le dictionnaire de mapping
SCENE_CLASSES = {
    "hub": HubScene,
    "null": NullScene,
    "dialogue": DialogueScene,
    "null_scene": NullScene,
    "cemetery_echo7": CemeteryScene,
    "tunnel_noir": TunnelScene,
    "marche_souterrain": MarketScene,
    "guardian_alpha": GuardianScene,
    "kernel_core": KernelScene,
}

def get_scene_class(scene_type: str):
    """Retourne la classe correspondante ou la classe de base par défaut."""
    return SCENE_CLASSES.get(scene_type, Scene)